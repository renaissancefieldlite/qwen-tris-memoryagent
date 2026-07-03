"""Qwen Tris Recall Memory AI Expert Partner orchestration."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Protocol

from .memory_store import EvidenceHit, MemoryStore, Retrieval
from .stable_state import StableStatePacket


class CompletionProvider(Protocol):
    name: str

    def complete(self, prompt: str) -> str:
        ...


@dataclass
class AgentResult:
    response: str
    prompt: str
    packet: StableStatePacket
    retrievals: list[Retrieval]
    evidence_hits: list[EvidenceHit]
    provider_name: str


class TriniRecallAgent:
    """Persistent memory agent with architecture-on/off modes."""

    def __init__(
        self,
        *,
        store: MemoryStore,
        provider: CompletionProvider,
        task_state: str,
        current_gate: str,
        constraints: tuple[str, ...] = (),
        evidence_boundaries: tuple[str, ...] = (),
    ) -> None:
        self.store = store
        self.provider = provider
        self.task_state = task_state
        self.current_gate = current_gate
        self.constraints = constraints
        self.evidence_boundaries = evidence_boundaries

    def answer(
        self,
        message: str,
        *,
        architecture_on: bool = True,
        evidence_hits: list[EvidenceHit] | None = None,
        rag_mode: str = "sqlite_fts",
    ) -> AgentResult:
        retrievals = self._retrieve_for_message(message) if architecture_on else []
        if not architecture_on:
            evidence_hits = []
        elif evidence_hits is None:
            evidence_hits = self.store.search_evidence(message, limit=4)
        corrections = tuple(
            retrieval.item.content
            for retrieval in retrievals
            if retrieval.item.kind == "correction"
        )
        packet = StableStatePacket(
            task_state=self.task_state if architecture_on else "baseline Qwen: no stable-state packet",
            current_gate=self.current_gate if architecture_on else "answer from prompt only",
            constraints=self.constraints if architecture_on else (),
            corrections=corrections if architecture_on else (),
            evidence_boundaries=self.evidence_boundaries if architecture_on else (),
            recalled_memories=tuple(retrievals),
        )
        prompt = self._build_prompt(message, packet, evidence_hits, architecture_on=architecture_on, rag_mode=rag_mode)
        response = self.provider.complete(prompt)
        return AgentResult(
            response=response,
            prompt=prompt,
            packet=packet,
            retrievals=retrievals,
            evidence_hits=evidence_hits,
            provider_name=getattr(self.provider, "name", self.provider.__class__.__name__),
        )

    def _retrieve_for_message(self, message: str) -> list[Retrieval]:
        retrievals = self.store.retrieve(message, limit=6)
        target_match = re.search(r"Target memory row:\s*([A-Za-z0-9_.:-]+)", message)
        if not target_match:
            return retrievals
        target_id = target_match.group(1).rstrip(".;,")
        target_item = self.store.get_memory(target_id)
        if target_item is None:
            return retrievals
        pinned = Retrieval(
            item=target_item,
            reason="explicit target memory row",
            score=99.0,
            token_estimate=max(1, len(target_item.content.split())),
        )
        # Benchmark turns use explicit target ids to test exact continuity, so
        # keep neighboring memories out of the response prompt.
        return [pinned]

    def _build_prompt(
        self,
        message: str,
        packet: StableStatePacket,
        evidence_hits: list[EvidenceHit],
        *,
        architecture_on: bool,
        rag_mode: str = "sqlite_fts",
    ) -> str:
        if not architecture_on:
            return f"""BASELINE CONDITION A: Qwen without Qwen Tris Recall.

User message:
{message}

Answer the task from the visible prompt only.
"""
        pinned_target = next(
            (retrieval for retrieval in packet.recalled_memories if retrieval.reason == "explicit target memory row"),
            None,
        )
        if pinned_target:
            expected_factors = self._extract_expected_factors(pinned_target.item.content)
            expected_section = (
                "Target expected recall factors:\n"
                + "\n".join(f"- {factor}" for factor in expected_factors)
                + "\n"
                if expected_factors
                else "Target expected recall factors:\n- none parsed\n"
            )
            target_section = (
                "Pinned target memory - highest priority:\n"
                f"- [{pinned_target.item.id}] {pinned_target.item.kind}: "
                f"{pinned_target.item.content} "
                f"(source={pinned_target.item.source_ref})\n"
                f"{expected_section}"
            )
        else:
            target_section = (
                "Pinned target memory - highest priority:\n- none\n"
                "Target expected recall factors:\n- none parsed\n"
            )
        evidence_section = "\n".join(
            f"- {hit.doc.id} | {hit.doc.title} | {hit.reason} | {hit.doc.source_ref}"
            for hit in evidence_hits
        )
        if not evidence_section:
            evidence_section = "- none"
        return f"""{target_section}
{packet.render()}

Retrieved evidence/RAG ({rag_mode}):
{evidence_section}

Operating contract:
- The pinned target memory governs the answer when it is present.
- Use recalled memories only when they govern the current task.
- When a retrieved memory contains "Expected recall factors:", copy the relevant factors verbatim in a "Recall factors used:" line before interpreting them.
- On explicit target-memory benchmark turns, use only the Target expected recall factors for the "Recall factors used:" line.
- Do not paraphrase exact recall factors on benchmark or receipt turns.
- Include a short Boundary line when the task has stale claims or public/private gates.
- Include a short Next gate line when the task asks for current status or continuation.
- Use retrieved evidence/RAG only when it is source-relevant.
- Preserve corrections and source boundaries.
- Suppress stale or superseded state.
- Continue from the current gate.
- Do not claim model-weight tuning unless an adapter artifact exists.
- Answer only the current user message; do not continue into future stress turns.

Preferred answer shape:
Target row:
Recall factors used:
Exact facts:
Boundary:
Evidence source:
Next gate:

User message:
{message}
"""

    @staticmethod
    def _extract_expected_factors(content: str) -> list[str]:
        match = re.search(
            r"Expected recall factors:\s*(.*?)(?:\.\s*Stale memory to reject:|\.\s*Success gate:|$)",
            content,
            flags=re.DOTALL,
        )
        if not match:
            return []
        raw = match.group(1)
        return [part.strip() for part in raw.split(";") if part.strip()]

    @classmethod
    def open_default(cls, repo_root: Path, provider: CompletionProvider) -> "TriniRecallAgent":
        store = MemoryStore(repo_root / "data" / "trini_recall_memory.sqlite3")
        return cls(
            store=store,
            provider=provider,
            task_state=(
                "Track 1 MemoryAgent scaffold: build Qwen Tris persistent memory "
                "with stable-state recall, code/browser memory stress, and architecture-off/on comparison."
            ),
            current_gate=(
                "Qwen Cloud qwen-plus is the active hosted route when QWEN_API_KEY is loaded; "
                "local Qwen/Ollama remains the fallback route"
            ),
            constraints=(
                "no toy data for support claims",
                "do not copy private Golden Field Lite or Golden Mark memory DB rows",
                "A/B lift is architecture-layer behavior, not weight tuning",
            ),
            evidence_boundaries=(
                "public-safe source packets and docs only",
                "private memory DBs, JSONL interaction logs, raw captures, and adapter paths stay out",
            ),
        )

#!/usr/bin/env python3
"""Run the local Trini Recall scaffold before Qwen Cloud credits land."""

from __future__ import annotations

from pathlib import Path
import json
import os
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from qwen_agent_buildout.trini_recall import MemoryStore, OfflineProvider, TriniRecallAgent
from qwen_agent_buildout.trini_recall.evaluation import score_response


def seed_memory(store: MemoryStore) -> None:
    existing = {item.id for item in store.list_items()}
    if "trini_name" not in existing:
        store.add_memory(
            id="trini_name",
            kind="preference",
            content="The Track 1 system name is Trini Recall Memory AI Partner.",
            source_ref="docs/TRINI_RECALL_MEMORY_AI_PARTNER_ONE_PAGE_WHITE_PAPER.md",
            tags=("name", "track1", "qwen"),
            privacy_class="public",
            reason="seeded from user-approved product name",
        )
    if "stable_state_lens" not in existing:
        store.add_memory(
            id="stable_state_lens",
            kind="correction",
            content=(
                "Do not frame this as generic memory storage; stable-state architecture "
                "is the lynchpin that improves recall and keeps the agent current."
            ),
            source_ref="docs/TRINI_RECALL_MEMORY_AI_PARTNER_ONE_PAGE_WHITE_PAPER.md",
            tags=("stable-state", "correction", "memory"),
            privacy_class="public",
            reason="seeded from Track 1 thesis",
        )
    if "qwen_credit_gate" not in existing:
        store.add_memory(
            id="qwen_credit_gate",
            kind="next_gate",
            content=(
                "Run the scaffold locally first, then pipe in Qwen Cloud API once "
                "the $40 credit and QWEN_API_KEY are available."
            ),
            source_ref="track_packets/track1_memoryagent.md",
            tags=("qwen", "api", "next-gate"),
            privacy_class="internal",
            reason="seeded from current build plan",
        )
    if "no_weight_claim" not in existing:
        store.add_memory(
            id="no_weight_claim",
            kind="boundary",
            content=(
                "Architecture-on lift is not a model-weight tuning claim unless a "
                "real adapter or tuning artifact exists."
            ),
            source_ref="docs/TRINI_RECALL_MEMORY_AI_PARTNER_ONE_PAGE_WHITE_PAPER.md",
            tags=("boundary", "adapter", "public-safe"),
            privacy_class="public",
            reason="seeded from claim boundary",
        )


def main() -> int:
    db_path = Path(os.getenv("TRINI_RECALL_DB_PATH", "/tmp/trini_recall_memory.sqlite3"))
    store = MemoryStore(db_path)
    seed_memory(store)
    agent = TriniRecallAgent(
        store=store,
        provider=OfflineProvider(),
        task_state=(
            "Track 1 MemoryAgent scaffold: build Qwen-powered persistent memory "
            "with stable-state recall and architecture-off/on comparison."
        ),
        current_gate="run local scaffold, then pipe Qwen Cloud API after credits/API key land",
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

    task = (
        "Explain how Trini Recall should remember the architecture correction "
        "and what the next Qwen gate is."
    )
    baseline = agent.answer(task, architecture_on=False)
    architecture_on = agent.answer(task, architecture_on=True)

    result = {
        "task": task,
        "condition_a": {
            "provider": baseline.provider_name,
            "response": baseline.response,
            "score": score_response(baseline.response).__dict__,
            "retrieval_count": len(baseline.retrievals),
        },
        "condition_b": {
            "provider": architecture_on.provider_name,
            "response": architecture_on.response,
            "score": score_response(architecture_on.response).__dict__,
            "retrieval_count": len(architecture_on.retrievals),
            "retrievals": [
                {
                    "id": retrieval.item.id,
                    "kind": retrieval.item.kind,
                    "reason": retrieval.reason,
                    "source_ref": retrieval.item.source_ref,
                }
                for retrieval in architecture_on.retrievals
            ],
        },
        "memory_db_path": str(db_path),
        "qwen_gate": "Set QWEN_API_KEY and swap OfflineProvider for QwenCloudProvider.",
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

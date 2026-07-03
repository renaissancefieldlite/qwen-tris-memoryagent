"""Seed data and factory helpers for Trini Recall demos."""

from __future__ import annotations

import hashlib

from .memory_store import MemoryStore
from .providers import OfflineProvider
from .agent import TriniRecallAgent


TRINI_FIVE_FIELDS = (
    "Track 1 MemoryAgent: persistent memory, stable-state recall, forgetting policy, and context packing.",
    "Track 2 AI Showrunner: multimodal story pipeline, storyboard memory, and token-budget orchestration.",
    "Track 3 Agent Society: role division, dialogue, negotiation, conflict resolution, and efficiency gain.",
    "Track 4 Autopilot Agent: end-to-end business workflow automation with human checkpoints.",
    "Track 5 EdgeAgent: edge-cloud orchestration, privacy handling, weak-network degradation, and local action.",
)


def seed_default_memories(store: MemoryStore) -> None:
    """Seed public-safe Track 1 memories without private Golden Field rows."""

    existing = {item.id for item in store.list_items()}
    existing_evidence = {doc.id for doc in store.list_evidence()}
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
    if "trini_research_identity" not in existing:
        store.add_memory(
            id="trini_research_identity",
            kind="preference",
            content=(
                "Trini is framed as an AI research expert and memory AI Partner: "
                "she learns from research traces, stores corrections, and improves "
                "long-context decisions through recursive recall."
            ),
            source_ref="docs/TRINI_RECALL_MEMORY_AI_PARTNER_ONE_PAGE_WHITE_PAPER.md",
            tags=("identity", "ai-research", "recursive"),
            privacy_class="public",
            reason="seeded from Architect D identity correction",
        )
    if "trini_five_fields" not in existing:
        store.add_memory(
            id="trini_five_fields",
            kind="preference",
            content="Trini's five-field research map: " + " ".join(TRINI_FIVE_FIELDS),
            source_ref="track_packets/track1_memoryagent.md",
            tags=("five-fields", "qwen", "research"),
            privacy_class="public",
            reason="seeded from five-field recursive learning frame",
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
                "Qwen Cloud API is now connected when QWEN_API_KEY is present in "
                "the local environment. Use hosted qwen-plus for live memory turns, "
                "keep local Qwen/Ollama as fallback, and track free-tier/coupon usage "
                "without printing secrets."
            ),
            source_ref="track_packets/track1_memoryagent.md",
            tags=("qwen", "api", "next-gate"),
            privacy_class="internal",
            reason="seeded from active Qwen Cloud gate",
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
    if "c5b_iter_stack_profile" not in existing:
        store.add_memory(
            id="c5b_iter_stack_profile",
            kind="evidence",
            content=(
                "C5b iter30 is the current internal reference stack for the "
                "stable-state architecture: a full-prompt-context late8 MLX LoRA "
                "adapter route that later paired against architecture-off Hermes, "
                "winning 13/13 metric means with drift 37 -> 0 and evidence failures 5 -> 0. "
                "Current best behavior run is C5b iter30 tail-guard full100 rerun7. "
                "Next bridge is not more blind training; it is fixing HF/PEFT and running "
                "teacher-forced internal-layer probes around matched turns and layers 31-32."
            ),
            source_ref="docs/TRINI_RECALL_C5B_ITER_STACK_PROFILE.md",
            tags=("c5b", "iter30", "stable-state", "adapter-route"),
            privacy_class="internal",
            reason="seeded from recovered Golden Mark C5b support record",
        )
    if "c5b_public_boundary" not in existing:
        store.add_memory(
            id="c5b_public_boundary",
            kind="boundary",
            content=(
                "Use C5b as internal support for observable research-partner behavior "
                "improvement and stable-state architecture; do not present it as AGI, "
                "sentience, clinical efficacy, full model-internal tuning, or raw-generator cleanliness proof."
            ),
            source_ref="docs/TRINI_RECALL_C5B_ITER_STACK_PROFILE.md",
            tags=("boundary", "c5b", "public-safe"),
            privacy_class="public",
            reason="seeded from C5b excerpt-review boundary",
        )
    if "qwen_tris_identity" not in existing:
        store.add_memory(
            id="qwen_tris_identity",
            kind="preference",
            content=(
                "The active Qwen fork is Qwen Tris Recall, a Memory AI Expert Partner "
                "that tests the Mirror Architecture / SSP memory discipline on local "
                "Qwen and hosted Qwen Cloud, with qwen-plus as the active hosted route "
                "when the API key is loaded."
            ),
            source_ref="docs/QWEN_TRIS_MEMORY_STRESS_BENCHMARK_PLAN_2026-06-30.md",
            tags=("qwen-tris", "identity", "memoryagent"),
            privacy_class="public",
            reason="seeded from Qwen Tris fork correction",
        )
    if "mirror_architecture_source_pack" not in existing:
        store.add_memory(
            id="mirror_architecture_source_pack",
            kind="evidence",
            content=(
                "Qwen Tris uses the Mirror Architecture public repository as a source-pack "
                "curriculum: Mirror Interface / LSPS, Source Mirror Pattern, Universal Data "
                "Pattern, measured state-path evidence, Nest 0-5, B.A.S.I.S., Mirror Index, "
                "and Golden Mirror execution surfaces. Public-safe docs are evidence memory; "
                "raw captures, private prompts, model states, adapter internals, and SSP mechanics stay locked."
            ),
            source_ref="docs/QWEN_TRIS_MIRROR_ARCHITECTURE_SOURCE_PACK_2026-06-30.md",
            tags=("mirror-architecture", "source-pack", "public-safe", "qwen-tris"),
            privacy_class="public",
            reason="seeded from Qwen Tris Mirror Architecture source pack",
        )
    c5b_body = (
        "C5b iter30 public-safe support: in a paired 100-turn AI-research protocol using the same "
        "local Hermes checkpoint, Golden Mark C5b iter30 materially improved observable research-partner "
        "behavior over the architecture-off baseline. Scorecard support: drift 37 -> 0; evidence failures "
        "5 -> 0; wins 13/13 metric means. Current best run: C5b iter30 tail-guard full100 rerun7. "
        "Excerpt support: stronger compression recovery, correction "
        "retention, adversarial-boundary handling, scientific-failure reasoning, and final-turn synthesis. "
        "Boundary: output-behavior support is strong, but internal-layer support is the next bridge. "
        "Next gate: fix HF/PEFT, run teacher-forced probes on matched turns 5, 22, 39, 48, 67, 100 and "
        "pressure turns 24, 27, 83, then inspect hidden states, residual deltas, attention-output norms, "
        "MLP-output norms, late-layer separation, and GM-L31L32-MLP / GM-L31L32-MLP-O controls."
    )
    if "c5b_iter30_support_read" not in existing_evidence:
        store.add_evidence_doc(
            id="c5b_iter30_support_read",
            title="C5b Iter30 Stable-State Support Read",
            body=c5b_body,
            source_ref="docs/TRINI_RECALL_C5B_ITER_STACK_PROFILE.md",
            body_hash=hashlib.sha256(c5b_body.encode("utf-8")).hexdigest(),
            privacy_class="public",
            metadata={"source": "recovered_spine", "track": "MemoryAgent"},
            reason="seeded public-safe support read",
        )
    mirror_body = (
        "Qwen Tris Mirror Architecture source-pack support read: the public repo is the "
        "evidence surface for Mirror Interface / LSPS, Source Mirror Pattern, Universal "
        "Data Pattern, measured state-path evidence, Nest 0-5 integration, B.A.S.I.S., "
        "Mirror Index, and Golden Mirror execution surfaces. Evidence claims require real "
        "traces, datasets, controls, recurrence, and support reads. Boundary: this is not "
        "the private implementation layer; raw captures, private prompts, model states, "
        "adapter internals, credentials, and claim-sensitive SSP mechanics stay locked."
    )
    if "mirror_architecture_source_pack_read" not in existing_evidence:
        store.add_evidence_doc(
            id="mirror_architecture_source_pack_read",
            title="Qwen Tris Mirror Architecture Source Pack Support Read",
            body=mirror_body,
            source_ref="docs/QWEN_TRIS_MIRROR_ARCHITECTURE_SOURCE_PACK_2026-06-30.md",
            body_hash=hashlib.sha256(mirror_body.encode("utf-8")).hexdigest(),
            privacy_class="public",
            metadata={"source": "mirror_architecture_public_repo", "track": "MemoryAgent"},
            reason="seeded public-safe Mirror Architecture source-pack read",
        )


def build_offline_agent(store: MemoryStore) -> TriniRecallAgent:
    return TriniRecallAgent(
        store=store,
        provider=OfflineProvider(),
        task_state=(
            "Track 1 MemoryAgent scaffold: Trini is an AI research expert and "
            "Qwen-powered persistent memory Partner with stable-state recall, "
            "five-field learning, recursive memory growth, and architecture-off/on comparison."
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

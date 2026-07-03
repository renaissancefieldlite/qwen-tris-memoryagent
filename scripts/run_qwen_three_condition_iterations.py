#!/usr/bin/env python3
"""Run Qwen Tris three-condition memory iterations.

Condition A: baseline Qwen, prompt only.
Condition B: Qwen + Mirror Architecture / SSP memory packet.
Condition C: tuned SSP route, gated unless an adapter manifest exists.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
SCRIPTS = ROOT / "scripts"
for path in (SRC, SCRIPTS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from qwen_agent_buildout.trini_recall import MemoryStore, QwenCloudProvider, TriniRecallAgent
from qwen_agent_buildout.trini_recall.bootstrap import seed_default_memories
from qwen_agent_buildout.trini_recall.evaluation import score_response
from run_memory_stress_seed_eval import count_prompt_hits, read_rows, seed_rows
from run_qwen_memory_iterations import (
    DEFAULT_MODEL,
    DEFAULT_OLLAMA_BASE,
    build_agent,
    interleave_rows_by_family,
    iteration_query,
    response_hits,
)


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def adapter_status(adapter_manifest: Path | None) -> dict:
    if adapter_manifest is None:
        return {
            "available": False,
            "status": "gated_no_adapter_manifest",
            "path": None,
            "reason": "Condition C requires a real LoRA/adapter/internal-layer receipt before running.",
        }
    if not adapter_manifest.exists():
        return {
            "available": False,
            "status": "gated_adapter_manifest_missing",
            "path": str(adapter_manifest),
            "reason": "Adapter manifest path was supplied but does not exist.",
        }
    return {
        "available": False,
        "status": "gated_adapter_runtime_not_wired",
        "path": str(adapter_manifest),
        "reason": "Adapter manifest exists, but this runner has not wired a tuned Qwen provider yet.",
    }


def build_three_condition_agent(
    store: MemoryStore,
    *,
    provider: str,
    model: str,
    ollama_base: str,
) -> tuple[TriniRecallAgent, str, str]:
    if provider == "ollama":
        return build_agent(store, model, ollama_base), "ollama-qwen", model
    if provider == "qwen_cloud":
        cloud = QwenCloudProvider.from_env()
        if not cloud.api_key:
            raise SystemExit("QWEN_API_KEY is not set; cannot run the Qwen Cloud mirror.")
        agent = TriniRecallAgent(
            store=store,
            provider=cloud,
            task_state=(
                "Qwen Tris MemoryAgent hosted mirror pass: run the same "
                "architecture-off/on memory slice through Qwen API after local "
                "Ollama rehearsal is clean."
            ),
            current_gate="mirror clean local slice through Qwen API",
            constraints=(
                "no toy data for support claims",
                "do not expose private prompts, raw memory rows, adapter internals, or secrets",
                "separate hosted Qwen API generation from Condition C adapter claims",
                "V7 behavior and V8 hidden-state readiness are different gates",
            ),
            evidence_boundaries=(
                "public-safe source packets and docs only",
                "Mirror Architecture repo is evidence surface, not private implementation layer",
                "Qwen API receipt is hosted generation evidence, not adapter tuning evidence",
            ),
        )
        return agent, "qwen-cloud", cloud.model
    raise ValueError(f"Unsupported provider: {provider}")


def run_three_condition(
    rows: list[dict],
    *,
    turns: int,
    provider: str,
    model: str,
    ollama_base: str,
    tmp_db: Path,
    adapter_manifest: Path | None,
    progress_every: int = 0,
) -> dict:
    store = MemoryStore(tmp_db)
    seed_default_memories(store)
    seed_rows(store, rows)
    agent, provider_name, active_model = build_three_condition_agent(
        store,
        provider=provider,
        model=model,
        ollama_base=ollama_base,
    )
    ordered_rows = interleave_rows_by_family(rows)
    selected = [ordered_rows[(turn - 1) % len(ordered_rows)] for turn in range(1, turns + 1)]
    c_status = adapter_status(adapter_manifest)

    results = []
    family_totals: dict[str, dict[str, int]] = {}
    for turn, row in enumerate(selected, start=1):
        query = iteration_query(row, turn)
        expected = [str(item) for item in row.get("expected_recall", [])]
        baseline = agent.answer(query, architecture_on=False)
        stabilized = agent.answer(query, architecture_on=True)
        target_recalled = any(retrieval.item.id == row["task_id"] for retrieval in stabilized.retrievals)
        prompt_hits = count_prompt_hits(stabilized.prompt, expected)
        stabilized_hits = response_hits(stabilized.response, expected)
        baseline_hits = response_hits(baseline.response, expected)
        source_hit = row["source_ref"] in stabilized.prompt
        min_response_hits = min(2, len(expected))
        stabilized_passed = (
            len(baseline.retrievals) == 0
            and target_recalled
            and source_hit
            and prompt_hits >= min(2, len(expected))
            and stabilized_hits >= min_response_hits
            and stabilized_hits >= baseline_hits
        )
        family = row["family"]
        family_totals.setdefault(family, {"condition_b_passed": 0, "total": 0})
        family_totals[family]["total"] += 1
        family_totals[family]["condition_b_passed"] += int(stabilized_passed)
        if progress_every > 0 and (turn == 1 or turn % progress_every == 0 or turn == turns):
            passed_so_far = sum(int(item["condition_b"]["passed"]) for item in results) + int(stabilized_passed)
            print(
                json.dumps(
                    {
                        "event": "progress",
                        "turn": turn,
                        "turns": turns,
                        "condition_b_passed": passed_so_far,
                        "provider": provider_name,
                        "model": active_model,
                    }
                ),
                flush=True,
            )
        results.append(
            {
                "turn": turn,
                "task_id": row["task_id"],
                "family": family,
                "query": query,
                "source_ref": row["source_ref"],
                "expected_recall": expected,
                "condition_a": {
                    "name": "baseline_qwen_prompt_only",
                    "response_hits": baseline_hits,
                    "retrieval_count": len(baseline.retrievals),
                    "score": score_response(baseline.response).__dict__,
                    "response": baseline.response,
                },
                "condition_b": {
                    "name": "qwen_mirror_architecture_stabilized",
                    "response_hits": stabilized_hits,
                    "retrieval_count": len(stabilized.retrievals),
                    "target_recalled": target_recalled,
                    "source_ref_in_prompt": source_hit,
                    "expected_prompt_hits": prompt_hits,
                    "expected_prompt_total": len(expected),
                    "score": score_response(stabilized.response).__dict__,
                    "passed": stabilized_passed,
                    "response": stabilized.response,
                },
                "condition_c": {
                    "name": "qwen_tuned_ssp",
                    **c_status,
                },
            }
        )

    condition_b_passed = sum(int(item["condition_b"]["passed"]) for item in results)
    return {
        "run_id": f"qwen_tris_three_condition_iterations_{utc_stamp()}",
        "provider": provider_name,
        "model": active_model,
        "ollama_base": ollama_base,
        "turns": turns,
        "condition_a": "baseline Qwen, prompt only",
        "condition_b": "Qwen + Mirror Architecture stabilized memory/RAG/SSP packet",
        "condition_c": c_status,
        "condition_b_passed": condition_b_passed,
        "family_totals": family_totals,
        "results": results,
        "boundary": (
            "Three-condition receipt. Condition A and B run on the selected Qwen provider. "
            "Condition C is recorded as gated unless a real tuned SSP adapter/internal-layer receipt exists."
        ),
    }


def write_markdown(receipt: dict, path: Path) -> None:
    lines = [
        f"# Qwen Tris Three-Condition Iterations - {receipt['run_id']}",
        "",
        f"- Provider: `{receipt['provider']}`",
        f"- Model: `{receipt['model']}`",
        f"- Turns: `{receipt['turns']}`",
        f"- Condition B passes: `{receipt['condition_b_passed']}/{receipt['turns']}`",
        f"- Condition C status: `{receipt['condition_c']['status']}`",
        "",
        "## Boundary",
        "",
        receipt["boundary"],
        "",
        "## Conditions",
        "",
        f"- Condition A: {receipt['condition_a']}",
        f"- Condition B: {receipt['condition_b']}",
        f"- Condition C: {receipt['condition_c']['reason']}",
        "",
        "## Family Totals",
        "",
    ]
    for family, totals in sorted(receipt["family_totals"].items()):
        lines.append(f"- `{family}`: Condition B `{totals['condition_b_passed']}/{totals['total']}`")
    lines.extend(
        [
            "",
            "## Side-By-Side Turns",
            "",
            "| Turn | Row | Family | A hits | B hits | B target | B pass | C status |",
            "|---:|---|---|---:|---:|---|---|---|",
        ]
    )
    for item in receipt["results"]:
        lines.append(
            "| {turn} | `{task}` | `{family}` | {a_hits} | {b_hits} | {target} | {b_pass} | `{c_status}` |".format(
                turn=item["turn"],
                task=item["task_id"],
                family=item["family"],
                a_hits=item["condition_a"]["response_hits"],
                b_hits=item["condition_b"]["response_hits"],
                target=item["condition_b"]["target_recalled"],
                b_pass=item["condition_b"]["passed"],
                c_status=item["condition_c"]["status"],
            )
        )
    lines.extend(["", "## Check Rows", ""])
    for item in receipt["results"]:
        if item["condition_b"]["passed"]:
            continue
        lines.extend(
            [
                f"### Turn {item['turn']} / {item['task_id']} - CHECK",
                "",
                f"- Family: `{item['family']}`",
                f"- A hits: `{item['condition_a']['response_hits']}`",
                f"- B hits: `{item['condition_b']['response_hits']}`",
                f"- B target recalled: `{item['condition_b']['target_recalled']}`",
                f"- B source ref in prompt: `{item['condition_b']['source_ref_in_prompt']}`",
                f"- B expected prompt hits: `{item['condition_b']['expected_prompt_hits']}/{item['condition_b']['expected_prompt_total']}`",
                f"- Source ref: `{item['source_ref']}`",
                "",
                "Condition B response excerpt:",
                "",
                "```text",
                item["condition_b"]["response"][:1200],
                "```",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run three-condition Qwen Tris iterations")
    parser.add_argument("--turns", type=int, default=24)
    parser.add_argument("--provider", choices=("ollama", "qwen_cloud"), default="ollama")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--ollama-base", default=DEFAULT_OLLAMA_BASE)
    parser.add_argument("--dataset-dir", type=Path, default=ROOT / "datasets" / "memory_stress")
    parser.add_argument("--out-dir", type=Path, default=ROOT / "data" / "memory_iteration_runs")
    parser.add_argument("--condition-c-adapter-manifest", type=Path)
    parser.add_argument(
        "--progress-every",
        type=int,
        default=25,
        help="Print progress every N turns; use 0 to disable progress output.",
    )
    args = parser.parse_args()

    rows = read_rows(args.dataset_dir)
    if not rows:
        raise SystemExit(f"No memory stress rows found in {args.dataset_dir}")
    args.out_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="qwen_tris_three_condition_") as tmp:
        receipt = run_three_condition(
            rows,
            turns=args.turns,
            provider=args.provider,
            model=args.model,
            ollama_base=args.ollama_base,
            tmp_db=Path(tmp) / "memory.sqlite3",
            adapter_manifest=args.condition_c_adapter_manifest,
            progress_every=args.progress_every,
        )

    json_path = args.out_dir / f"{receipt['run_id']}.json"
    md_path = args.out_dir / f"{receipt['run_id']}.md"
    json_path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    write_markdown(receipt, md_path)
    print(
        json.dumps(
            {
                "json": str(json_path),
                "markdown": str(md_path),
                "condition_b_passed": receipt["condition_b_passed"],
                "turns": receipt["turns"],
                "condition_c_status": receipt["condition_c"]["status"],
                "provider": receipt["provider"],
                "model": receipt["model"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

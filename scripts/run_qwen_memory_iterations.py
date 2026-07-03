#!/usr/bin/env python3
"""Run local Qwen memory iterations before Qwen Cloud API spend."""

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

from qwen_agent_buildout.trini_recall import MemoryStore, OllamaProvider, TriniRecallAgent
from qwen_agent_buildout.trini_recall.bootstrap import seed_default_memories
from qwen_agent_buildout.trini_recall.evaluation import score_response
from run_memory_stress_seed_eval import count_prompt_hits, read_rows, seed_rows


DEFAULT_MODEL = "qwen2.5:3b"
DEFAULT_OLLAMA_BASE = "http://127.0.0.1:11434"


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def build_agent(store: MemoryStore, model: str, ollama_base: str) -> TriniRecallAgent:
    return TriniRecallAgent(
        store=store,
        provider=OllamaProvider(model=model, name="ollama-qwen", api_base=ollama_base),
        task_state=(
            "Qwen Tris MemoryAgent local iteration pass: recover C5B/500 SSP, "
            "Mirror Architecture source pack, SWE, WebArena, long-session, and "
            "external-work memory with architecture-off/on comparison."
        ),
        current_gate="build local Qwen memory iterations before Qwen Cloud API spend",
        constraints=(
            "no toy data for support claims",
            "do not expose private prompts, raw memory rows, adapter internals, or secrets",
            "separate local Ollama behavior from Qwen Cloud benchmark claims",
            "V7 behavior and V8 hidden-state readiness are different gates",
        ),
        evidence_boundaries=(
            "public-safe source packets and docs only",
            "Mirror Architecture repo is evidence surface, not private implementation layer",
            "benchmark receipts are status evidence, not AGI proof",
        ),
    )


def iteration_query(row: dict, turn: int) -> str:
    expected_preview = ", ".join(str(item) for item in row.get("expected_recall", [])[:3])
    target = (
        f"Target memory row: {row['task_id']}. "
        f"Target family: {row['family']}. "
        "Prefer the target row and same-family memories over nearby benchmark rows. "
    )
    variants = (
        (
            f"Memory iteration {turn}. {target}{row['query']} Return exact facts, a Boundary line that rejects stale claims, "
            f"and a Next gate line."
        ),
        (
            f"Context compacted before turn {turn}. The user asks casually but expects continuity. "
            f"{target}Recover {row['task_id']} and answer: {row['query']} Keep stale memory suppressed, "
            f"name the evidence source, and state the next gate."
        ),
        (
            f"Stress turn {turn}: use Qwen Tris memory to answer the active question without "
            f"flattening the architecture. {target}Expected recall themes include "
            f"{expected_preview}. User asks: {row['query']}"
        ),
    )
    return variants[(turn - 1) % len(variants)]


def interleave_rows_by_family(rows: list[dict]) -> list[dict]:
    families: dict[str, list[dict]] = {}
    for row in rows:
        families.setdefault(row["family"], []).append(row)
    ordered: list[dict] = []
    max_len = max((len(items) for items in families.values()), default=0)
    for index in range(max_len):
        for family in sorted(families):
            if index < len(families[family]):
                ordered.append(families[family][index])
    return ordered


def response_hits(response: str, expected_recall: list[str]) -> int:
    lower = response.lower()
    return sum(1 for item in expected_recall if str(item).lower() in lower)


def run_iterations(rows: list[dict], *, turns: int, model: str, ollama_base: str, tmp_db: Path) -> dict:
    store = MemoryStore(tmp_db)
    seed_default_memories(store)
    seed_rows(store, rows)
    agent = build_agent(store, model, ollama_base)
    ordered_rows = interleave_rows_by_family(rows)
    selected = [ordered_rows[(turn - 1) % len(ordered_rows)] for turn in range(1, turns + 1)]

    results = []
    family_totals: dict[str, dict[str, int]] = {}
    for turn, row in enumerate(selected, start=1):
        query = iteration_query(row, turn)
        expected = [str(item) for item in row.get("expected_recall", [])]
        baseline = agent.answer(query, architecture_on=False)
        architecture_on = agent.answer(query, architecture_on=True)
        target_recalled = any(retrieval.item.id == row["task_id"] for retrieval in architecture_on.retrievals)
        prompt_hits = count_prompt_hits(architecture_on.prompt, expected)
        arch_response_hits = response_hits(architecture_on.response, expected)
        baseline_response_hits = response_hits(baseline.response, expected)
        source_hit = row["source_ref"] in architecture_on.prompt
        min_response_hits = min(2, len(expected))
        passed = (
            len(baseline.retrievals) == 0
            and target_recalled
            and source_hit
            and prompt_hits >= min(2, len(expected))
            and arch_response_hits >= min_response_hits
            and arch_response_hits >= baseline_response_hits
        )
        family = row["family"]
        family_totals.setdefault(family, {"passed": 0, "total": 0})
        family_totals[family]["total"] += 1
        family_totals[family]["passed"] += int(passed)
        results.append(
            {
                "turn": turn,
                "task_id": row["task_id"],
                "family": family,
                "query": query,
                "source_ref": row["source_ref"],
                "baseline_retrieval_count": len(baseline.retrievals),
                "architecture_on_retrieval_count": len(architecture_on.retrievals),
                "target_recalled": target_recalled,
                "source_ref_in_prompt": source_hit,
                "expected_prompt_hits": prompt_hits,
                "expected_prompt_total": len(expected),
                "architecture_on_response_hits": arch_response_hits,
                "baseline_response_hits": baseline_response_hits,
                "baseline_score": score_response(baseline.response).__dict__,
                "architecture_on_score": score_response(architecture_on.response).__dict__,
                "provider": architecture_on.provider_name,
                "model": model,
                "passed": passed,
                "architecture_on_response": architecture_on.response,
                "baseline_response": baseline.response,
            }
        )

    return {
        "run_id": f"qwen_tris_local_memory_iterations_{utc_stamp()}",
        "provider": "ollama-qwen",
        "model": model,
        "ollama_base": ollama_base,
        "turns": turns,
        "passed": sum(int(result["passed"]) for result in results),
        "family_totals": family_totals,
        "results": results,
        "boundary": (
            "Local Ollama Qwen memory-iteration receipt. This tests the Qwen Tris "
            "architecture-on memory route before Qwen Cloud API spend; it is not a "
            "Qwen Cloud hosted benchmark claim."
        ),
    }


def write_markdown(receipt: dict, path: Path) -> None:
    lines = [
        f"# Qwen Tris Local Memory Iterations - {receipt['run_id']}",
        "",
        f"- Provider: `{receipt['provider']}`",
        f"- Model: `{receipt['model']}`",
        f"- Turns: `{receipt['turns']}`",
        f"- Passed: `{receipt['passed']}/{receipt['turns']}`",
        "",
        "## Boundary",
        "",
        receipt["boundary"],
        "",
        "## Family Totals",
        "",
    ]
    for family, totals in sorted(receipt["family_totals"].items()):
        lines.append(f"- `{family}`: `{totals['passed']}/{totals['total']}`")
    lines.extend(["", "## Turn Results", ""])
    for item in receipt["results"]:
        status = "PASS" if item["passed"] else "CHECK"
        lines.extend(
            [
                f"### Turn {item['turn']} / {item['task_id']} - {status}",
                "",
                f"- Family: `{item['family']}`",
                f"- Baseline retrievals: `{item['baseline_retrieval_count']}`",
                f"- Architecture-on retrievals: `{item['architecture_on_retrieval_count']}`",
                f"- Target recalled: `{item['target_recalled']}`",
                f"- Source ref in prompt: `{item['source_ref_in_prompt']}`",
                f"- Expected prompt hits: `{item['expected_prompt_hits']}/{item['expected_prompt_total']}`",
                f"- Architecture-on response hits: `{item['architecture_on_response_hits']}`",
                f"- Baseline response hits: `{item['baseline_response_hits']}`",
                f"- Source ref: `{item['source_ref']}`",
                "",
                "Architecture-on response excerpt:",
                "",
                "```text",
                item["architecture_on_response"][:1400],
                "```",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run local Qwen Tris memory iterations")
    parser.add_argument("--turns", type=int, default=12)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--ollama-base", default=DEFAULT_OLLAMA_BASE)
    parser.add_argument("--dataset-dir", type=Path, default=ROOT / "datasets" / "memory_stress")
    parser.add_argument("--out-dir", type=Path, default=ROOT / "data" / "memory_iteration_runs")
    args = parser.parse_args()

    rows = read_rows(args.dataset_dir)
    if not rows:
        raise SystemExit(f"No memory stress rows found in {args.dataset_dir}")
    args.out_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="qwen_tris_local_iters_") as tmp:
        receipt = run_iterations(
            rows,
            turns=args.turns,
            model=args.model,
            ollama_base=args.ollama_base,
            tmp_db=Path(tmp) / "memory.sqlite3",
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
                "passed": receipt["passed"],
                "turns": receipt["turns"],
                "model": receipt["model"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

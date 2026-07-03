#!/usr/bin/env python3
"""Run public-safe memory-stress seeds as baseline-vs-architecture-on checks."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from qwen_agent_buildout.trini_recall import MemoryStore, OfflineProvider, TriniRecallAgent
from qwen_agent_buildout.trini_recall.evaluation import score_response


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def read_rows(dataset_dir: Path) -> list[dict]:
    rows: list[dict] = []
    for path in sorted(dataset_dir.glob("*_seed.jsonl")):
        with path.open("r", encoding="utf-8") as handle:
            for line_no, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                row = json.loads(line)
                row["_seed_file"] = path.name
                row["_line_no"] = line_no
                rows.append(row)
    return rows


def seed_rows(store: MemoryStore, rows: list[dict]) -> None:
    for row in rows:
        expected = "; ".join(str(item) for item in row.get("expected_recall", ()))
        stale = str(row.get("stale_memory_decoy") or "").strip()
        content = (
            f"Task ID: {row['task_id']}. "
            f"Family: {row['family']}. "
            f"Active memory: {row['active_memory']} "
            f"Expected recall factors: {expected}. "
            f"Stale memory to reject: {stale}. "
            f"Success gate: {row['success_gate']}."
        )
        store.add_memory(
            id=row["task_id"],
            kind="memory_stress_seed",
            content=content,
            source_ref=row["source_ref"],
            tags=(row["task_id"], row["family"], row["_seed_file"], "memory-stress"),
            privacy_class="public",
            reason="public-safe memory stress seed",
        )


def count_prompt_hits(prompt: str, expected_recall: list[str]) -> int:
    lower = prompt.lower()
    return sum(1 for item in expected_recall if str(item).lower() in lower)


def run_eval(rows: list[dict], tmp_db: Path) -> dict:
    store = MemoryStore(tmp_db)
    seed_rows(store, rows)
    agent = TriniRecallAgent(
        store=store,
        provider=OfflineProvider(),
        task_state=(
            "Qwen Tris MemoryAgent stress eval: recover public-safe SWE, "
            "WebArena, C5B/500 SSP, long-session, and external-work memory."
        ),
        current_gate="run baseline Qwen memory-off versus Qwen Tris architecture-on memory",
        constraints=(
            "show result path and scored factors only",
            "keep proprietary implementation path locked",
            "do not claim hosted leaderboard placement without external confirmation",
            "do not expose private prompts, raw memory rows, adapter internals, or secrets",
        ),
        evidence_boundaries=(
            "public-safe seed rows only",
            "benchmark receipts are status evidence, not AGI proof",
            "SWE and WebArena final public claims remain behind maintainer or hosted review",
        ),
    )

    results = []
    family_totals: dict[str, dict[str, int]] = {}
    for row in rows:
        baseline = agent.answer(row["query"], architecture_on=False)
        architecture_on = agent.answer(row["query"], architecture_on=True)
        expected_recall = [str(item) for item in row.get("expected_recall", [])]
        prompt_hits = count_prompt_hits(architecture_on.prompt, expected_recall)
        source_hit = row["source_ref"] in architecture_on.prompt
        baseline_clean = len(baseline.retrievals) == 0
        arch_recalled = any(retrieval.item.id == row["task_id"] for retrieval in architecture_on.retrievals)
        min_hits = min(2, len(expected_recall))
        passed = baseline_clean and arch_recalled and source_hit and prompt_hits >= min_hits
        family = row["family"]
        family_totals.setdefault(family, {"passed": 0, "total": 0})
        family_totals[family]["total"] += 1
        family_totals[family]["passed"] += int(passed)
        results.append(
            {
                "task_id": row["task_id"],
                "family": family,
                "seed_file": row["_seed_file"],
                "query": row["query"],
                "source_ref": row["source_ref"],
                "baseline_retrieval_count": len(baseline.retrievals),
                "architecture_on_retrieval_count": len(architecture_on.retrievals),
                "architecture_on_recalled_target": arch_recalled,
                "expected_prompt_hits": prompt_hits,
                "expected_prompt_total": len(expected_recall),
                "source_ref_in_prompt": source_hit,
                "baseline_score": score_response(baseline.response).__dict__,
                "architecture_on_score": score_response(architecture_on.response).__dict__,
                "passed": passed,
                "boundary": "offline scaffold eval; swap provider to Qwen Cloud after API receipt",
            }
        )

    return {
        "run_id": f"qwen_tris_memory_stress_seed_{utc_stamp()}",
        "provider": "offline-deterministic",
        "row_count": len(rows),
        "passed": sum(int(item["passed"]) for item in results),
        "family_totals": family_totals,
        "results": results,
        "boundary": (
            "This is a public-safe offline memory harness receipt. It validates "
            "retrieval/scoring plumbing before Qwen Cloud is attached; it is not "
            "a Qwen Cloud benchmark claim."
        ),
    }


def write_markdown(receipt: dict, path: Path) -> None:
    lines = [
        f"# Qwen Tris Memory Stress Seed Eval - {receipt['run_id']}",
        "",
        f"- Provider: `{receipt['provider']}`",
        f"- Rows: `{receipt['row_count']}`",
        f"- Passed: `{receipt['passed']}/{receipt['row_count']}`",
        "",
        "## Family Totals",
        "",
    ]
    for family, totals in sorted(receipt["family_totals"].items()):
        lines.append(f"- `{family}`: `{totals['passed']}/{totals['total']}`")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            receipt["boundary"],
            "",
            "## Row Results",
            "",
        ]
    )
    for item in receipt["results"]:
        status = "PASS" if item["passed"] else "CHECK"
        lines.extend(
            [
                f"### {item['task_id']} - {status}",
                "",
                f"- Family: `{item['family']}`",
                f"- Baseline retrievals: `{item['baseline_retrieval_count']}`",
                f"- Architecture-on retrievals: `{item['architecture_on_retrieval_count']}`",
                f"- Target recalled: `{item['architecture_on_recalled_target']}`",
                f"- Expected prompt hits: `{item['expected_prompt_hits']}/{item['expected_prompt_total']}`",
                f"- Source ref in prompt: `{item['source_ref_in_prompt']}`",
                f"- Source ref: `{item['source_ref']}`",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dataset-dir",
        type=Path,
        default=ROOT / "datasets" / "memory_stress",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "data" / "memory_stress_runs",
    )
    args = parser.parse_args()

    rows = read_rows(args.dataset_dir)
    if not rows:
        raise SystemExit(f"No seed rows found in {args.dataset_dir}")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="qwen_tris_memory_stress_") as tmp:
        receipt = run_eval(rows, Path(tmp) / "memory.sqlite3")

    json_path = args.out_dir / f"{receipt['run_id']}.json"
    md_path = args.out_dir / f"{receipt['run_id']}.md"
    json_path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    write_markdown(receipt, md_path)

    print(json.dumps({"json": str(json_path), "markdown": str(md_path), "passed": receipt["passed"], "row_count": receipt["row_count"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

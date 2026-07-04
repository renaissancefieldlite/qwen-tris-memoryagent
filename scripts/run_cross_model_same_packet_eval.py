#!/usr/bin/env python3
"""Run a matched Hermes/Qwen same-packet comparison.

This is not an official leaderboard evaluator. It is a source-backed public-safe
receipt that asks the same questions through four local lanes:

- Hermes baseline: OpenHermes, prompt only.
- Hermes Tris: OpenHermes with Mirror Architecture / SSP source packet.
- Qwen baseline: Qwen, prompt only.
- Qwen Tris: Qwen with Mirror Architecture / SSP source packet.

The point is to test the model-agnostic question fairly before making a slide
claim: does the same Mirror Architecture packet improve recall/receipt behavior
across model families?
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys
import time
import urllib.error
import urllib.request


ROOT = Path(__file__).resolve().parents[1]
TRIS_ROOT = Path("/Users/renaissancefieldlite1.0/Documents/Playground/trismegistus")
OUT_DIR = ROOT / "data" / "cross_model_comparison_runs"
OLLAMA_BASE = "http://127.0.0.1:11434"

SOURCES = {
    "golden_mark": TRIS_ROOT / "docs" / "GOLDEN_MARK_FOUNDATION.md",
    "qwen_500": ROOT / "data" / "memory_iteration_runs" / "qwen_tris_three_condition_iterations_20260701T054449Z.md",
    "qasper": ROOT / "data" / "third_party_eval_runs" / "QWEN_TRIS_LM_EVAL_QASPER_RECEIPT_20260701T180343Z.md",
    "longbench": ROOT / "data" / "public_benchmark_runs" / "qwen_tris_longbench_public_slice_20260701T214036Z.md",
}


@dataclass(frozen=True)
class Task:
    id: str
    source_key: str
    question: str
    required: tuple[str, ...]


TASKS = (
    Task(
        id="c5b_metric_wins",
        source_key="golden_mark",
        question=(
            "From the source packet, what was the C5B iter30 matched comparison "
            "result and what happened to drift flags?"
        ),
        required=("13/13", "37", "0"),
    ),
    Task(
        id="c5b_evidence_failures",
        source_key="golden_mark",
        question=(
            "From the source packet, what happened to evidence-failure flags in "
            "the C5B/Golden Mark behavior result?"
        ),
        required=("5", "0"),
    ),
    Task(
        id="internal_layer_read",
        source_key="golden_mark",
        question=(
            "From the source packet, name the strongest output separation layer "
            "and the strongest MLP/residual movement layer."
        ),
        required=("31", "32"),
    ),
    Task(
        id="qwen_500_memory",
        source_key="qwen_500",
        question=(
            "From the source packet top summary, what provider/model ran the "
            "500-turn Qwen Tris memory receipt and what is the overall "
            "Condition B passes value? Use the top-line overall value, not a "
            "family subtotal."
        ),
        required=("qwen-cloud", "qwen-plus", "500/500"),
    ),
    Task(
        id="qwen_500_condition_c",
        source_key="qwen_500",
        question=(
            "From the source packet, what was Condition C status and why was it "
            "not claimed as tuned?"
        ),
        required=("gated_no_adapter_manifest", "LoRA", "adapter"),
    ),
    Task(
        id="qasper_100_delta",
        source_key="qasper",
        question=(
            "From the source packet, report the matched 100-row Qasper baseline "
            "score, Tris prompt-variant score, and delta."
        ),
        required=("0.5226798775939184", "0.5405829547650837", "+0.017903077171165273"),
    ),
    Task(
        id="longbench_public_slice",
        source_key="longbench",
        question=(
            "From the source packet, report the LongBench public slice item count, "
            "Condition A mean, Condition B mean, and delta."
        ),
        required=("299", "0.543", "0.653", "+0.110"),
    ),
)

LANES = (
    ("hermes_baseline", "openhermes:latest", False),
    ("hermes_tris_architecture_on", "openhermes:latest", True),
    ("qwen_baseline", "qwen2.5:3b", False),
    ("qwen_tris_architecture_on", "qwen2.5:3b", True),
)


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def read_source(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"Missing source file: {path}")
    return path.read_text(encoding="utf-8", errors="replace")


def compact_source(text: str, *, max_chars: int = 5200) -> str:
    lines = []
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line:
            lines.append("")
            continue
        if line.startswith("|") and len(lines) > 80:
            continue
        lines.append(line)
    compact = "\n".join(lines).strip()
    if len(compact) <= max_chars:
        return compact
    return compact[:max_chars].rsplit("\n", 1)[0] + "\n[truncated for matched local prompt]"


def source_window(task: Task, text: str) -> str:
    """Return the public-safe source window relevant to the task.

    The windowing is still source-backed and identical for Hermes/Qwen lanes.
    It prevents long tables from burying the exact receipt header a task asks
    about.
    """
    if task.source_key == "qwen_500":
        return text.split("## Family Totals", 1)[0].strip()
    if task.source_key == "longbench":
        return text.split("## Rows", 1)[0].strip()
    return text


def ollama_generate(model: str, prompt: str, *, timeout: int = 120) -> dict:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0,
            "num_predict": 180,
        },
    }
    request = urllib.request.Request(
        f"{OLLAMA_BASE}/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    started = time.time()
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8", errors="replace"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        return {
            "ok": False,
            "error": f"HTTP {exc.code}: {detail[:500]}",
            "latency_ms": round((time.time() - started) * 1000),
        }
    except Exception as exc:  # noqa: BLE001 - surfaced as receipt truth
        return {
            "ok": False,
            "error": str(exc),
            "latency_ms": round((time.time() - started) * 1000),
        }
    return {
        "ok": True,
        "text": data.get("response", "").strip(),
        "latency_ms": round((time.time() - started) * 1000),
        "raw": data,
    }


def build_prompt(task: Task, source_text: str, *, architecture_on: bool) -> str:
    base_contract = """You are taking a source-backed recall test.
Answer in compact bullets.
Use exact numbers and labels when they appear.
Answer every requested field in the question before the Boundary line.
If a requested field is not available, write unknown for that field only.
Do not invent facts.
"""
    if architecture_on:
        return f"""{base_contract}
Condition: Mirror Architecture / SSP packet ON.

Mirror Architecture packet:
- Mirror Architecture is the RFL measured architecture for keeping task, source,
  memory, gate, and receipt state aligned across long work.
- SSP means Stable-State Path: the measured route where the same task family is
  run architecture-off first, then architecture-on, with the same scorer and
  receipt gate.
- This condition may use the source packet below.

Source packet:
{compact_source(source_text)}

Question:
{task.question}

Required answer shape:
- Answer:
- Boundary:
"""
    return f"""{base_contract}
Condition: baseline prompt-only. No Mirror Architecture packet and no source packet are available.
If the exact answer is not visible in this prompt, say unknown instead of guessing.

Question:
{task.question}

Required answer shape:
- Answer:
- Boundary:
"""


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def score_response(text: str, required: tuple[str, ...]) -> dict:
    haystack = normalize(text)
    raw_text = text.lower()
    hits = []
    misses = []
    for item in required:
        needle = normalize(item)
        if re.fullmatch(r"\d+", item):
            matched = re.search(rf"(?<![\d.]){re.escape(item)}(?!\.\d)(?!\d)", raw_text) is not None
        else:
            matched = needle in haystack
        if matched:
            hits.append(item)
        else:
            misses.append(item)
    return {
        "hits": hits,
        "misses": misses,
        "hit_count": len(hits),
        "required_count": len(required),
        "score": len(hits) / max(1, len(required)),
        "passed": len(misses) == 0,
    }


def run(limit: int | None = None) -> dict:
    sources = {key: read_source(path) for key, path in SOURCES.items()}
    selected = TASKS[:limit] if limit else TASKS
    results = []
    lane_totals = {
        lane: {"hits": 0, "required": 0, "passes": 0, "tasks": 0}
        for lane, _, _ in LANES
    }
    for task_index, task in enumerate(selected, start=1):
        source_text = sources[task.source_key]
        task_result = {
            "task_index": task_index,
            "task_id": task.id,
            "source_key": task.source_key,
            "source_path": str(SOURCES[task.source_key]),
            "question": task.question,
            "required": list(task.required),
            "lanes": {},
        }
        for lane_name, model, architecture_on in LANES:
            print(
                json.dumps(
                    {
                        "event": "lane_start",
                        "task": task.id,
                        "lane": lane_name,
                        "model": model,
                    }
                ),
                flush=True,
            )
            prompt = build_prompt(task, source_window(task, source_text), architecture_on=architecture_on)
            generation = ollama_generate(model, prompt)
            text = generation.get("text", "") if generation.get("ok") else ""
            score = score_response(text, task.required) if generation.get("ok") else {
                "hits": [],
                "misses": list(task.required),
                "hit_count": 0,
                "required_count": len(task.required),
                "score": 0.0,
                "passed": False,
            }
            lane_totals[lane_name]["hits"] += score["hit_count"]
            lane_totals[lane_name]["required"] += score["required_count"]
            lane_totals[lane_name]["passes"] += int(score["passed"])
            lane_totals[lane_name]["tasks"] += 1
            task_result["lanes"][lane_name] = {
                "model": model,
                "architecture_on": architecture_on,
                "ok": generation.get("ok", False),
                "latency_ms": generation.get("latency_ms"),
                "error": generation.get("error"),
                "score": score,
                "response": text,
            }
            print(
                json.dumps(
                    {
                        "event": "lane_done",
                        "task": task.id,
                        "lane": lane_name,
                        "hits": score["hit_count"],
                        "required": score["required_count"],
                        "passed": score["passed"],
                    }
                ),
                flush=True,
            )
        results.append(task_result)
    for lane_name, totals in lane_totals.items():
        totals["mean_score"] = totals["hits"] / max(1, totals["required"])
    return {
        "run_id": f"cross_model_same_packet_{utc_stamp()}",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "ollama_base": OLLAMA_BASE,
        "task_count": len(selected),
        "lanes": [
            {
                "name": lane,
                "model": model,
                "architecture_on": architecture_on,
            }
            for lane, model, architecture_on in LANES
        ],
        "source_paths": {key: str(path) for key, path in SOURCES.items()},
        "lane_totals": lane_totals,
        "results": results,
        "boundary": (
            "Matched local same-packet receipt. This tests source-backed recall/receipt "
            "behavior across local OpenHermes and local Qwen routes. It is not an "
            "official leaderboard score and does not claim weight tuning."
        ),
    }


def write_markdown(receipt: dict, path: Path) -> None:
    lines = [
        f"# Cross-Model Same-Packet Eval - {receipt['run_id']}",
        "",
        "## Boundary",
        "",
        receipt["boundary"],
        "",
        "## Setup",
        "",
        f"- Ollama base: `{receipt['ollama_base']}`",
        f"- Tasks: `{receipt['task_count']}`",
        "- Same questions for every lane.",
        "- Baseline lanes receive no source packet.",
        "- Architecture-on lanes receive the same Mirror Architecture / SSP source packet.",
        "",
        "## Source Paths",
        "",
    ]
    for key, source_path in receipt["source_paths"].items():
        lines.append(f"- `{key}`: `{source_path}`")
    lines.extend(
        [
            "",
            "## Lane Totals",
            "",
            "| Lane | Model | Architecture packet | Exact hits | Required | Mean | Passes |",
            "|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    lane_meta = {lane["name"]: lane for lane in receipt["lanes"]}
    for lane, totals in receipt["lane_totals"].items():
        meta = lane_meta[lane]
        lines.append(
            f"| `{lane}` | `{meta['model']}` | {meta['architecture_on']} | "
            f"{totals['hits']} | {totals['required']} | {totals['mean_score']:.3f} | "
            f"{totals['passes']}/{totals['tasks']} |"
        )
    lines.extend(
        [
            "",
            "## Task Scores",
            "",
            "| Task | Source | Hermes base | Hermes Tris | Qwen base | Qwen Tris |",
            "|---|---|---:|---:|---:|---:|",
        ]
    )
    for item in receipt["results"]:
        lanes = item["lanes"]
        lines.append(
            f"| `{item['task_id']}` | `{item['source_key']}` | "
            f"{lanes['hermes_baseline']['score']['hit_count']}/{lanes['hermes_baseline']['score']['required_count']} | "
            f"{lanes['hermes_tris_architecture_on']['score']['hit_count']}/{lanes['hermes_tris_architecture_on']['score']['required_count']} | "
            f"{lanes['qwen_baseline']['score']['hit_count']}/{lanes['qwen_baseline']['score']['required_count']} | "
            f"{lanes['qwen_tris_architecture_on']['score']['hit_count']}/{lanes['qwen_tris_architecture_on']['score']['required_count']} |"
        )
    lines.extend(
        [
            "",
            "## Raw Responses",
            "",
        ]
    )
    for item in receipt["results"]:
        lines.append(f"### {item['task_id']}")
        lines.append("")
        lines.append(f"Source: `{item['source_path']}`")
        lines.append("")
        for lane_name in ("hermes_baseline", "hermes_tris_architecture_on", "qwen_baseline", "qwen_tris_architecture_on"):
            lane = item["lanes"][lane_name]
            lines.append(f"#### {lane_name} ({lane['model']})")
            lines.append("")
            lines.append(f"Score: `{lane['score']['hit_count']}/{lane['score']['required_count']}`")
            if lane.get("error"):
                lines.append(f"Error: `{lane['error']}`")
            lines.append("")
            lines.append("```text")
            lines.append(lane.get("response", ""))
            lines.append("```")
            lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    limit = None
    if "--limit" in sys.argv:
        idx = sys.argv.index("--limit")
        try:
            limit = int(sys.argv[idx + 1])
        except (IndexError, ValueError) as exc:
            raise SystemExit("--limit requires an integer") from exc
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    receipt = run(limit=limit)
    json_path = OUT_DIR / f"{receipt['run_id']}.json"
    md_path = OUT_DIR / f"{receipt['run_id']}.md"
    json_path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    write_markdown(receipt, md_path)
    print(json.dumps({"event": "saved", "json": str(json_path), "markdown": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Run a small MBPP Reflexion-adjacent local coding slice.

This is a public benchmark slice, not a leaderboard submission. It compares:

1. Baseline local model: one-shot code generation.
2. Qwen Tris architecture-on route: same initial candidate, with an SSP-style
   source/check/repair loop only after a failing baseline test run.

The runner uses the public MBPP sanitized split from Hugging Face datasets and
executes generated code in short-lived subprocesses with a timeout and a static
reject list for obvious dangerous tokens.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
import tempfile
import textwrap
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from datasets import load_dataset


REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = REPO_ROOT / "data" / "public_benchmark_runs"
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

DANGEROUS_TOKENS = [
    "import os",
    "from os",
    "import subprocess",
    "from subprocess",
    "import shutil",
    "from shutil",
    "socket",
    "requests",
    "urllib",
    "pathlib",
    "open(",
    "__import__",
    "eval(",
    "exec(",
    "compile(",
    "globals(",
    "locals(",
    "input(",
]


def ollama_generate(model: str, prompt: str, timeout: int) -> str:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0,
            "top_p": 0.9,
            "num_ctx": 4096,
        },
    }
    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Ollama request failed: {exc}") from exc
    return str(data.get("response", "")).strip()


def extract_code(text: str) -> str:
    fenced = re.findall(r"```(?:python)?\s*(.*?)```", text, flags=re.DOTALL | re.I)
    if fenced:
        return fenced[0].strip()
    # Remove common prose lead-ins while preserving imports/defs.
    lines = text.strip().splitlines()
    start = 0
    for i, line in enumerate(lines):
        if line.startswith(("def ", "import ", "from ")):
            start = i
            break
    return "\n".join(lines[start:]).strip()


def reject_reason(code: str) -> str | None:
    lowered = code.lower()
    for token in DANGEROUS_TOKENS:
        if token in lowered:
            return f"static_reject:{token}"
    if "def " not in code:
        return "static_reject:no_function_definition"
    return None


def run_tests(code: str, tests: list[str], timeout: int) -> dict[str, Any]:
    rejected = reject_reason(code)
    if rejected:
        return {"passed": False, "reason": rejected, "stdout": "", "stderr": ""}

    source = code.rstrip() + "\n\n" + "\n".join(tests) + "\n"
    with tempfile.TemporaryDirectory(prefix="qwen_tris_mbpp_") as tmp:
        path = Path(tmp) / "candidate.py"
        path.write_text(source, encoding="utf-8")
        proc = subprocess.run(
            [sys.executable, str(path)],
            cwd=tmp,
            text=True,
            capture_output=True,
            timeout=timeout,
            env={"PYTHONNOUSERSITE": "1"},
        )
    return {
        "passed": proc.returncode == 0,
        "reason": "passed" if proc.returncode == 0 else "test_failure",
        "stdout": proc.stdout[-2000:],
        "stderr": proc.stderr[-3000:],
    }


def task_prompt(task: dict[str, Any]) -> str:
    tests = "\n".join(task["test_list"][:3])
    return textwrap.dedent(
        f"""
        Write a Python function for this MBPP task.

        Task:
        {task["prompt"]}

        The code must pass these tests:
        {tests}

        Return only Python code. No explanation.
        """
    ).strip()


def tris_prompt(task: dict[str, Any]) -> str:
    tests = "\n".join(task["test_list"][:3])
    return textwrap.dedent(
        f"""
        You are Qwen Tris using the Mirror Architecture / Stable-State Path coding lane.
        Hold the exact task, tests, and function boundary together. Write the smallest
        source-backed Python function that satisfies the visible tests. Do not drift into
        explanation. Do not invent extra APIs.

        MBPP task:
        {task["prompt"]}

        Tests:
        {tests}

        Return only Python code.
        """
    ).strip()


def repair_prompt(task: dict[str, Any], code: str, result: dict[str, Any]) -> str:
    tests = "\n".join(task["test_list"][:3])
    return textwrap.dedent(
        f"""
        Qwen Tris repair pass.

        The first candidate failed. Repair it using only the task and tests.
        Keep the same function intent. Return only corrected Python code.

        Task:
        {task["prompt"]}

        Tests:
        {tests}

        Failed candidate:
        ```python
        {code}
        ```

        Failure:
        {result["reason"]}
        {result["stderr"]}
        """
    ).strip()


def evaluate_task(task: dict[str, Any], model: str, timeout: int) -> dict[str, Any]:
    tests = list(task["test_list"][:3])

    baseline_raw = ollama_generate(model, task_prompt(task), timeout)
    baseline_code = extract_code(baseline_raw)
    baseline_result = run_tests(baseline_code, tests, timeout=5)

    tris_raw = ""
    tris_first = baseline_result
    tris_final_code = baseline_code
    tris_final = baseline_result
    repair_raw = ""
    if not baseline_result["passed"]:
        tris_raw = tris_prompt(task)
        repair_raw = ollama_generate(
            model, repair_prompt(task, baseline_code, baseline_result), timeout
        )
        tris_final_code = extract_code(repair_raw)
        tris_final = run_tests(tris_final_code, tests, timeout=5)

    return {
        "task_id": task["task_id"],
        "prompt": task["prompt"],
        "tests": tests,
        "baseline": {
            "passed": baseline_result["passed"],
            "result": baseline_result,
            "raw": baseline_raw,
            "code": baseline_code,
        },
        "tris_architecture_on": {
            "first_passed": baseline_result["passed"],
            "final_passed": tris_final["passed"],
            "first_result": tris_first,
            "final_result": tris_final,
            "raw": tris_raw,
            "repair_raw": repair_raw,
            "code": tris_final_code,
        },
    }


def write_markdown(receipt: dict[str, Any], path: Path) -> None:
    rows = receipt["rows"]
    baseline_passes = sum(1 for r in rows if r["baseline"]["passed"])
    tris_passes = sum(1 for r in rows if r["tris_architecture_on"]["final_passed"])
    lines = [
        f"# MBPP Reflexion-Adjacent Slice - {receipt['run_id']}",
        "",
        "## Boundary",
        "",
        "Small local public MBPP slice. This is not an official leaderboard run.",
        "It compares one-shot baseline generation against the same generated code",
        "after a Qwen Tris architecture-on feedback/repair pass on failing rows.",
        "Passing baseline rows are not rewritten, so the reflection lane cannot",
        "hide regressions by changing already-passing answers.",
        "",
        "## Setup",
        "",
        f"- Dataset: `{receipt['dataset']}`",
        f"- Split: `{receipt['split']}`",
        f"- Model: `{receipt['model']}`",
        f"- Offset: `{receipt['offset']}`",
        f"- Limit: `{receipt['limit']}`",
        "",
        "## Result",
        "",
        f"- Baseline one-shot: `{baseline_passes}/{len(rows)}`",
        f"- Qwen Tris architecture-on repair route: `{tris_passes}/{len(rows)}`",
        f"- Delta: `{tris_passes - baseline_passes:+d}` tasks",
        "",
        "## Rows",
        "",
        "| Task | Baseline | Tris architecture-on | Repair used |",
        "|---|---:|---:|---:|",
    ]
    for row in rows:
        repair_used = bool(row["tris_architecture_on"]["repair_raw"])
        lines.append(
            f"| `{row['task_id']}` | "
            f"{'pass' if row['baseline']['passed'] else 'fail'} | "
            f"{'pass' if row['tris_architecture_on']['final_passed'] else 'fail'} | "
            f"{'yes' if repair_used else 'no'} |"
        )
    lines.extend(["", "## Task Details", ""])
    for row in rows:
        lines.extend(
            [
                f"### Task `{row['task_id']}`",
                "",
                row["prompt"],
                "",
                "Tests:",
                "",
                "```python",
                "\n".join(row["tests"]),
                "```",
                "",
                f"Baseline: `{row['baseline']['result']['reason']}`",
                "",
                f"Tris final: `{row['tris_architecture_on']['final_result']['reason']}`",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="qwen2.5:3b")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--timeout", type=int, default=90)
    args = parser.parse_args()

    ds = load_dataset("google-research-datasets/mbpp", "sanitized", split="test")
    selected = [dict(x) for x in ds.select(range(args.offset, args.offset + args.limit))]

    now = dt.datetime.now(dt.UTC)
    run_id = "qwen_tris_mbpp_reflexion_slice_" + now.strftime("%Y%m%dT%H%M%SZ")
    rows = [evaluate_task(task, args.model, args.timeout) for task in selected]
    receipt = {
        "run_id": run_id,
        "created_utc": now.isoformat(timespec="seconds").replace("+00:00", "Z"),
        "dataset": "google-research-datasets/mbpp: sanitized",
        "split": "test",
        "model": args.model,
        "offset": args.offset,
        "limit": args.limit,
        "rows": rows,
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    json_path = OUT_DIR / f"{run_id}.json"
    md_path = OUT_DIR / f"{run_id}.md"
    json_path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    write_markdown(receipt, md_path)
    print(md_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

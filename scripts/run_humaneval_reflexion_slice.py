#!/usr/bin/env python3
"""Run a small HumanEval-instruct Reflexion-adjacent local coding slice.

This runner mirrors the public HumanEval-instruct shape from the local
lm-evaluation-harness inventory, while keeping execution bounded and honest:

1. Baseline local model writes code once.
2. The generated code is tested against the public HumanEval test.
3. Qwen Tris architecture-on only receives feedback for failing baseline rows.
4. Passing baseline rows are preserved and never rewritten.

This is not an official HumanEval leaderboard run.
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
        "options": {"temperature": 0, "top_p": 0.9, "num_ctx": 4096},
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
    lines = text.strip().splitlines()
    start = 0
    for i, line in enumerate(lines):
        if line.startswith(("from typing", "import ", "def ")):
            start = i
            break
    return "\n".join(lines[start:]).strip()


def reject_reason(code: str, entry_point: str) -> str | None:
    lowered = code.lower()
    for token in DANGEROUS_TOKENS:
        if token in lowered:
            return f"static_reject:{token}"
    if f"def {entry_point}" not in code:
        return f"static_reject:missing_entry_point:{entry_point}"
    return None


def run_tests(code: str, test_source: str, entry_point: str, timeout: int) -> dict[str, Any]:
    rejected = reject_reason(code, entry_point)
    if rejected:
        return {"passed": False, "reason": rejected, "stdout": "", "stderr": ""}

    source = code.rstrip() + "\n\n" + test_source.strip() + f"\n\ncheck({entry_point})\n"
    with tempfile.TemporaryDirectory(prefix="qwen_tris_humaneval_") as tmp:
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


def baseline_prompt(task: dict[str, Any]) -> str:
    return textwrap.dedent(
        f"""
        Write a solution to the following HumanEval problem and make sure it
        passes the tests. Return only complete Python code.

        ```python
        {task["prompt"]}
        ```
        """
    ).strip()


def repair_prompt(task: dict[str, Any], code: str, result: dict[str, Any]) -> str:
    return textwrap.dedent(
        f"""
        Qwen Tris HumanEval repair pass.

        Use the Mirror Architecture / Stable-State Path coding lane:
        hold the original function signature, the docstring intent, and the
        test failure together. Repair the code with the smallest correct change.
        Return only complete Python code.

        Original prompt:
        ```python
        {task["prompt"]}
        ```

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
    baseline_raw = ollama_generate(model, baseline_prompt(task), timeout)
    baseline_code = extract_code(baseline_raw)
    baseline_result = run_tests(
        baseline_code, task["test"], task["entry_point"], timeout=5
    )

    repair_raw = ""
    final_code = baseline_code
    final_result = baseline_result
    if not baseline_result["passed"]:
        repair_raw = ollama_generate(
            model, repair_prompt(task, baseline_code, baseline_result), timeout
        )
        final_code = extract_code(repair_raw)
        final_result = run_tests(final_code, task["test"], task["entry_point"], timeout=5)

    return {
        "task_id": task["task_id"],
        "entry_point": task["entry_point"],
        "prompt": task["prompt"],
        "baseline": {
            "passed": baseline_result["passed"],
            "result": baseline_result,
            "raw": baseline_raw,
            "code": baseline_code,
        },
        "tris_architecture_on": {
            "final_passed": final_result["passed"],
            "final_result": final_result,
            "repair_raw": repair_raw,
            "code": final_code,
        },
    }


def write_markdown(receipt: dict[str, Any], path: Path) -> None:
    rows = receipt["rows"]
    baseline_passes = sum(1 for r in rows if r["baseline"]["passed"])
    tris_passes = sum(1 for r in rows if r["tris_architecture_on"]["final_passed"])
    lines = [
        f"# HumanEval-Instruct Reflexion-Adjacent Slice - {receipt['run_id']}",
        "",
        "## Boundary",
        "",
        "Small local public HumanEval-instruct slice. This is not an official",
        "leaderboard run. It compares baseline one-shot code generation against",
        "the same generated code after a Qwen Tris architecture-on repair pass",
        "on failing rows only.",
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
        "| Task | Entry point | Baseline | Tris architecture-on | Repair used |",
        "|---|---|---:|---:|---:|",
    ]
    for row in rows:
        repair_used = bool(row["tris_architecture_on"]["repair_raw"])
        lines.append(
            f"| `{row['task_id']}` | `{row['entry_point']}` | "
            f"{'pass' if row['baseline']['passed'] else 'fail'} | "
            f"{'pass' if row['tris_architecture_on']['final_passed'] else 'fail'} | "
            f"{'yes' if repair_used else 'no'} |"
        )
    lines.extend(["", "## Failure/Repair Notes", ""])
    for row in rows:
        if row["baseline"]["passed"] and row["tris_architecture_on"]["final_passed"]:
            continue
        lines.extend(
            [
                f"### `{row['task_id']}`",
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
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--timeout", type=int, default=90)
    args = parser.parse_args()

    ds = load_dataset("openai/openai_humaneval", split="test")
    selected = [dict(x) for x in ds.select(range(args.offset, args.offset + args.limit))]
    now = dt.datetime.now(dt.UTC)
    run_id = "qwen_tris_humaneval_reflexion_slice_" + now.strftime("%Y%m%dT%H%M%SZ")
    rows = [evaluate_task(task, args.model, args.timeout) for task in selected]
    receipt = {
        "run_id": run_id,
        "created_utc": now.isoformat(timespec="seconds").replace("+00:00", "Z"),
        "dataset": "openai/openai_humaneval",
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

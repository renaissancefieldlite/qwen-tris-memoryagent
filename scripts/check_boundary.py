#!/usr/bin/env python3
"""Check for obvious private-source artifacts before packaging."""

from __future__ import annotations

import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
BLOCKED_NAMES = {
    ".env",
    "agent_config.yaml",
}
BLOCKED_SUFFIXES = {
    ".sqlite",
    ".sqlite3",
    ".db",
    ".jsonl",
}
BLOCKED_PARTS = {
    "private",
    "secrets",
    "raw",
    "captures",
    "outputs",
}
SKIP_PARTS = {
    ".git",
    "__pycache__",
    "runtime",
    ".venv",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "node_modules",
}


def is_allowed_public_seed_jsonl(rel: pathlib.Path) -> bool:
    return (
        len(rel.parts) == 3
        and rel.parts[0] == "datasets"
        and rel.parts[1] == "memory_stress"
        and rel.name.endswith("_seed.jsonl")
    )


def main() -> int:
    blocked: list[pathlib.Path] = []
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        parts = set(rel.parts)
        if any(part in SKIP_PARTS for part in parts):
            continue
        if any(part in BLOCKED_PARTS for part in parts):
            blocked.append(rel)
            continue
        if path.name in BLOCKED_NAMES:
            blocked.append(rel)
            continue
        if path.suffix == ".jsonl" and is_allowed_public_seed_jsonl(rel):
            continue
        if path.suffix in BLOCKED_SUFFIXES:
            blocked.append(rel)

    if blocked:
        print("Blocked private or runtime artifacts found:")
        for rel in blocked[:100]:
            print(f"- {rel}")
        if len(blocked) > 100:
            print(f"... {len(blocked) - 100} more")
        return 1

    print("Boundary check passed: no obvious private/runtime artifacts found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

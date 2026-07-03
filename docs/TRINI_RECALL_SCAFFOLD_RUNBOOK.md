# Trini Recall Scaffold Runbook

Status: local scaffold, ready before Qwen Cloud credits/API key land.

## What Is Built Now

- SQLite/FTS persistent memory store.
- Memory event ledger for creation, supersession, retirement, and blocking.
- Retrieval log with reasons, scores, token estimates, and source refs.
- Stable-state packet renderer.
- Architecture-off versus architecture-on agent path.
- Offline deterministic provider for local verification.
- Qwen Cloud provider stub gated on `QWEN_API_KEY`.
- Simple scoring helpers for drift/correction/evidence/next-gate signals.

## Local Run

```bash
python3 scripts/run_trini_recall_demo.py
```

Expected behavior:

- Condition A returns a baseline response with no memory retrieval.
- Condition B retrieves seeded Trini Recall memories, includes retrieval
  reasons, and preserves the current Qwen API gate.
- The demo DB is created at `/tmp/trini_recall_memory.sqlite3` by default so
  runtime state does not enter the repo.

To choose a persistent local DB path:

```bash
TRINI_RECALL_DB_PATH=/tmp/trini_recall_memory.sqlite3 python3 scripts/run_trini_recall_demo.py
```

## Qwen Cloud Gate

When the $40 credit/API key lands:

```bash
export QWEN_API_KEY="..."
export QWEN_MODEL="qwen-plus"
```

Then replace the provider in the runner:

```python
from qwen_agent_buildout.trini_recall import QwenCloudProvider

agent = TriniRecallAgent.open_default(ROOT, QwenCloudProvider.from_env())
```

Three-condition hosted mirror command:

```bash
python3 scripts/run_qwen_three_condition_iterations.py --provider qwen_cloud --turns 24
```

Recommended hosted scale order:

```text
24 hosted turns
-> 100 hosted turns
-> 500 hosted turns only after the smaller hosted receipts are clean
```

Do not claim Qwen Cloud results until the run log includes:

- model name;
- timestamp;
- API route;
- prompt packet hash or source packet path;
- Condition A output;
- Condition B output;
- retrieval log;
- scorecard.

## Stretch C Gate

Condition C is adapter/LoRA only. It requires:

- real Qwen tuning or adapter path;
- trained/loaded adapter artifact;
- adapter-on scorecard;
- adapter-off or wrong-adapter control if possible.

Until then, the supported claim is architecture-layer behavioral lift, not
model-weight tuning.

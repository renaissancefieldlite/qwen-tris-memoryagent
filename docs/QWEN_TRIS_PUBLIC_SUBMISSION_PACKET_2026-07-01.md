# Qwen Tris Public Submission Packet - 2026-07-01

## Project

Qwen Tris Recall Memory AI Partner is the Qwen Cloud MemoryAgent version of the
Renaissance Field Lite Trismegistus / Mirror Architecture stack.

The build tests whether a Qwen model becomes more reliable over long technical
work when paired with Mirror Architecture measured Stable-State Path plus
memory/RAG rails instead of a generic prompt-only memory surface.

## Track

Track 1: MemoryAgent.

## Repository / License / Run Instructions

Repository requirement:

```text
The final submitted repo must be public and open source.
```

Prepared local files:

```text
LICENSE
README.md
.env.example
docs/ARCHITECTURE.md
docs/SUBMISSION_CHECKLIST_QWEN.md
src/qwen_agent_buildout/trini_recall/alibaba_qwen_cloud_client.py
scripts/run_trini_recall_ui.py
```

License:

```text
MIT
```

Local run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .
cp .env.example .env.local
set -a
source .env.local
set +a
python3 scripts/run_trini_recall_ui.py --port 9471
```

Architecture diagram:

```text
docs/ARCHITECTURE.md
```

## Model And Cloud Proof

Hosted Qwen route:

```text
https://dashscope-intl.aliyuncs.com/compatible-mode/v1
```

Code file demonstrating Qwen Cloud / Alibaba Cloud API usage:

```text
src/qwen_agent_buildout/trini_recall/alibaba_qwen_cloud_client.py
```

Provider and model:

```text
provider: qwen-cloud
model: qwen-plus
```

Cloud/free-tier proof:

```text
docs/qwen_cloud_deployment_proof/qwen_cloud_free_tier_active_20260701T040738Z.png
```

Alibaba/Qwen proof recording:

```text
docs/qwen_cloud_deployment_proof/USE_THIS_ALIBABA_QWEN_CLOUD_PROOF_2026-07-04_v02_RUNNING_TRIS.mp4
docs/qwen_cloud_deployment_proof/USE_THIS_ALIBABA_QWEN_CLOUD_PROOF_2026-07-04_v02_RUNNING_TRIS_RECEIPT.md
docs/qwen_cloud_deployment_proof/USE_THIS_ALIBABA_QWEN_CLOUD_PROOF_2026-07-04_v02_RUNNING_TRIS_CONTACT_SHEET.jpg
```

What it shows:

```text
The v02 proof clip shows the Alibaba/Qwen account route, the public-safe Qwen
API client, a masked live API receipt, and an actual Qwen Tris Recall
architecture-on turn routed through QwenCloudProvider using qwen-plus.
```

Remaining deployment gate:

```text
If judges require a hosted backend URL rather than API-backed proof from the
local build, mirror the same proof through an Alibaba Cloud container and attach
that short recording as the next receipt.
```

Console state observed:

```text
248 eligible models with free quota available
Free quota only / auto-stop when free quota runs out
$40 coupon visible under Benefits -> Coupon
```

## Evaluation Shape

Condition A:

```text
Baseline Qwen, prompt-only.
```

Condition B:

```text
Qwen + Mirror Architecture measured SSP plus memory/RAG packet.
```

Condition C:

```text
Gated. Requires a real tuned adapter, LoRA, or internal-layer receipt before
any tuned-checkpoint claim.
```

## Hosted Receipts

```text
1-turn smoke:
data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T034331Z.md

24-turn hosted slice:
data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T034823Z.md

100-turn hosted slice:
data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T040738Z.md

500-turn hosted slice:
data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T054449Z.md

Second hosted Qwen model slice:
data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T070452Z.md
```

## Live UI Receipt

```text
Desktop launcher:
/Users/renaissancefieldlite1.0/Desktop/Qwen Tris Recall.command

Local surface:
http://127.0.0.1:9471/

Runtime route:
Qwen Cloud API -> qwen-plus

Fallback routes:
local Qwen qwen2.5:3b via Ollama
local Nemotron Nano GGUF via Ollama

Persistence:
SQLite memory + JSONL audit log under
/Users/renaissancefieldlite1.0/Library/Application Support/QwenTrisRecall/
```

Live smoke:

```text
route: qwen_cloud
provider: QwenCloudProvider
model: qwen-plus
rag_mode: langchain_sqlite_fts
```

Qwen account state:

```text
Qwen free-tier access is active in the operator account, and the operator
observed a $40 coupon under Benefits -> Coupon. No API keys or secrets are
included in this packet.
```

## Headline Result

```text
Condition B passed 500/500 hosted Qwen Cloud turns.
```

500-turn family totals:

```text
C5B / 500 SSP state-path recall: 153/153
External work receipts: 58/58
Long-session coherence: 58/58
Mirror Architecture source pack: 115/115
SWE code memory: 58/58
WebArena browser memory: 58/58
```

Second hosted model check:

```text
qwen3.7-plus passed the same 24-turn hosted architecture-on slice: 24/24.
It is a valid higher-latency comparison model; qwen-plus remains the practical
default route for longer runs.
```

## Why It Matters

The memory test is not an easy chatbot recall demo. It uses collapse-prone
state:

- C5B / Golden Mark Stable-State Path lane.
- Mirror Architecture source-pack recall.
- SWE-style code memory.
- WebArena-style browser memory.
- Long-session coherence.
- External work and approval-gate receipts.

The public-safe read is:

```text
Qwen prompt-only is the baseline. Qwen with Mirror Architecture measured SSP
plus memory/RAG rails preserved target recall across the hosted 500-turn stress
run.
```

## Reflexion Comparison Lane

Reflexion is the closest public research comparison family for the memory and
self-improvement claim. Reflexion compares a plain language agent against a
route that turns task feedback into verbal reflection and carries that
reflection forward through episodic memory.

Qwen Tris uses the same broad scientific pattern, but with a different RFL
architecture:

| Comparison family | What it tests | Public-safe Qwen Tris bridge |
|---|---|---|
| Reflexion | Baseline route vs feedback/reflection memory route | Baseline model vs Mirror Architecture / SSP architecture-on route |
| HumanEval / MBPP coding | Functional code generation and repair | MBPP/HumanEval-style local coding slice plus SWE-style and bounty/PR receipts |
| HotPotQA / QA | Source-grounded multi-hop reasoning | Qasper and LongBench public-answer-key receipts |
| ALFWorld / environment action | Sequential task execution | WebArena-style browser mission traces and local browser receipts |
| External work | Not the primary Reflexion target | Tris bounty, pull-request, outreach, and approval-gate receipts |

Current same-packet cross-model bridge:

```text
Same source packet. Same scorer. Different model family.
Hermes baseline: 1/20 exact hits, 0/7 task passes.
Hermes Tris architecture-on: 20/20 exact hits, 7/7 task passes.
Qwen baseline: 0/20 exact hits, 0/7 task passes.
Qwen Tris architecture-on: 20/20 exact hits, 7/7 task passes.
```

Receipt:

```text
data/cross_model_comparison_runs/cross_model_same_packet_20260704T021424Z.md
```

Reflexion-adjacent coding slice:

```text
data/public_benchmark_runs/qwen_tris_mbpp_reflexion_slice_20260704T062754Z.md
```

Result:

```text
Dataset: google-research-datasets/mbpp, sanitized test split
Model: local qwen2.5:3b via Ollama
Baseline one-shot: 67/100
Qwen Tris architecture-on repair route: 71/100
Delta: +4 tasks
```

Read:

```text
This is a local MBPP slice, not an official leaderboard run. It shows the
Reflexion-shaped mechanism at 100-row scale: the same initial generated code is
tested first, then Qwen Tris only enters on failing rows with a bounded
feedback/repair pass. Passing baseline rows are not rewritten. The 100-row run
repaired tasks 59, 71, 98, and 162.
```

HumanEval-instruct slice:

```text
data/public_benchmark_runs/qwen_tris_humaneval_reflexion_slice_20260704T062754Z.md
```

Result:

```text
Dataset: openai/openai_humaneval, test split
Model: local qwen2.5:3b via Ollama
Baseline one-shot: 14/20
Qwen Tris architecture-on repair route: 14/20
Delta: +0 tasks
```

Read:

```text
The HumanEval slice confirms the runner and boundary work, but the current
repair prompt did not improve the first 20 rows. MBPP is the stronger current
Reflexion-adjacent coding signal; HumanEval needs a larger slice or improved
repair discipline before stronger language.
```

Boundary:

```text
This is a Reflexion-adjacent comparison lane, not a claim that Qwen Tris has
beaten Reflexion on the original Reflexion benchmark suite. Stronger coding
comparison language requires a larger MBPP/HumanEval slice or the official
evaluator route.
```

## Public Boundary

This package may show:

- receipt paths;
- scored family totals;
- hosted Qwen base URL;
- public-safe screenshots;
- public-safe task families;
- honest next gates.

This package does not show:

- private prompts;
- raw private memory rows;
- adapter internals;
- secrets or API keys;
- proprietary implementation mechanics;
- AGI, sentience, or public leaderboard claims.

## Next Gates

1. Publish this as a public-safe GitHub repo/package.
2. Add a short demo video or screenshots showing the Qwen Tris memory surface.
3. Run the same 500-turn slice through additional Qwen API variants if the free
   quota or coupon supports it.
4. Only after a real tuning route exists, run Condition C with a real adapter or
   internal-layer receipt.
5. Backport the clean memory-stress harness to Hermes Trismegistus V21.

# Qwen Tris Reflexion Comparison Lane - 2026-07-03

## Purpose

This lane gives Qwen Tris a respected public comparison family without
flattening the project into generic "memory prompting."

Reflexion is the relevant academic comparison because it showed that language
agents can improve without weight updates by converting task feedback into
verbal self-reflection and storing that reflection in an episodic memory buffer.

Qwen Tris is adjacent, but not identical:

- Reflexion: feedback -> verbal reflection -> episodic memory -> next trial.
- Qwen Tris: source receipts -> Mirror Architecture / SSP packet -> RAG and
  audit memory -> cross-model task recall -> next gate.

## Primary Public References

Reflexion paper:

```text
https://arxiv.org/abs/2303.11366
```

Reflexion code / logs:

```text
https://github.com/noahshinn/reflexion
```

OpenReview page:

```text
https://openreview.net/forum?id=vAElhFcKW6
```

## Public-Safe Comparison Read

Claim:

```text
Qwen Tris follows the same broad scientific pattern as Reflexion: compare a
plain baseline agent to an architecture-on route that adds structured memory
and feedback. The difference is that Qwen Tris anchors the memory in source
receipts, Mirror Architecture / SSP packets, and cross-model recall gates.
```

Evidence we have now:

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

Public evaluator evidence already attached to Qwen Tris:

```text
LongBench 150-row adaptive scale:
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T143102Z.md

Qasper 100-row receipt:
data/third_party_eval_runs/QWEN_TRIS_LM_EVAL_QASPER_RECEIPT_20260701T180343Z.md
```

Real-world external-work receipt family:

```text
Hermes/Tris bounty and pull-request lanes exist separately. These prove that
the architecture can route from research/coding memory into actual external
work, not only benchmark rows.
```

## What We Should Not Claim Yet

Do not claim:

```text
Qwen Tris beats Reflexion on the original Reflexion benchmark suite.
```

That requires running matched task families from the Reflexion paper or clean
equivalents:

- HumanEval / coding self-repair.
- ALFWorld / sequential decision-making.
- HotPotQA / multi-hop QA.

## Clean Comparison Plan

### Gate 1 - Paper-Aligned Framing

Use Reflexion as the public reference pattern:

```text
baseline route vs memory/feedback route
```

This is already supported by Qwen Tris same-packet receipts.

### Gate 2 - Coding Lane

Use our existing SWE / bounty / PR route as the real coding lane.

Public wording:

```text
Reflexion showed coding gains through verbal feedback on HumanEval. Qwen Tris
extends the same baseline-vs-architecture-on idea into source-backed coding
work, SWE-style patch synthesis, and real GitHub PR receipts.
```

Boundary:

```text
SWE-bench leaderboard language waits on official compatible review/receipt.
```

### Gate 3 - QA Lane

Run or cite existing Qasper / LongBench public-answer-key receipts as the
multi-hop/source QA lane.

Current best public-safe read:

```text
On the 150-row LongBench adaptive slice, Qwen Tris improved the matched
baseline from 0.571 to 0.676 mean score, a +0.105 delta.
```

### Gate 4 - Environment / Browser Lane

Use WebArena-style tasks and browser mission traces as the practical equivalent
of sequential environment action. Do not call it ALFWorld unless ALFWorld is
actually run.

### Gate 5 - Paid-Work Lane

This is where Qwen Tris / Hermes Tris goes beyond Reflexion:

```text
The agent is not only reflecting after a toy task. It is using the same memory
and receipt discipline to triage bounties, draft outreach, handle PR loops, and
produce external work receipts.
```

## One-Slide Wording

```text
Reflexion proved a simple thing with a major consequence:
agents improve when they can reflect on failure and carry that reflection
forward.

Qwen Tris tests the broader RFL claim:
does a source-backed Mirror Architecture / SSP packet improve memory, recall,
coding continuity, browser work, and paid-work execution across model families?

Our first same-packet result says yes locally:
prompt-only Hermes/Qwen routes missed the receipt facts, while the Tris
architecture-on lanes recovered 20/20 required facts on the same seven tasks.
```

## Next Gate

Build one matched comparison table for the submission packet:

```text
Reflexion family:
HumanEval / HotPotQA / ALFWorld pattern.

Qwen Tris receipts:
same-packet cross-model recall, LongBench, Qasper, SWE-style coding route,
browser mission trace, paid-work PR/bounty receipts.
```

Then, if time allows, run one small official Reflexion-adjacent task:

```text
HumanEval or MBPP local coding self-repair slice.
```

This gives the public story a real academic bridge without overclaiming.

## MBPP Slice Receipt

Runner:

```text
scripts/run_mbpp_reflexion_slice.py
```

Receipt:

```text
data/public_benchmark_runs/qwen_tris_mbpp_reflexion_slice_20260704T062754Z.md
```

Result:

```text
Dataset: google-research-datasets/mbpp, sanitized test split
Model: local qwen2.5:3b via Ollama
Offset: 0
Limit: 100
Baseline one-shot: 67/100
Qwen Tris architecture-on repair route: 71/100
Delta: +4 tasks
```

Read:

```text
This is the clean Reflexion-adjacent shape: baseline writes code, tests run,
and the Qwen Tris route only receives failure feedback on rows that failed.
Passing baseline rows are preserved. The 100-row scale repaired tasks 59, 71,
98, and 162, and does not claim official leaderboard status.
```

## HumanEval-Instruct Slice Receipt

Runner:

```text
scripts/run_humaneval_reflexion_slice.py
```

Receipt:

```text
data/public_benchmark_runs/qwen_tris_humaneval_reflexion_slice_20260704T062754Z.md
```

Result:

```text
Dataset: openai/openai_humaneval, test split
Model: local qwen2.5:3b via Ollama
Offset: 0
Limit: 20
Baseline one-shot: 14/20
Qwen Tris architecture-on repair route: 14/20
Delta: +0 tasks
```

Read:

```text
The HumanEval-instruct slice confirms the runner and boundary. It did not
separate from baseline on the first 20 rows. This should stay as a receipt and
next-gate pointer, not headline evidence.
```

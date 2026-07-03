# Qwen Tris Public Verification Ladder

Date: 2026-07-01

This document defines how Qwen Tris moves from internal memory receipts into
public, answer-key-based verification. It is a testing ladder, not a public
leaderboard claim.

## Current Proof Base

### Internal Memory / SSP Harness

Receipt:

```text
data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T054449Z.md
```

Read:

```text
Condition B, Qwen plus Mirror Architecture measured SSP and memory/RAG packet,
passed 500/500 hosted Qwen Cloud turns across six memory-stress families.
```

Support level:

```text
Hosted Qwen generation plus memory/SSP operating-layer evidence is attached.
Adapter, internal-layer, and leaderboard rows attach when their independent
receipts land.
```

### Second Hosted Qwen Model Slice

Receipt:

```text
data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T070452Z.md
```

Read:

```text
qwen3.7-plus passed the same architecture-on memory slice at 24/24. It is a
valid comparison route, but qwen-plus is the practical default because it is
faster for long runs.
```

## Public Benchmark Candidate: LongBench

LongBench is a public long-context benchmark with answer keys. It covers
single-document QA, multi-document QA, summarization, few-shot classification,
synthetic retrieval/counting, and code-completion style tasks. The current
Hugging Face dataset loader is blocked by deprecated dataset-script handling,
so this repo uses the official `data.zip` from `THUDM/LongBench` directly.

Runner:

```text
scripts/run_longbench_public_slice.py
```

Current smoke receipt:

```text
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T121718Z.md
```

Result:

```text
Items: 6
Condition A baseline Qwen mean: 1.000
Condition B Qwen Tris mean: 0.994
Delta: -0.006
```

Family totals:

```text
passage_retrieval_en_e: A 1.000 / B 1.000
trec_e: A 1.000 / B 1.000
multifieldqa_en_e: A 1.000 / B 0.983
```

Interpretation:

```text
This tiny public smoke verifies that the public LongBench runner works and that
both routes can answer easy answer-key rows. It does not yet prove Tris is more
accurate than baseline on LongBench because baseline saturated the easy rows.
The one B-side miss is a token-F1 wording difference, not a source failure.
```

Failed prompt-tightening check:

```text
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T121851Z.md
```

Read:

```text
Over-tightening the B prompt made one QA row worse. Reverted. Public benchmark
receipts are already useful because they catch prompt over-control.
```

Current Silver receipt:

```text
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T132826Z.md
```

Silver result:

```text
Items: 60
Condition A baseline Qwen mean: 0.481
Condition B Qwen Tris mean: 0.592
Delta: +0.111
```

Silver family totals:

```text
passage_retrieval_en_e: A 1.000 / B 1.000 / delta +0.000
passage_count_e: A 0.200 / B 0.100 / delta -0.100
trec_e: A 0.000 / B 0.700 / delta +0.700
multifieldqa_en_e: A 0.456 / B 0.523 / delta +0.066
qasper_e: A 0.568 / B 0.567 / delta -0.002
hotpotqa_e: A 0.663 / B 0.663 / delta +0.000
```

Silver interpretation:

```text
This is a positive public answer-key receipt. Qwen Tris beats the matched
baseline overall on the 60-row slice. After the task-adaptive patch, the
architecture-on route preserves the TREC output-format win and also improves
MultiFieldQA token-F1. This is not a full LongBench leaderboard claim.
```

Passage-count boundary:

```text
PassageCount remains the hard lane. Official prompt templates and a qwen-max
spot check did not solve it. A naive exact-text dedupe tool also failed to
reproduce the first-10 answer key, so this needs a public-source construction
audit before any tool-assisted claim.
```

Previous 150-row scale receipt:

```text
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T131355Z.md
```

150-row scale result:

```text
Items: 150
Condition A baseline Qwen mean: 0.578
Condition B Qwen Tris mean: 0.597
Delta: +0.020
```

150-row family totals:

```text
passage_retrieval_en_e: A 1.000 / B 1.000 / delta +0.000
passage_count_e: A 0.360 / B 0.280 / delta -0.080
trec_e: A 0.320 / B 0.560 / delta +0.240
multifieldqa_en_e: A 0.627 / B 0.605 / delta -0.022
qasper_e: A 0.504 / B 0.504 / delta +0.001
hotpotqa_e: A 0.655 / B 0.635 / delta -0.020
```

150-row interpretation:

```text
The larger slice stays positive overall, with the strongest repeatable gain on
TREC label discipline. It also exposes the next repair: Tris needs
task-adaptive answer discipline because extractive QA token-F1 can regress when
the global instruction is too strict or too broad.
```

Current 150-row adaptive scale receipt:

```text
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T143102Z.md
```

150-row adaptive scale result:

```text
Items: 150
Condition A baseline Qwen mean: 0.571
Condition B Qwen Tris mean: 0.676
Delta: +0.105
```

150-row adaptive family totals:

```text
passage_retrieval_en_e: A 1.000 / B 1.000 / delta +0.000
passage_count_e: A 0.320 / B 0.440 / delta +0.120
trec_e: A 0.320 / B 0.720 / delta +0.400
multifieldqa_en_e: A 0.627 / B 0.641 / delta +0.014
qasper_e: A 0.502 / B 0.599 / delta +0.097
hotpotqa_e: A 0.655 / B 0.655 / delta +0.000
```

150-row adaptive interpretation:

```text
The task-adaptive route is the current best public scale receipt. It improves
the 150-row delta from +0.020 to +0.105, keeps retrieval and HotpotQA at parity,
preserves the TREC classification/output-format win, moves PassageCount positive,
keeps MultiFieldQA positive, and repairs Qasper into a positive family.
```

Current 300-row scale receipt:

```text
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T150444Z.md
```

Prior 300-row scale result:

```text
Items scored: 299
Provider-blocked rows skipped: 1
Condition A baseline Qwen mean: 0.579
Condition B Qwen Tris mean: 0.655
Delta: +0.076
```

300-row family totals:

```text
passage_retrieval_en_e: n=49 A 1.000 / B 1.000 / delta +0.000
passage_count_e: n=50 A 0.340 / B 0.280 / delta -0.060
trec_e: n=50 A 0.320 / B 0.740 / delta +0.420
multifieldqa_en_e: n=50 A 0.625 / B 0.635 / delta +0.010
qasper_e: n=50 A 0.493 / B 0.595 / delta +0.102
hotpotqa_e: n=50 A 0.702 / B 0.686 / delta -0.016
```

300-row interpretation:

```text
The 300-row expansion is positive overall and is now the strongest scale receipt
by row count. It confirms that the architecture-on prompt discipline is not only
a tiny-slice artifact. The clear wins are TREC and Qasper. Retrieval is
saturated parity. PassageCount and HotpotQA regressed in this larger slice and
must be treated as repair lanes, not hidden.
```

Focused repair receipts:

```text
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T152102Z.md
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T152843Z.md
```

Focused repair read:

```text
The scorer now extracts final numeric answers for PassageCount instead of the
first integer in a verbose reasoning spill. HotpotQA two-hop answer-span repair
turned positive on the 50-row HotpotQA lane: A 0.698 / B 0.712 / delta +0.015.
PassageCount pass-through reduced over-control but did not fully solve the
family: A 0.360 / B 0.340 / delta -0.020 on the verification slice.
```

Official source audit:

```text
The official THUDM LongBench source was cloned under
source_inventory/THUDM_LongBench_official/. The local runner now mirrors the
official synthetic numeric-task scoring rule from LongBench/metrics.py:
extract every number from the prediction and score correct-number-count divided
by emitted-number-count. This replaces the stale final-integer-only scorer.
```

Naive PassageCount construction audit:

```text
Rendered-context exact body dedupe matched only 20/50 of the first public
PassageCount-E rows. That means a deterministic PassageCount helper must
reproduce the official construction semantics or be clearly labeled as a
separate tool-assisted route. Naive dedupe is not enough.
```

Current official-aligned 300-row receipt:

```text
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T161053Z.md
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T161053Z.json
```

Current official-aligned 300-row result:

```text
Items scored: 299
Provider-blocked rows skipped: 1
Condition A baseline Qwen mean: 0.575
Condition B Qwen Tris mean: 0.669
Delta: +0.094
```

Current official-aligned family totals:

```text
passage_retrieval_en_e: n=49 A 1.000 / B 1.000 / delta +0.000
passage_count_e: n=50 A 0.343 / B 0.343 / delta -0.000
trec_e: n=50 A 0.300 / B 0.740 / delta +0.440
multifieldqa_en_e: n=50 A 0.611 / B 0.636 / delta +0.025
qasper_e: n=50 A 0.492 / B 0.598 / delta +0.105
hotpotqa_e: n=50 A 0.711 / B 0.701 / delta -0.010
```

Superseded read before the negative-family repair:

```text
This was the current public LongBench-E scale proof before the later
negative-family repair. Qwen Tris beat matched
baseline Qwen overall by +0.094 on 299 scored rows under official prompt
templates and official synthetic numeric scoring. The clean lift lanes are TREC
and Qasper; MultiFieldQA is modestly positive; retrieval is saturated parity;
PassageCount is parity; HotpotQA was the remaining slight-negative repair lane.
The repaired current receipt is recorded in the Negative Family Repair Gate.
```

## Qasper Lock Gate

Architect D corrected the next gate after the 300-row expansion: Qasper needed
to be locked instead of assumed from the first 50 rows.

Failed held-out check:

```text
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T171030Z.md
Window: qasper_e rows 51-100
Items: 50
Skipped provider-blocked rows: 0
Condition A baseline Qwen mean: 0.476
Condition B Qwen Tris mean: 0.467
Delta: -0.010
```

Repair:

```text
Qasper answer discipline was patched to keep concise answers while preserving
complete supported spans for dataset definitions, dataset sizes, corpus sizes,
performance/results values, language/code lists, methods, baselines, and
"what is X" questions.
```

Repaired held-out check:

```text
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T171624Z.md
Window: qasper_e rows 51-100
Items: 50
Skipped provider-blocked rows: 0
Condition A baseline Qwen mean: 0.483
Condition B Qwen Tris mean: 0.519
Delta: +0.036
```

Repaired first-window repeat:

```text
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T172019Z.md
Window: qasper_e rows 1-50
Items: 50
Skipped provider-blocked rows: 0
Condition A baseline Qwen mean: 0.494
Condition B Qwen Tris mean: 0.545
Delta: +0.051
```

Combined lock receipt:

```text
data/public_benchmark_runs/qwen_tris_qasper_lock_20260701T172350Z.md
data/public_benchmark_runs/qwen_tris_qasper_lock_20260701T172350Z.json

Items: 100
Skipped provider-blocked rows: 0
Condition A baseline Qwen mean: 0.488
Condition B Qwen Tris mean: 0.532
Delta: +0.044
Wins / losses / ties: 30 / 17 / 53
```

Read:

```text
Qasper is now locked as a positive public LongBench-E proof lane across two
adjacent 50-row windows under the same repaired Qasper answer discipline. This
does not mean every row is solved. It means the Qasper answer-span discipline
now beats matched baseline Qwen across 100 public Qasper rows with zero skipped
provider rows.
```

## Certification-Style Gates

### Bronze Gate - Public Smoke

Requirement:

```text
Run at least 6 public LongBench rows across retrieval, classification, and QA.
Save JSON + Markdown receipts. No secrets. No leaderboard claim.
```

Status:

```text
Complete.
```

### Silver Gate - Stratified Public Slice

Requirement:

```text
Run 60 public LongBench-E rows:
- 10 passage_retrieval_en_e
- 10 passage_count_e
- 10 trec_e
- 10 multifieldqa_en_e
- 10 qasper_e
- 10 hotpotqa_e or 2wikimqa_e

Report per-family A/B scores, delta, and failure taxonomy.
```

Pass condition:

```text
Condition B must match or beat Condition A overall, or failures must identify a
clear prompt/scoring issue before scaling. No cherry-picking: the chosen row
order must be recorded before results are interpreted.
```

Status:

```text
Complete. Condition B beat Condition A overall by +0.111 on the current
task-adaptive 60-row slice. Keep row-level failures attached to the receipt.
```

### Gold Gate - Full Public LongBench-E Subset

Requirement:

```text
Run a full selected LongBench-E subset with public answer keys and reproducible
row selection. Publish the runner, prompt conditions, JSON receipts, and summary
table. Still no leaderboard claim unless submitted through the official
benchmark process.
```

Current status:

```text
In progress. Two adjacent repaired official-aligned public LongBench-E
300-row windows are complete and parity-or-positive by reported family:
offset-0 at +0.092 overall and held-out offset-50 at +0.110 overall. Each
window logged one provider-blocked row. TREC is the strongest repeatable lift
family; Qasper, MultiFieldQA, and HotpotQA preserve positive direction.
PassageCount is now a labeled pass-through parity gate, not an architecture-lift
claim. PassageCount needs a bounded construction/tool lane only if we want it
to become an agent-action proof.
```

### Agent-Action Gate

Benchmarks:

```text
WebArena / BrowserGym-style visible browser tasks.
GAIA-style source-backed tasks.
SWE-bench Verified / coding helper tasks.
```

Read:

```text
These show action accuracy and tool-use discipline, not only memory recall.
They should stay separate from the LongBench memory/long-context proof.
```

### Third-Party / Certification Gate

Meaning:

```text
There is no generic "certified AI expert" label that proves this system. The
closest strong proof is a public benchmark with answer keys, reproducible code,
and optionally a hosted or third-party evaluator.
```

Candidates:

```text
LongBench / LongBench-E for long-context accuracy.
LoCoMo or similar long-term conversation-memory benchmarks for memory over time.
RULER-style synthetic long-context tasks for needle/retrieval stress.
GAIA for real-world multi-step task accuracy.
WebArena / BrowserGym for browser action accuracy.
SWE-bench Verified for code-patch accuracy.
```

Current lm-eval Qasper receipt:

```text
data/third_party_eval_runs/QWEN_TRIS_LM_EVAL_QASPER_RECEIPT_20260701T180343Z.md

Evaluator: EleutherAI lm-evaluation-harness
Harness HEAD: 97a5e2c710e2b56b9dd48f367bb6fe87bbb2c176
Official task: longbench_qasper_e
Architecture-on task variant: qwen_tris_qasper_e
Dataset: Xnhyacinth/LongBench / qasper_e
Model: qwen-plus
```

Matched 100-row third-party result:

```text
Baseline official score: 0.5226798775939184
Tris prompt-variant score: 0.5405829547650837
Delta: +0.017903077171165273
Wins / losses / ties: 20 / 22 / 58
```

Full official baseline:

```text
Score: 0.4812428635163242
Rows: 224 / 224
```

Full Tris prompt-variant:

```text
Score: 0.48259642030075983
Rows: 224 / 224
Delta: +0.00135355678443563
Result JSON:
data/third_party_eval_runs/lm_eval_qasper_tris_prompt_full_20260701T190001Z/qwen-plus/results_2026-07-01T13-08-47.277911.json
```

Boundary:

```text
The third-party harness reproduces a positive 100-row Qasper result for the
repaired Tris answer-span discipline. The full 224-row Qasper run is also
positive, but only slightly. Use the full run as direction-preservation
evidence, not as a large-lift claim. The stronger Qasper signal remains the
locked 100-row public slice and the matched 100-row lm-eval receipt.
```

## Next Clean Move

## Negative Family Repair Gate

Architect D corrected the scale order: repair negative families before spending
into larger slices. The prior official-aligned 300-row receipt showed
PassageCount at parity and HotpotQA as the only real slight-negative family.

Prior official-aligned 300-row receipt:

```text
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T161053Z.md
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T161053Z.json
```

Repair applied:

```text
PassageCount remains pass-through under the official LongBench prompt and
official numeric-fraction scoring. Added architecture wording over-steers this
synthetic count task.

HotpotQA descriptor/list questions now pass through the official LongBench
prompt and baseline system prompt. The inspected regression was a descriptor
bridge row where the model needed to find the German-cinematographer passage,
then follow the linked film passage before naming the actors.
```

Focused HotpotQA repair receipt:

```text
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T193249Z.md
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T193249Z.json
Items: 50
Skipped provider-blocked rows: 0
Condition A baseline Qwen mean: 0.698
Condition B Qwen Tris mean: 0.725
Delta: +0.027
Wins / losses / ties: 2 / 1 / 47
```

Repaired 300-row verification receipt:

```text
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T195427Z.md
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T195427Z.json
Items scored: 299
Provider-blocked rows skipped: 1
Condition A baseline Qwen mean: 0.574
Condition B Qwen Tris mean: 0.666
Delta: +0.092
```

Repaired family totals:

```text
passage_retrieval_en_e: n=49 A 1.000 / B 1.000 / delta +0.000
passage_count_e: n=50 A 0.341 / B 0.344 / delta +0.004
trec_e: n=50 A 0.280 / B 0.740 / delta +0.460
multifieldqa_en_e: n=50 A 0.615 / B 0.624 / delta +0.009
qasper_e: n=50 A 0.508 / B 0.569 / delta +0.062
hotpotqa_e: n=50 A 0.707 / B 0.726 / delta +0.018
```

Read:

```text
The six-family 300-row LongBench-E slice is now parity-or-positive across every
reported family under the current official-prompt and official-scoring route.
This is still not a full LongBench leaderboard claim. It is a local/public
answer-key scale receipt with provider-block accounting. Pass-through rows still
use live Qwen calls, so row-level drift remains possible and must be logged on
the next scale.
```

## Held-Out Scale Gate

Architect D pushed the scale discipline onto the next adjacent public
LongBench-E window before claiming the repaired lane was stable. The first
held-out run stayed positive overall but exposed a MultiFieldQA negative
family. MultiFieldQA was repaired with minimum exact supported-span discipline.
The second held-out run showed that live PassageCount calls could drift negative
despite being a no-lift task, so PassageCount became a literal labeled
pass-through parity gate.

Final held-out 300-row receipt:

```text
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T214036Z.md
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T214036Z.json
Items scored: 299
Provider-blocked rows skipped: 1
Condition A baseline Qwen mean: 0.543
Condition B Qwen Tris mean: 0.653
Delta: +0.110
```

Final held-out family totals:

```text
passage_retrieval_en_e: n=50 A 1.000 / B 1.000 / delta +0.000
passage_count_e: n=50 A 0.383 / B 0.383 / delta +0.000
trec_e: n=49 A 0.163 / B 0.735 / delta +0.571
multifieldqa_en_e: n=50 A 0.470 / B 0.513 / delta +0.044
qasper_e: n=50 A 0.482 / B 0.510 / delta +0.028
hotpotqa_e: n=50 A 0.755 / B 0.780 / delta +0.025
```

Final held-out wins / losses / ties:

```text
passage_retrieval_en_e: 0 / 0 / 50
passage_count_e: 0 / 0 / 50
trec_e: 28 / 0 / 21
multifieldqa_en_e: 16 / 12 / 22
qasper_e: 17 / 9 / 24
hotpotqa_e: 3 / 2 / 45
```

Read:

```text
The held-out offset-50 scale gate passed with no negative reported families.
The honest proof language is: two adjacent 300-row public LongBench-E windows
are now all-family parity-or-positive under local Qwen Cloud execution, official
prompt templates where applicable, official scorer logic where applicable, and
provider-block accounting. This is not a leaderboard claim.
```

## Next Clean Move

Scale only after preserving the all-family parity-or-positive boundary:

```text
1. Run the next larger official-aligned LongBench-E slice with the current
   HotpotQA descriptor/list pass-through and PassageCount official-prompt
   pass-through intact.
2. Stop and repair again if any family goes negative.
3. Keep Qasper separately locked; do not overfit Qasper unless a larger Qasper
   window regresses.
4. Keep PassageCount construction/tool work as a labeled future lane unless it
   reproduces official LongBench construction semantics.
```

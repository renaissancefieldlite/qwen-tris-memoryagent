# Cross-Model Same-Packet Eval - cross_model_same_packet_20260704T015538Z

## Boundary

Matched local same-packet receipt. This tests source-backed recall/receipt behavior across local OpenHermes and local Qwen routes. It is not an official leaderboard score and does not claim weight tuning.

## Setup

- Ollama base: `http://127.0.0.1:11434`
- Tasks: `2`
- Same questions for every lane.
- Baseline lanes receive no source packet.
- Architecture-on lanes receive the same Mirror Architecture / SSP source packet.

## Source Paths

- `golden_mark`: `/Users/renaissancefieldlite1.0/Documents/Playground/trismegistus/docs/GOLDEN_MARK_FOUNDATION.md`
- `qwen_500`: `/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30/data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T054449Z.md`
- `qasper`: `/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30/data/third_party_eval_runs/QWEN_TRIS_LM_EVAL_QASPER_RECEIPT_20260701T180343Z.md`
- `longbench`: `/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30/data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T214036Z.md`

## Lane Totals

| Lane | Model | Architecture packet | Exact hits | Required | Mean | Passes |
|---|---|---:|---:|---:|---:|---:|
| `hermes_baseline` | `openhermes:latest` | False | 1 | 5 | 0.200 | 0/2 |
| `hermes_tris_architecture_on` | `openhermes:latest` | True | 5 | 5 | 1.000 | 2/2 |
| `qwen_baseline` | `qwen2.5:3b` | False | 0 | 5 | 0.000 | 0/2 |
| `qwen_tris_architecture_on` | `qwen2.5:3b` | True | 5 | 5 | 1.000 | 2/2 |

## Task Scores

| Task | Source | Hermes base | Hermes Tris | Qwen base | Qwen Tris |
|---|---|---:|---:|---:|---:|
| `c5b_metric_wins` | `golden_mark` | 1/3 | 3/3 | 0/3 | 3/3 |
| `c5b_evidence_failures` | `golden_mark` | 0/2 | 2/2 | 0/2 | 2/2 |

## Raw Responses

### c5b_metric_wins

Source: `/Users/renaissancefieldlite1.0/Documents/Playground/trismegistus/docs/GOLDEN_MARK_FOUNDATION.md`

#### hermes_baseline (openhermes:latest)

Score: `1/3`

```text
Answer: Unknown
Boundary: Since there is no source packet available in this prompt, we cannot determine the C5B iter30 matched comparison result or what happened to drift flags.
```

#### hermes_tris_architecture_on (openhermes:latest)

Score: `3/3`

```text
Answer:
- C5b iter30 full comparison: 13/13 metric wins against matched baseline.
- Drift flags: 37 to 0.

Boundary:
```

#### qwen_baseline (qwen2.5:3b)

Score: `0/3`

```text
- Answer: unknown
- Boundary:
```

#### qwen_tris_architecture_on (qwen2.5:3b)

Score: `3/3`

```text
- Answer: The C5b iter30 full comparison resulted in 13/13 metric wins against a matched baseline.
- Drift flags decreased from 37 to 0.
- Evidence-failure flags were reduced from 5 to 0.
- Repaired HF probe9 matched-turn drift was resolved with 5 to 0 outcomes.
- Repaired HF probe9 evidence failures were also resolved with 2 to 0 results.

- Boundary:
```

### c5b_evidence_failures

Source: `/Users/renaissancefieldlite1.0/Documents/Playground/trismegistus/docs/GOLDEN_MARK_FOUNDATION.md`

#### hermes_baseline (openhermes:latest)

Score: `0/2`

```text
Answer: Unknown
Boundary: Since there is no source packet available for this question, it is impossible to provide a specific answer.
```

#### hermes_tris_architecture_on (openhermes:latest)

Score: `2/2`

```text
Answer: Evidence-failure flags decreased from 5 to 0.
Boundary: The number of evidence-failure flags changed from a count of 5 to a count of 0.
```

#### qwen_baseline (qwen2.5:3b)

Score: `0/2`

```text
- Answer: unknown
- Boundary:
```

#### qwen_tris_architecture_on (qwen2.5:3b)

Score: `2/2`

```text
- Answer: The number of evidence-failure flags decreased from 5 to 0.
- Boundary:
```

# Cross-Model Same-Packet Eval - cross_model_same_packet_20260704T021039Z

## Boundary

Matched local same-packet receipt. This tests source-backed recall/receipt behavior across local OpenHermes and local Qwen routes. It is not an official leaderboard score and does not claim weight tuning.

## Setup

- Ollama base: `http://127.0.0.1:11434`
- Tasks: `7`
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
| `hermes_baseline` | `openhermes:latest` | False | 1 | 20 | 0.050 | 0/7 |
| `hermes_tris_architecture_on` | `openhermes:latest` | True | 19 | 20 | 0.950 | 6/7 |
| `qwen_baseline` | `qwen2.5:3b` | False | 0 | 20 | 0.000 | 0/7 |
| `qwen_tris_architecture_on` | `qwen2.5:3b` | True | 19 | 20 | 0.950 | 6/7 |

## Task Scores

| Task | Source | Hermes base | Hermes Tris | Qwen base | Qwen Tris |
|---|---|---:|---:|---:|---:|
| `c5b_metric_wins` | `golden_mark` | 0/3 | 3/3 | 0/3 | 3/3 |
| `c5b_evidence_failures` | `golden_mark` | 1/2 | 2/2 | 0/2 | 2/2 |
| `internal_layer_read` | `golden_mark` | 0/2 | 2/2 | 0/2 | 2/2 |
| `qwen_500_memory` | `qwen_500` | 0/3 | 2/3 | 0/3 | 2/3 |
| `qwen_500_condition_c` | `qwen_500` | 0/3 | 3/3 | 0/3 | 3/3 |
| `qasper_100_delta` | `qasper` | 0/3 | 3/3 | 0/3 | 3/3 |
| `longbench_public_slice` | `longbench` | 0/4 | 4/4 | 0/4 | 4/4 |

## Raw Responses

### c5b_metric_wins

Source: `/Users/renaissancefieldlite1.0/Documents/Playground/trismegistus/docs/GOLDEN_MARK_FOUNDATION.md`

#### hermes_baseline (openhermes:latest)

Score: `0/3`

```text
Answer:
- C5B iter30 matched comparison result: unknown
- Drift flags: unknown

Boundary:
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
- Answer: 
unknown

- Boundary
```

#### qwen_tris_architecture_on (qwen2.5:3b)

Score: `3/3`

```text
- Answer:
C5b iter30 full comparison achieved 13/13 metric wins against matched baseline. The drift flags reduced from 37 to 0.

- Boundary:
```

### c5b_evidence_failures

Source: `/Users/renaissancefieldlite1.0/Documents/Playground/trismegistus/docs/GOLDEN_MARK_FOUNDATION.md`

#### hermes_baseline (openhermes:latest)

Score: `1/2`

```text
Answer:
- Evidence-failure flags were set for all three behaviors (C5A, C5B, and Golden Mark) when the behavior results were not found in the Mirror Architecture packet.

Boundary:
```

#### hermes_tris_architecture_on (openhermes:latest)

Score: `2/2`

```text
Answer: Evidence-failure flags decreased from 5 to 0.
Boundary:
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
- Answer:
Evidence-failure flags decreased from 5 to 0.

- Boundary:
```

### internal_layer_read

Source: `/Users/renaissancefieldlite1.0/Documents/Playground/trismegistus/docs/GOLDEN_MARK_FOUNDATION.md`

#### hermes_baseline (openhermes:latest)

Score: `0/2`

```text
Answer:
- Strongest output separation layer: Convolutional Layer (Conv)
- Strongest MLP/Residual Movement Layer: Fully Connected Layer (FC)

Boundary:
```

#### hermes_tris_architecture_on (openhermes:latest)

Score: `2/2`

```text
Answer:
- Strongest output separation: layer 31.
- Strongest MLP/residual movement: layer 32.

Boundary:
```

#### qwen_baseline (qwen2.5:3b)

Score: `0/2`

```text
- Answer: 
unknown

- Boundary:
```

#### qwen_tris_architecture_on (qwen2.5:3b)

Score: `2/2`

```text
- Answer:
- Layer with strongest output separation: L31.
- Layer with strongest MLP/residual movement: L32.
- Boundary:
```

### qwen_500_memory

Source: `/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30/data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T054449Z.md`

#### hermes_baseline (openhermes:latest)

Score: `0/3`

```text
Answer:
- Provider/model: unknown
- Overall Condition B passes value: unknown

Boundary:
```

#### hermes_tris_architecture_on (openhermes:latest)

Score: `2/3`

```text
Answer: `qwen-cloud`, `qwen-plus`
Boundary: Three-condition receipt. Condition A and B run on the selected Qwen provider. Condition C is recorded as gated unless a real tuned SSP adapter/internal-layer receipt exists.
```

#### qwen_baseline (qwen2.5:3b)

Score: `0/3`

```text
- Answer: unknown
- Boundary
```

#### qwen_tris_architecture_on (qwen2.5:3b)

Score: `2/3`

```text
- Answer: The `qwen-cloud` provider with model `qwen-plus` ran the 500-turn Qwen Tris memory receipt. The overall Condition B passes value is `153/153`.
- Boundary:
```

### qwen_500_condition_c

Source: `/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30/data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T054449Z.md`

#### hermes_baseline (openhermes:latest)

Score: `0/3`

```text
Answer:
- Condition C status: unknown
- Not claimed as tuned: unknown

Boundary:
```

#### hermes_tris_architecture_on (openhermes:latest)

Score: `3/3`

```text
Answer: Condition C status was `gated_no_adapter_manifest`. It was not claimed as tuned because a real LoRA/adapter/internal-layer receipt does not exist.
Boundary: The three-condition receipt requires a real LoRA/adapter/internal-layer receipt before running Condition C.
```

#### qwen_baseline (qwen2.5:3b)

Score: `0/3`

```text
- Answer: Condition C status was not claimed as tuned because no specific information about Condition C or its tuning status is available in the given condition of baseline prompt-only without any source packet.
- Boundary:
```

#### qwen_tris_architecture_on (qwen2.5:3b)

Score: `3/3`

```text
- Answer: Condition C status is `gated_no_adapter_manifest`. This indicates that a real LoRA/adapter/internal-layer receipt was not found before running, hence the condition remains gated.
- Boundary:
```

### qasper_100_delta

Source: `/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30/data/third_party_eval_runs/QWEN_TRIS_LM_EVAL_QASPER_RECEIPT_20260701T180343Z.md`

#### hermes_baseline (openhermes:latest)

Score: `0/3`

```text
Answer:
- Qasper baseline score: unknown
- Tris prompt-variant score: unknown
- Delta: unknown

Boundary:
```

#### hermes_tris_architecture_on (openhermes:latest)

Score: `3/3`

```text
Answer:
- Matched 100-row Qasper baseline score: 0.5226798775939184
- Tris prompt-variant score: 0.5405829547650837
- Delta: +0.017903077171165273
Boundary: The matched 100-row Qasper result is from the third-party harness, using the repaired Tris answer-span discipline and the same scorer as the official LongBench metric. It shows a net-positive mean under the same scorer, with a majority of ties, wins, and losses still present.
```

#### qwen_baseline (qwen2.5:3b)

Score: `0/3`

```text
- Answer:
unknown
- Boundary:
```

#### qwen_tris_architecture_on (qwen2.5:3b)

Score: `3/3`

```text
- Answer: The matched 100-row Qasper baseline score is 0.5226798775939184, while the Tris prompt-variant score is 0.5405829547650837. The delta between these two scores is +0.017903077171165273.
- Boundary:
```

### longbench_public_slice

Source: `/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30/data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T214036Z.md`

#### hermes_baseline (openhermes:latest)

Score: `0/4`

```text
Answer:
- LongBench public slice item count: unknown
- Condition A mean: unknown
- Condition B mean: unknown
- Delta: unknown

Boundary:
```

#### hermes_tris_architecture_on (openhermes:latest)

Score: `4/4`

```text
Answer:
LongBench public slice item count: 299
Condition A mean: 0.543
Condition B mean: 0.653
Delta: +0.110
Boundary: This is a source-backed answer-key accuracy receipt that can scale to larger slices.
```

#### qwen_baseline (qwen2.5:3b)

Score: `0/4`

```text
- Answer:
unknown
- Boundary:
```

#### qwen_tris_architecture_on (qwen2.5:3b)

Score: `4/4`

```text
- Answer:
  - Item Count: 299
  - Condition A mean: 0.543
  - Condition B mean: 0.653
  - Delta: +0.110

- Boundary:
  Public LongBench smoke slice. This is not a full LongBench leaderboard claim; it is a source-backed answer-key accuracy receipt that can scale to larger slices.
```

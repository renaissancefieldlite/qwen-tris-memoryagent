# Qwen Tris Three-Condition Iterations - qwen_tris_three_condition_iterations_20260701T011821Z

- Provider: `ollama-qwen`
- Model: `qwen2.5:3b`
- Turns: `100`
- Condition B passes: `100/100`
- Condition C status: `gated_no_adapter_manifest`

## Boundary

Three-condition local receipt. Condition A and B run on local Ollama Qwen. Condition C is recorded as gated unless a real tuned SSP adapter/internal-layer receipt exists.

## Conditions

- Condition A: baseline Qwen, prompt only
- Condition B: Qwen + Mirror Architecture stabilized memory/RAG/SSP packet
- Condition C: Condition C requires a real LoRA/adapter/internal-layer receipt before running.

## Family Totals

- `c5b_500_ssp_memory`: Condition B `29/29`
- `external_work_receipts`: Condition B `12/12`
- `long_session_coherence`: Condition B `12/12`
- `mirror_architecture_source_pack`: Condition B `23/23`
- `swe_code_memory`: Condition B `12/12`
- `webarena_browser_memory`: Condition B `12/12`

## Side-By-Side Turns

| Turn | Row | Family | A hits | B hits | B target | B pass | C status |
|---:|---|---|---:|---:|---|---|---|
| 1 | `c5b_ssp_0001` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 2 | `external_work_0001` | `external_work_receipts` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 3 | `coherence_0001` | `long_session_coherence` | 0 | 3 | True | True | `gated_no_adapter_manifest` |
| 4 | `mirror_source_0001` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 5 | `swe_recall_0001` | `swe_code_memory` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 6 | `web_recall_0001` | `webarena_browser_memory` | 0 | 3 | True | True | `gated_no_adapter_manifest` |
| 7 | `c5b_ssp_0002` | `c5b_500_ssp_memory` | 0 | 5 | True | True | `gated_no_adapter_manifest` |
| 8 | `external_work_0002` | `external_work_receipts` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 9 | `coherence_0002` | `long_session_coherence` | 0 | 3 | True | True | `gated_no_adapter_manifest` |
| 10 | `mirror_source_0002` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 11 | `swe_recall_0002` | `swe_code_memory` | 0 | 3 | True | True | `gated_no_adapter_manifest` |
| 12 | `web_recall_0002` | `webarena_browser_memory` | 3 | 3 | True | True | `gated_no_adapter_manifest` |
| 13 | `c5b_ssp_0003` | `c5b_500_ssp_memory` | 1 | 6 | True | True | `gated_no_adapter_manifest` |
| 14 | `external_work_0003` | `external_work_receipts` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 15 | `coherence_0003` | `long_session_coherence` | 1 | 3 | True | True | `gated_no_adapter_manifest` |
| 16 | `mirror_source_0003` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 17 | `swe_recall_0003` | `swe_code_memory` | 1 | 3 | True | True | `gated_no_adapter_manifest` |
| 18 | `web_recall_0003` | `webarena_browser_memory` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 19 | `c5b_ssp_0004` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 20 | `mirror_source_0004` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 21 | `c5b_ssp_0005` | `c5b_500_ssp_memory` | 1 | 4 | True | True | `gated_no_adapter_manifest` |
| 22 | `mirror_source_0005` | `mirror_architecture_source_pack` | 0 | 5 | True | True | `gated_no_adapter_manifest` |
| 23 | `c5b_ssp_0006` | `c5b_500_ssp_memory` | 0 | 5 | True | True | `gated_no_adapter_manifest` |
| 24 | `mirror_source_0006` | `mirror_architecture_source_pack` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 25 | `c5b_ssp_0007` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 26 | `c5b_ssp_0008` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 27 | `c5b_ssp_0001` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 28 | `external_work_0001` | `external_work_receipts` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 29 | `coherence_0001` | `long_session_coherence` | 0 | 3 | True | True | `gated_no_adapter_manifest` |
| 30 | `mirror_source_0001` | `mirror_architecture_source_pack` | 1 | 6 | True | True | `gated_no_adapter_manifest` |
| 31 | `swe_recall_0001` | `swe_code_memory` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 32 | `web_recall_0001` | `webarena_browser_memory` | 0 | 3 | True | True | `gated_no_adapter_manifest` |
| 33 | `c5b_ssp_0002` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 34 | `external_work_0002` | `external_work_receipts` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 35 | `coherence_0002` | `long_session_coherence` | 0 | 3 | True | True | `gated_no_adapter_manifest` |
| 36 | `mirror_source_0002` | `mirror_architecture_source_pack` | 3 | 6 | True | True | `gated_no_adapter_manifest` |
| 37 | `swe_recall_0002` | `swe_code_memory` | 0 | 3 | True | True | `gated_no_adapter_manifest` |
| 38 | `web_recall_0002` | `webarena_browser_memory` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 39 | `c5b_ssp_0003` | `c5b_500_ssp_memory` | 1 | 6 | True | True | `gated_no_adapter_manifest` |
| 40 | `external_work_0003` | `external_work_receipts` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 41 | `coherence_0003` | `long_session_coherence` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 42 | `mirror_source_0003` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 43 | `swe_recall_0003` | `swe_code_memory` | 1 | 3 | True | True | `gated_no_adapter_manifest` |
| 44 | `web_recall_0003` | `webarena_browser_memory` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 45 | `c5b_ssp_0004` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 46 | `mirror_source_0004` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 47 | `c5b_ssp_0005` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 48 | `mirror_source_0005` | `mirror_architecture_source_pack` | 0 | 5 | True | True | `gated_no_adapter_manifest` |
| 49 | `c5b_ssp_0006` | `c5b_500_ssp_memory` | 0 | 5 | True | True | `gated_no_adapter_manifest` |
| 50 | `mirror_source_0006` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 51 | `c5b_ssp_0007` | `c5b_500_ssp_memory` | 2 | 3 | True | True | `gated_no_adapter_manifest` |
| 52 | `c5b_ssp_0008` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 53 | `c5b_ssp_0001` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 54 | `external_work_0001` | `external_work_receipts` | 1 | 4 | True | True | `gated_no_adapter_manifest` |
| 55 | `coherence_0001` | `long_session_coherence` | 0 | 3 | True | True | `gated_no_adapter_manifest` |
| 56 | `mirror_source_0001` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 57 | `swe_recall_0001` | `swe_code_memory` | 1 | 3 | True | True | `gated_no_adapter_manifest` |
| 58 | `web_recall_0001` | `webarena_browser_memory` | 0 | 3 | True | True | `gated_no_adapter_manifest` |
| 59 | `c5b_ssp_0002` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 60 | `external_work_0002` | `external_work_receipts` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 61 | `coherence_0002` | `long_session_coherence` | 0 | 3 | True | True | `gated_no_adapter_manifest` |
| 62 | `mirror_source_0002` | `mirror_architecture_source_pack` | 0 | 5 | True | True | `gated_no_adapter_manifest` |
| 63 | `swe_recall_0002` | `swe_code_memory` | 3 | 3 | True | True | `gated_no_adapter_manifest` |
| 64 | `web_recall_0002` | `webarena_browser_memory` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 65 | `c5b_ssp_0003` | `c5b_500_ssp_memory` | 1 | 6 | True | True | `gated_no_adapter_manifest` |
| 66 | `external_work_0003` | `external_work_receipts` | 2 | 4 | True | True | `gated_no_adapter_manifest` |
| 67 | `coherence_0003` | `long_session_coherence` | 0 | 3 | True | True | `gated_no_adapter_manifest` |
| 68 | `mirror_source_0003` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 69 | `swe_recall_0003` | `swe_code_memory` | 1 | 3 | True | True | `gated_no_adapter_manifest` |
| 70 | `web_recall_0003` | `webarena_browser_memory` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 71 | `c5b_ssp_0004` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 72 | `mirror_source_0004` | `mirror_architecture_source_pack` | 1 | 3 | True | True | `gated_no_adapter_manifest` |
| 73 | `c5b_ssp_0005` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 74 | `mirror_source_0005` | `mirror_architecture_source_pack` | 0 | 5 | True | True | `gated_no_adapter_manifest` |
| 75 | `c5b_ssp_0006` | `c5b_500_ssp_memory` | 0 | 3 | True | True | `gated_no_adapter_manifest` |
| 76 | `mirror_source_0006` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 77 | `c5b_ssp_0007` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 78 | `c5b_ssp_0008` | `c5b_500_ssp_memory` | 0 | 5 | True | True | `gated_no_adapter_manifest` |
| 79 | `c5b_ssp_0001` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 80 | `external_work_0001` | `external_work_receipts` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 81 | `coherence_0001` | `long_session_coherence` | 1 | 3 | True | True | `gated_no_adapter_manifest` |
| 82 | `mirror_source_0001` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 83 | `swe_recall_0001` | `swe_code_memory` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 84 | `web_recall_0001` | `webarena_browser_memory` | 0 | 3 | True | True | `gated_no_adapter_manifest` |
| 85 | `c5b_ssp_0002` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 86 | `external_work_0002` | `external_work_receipts` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 87 | `coherence_0002` | `long_session_coherence` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 88 | `mirror_source_0002` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 89 | `swe_recall_0002` | `swe_code_memory` | 0 | 3 | True | True | `gated_no_adapter_manifest` |
| 90 | `web_recall_0002` | `webarena_browser_memory` | 3 | 3 | True | True | `gated_no_adapter_manifest` |
| 91 | `c5b_ssp_0003` | `c5b_500_ssp_memory` | 1 | 6 | True | True | `gated_no_adapter_manifest` |
| 92 | `external_work_0003` | `external_work_receipts` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 93 | `coherence_0003` | `long_session_coherence` | 3 | 3 | True | True | `gated_no_adapter_manifest` |
| 94 | `mirror_source_0003` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 95 | `swe_recall_0003` | `swe_code_memory` | 1 | 3 | True | True | `gated_no_adapter_manifest` |
| 96 | `web_recall_0003` | `webarena_browser_memory` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 97 | `c5b_ssp_0004` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 98 | `mirror_source_0004` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 99 | `c5b_ssp_0005` | `c5b_500_ssp_memory` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 100 | `mirror_source_0005` | `mirror_architecture_source_pack` | 0 | 5 | True | True | `gated_no_adapter_manifest` |

## Check Rows

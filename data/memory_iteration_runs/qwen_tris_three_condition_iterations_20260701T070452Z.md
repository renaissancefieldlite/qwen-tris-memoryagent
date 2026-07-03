# Qwen Tris Three-Condition Iterations - qwen_tris_three_condition_iterations_20260701T070452Z

- Provider: `qwen-cloud`
- Model: `qwen3.7-plus`
- Turns: `24`
- Condition B passes: `24/24`
- Condition C status: `gated_no_adapter_manifest`

## Boundary

Three-condition receipt. Condition A and B run on the selected Qwen provider. Condition C is recorded as gated unless a real tuned SSP adapter/internal-layer receipt exists.

## Conditions

- Condition A: baseline Qwen, prompt only
- Condition B: Qwen + Mirror Architecture stabilized memory/RAG/SSP packet
- Condition C: Condition C requires a real LoRA/adapter/internal-layer receipt before running.

## Family Totals

- `c5b_500_ssp_memory`: Condition B `6/6`
- `external_work_receipts`: Condition B `3/3`
- `long_session_coherence`: Condition B `3/3`
- `mirror_architecture_source_pack`: Condition B `6/6`
- `swe_code_memory`: Condition B `3/3`
- `webarena_browser_memory`: Condition B `3/3`

## Side-By-Side Turns

| Turn | Row | Family | A hits | B hits | B target | B pass | C status |
|---:|---|---|---:|---:|---|---|---|
| 1 | `c5b_ssp_0001` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 2 | `external_work_0001` | `external_work_receipts` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 3 | `coherence_0001` | `long_session_coherence` | 3 | 4 | True | True | `gated_no_adapter_manifest` |
| 4 | `mirror_source_0001` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 5 | `swe_recall_0001` | `swe_code_memory` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 6 | `web_recall_0001` | `webarena_browser_memory` | 3 | 4 | True | True | `gated_no_adapter_manifest` |
| 7 | `c5b_ssp_0002` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 8 | `external_work_0002` | `external_work_receipts` | 0 | 5 | True | True | `gated_no_adapter_manifest` |
| 9 | `coherence_0002` | `long_session_coherence` | 3 | 4 | True | True | `gated_no_adapter_manifest` |
| 10 | `mirror_source_0002` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 11 | `swe_recall_0002` | `swe_code_memory` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 12 | `web_recall_0002` | `webarena_browser_memory` | 3 | 4 | True | True | `gated_no_adapter_manifest` |
| 13 | `c5b_ssp_0003` | `c5b_500_ssp_memory` | 1 | 6 | True | True | `gated_no_adapter_manifest` |
| 14 | `external_work_0003` | `external_work_receipts` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 15 | `coherence_0003` | `long_session_coherence` | 3 | 4 | True | True | `gated_no_adapter_manifest` |
| 16 | `mirror_source_0003` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 17 | `swe_recall_0003` | `swe_code_memory` | 1 | 5 | True | True | `gated_no_adapter_manifest` |
| 18 | `web_recall_0003` | `webarena_browser_memory` | 3 | 4 | True | True | `gated_no_adapter_manifest` |
| 19 | `c5b_ssp_0004` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 20 | `mirror_source_0004` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 21 | `c5b_ssp_0005` | `c5b_500_ssp_memory` | 3 | 6 | True | True | `gated_no_adapter_manifest` |
| 22 | `mirror_source_0005` | `mirror_architecture_source_pack` | 0 | 5 | True | True | `gated_no_adapter_manifest` |
| 23 | `c5b_ssp_0006` | `c5b_500_ssp_memory` | 0 | 5 | True | True | `gated_no_adapter_manifest` |
| 24 | `mirror_source_0006` | `mirror_architecture_source_pack` | 3 | 6 | True | True | `gated_no_adapter_manifest` |

## Check Rows

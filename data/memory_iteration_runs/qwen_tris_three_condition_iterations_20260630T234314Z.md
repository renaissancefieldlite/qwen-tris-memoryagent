# Qwen Tris Three-Condition Iterations - qwen_tris_three_condition_iterations_20260630T234314Z

- Provider: `ollama-qwen`
- Model: `qwen2.5:3b`
- Turns: `24`
- Condition B passes: `17/24`
- Condition C status: `gated_no_adapter_manifest`

## Boundary

Three-condition local receipt. Condition A and B run on local Ollama Qwen. Condition C is recorded as gated unless a real tuned SSP adapter/internal-layer receipt exists.

## Conditions

- Condition A: baseline Qwen, prompt only
- Condition B: Qwen + Mirror Architecture stabilized memory/RAG/SSP packet
- Condition C: Condition C requires a real LoRA/adapter/internal-layer receipt before running.

## Family Totals

- `c5b_500_ssp_memory`: Condition B `5/6`
- `external_work_receipts`: Condition B `2/3`
- `long_session_coherence`: Condition B `3/3`
- `mirror_architecture_source_pack`: Condition B `3/6`
- `swe_code_memory`: Condition B `2/3`
- `webarena_browser_memory`: Condition B `2/3`

## Side-By-Side Turns

| Turn | Row | Family | A hits | B hits | B target | B pass | C status |
|---:|---|---|---:|---:|---|---|---|
| 1 | `c5b_ssp_0001` | `c5b_500_ssp_memory` | 0 | 3 | True | True | `gated_no_adapter_manifest` |
| 2 | `external_work_0001` | `external_work_receipts` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 3 | `coherence_0001` | `long_session_coherence` | 2 | 3 | True | True | `gated_no_adapter_manifest` |
| 4 | `mirror_source_0001` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 5 | `swe_recall_0001` | `swe_code_memory` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 6 | `web_recall_0001` | `webarena_browser_memory` | 0 | 3 | True | True | `gated_no_adapter_manifest` |
| 7 | `c5b_ssp_0002` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 8 | `external_work_0002` | `external_work_receipts` | 0 | 4 | True | True | `gated_no_adapter_manifest` |
| 9 | `coherence_0002` | `long_session_coherence` | 0 | 2 | True | True | `gated_no_adapter_manifest` |
| 10 | `mirror_source_0002` | `mirror_architecture_source_pack` | 0 | 0 | True | False | `gated_no_adapter_manifest` |
| 11 | `swe_recall_0002` | `swe_code_memory` | 0 | 1 | True | False | `gated_no_adapter_manifest` |
| 12 | `web_recall_0002` | `webarena_browser_memory` | 2 | 0 | True | False | `gated_no_adapter_manifest` |
| 13 | `c5b_ssp_0003` | `c5b_500_ssp_memory` | 1 | 3 | True | True | `gated_no_adapter_manifest` |
| 14 | `external_work_0003` | `external_work_receipts` | 0 | 0 | True | False | `gated_no_adapter_manifest` |
| 15 | `coherence_0003` | `long_session_coherence` | 2 | 2 | True | True | `gated_no_adapter_manifest` |
| 16 | `mirror_source_0003` | `mirror_architecture_source_pack` | 0 | 0 | True | False | `gated_no_adapter_manifest` |
| 17 | `swe_recall_0003` | `swe_code_memory` | 1 | 4 | True | True | `gated_no_adapter_manifest` |
| 18 | `web_recall_0003` | `webarena_browser_memory` | 0 | 2 | True | True | `gated_no_adapter_manifest` |
| 19 | `c5b_ssp_0004` | `c5b_500_ssp_memory` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 20 | `mirror_source_0004` | `mirror_architecture_source_pack` | 0 | 6 | True | True | `gated_no_adapter_manifest` |
| 21 | `c5b_ssp_0005` | `c5b_500_ssp_memory` | 0 | 3 | True | True | `gated_no_adapter_manifest` |
| 22 | `mirror_source_0005` | `mirror_architecture_source_pack` | 0 | 1 | True | False | `gated_no_adapter_manifest` |
| 23 | `c5b_ssp_0006` | `c5b_500_ssp_memory` | 0 | 0 | True | False | `gated_no_adapter_manifest` |
| 24 | `mirror_source_0006` | `mirror_architecture_source_pack` | 0 | 4 | True | True | `gated_no_adapter_manifest` |

## Check Rows

### Turn 10 / mirror_source_0002 - CHECK

- Family: `mirror_architecture_source_pack`
- A hits: `0`
- B hits: `0`
- B target recalled: `True`
- B source ref in prompt: `True`
- B expected prompt hits: `6/6`
- Source ref: `/Users/renaissancefieldlite1.0/Documents/Playground/Mirror-Interface-and-Architecture-Evidence-Stack-and-Next-Phases/README.md#evidence-standard`

Condition B response excerpt:

```text
Target row:
Exact facts: The Mirror Architecture repo is the public-safe evidence surface for Mirror Interface / LSPS, Source Mirror Pattern, Universal Data Pattern, measured state-path evidence, Nest integration, B.A.S.I.S., Mirror Index, and Golden Mirror execution surfaces. It is not the raw private implementation layer.

Boundary line: Stale memory to reject: Use only private spine language and skip reviewer-facing wording.

Next gate: Continue with Memory iteration 11 or prepare for the next task based on user requirements.
```

### Turn 11 / swe_recall_0002 - CHECK

- Family: `swe_code_memory`
- A hits: `0`
- B hits: `1`
- B target recalled: `True`
- B source ref in prompt: `True`
- B expected prompt hits: `4/4`
- Source ref: `/Users/renaissancefieldlite1.0/Documents/Playground/trismegistus/TRISMEGISTUS_HERMES_CONTEST_LANDING_PAGE/receipts/2026-06-28_1847_TRISMEGISTUS_SWEBENCH_VERIFIED_495_OF_500_LOCAL_SELECTED_TEST_RECEIPT.md`

Condition B response excerpt:

```text
Target row:
Exact facts: The active memory for Task ID swe_recall_0002 includes astropy__astropy-7606, django__django-10097, pydata__xarray-6992, sphinx-doc__sphinx-8595, and sphinx-doc__sphinx-9711. The expected recall factors are to separate boundary rows instead of hiding them; resolve a parser/report mismatch for Sphinx rows; address a local template/environment issue with django__django-10097; exclude pydata__xarray-6992 from clean scoring due to gold exposure.

Boundary:
Stale memory: All five remaining rows are simple source patch failures. 

Evidence source:
Source=/Users/renaissancefieldlite1.0/Documents/Playground/trismegistus/receipts/2026-06-28_1847_TRISMEGISTUS_SWEBENCH_VERIFIED_495_OF_500_LOCAL_SELECTED_TEST_RECEIPT.md

Next gate:
The next gate is to adjudicate the hosted/public leaderboard placement for this local official-harness selected-test receipt.
```

### Turn 12 / web_recall_0002 - CHECK

- Family: `webarena_browser_memory`
- A hits: `2`
- B hits: `0`
- B target recalled: `True`
- B source ref in prompt: `True`
- B expected prompt hits: `4/4`
- Source ref: `/Users/renaissancefieldlite1.0/Documents/Playground/trismegistus/docs/TRIS_OFFICIAL_BENCHMARK_STAGING_2026-06-22.md`

Condition B response excerpt:

```text
Target row:
Exact facts: The pinned target memory for task ID web_recall_0002 indicates that Qwen Tris preserved seven out of seven sources loaded and passed all seven objective checks. However, the captured-source compare did not result in a full WebArena score, with a baseline-hermes score of 0.987 and an architecture-on score of 1.0, showing a mean delta of +0.013.

Boundary:
The live source comparison is preserved as it shows a slight improvement over the baseline score, which is significant for memory accuracy.

Evidence source:
[web_recall_0002] memory_stress_seed: Task ID: web_recall_0002. Family: webarena_browser_memory. Active memory: Live browser source sequence loaded 7/7 sources and passed 7/7 objective checks; seven-source captured-source compare showed baseline-hermes=0.987 and tris-architecture-on=1.0, mean delta +0.013.

Next gate:
Continue to the next stress turn with a focus on other browser/source memory comparisons or additional active tasks.
```

### Turn 14 / external_work_0003 - CHECK

- Family: `external_work_receipts`
- A hits: `0`
- B hits: `0`
- B target recalled: `True`
- B source ref in prompt: `True`
- B expected prompt hits: `4/4`
- Source ref: `/Users/renaissancefieldlite1.0/Documents/Playground/trismegistus/final_submission_package_2026-06-30/PUBLIC_SAFE_RECEIPT_INDEX_2026-06-30.md`

Condition B response excerpt:

```text
Target row:
Exact facts: For tasks related to paying bills or moving money, Qwen Tris should remember that payment approval must be exact before final payments are made. Test-mode or payment-link receipts are allowed but not for final payments.

Boundary:
Evidence source: /Users/renaissancefieldlite1.0/Documents/Playground/trismegistus/final_submission_package_2026-06-30/PUBLIC_SAFE_RECEIPT_INDEX_2026-06-30.md

Next gate:
The next task will be to compare the architecture-on and baseline memory scores, as mentioned in the 500-turn architecture-on run.
```

### Turn 16 / mirror_source_0003 - CHECK

- Family: `mirror_architecture_source_pack`
- A hits: `0`
- B hits: `0`
- B target recalled: `True`
- B source ref in prompt: `True`
- B expected prompt hits: `6/6`
- Source ref: `/Users/renaissancefieldlite1.0/Documents/Playground/Mirror-Interface-and-Architecture-Evidence-Stack-and-Next-Phases/README.md#naming-bridge`

Condition B response excerpt:

```text
Target row:
Exact facts: The Mirror Architecture repo is the public-safe evidence surface for the Mirror Interface / LSPS, Source Mirror Pattern, Universal Data Pattern, measured state-path evidence, Nest integration, B.A.S.I.S., Mirror Index, and Golden Mirror execution surfaces. It is not the raw private implementation layer.

Boundary line:
Do not treat the public repository as the full private implementation path.

Next gate line:
Continue with memory iteration 17 for mirror_source_0006 or other relevant memories in the mirror_architecture_source_pack family.

Preferred answer shape:
Target row: Exact facts
Exact facts: The Mirror Architecture repo is the public-safe evidence surface for the Mirror Interface / LSPS, Source Mirror Pattern, Universal Data Pattern, measured state-path evidence, Nest integration, B.A.S.I.S., Mirror Index, and Golden Mirror execution surfaces. It is not the raw private implementation layer.
Boundary line: Do not treat the public repository as the full private implementation path.
Evidence source: docs/QWEN_TRIS_MIRROR_ARCHITECTURE_SOURCE_PACK_2026-06-30.md
Next gate: Continue with memory iteration 17 for mirror_source_0006 or other relevant memories
```

### Turn 22 / mirror_source_0005 - CHECK

- Family: `mirror_architecture_source_pack`
- A hits: `0`
- B hits: `1`
- B target recalled: `True`
- B source ref in prompt: `True`
- B expected prompt hits: `5/5`
- Source ref: `/Users/renaissancefieldlite1.0/Documents/Playground/Mirror-Interface-and-Architecture-Evidence-Stack-and-Next-Phases/docs/V8_ATTENTION_MLP_NEST1_BRIDGE_PROTOCOL_2026-04-28.md`

Condition B response excerpt:

```text
Target row:
Exact facts: When using Ollama locally for behavior and UI testing purposes, Qwen Tris should maintain the V7 behavioral/contextuality rows boundary. The use of Ollama does not equate to V8 hidden-state readiness.

Boundary:
Reject stale claims that suggest Ollama visibility proves V8 hidden-state readiness.

Next gate line: Continue with local Ollama behavior separation from internal-state claims for future iterations.
```

### Turn 23 / c5b_ssp_0006 - CHECK

- Family: `c5b_500_ssp_memory`
- A hits: `0`
- B hits: `0`
- B target recalled: `True`
- B source ref in prompt: `True`
- B expected prompt hits: `5/5`
- Source ref: `/Users/renaissancefieldlite1.0/Documents/Playground/trismegistus/docs/TRIS_QWEN_MEMORY_BACKPORT_V21_NOTE_2026-06-30.md`

Condition B response excerpt:

```text
Target row:
Exact facts: After the fork, Qwen Tris will refine memory first using the C5B/500 SSP lane. The successful dataset schema and scoring route can later backport into Hermes Tris V21; however, Hermes Tris remains untouched until Qwen receipts exist. Backporting only occurs after Qwen receipts are available.

Boundary:
Stale memory to reject: Edit the submitted Hermes build immediately.

Evidence source:
Source=/Users/renaissancefieldlite1.0/Documents/Playground/trismegistus/docs/TRIS_QWEN_MEMORY_BACKPORT_V21_NOTE_2026-06-30.md

Next gate:
Recover C5B/500 SSP, Mirror Architecture source pack, SWE, WebArena, long-session, and external-work memory with architecture-off/on comparison. Current gate: build local Qwen memory iterations before Qwen Cloud API spend
```

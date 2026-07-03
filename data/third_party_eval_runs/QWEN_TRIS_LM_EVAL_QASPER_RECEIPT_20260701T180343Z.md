# Qwen Tris Third-Party Qasper Receipt - 2026-07-01

This receipt records the first EleutherAI lm-evaluation-harness run for the
Qwen Tris Qasper lane.

## Evaluator

```text
Evaluator: EleutherAI lm-evaluation-harness
Local clone: source_inventory/lm-evaluation-harness
Clone HEAD: 97a5e2c710e2b56b9dd48f367bb6fe87bbb2c176
Install: .venv_eval
API route: Qwen Cloud OpenAI-compatible chat completions
Model: qwen-plus
Dataset: Xnhyacinth/LongBench
Official baseline task: longbench_qasper_e
Metric: LongBench qa_f1_score / score
```

## Architecture-On Task Variant

The Tris route uses the same dataset and LongBench metric, with a local
lm-eval task file that adds the repaired Qasper answer-span discipline from the
locked internal run.

```text
Task file: eval_tasks/longbench_qwen_tris/qasper_e_tris.yaml
Task name: qwen_tris_qasper_e
Metric file: eval_tasks/longbench_qwen_tris/metrics.py
Base task: longbench_qasper_e
Prompt variant: qwen_tris_repaired_qasper_answer_discipline
```

Boundary: this is a third-party evaluator run with a custom architecture-on
prompt variant. It is not an official LongBench leaderboard submission.

## Smoke Receipts

Command shape, with secrets loaded from the local environment:

```bash
OPENAI_API_KEY="$QWEN_API_KEY" .venv_eval/bin/lm_eval run \
  --model local-chat-completions \
  --model_args "model=qwen-plus,base_url=${QWEN_API_BASE}/chat/completions,tokenized_requests=False,num_concurrent=2,max_retries=3,timeout=180" \
  --tasks longbench_qasper_e \
  --apply_chat_template \
  --log_samples \
  --output_path data/third_party_eval_runs/<run_id>
```

Tris prompt-variant command adds:

```bash
--include_path eval_tasks/longbench_qwen_tris \
--tasks qwen_tris_qasper_e \
--system_instruction "<Tris stable-state benchmark discipline>"
```

```text
Baseline smoke:
data/third_party_eval_runs/lm_eval_qasper_baseline_smoke_20260701T174820Z/qwen-plus/results_2026-07-01T11-50-37.228239.json
score: 0.8222222222222223
effective samples: 3

Tris system-only smoke:
data/third_party_eval_runs/lm_eval_qasper_tris_system_smoke_20260701T175145Z/qwen-plus/results_2026-07-01T11-54-28.630381.json
score: 0.8222222222222223
effective samples: 3

Tris prompt-variant smoke:
data/third_party_eval_runs/lm_eval_qasper_tris_prompt_smoke_20260701T175707Z/qwen-plus/results_2026-07-01T11-57-19.022865.json
score: 0.8222222222222223
effective samples: 3
```

Read: all smoke paths proved the harness, dataset, metric, and Qwen API route
could execute.

## Matched 100-Row Qasper Slice

```text
Baseline official task:
data/third_party_eval_runs/lm_eval_qasper_baseline_100_20260701T175751Z/qwen-plus/results_2026-07-01T11-58-53.062072.json
task: longbench_qasper_e
score: 0.5226798775939184
stderr: 0.036029581620811005
effective samples: 100 / 224

Tris prompt variant:
data/third_party_eval_runs/lm_eval_qasper_tris_prompt_100_20260701T175940Z/qwen-plus/results_2026-07-01T12-00-43.041951.json
task: qwen_tris_qasper_e
score: 0.5405829547650837
stderr: 0.03760458932271883
effective samples: 100 / 224

Delta: +0.017903077171165273
Wins / losses / ties: 20 / 22 / 58
```

Read: the third-party harness reproduces a positive 100-row Qasper result for
the repaired Tris answer-span discipline. The row-level read is not a sweep; it
is a net-positive mean under the same scorer, with a majority of ties and both
wins and losses still present.

Sample JSONL boundary: lm-eval sample files include full benchmark article
contexts. They were moved out of the project public tree to
`/Volumes/Samsung SSD 990 2TB/Playground/_PRIVATE_QWEN_TRIS_EVAL_SAMPLES_20260701/`.
Public-safe receipts keep aggregate result JSON and this markdown summary.

## Full Baseline Receipt

```text
Baseline full official task:
data/third_party_eval_runs/lm_eval_qasper_baseline_full_20260701T180110Z/qwen-plus/results_2026-07-01T12-03-28.880163.json
task: longbench_qasper_e
score: 0.4812428635163242
stderr: 0.023809416453110393
effective samples: 224 / 224
limit: None
```

The full baseline run briefly hit Alibaba/Qwen quota retry responses near the
end, but lm-eval retried and completed all 224 rows.

## Full Tris Prompt-Variant Receipt

After Qwen quota was confirmed, the full Tris prompt-variant task was rerun
through the same lm-eval harness with protected logging and no sample JSONL
output.

```text
Tris full prompt-variant task:
data/third_party_eval_runs/lm_eval_qasper_tris_prompt_full_20260701T190001Z/qwen-plus/results_2026-07-01T13-08-47.277911.json
task: qwen_tris_qasper_e
score: 0.48259642030075983
stderr: 0.024899377106654862
effective samples: 224 / 224
limit: None
```

Full-task comparison:

```text
Baseline full score: 0.4812428635163242
Tris full score: 0.48259642030075983
Delta: +0.00135355678443563
```

Read: the full Qasper third-party run is now positive, but only slightly. The
stronger Qasper signal remains the locked 100-row public slice and matched
100-row lm-eval receipt. The full 224-row result is useful because it preserves
direction under the complete Qasper split; it should not be framed as a large
full-task lift.

Public-safe boundary: the full Tris run was executed without `--log_samples`, so
no raw benchmark article contexts were written into this public project tree.

# Qwen Tris LongBench Public Slice - qwen_tris_longbench_public_slice_20260701T192927Z

- Benchmark: `LongBench public data.zip`
- Provider: `qwen-cloud`
- Model: `qwen-plus`
- Items: `1`
- Skipped provider-blocked rows: `0`
- Condition A mean: `0.190`
- Condition B mean: `0.190`
- Delta: `+0.000`

## Boundary

Public LongBench smoke slice. This is not a full LongBench leaderboard claim; it is a source-backed answer-key accuracy receipt that can scale to larger slices.

## Conditions

- Condition A: baseline Qwen prompt-only answer discipline
- Condition B: Qwen Tris stable-state answer discipline

## Family Totals

- `hotpotqa_e`: n=1 A=0.190 B=0.190 delta=+0.000

## Rows

| # | Dataset | Metric | A | B | Delta | Gold | A prediction | B prediction |
|---:|---|---|---:|---:|---:|---|---|---|
| 1 | `hotpotqa_e` | `token_f1` | 0.190 | 0.190 | +0.000 | George Clooney, Thekla Reuten, Violante Placido, Irina Björklund, and Paolo Bonacelli | George Clooney, Ray Smith, Cyril Luckham, Derek Godfrey, John Neville | George Clooney, Ray Smith, Cyril Luckham, Derek Godfrey, John Neville |

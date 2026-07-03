# Qwen Tris LongBench Public Slice - qwen_tris_longbench_public_slice_20260701T192500Z

- Benchmark: `LongBench public data.zip`
- Provider: `qwen-cloud`
- Model: `qwen-plus`
- Items: `1`
- Skipped provider-blocked rows: `0`
- Condition A mean: `0.952`
- Condition B mean: `0.000`
- Delta: `-0.952`

## Boundary

Public LongBench smoke slice. This is not a full LongBench leaderboard claim; it is a source-backed answer-key accuracy receipt that can scale to larger slices.

## Conditions

- Condition A: baseline Qwen prompt-only answer discipline
- Condition B: Qwen Tris stable-state answer discipline

## Family Totals

- `hotpotqa_e`: n=1 A=0.952 B=0.000 delta=-0.952

## Rows

| # | Dataset | Metric | A | B | Delta | Gold | A prediction | B prediction |
|---:|---|---|---:|---:|---:|---|---|---|
| 1 | `hotpotqa_e` | `token_f1` | 0.952 | 0.000 | -0.952 | George Clooney, Thekla Reuten, Violante Placido, Irina Björklund, and Paolo Bonacelli | George Clooney, Violante Placido, Thekla Reuten, Irina Björklund, Paolo Bonacelli | John Neville, Ray Smith, Cyril Luckham, Derek Godfrey, Ann Bell |

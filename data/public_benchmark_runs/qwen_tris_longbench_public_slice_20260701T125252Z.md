# Qwen Tris LongBench Public Slice - qwen_tris_longbench_public_slice_20260701T125252Z

- Benchmark: `LongBench public data.zip`
- Provider: `qwen-cloud`
- Model: `qwen-plus`
- Items: `10`
- Condition A mean: `0.200`
- Condition B mean: `0.100`
- Delta: `-0.100`

## Boundary

Public LongBench smoke slice. This is not a full LongBench leaderboard claim; it is a source-backed answer-key accuracy receipt that can scale to larger slices.

## Conditions

- Condition A: baseline Qwen prompt-only answer discipline
- Condition B: Qwen Tris stable-state answer discipline

## Family Totals

- `passage_count_e`: n=10 A=0.200 B=0.100 delta=-0.100

## Rows

| # | Dataset | Metric | A | B | Delta | Gold | A prediction | B prediction |
|---:|---|---|---:|---:|---:|---|---|---|
| 1 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 6 | 5 | 5 |
| 2 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 10 | 7 | 7 |
| 3 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 4 | 3 | 3 |
| 4 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 6 | 5 | 4 |
| 5 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 12 | Let's carefully compare all 18 paragraphs to identify duplicates.  We'll group identical paragraphs by content (ignoring | 7 |
| 6 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 8 | 4 | 4 |
| 7 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 9 | 7 | 7 |
| 8 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 7 | 7 | 7 |
| 9 | `passage_count_e` | `numeric_accuracy` | 1.000 | 0.000 | -1.000 | 3 | 3 | 4 |
| 10 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 9 | Let's carefully compare all 11 paragraphs to identify duplicates.  We'll group identical paragraphs:  - Paragraph 1: Kew | 5 |

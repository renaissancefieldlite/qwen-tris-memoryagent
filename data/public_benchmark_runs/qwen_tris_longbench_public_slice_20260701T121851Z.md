# Qwen Tris LongBench Public Slice - qwen_tris_longbench_public_slice_20260701T121851Z

- Benchmark: `LongBench public data.zip`
- Provider: `qwen-cloud`
- Model: `qwen-plus`
- Items: `6`
- Condition A mean: `1.000`
- Condition B mean: `0.974`
- Delta: `-0.026`

## Boundary

Public LongBench smoke slice. This is not a full LongBench leaderboard claim; it is a source-backed answer-key accuracy receipt that can scale to larger slices.

## Conditions

- Condition A: baseline Qwen prompt-only answer discipline
- Condition B: Qwen Tris stable-state answer discipline

## Family Totals

- `passage_retrieval_en_e`: n=2 A=1.000 B=1.000 delta=+0.000
- `trec_e`: n=2 A=1.000 B=1.000 delta=+0.000
- `multifieldqa_en_e`: n=2 A=1.000 B=0.923 delta=-0.077

## Rows

| # | Dataset | Metric | A | B | Delta | Gold | A prediction | B prediction |
|---:|---|---|---:|---:|---:|---|---|---|
| 1 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 6 | Paragraph 6 | Paragraph 6 |
| 2 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 1 | Paragraph 1 | Paragraph 1 |
| 3 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 4 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Date | Date | Date |
| 5 | `multifieldqa_en_e` | `token_f1` | 1.000 | 0.846 | -0.154 | Exposure to sunlight or strong light may cause permanent yellow spot damage on the screen. | Exposure to sunlight or strong light may cause permanent yellow spot damage on the screen. | Exposure to direct sunlight may cause permanent yellow spot damage on the screen. |
| 6 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Vice Admiral. | Vice Admiral | Vice Admiral |

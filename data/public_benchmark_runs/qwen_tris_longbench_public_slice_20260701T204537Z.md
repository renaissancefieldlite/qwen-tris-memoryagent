# Qwen Tris LongBench Public Slice - qwen_tris_longbench_public_slice_20260701T204537Z

- Benchmark: `LongBench public data.zip`
- Provider: `qwen-cloud`
- Model: `qwen-plus`
- Items: `298`
- Skipped provider-blocked rows: `2`
- Condition A mean: `0.540`
- Condition B mean: `0.647`
- Delta: `+0.107`

## Boundary

Public LongBench smoke slice. This is not a full LongBench leaderboard claim; it is a source-backed answer-key accuracy receipt that can scale to larger slices.

## Conditions

- Condition A: baseline Qwen prompt-only answer discipline
- Condition B: Qwen Tris stable-state answer discipline

## Family Totals

- `passage_retrieval_en_e`: n=49 A=1.000 B=1.000 delta=+0.000
- `passage_count_e`: n=50 A=0.364 B=0.382 delta=+0.018
- `trec_e`: n=49 A=0.184 B=0.755 delta=+0.571
- `multifieldqa_en_e`: n=50 A=0.464 B=0.443 delta=-0.021
- `qasper_e`: n=50 A=0.480 B=0.510 delta=+0.030
- `hotpotqa_e`: n=50 A=0.748 B=0.800 delta=+0.052

## Skipped Provider-Blocked Rows

- row 26 `passage_retrieval_en_e` condition `tris` _id `ea5586b6e23b0aa0e9fe7b18cfb767310a0f674b8cc50728`: provider returned data_inspection_failed
- row 116 `trec_e` condition `baseline` _id `46277319e9552e62f870ccefb9cc905c5d00813866e923e7`: provider returned data_inspection_failed

## Rows

| # | Dataset | Metric | A | B | Delta | Gold | A prediction | B prediction |
|---:|---|---|---:|---:|---:|---|---|---|
| 1 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 6 | Paragraph 6 | Paragraph 6 |
| 2 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 6 | Paragraph 6 | Paragraph 6 |
| 3 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 12 | Paragraph 12 | Paragraph 12 |
| 4 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 7 | Paragraph 7 | Paragraph 7 |
| 5 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 3 | Paragraph 3 | Paragraph 3 |
| 6 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 2 | Paragraph 2 | Paragraph 2 |
| 7 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 8 | Paragraph 8 | Paragraph 8 |
| 8 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 11 | Paragraph 11 | Paragraph 11 |
| 9 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 8 | Paragraph 8 | Paragraph 8 |
| 10 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 3 | Paragraph 3 | Paragraph 3 |
| 11 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 11 | Paragraph 11 | Paragraph 11 |
| 12 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 7 | Paragraph 7 | Paragraph 7 |
| 13 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 7 | Paragraph 7 | Paragraph 7 |
| 14 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 3 | Paragraph 3 | Paragraph 3 |
| 15 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 5 | Paragraph 5 | Paragraph 5 |
| 16 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 3 | Paragraph 3 | Paragraph 3 |
| 17 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 4 | Paragraph 4 | Paragraph 4 |
| 18 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 1 | Paragraph 1 | Paragraph 1 |
| 19 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 2 | Paragraph 2 | Paragraph 2 |
| 20 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 2 | Paragraph 2 | Paragraph 2 |
| 21 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 4 | Paragraph 4 | Paragraph 4 |
| 22 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 7 | Paragraph 7 | Paragraph 7 |
| 23 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 1 | Paragraph 1 | Paragraph 1 |
| 24 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 14 | Paragraph 14 | Paragraph 14 |
| 25 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 12 | Paragraph 12 | Paragraph 12 |
| 27 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 5 | Paragraph 5 | Paragraph 5 |
| 28 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 10 | Paragraph 10 | Paragraph 10 |
| 29 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 8 | Paragraph 8 | Paragraph 8 |
| 30 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 7 | Paragraph 7 | Paragraph 7 |
| 31 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 2 | Paragraph 2 | Paragraph 2 |
| 32 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 2 | Paragraph 2 | Paragraph 2 |
| 33 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 11 | Paragraph 11 | Paragraph 11 |
| 34 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 5 | Paragraph 5 | Paragraph 5 |
| 35 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 4 | Paragraph 4 | Paragraph 4 |
| 36 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 9 | Paragraph 9 | Paragraph 9 |
| 37 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 4 | Paragraph 4 | Paragraph 4 |
| 38 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 9 | Paragraph 9 | Paragraph 9 |
| 39 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 4 | Paragraph 4 | Paragraph 4 |
| 40 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 9 | Paragraph 9 | Paragraph 9 |
| 41 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 4 | Paragraph 4 | Paragraph 4 |
| 42 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 1 | Paragraph 1 | Paragraph 1 |
| 43 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 11 | Paragraph 11 | Paragraph 11 |
| 44 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 2 | Paragraph 2 | Paragraph 2 |
| 45 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 3 | Paragraph 3 | Paragraph 3 |
| 46 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 9 | Paragraph 9 | Paragraph 9 |
| 47 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 1 | Paragraph 1 | Paragraph 1 |
| 48 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 8 | Paragraph 8 | Paragraph 8 |
| 49 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 5 | Paragraph 5 | Paragraph 5 |
| 50 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 10 | Paragraph 10 | Paragraph 10 |
| 51 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 52 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 53 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 6 | 5 | 5 |
| 54 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 9 | 6 | 6 |
| 55 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 14 | 9 | 7 |
| 56 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 57 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 58 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 59 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 60 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 12 | 7 | 7 |
| 61 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 10 | 7 | 7 |
| 62 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 8 | 5 | 5 |
| 63 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 4 | 4 | 4 |
| 64 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 6 | 6 | 6 |
| 65 | `passage_count_e` | `official_numeric_fraction` | 0.062 | 0.000 | -0.062 | 7 | We are given 10 paragraphs and asked to count how many **unique** (non-duplicate) paragraphs there are.  Let’s compare t | 5 |
| 66 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 15 | 8 | 8 |
| 67 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 7 | 4 | 4 |
| 68 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.076 | +0.076 | 12 | 8 | We are given 12 paragraphs and asked to count how many **unique** (non-duplicate) paragraphs there are.  Let’s compare t |
| 69 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 70 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 5 | 4 | 4 |
| 71 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 6 | 4 | 4 |
| 72 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 11 | 7 | 6 |
| 73 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 10 | 6 | 6 |
| 74 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 8 | 6 | 6 |
| 75 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 11 | 5 | 5 |
| 76 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 5 | 4 | 4 |
| 77 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 78 | `passage_count_e` | `official_numeric_fraction` | 0.082 | 0.000 | -0.082 | 6 | We are given 12 paragraphs and asked to count how many **unique** (non-duplicate) paragraphs there are.  Let’s compare t | 5 |
| 79 | `passage_count_e` | `official_numeric_fraction` | 0.043 | 0.000 | -0.043 | 8 | We are given 14 paragraphs and asked to count how many **unique** (non-duplicate) paragraphs there are.  Let’s compare t | 7 |
| 80 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 81 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 9 | 7 | 7 |
| 82 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 9 | 7 | 7 |
| 83 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 4 | 4 | 4 |
| 84 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 11 | 7 | 7 |
| 85 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 2 | 3 | 3 |
| 86 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 8 | 4 | 4 |
| 87 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 88 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 2 | 3 | 3 |
| 89 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 5 | 5 | 5 |
| 90 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 14 | 6 | 7 |
| 91 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 92 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 7 | 5 | 5 |
| 93 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 7 | 4 | 4 |
| 94 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 95 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 96 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 97 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 9 | 8 | 7 |
| 98 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 1.000 | +1.000 | 5 | 4 | 5 |
| 99 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 13 | 9 | 8 |
| 100 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 7 | 4 | 4 |
| 101 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Individual | Type: Individual | Individual |
| 102 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 103 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Definition of something | Type: Element and substance | Definition of something |
| 104 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Date | Type: Date | Date |
| 105 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 106 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Other location | Type: Other location | Other location |
| 107 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Description of a person | Description of a person | Description of a person |
| 108 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Other number | Type: Frequency | Frequency |
| 109 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Distance, linear measure | Type: Distance, linear measure | Distance, linear measure |
| 110 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Expression abbreviated | Type: Expression abbreviated | Expression abbreviated |
| 111 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Lasting time of somethin | Type: Description of something | Number of something |
| 112 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Definition of something | Type: Definition of something | Definition of something |
| 113 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Other location | Type: Astronomical object | Other entity |
| 114 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Other location | Other location | Other location |
| 115 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Individual | Type: Individual | Individual |
| 117 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Definition of something | Type: Definition of something | Definition of something |
| 118 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Other location | Type: Mountain | Other entity |
| 119 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Mountain | Type: Mountain | Mountain |
| 120 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Distance, linear measure | Number of something | Number of something |
| 121 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 122 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Lasting time of somethin | Type: Lasting time of somethin | Lasting time of somethin |
| 123 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Definition of something | Type: Definition of something | Definition of something |
| 124 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Definition of something | Type: Disease and medicine | Disease and medicine |
| 125 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | City | City | City |
| 126 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Definition of something | Type: Food | Definition of something |
| 127 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Reason | Type: Reason | Reason |
| 128 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Other entity | Type: Number of something | Other number |
| 129 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Definition of something | Type: Definition of something | Definition of something |
| 130 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Vehicle | Type: Vehicle | Vehicle |
| 131 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Element and substance | Type: Element and substance | Element and substance |
| 132 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Definition of something | Type: Definition of something | Definition of something |
| 133 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Date | Type: Date | Date |
| 134 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Individual | Type: Individual | Individual |
| 135 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Other entity | Type: Price | Price |
| 136 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Element and substance | Type: Element and substance | Definition of something |
| 137 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Currency name | Type: Currency | Currency |
| 138 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Definition of something | Type: Definition of something | Definition of something |
| 139 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Definition of something | Type: Definition of something | Definition of something |
| 140 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Description of something | Type: Description of something | Description of something |
| 141 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Plant | Type: Other entity | Definition of something |
| 142 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Number of something | Type: Number of something | Number of something |
| 143 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Individual | Type: Individual | Individual |
| 144 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Individual | Type: Individual | Individual |
| 145 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Manner of an action | Type: Manner of an action | Manner of an action |
| 146 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 147 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Color | Color | Color |
| 148 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Description of a person | Type: Description of a person | Description of a person |
| 149 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 150 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Vehicle | Type: Product | Product |
| 151 | `multifieldqa_en_e` | `token_f1` | 0.200 | 0.364 | +0.164 | The focus of the study was on the reactive radical ethynyl (C$_2$H). | C$_2$H | ethynyl (C$_2$H) |
| 152 | `multifieldqa_en_e` | `token_f1` | 0.500 | 0.273 | -0.227 | Other toxic products. | Other toxic products, rather than against saline (genuine placebo). | None of the vaccines were trialed against genuine placebo; they were only compared with other toxic products rather than |
| 153 | `multifieldqa_en_e` | `token_f1` | 0.533 | 0.533 | +0.000 | The authors used simulated data and real data from a wireless MISO channel. | Simulated and real data | simulated and real data |
| 154 | `multifieldqa_en_e` | `token_f1` | 0.341 | 0.419 | +0.077 | Verifying other meta-information such as patient's gender, age, race, etc. | Applying the findings to non-Japanese EHRs, verifying other meta-information (e.g., patient's gender, age, race, religio | Applying the findings to non-Japanese EHRs, verifying other meta-information such as patient's gender, age, race, religi |
| 155 | `multifieldqa_en_e` | `token_f1` | 0.125 | 0.125 | +0.000 | The three subsets are V+, V0, and V-, determined by the Kullback-Leibler information distance. | V⁺, V₀, and V⁻ | V⁺, V₀, and V⁻ |
| 156 | `multifieldqa_en_e` | `token_f1` | 0.647 | 0.468 | -0.179 | $\int f'(u) \psi^2 \le \int \| \nabla \psi\|^2, \forall \psi \in C_c^2$. | A solution $ u $ of $ -\Delta u = f(u) $ in $ \mathbb{R}^N $ is stable provided   $$ \int f'(u) \psi^2 \le \int \| \nabla | A solution $ u $ of $ -\Delta u = f(u) $ in $ {\mathbb{R}}^N $ is stable provided   \[ \int f'(u) \psi^2 \le \int \| \nab |
| 157 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | 21. | 21 | 21 |
| 158 | `multifieldqa_en_e` | `token_f1` | 0.000 | 0.000 | +0.000 | 48V. | 20V | 20V |
| 159 | `multifieldqa_en_e` | `token_f1` | 0.667 | 0.667 | +0.000 | The Wallace electorate. | Wallace | Wallace |
| 160 | `multifieldqa_en_e` | `token_f1` | 0.600 | 0.600 | +0.000 | The paper was published on 7 March 2023. | 7 March 2023 | 7 March 2023 |
| 161 | `multifieldqa_en_e` | `token_f1` | 0.222 | 0.222 | +0.000 | Weep Not, Child was first published in 1964. | 1964 | 1964 |
| 162 | `multifieldqa_en_e` | `token_f1` | 0.516 | 0.444 | -0.072 | Multiple vacuum processing apparatuses are arranged in parallel. | The vacuum processing system is configured with multiple vacuum processing apparatuses arranged in parallel, where all v | The vacuum processing system is configured with multiple vacuum processing apparatuses arranged in parallel, where all v |
| 163 | `multifieldqa_en_e` | `token_f1` | 0.452 | 0.203 | -0.249 | NFPA and FPSA greatly outperform GMRES and DSA. | NFPA and FPSA tremendously outperform GMRES and DSA in runtime and require far fewer iterations, by orders of magnitude, | NFPA and FPSA tremendously outperform GMRES and DSA in runtime for all cases, with runtimes and iterations greatly reduc |
| 164 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Romance novels and women's fiction. | Romance novels and women's fiction | romance novels and women's fiction |
| 165 | `multifieldqa_en_e` | `token_f1` | 0.667 | 0.667 | +0.000 | URPC2017, URPC2018, URPC2019, URPC2020_ZJ and URPC2020_DL. | URPC2017 and URPC2018 | URPC2017 and URPC2018 |
| 166 | `multifieldqa_en_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Unknown. | No, there is no solid proof of the existence of heaven and hell; nothing can give a solid proof of their existence, nor  | Nothing can give a solid proof of the existence of heaven and hell, yet, nothing can disprove it either. |
| 167 | `multifieldqa_en_e` | `token_f1` | 0.875 | 0.737 | -0.138 | He became deputy prime minister and minister of finance. | Deputy Prime Minister and Minister of Finance | Deputy Prime Minister of New Zealand and Minister of Finance |
| 168 | `multifieldqa_en_e` | `token_f1` | 0.600 | 0.600 | +0.000 | The generative interactive model used in the method is called the Coupled Generalized Dynamic Bayesian Network (C-GDBN). | Coupled Generalized Dynamic Bayesian Network (C-GDBN) | coupled generalized dynamic Bayesian network (C-GDBN) |
| 169 | `multifieldqa_en_e` | `token_f1` | 0.121 | 0.077 | -0.044 | It uses a content-recognition module or algorithm. | A media application determines the context of an event using a content-recognition module or algorithm that may employ t | A media application determines the context of an event using a content-recognition module or algorithm that may employ o |
| 170 | `multifieldqa_en_e` | `token_f1` | 0.261 | 0.200 | -0.061 | Smartphones are more compact and power constrained. | Smartphones are more compact and power-constrained (limited to ~1W), require integrated cellular modems, and have strict | Smartphones are far more compact and power constrained, with SoCs limited to around 1W due to batteries and thermal diss |
| 171 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | 172. | 172 | 172 |
| 172 | `multifieldqa_en_e` | `token_f1` | 0.857 | 0.621 | -0.236 | An unsupervised method based on the information bottleneck and contrastive learning. | Unsupervised method based on the information bottleneck using contrastive learning and compositional communication. | An unsupervised method based on the information bottleneck to capture both referential complexity and task-specific util |
| 173 | `multifieldqa_en_e` | `token_f1` | 0.486 | 0.514 | +0.028 | The longerons bow up from the building surface, forming a "banana" shape. | The problem is that the once straight longerons bow up from the building surface, forming an unacceptable "banana" shape | The problem encountered when building the fuselage sides is that the once straight longerons bow up from the building su |
| 174 | `multifieldqa_en_e` | `token_f1` | 0.061 | 0.071 | +0.011 | The belief entropy decreases more steadily. | The time required to update the robot's belief does not increase with the complexity of the environment (e.g., number of | The time required to update the robot's belief does not increase with the complexity of the environment, and in fact, be |
| 175 | `multifieldqa_en_e` | `token_f1` | 0.286 | 0.286 | +0.000 | Players can skip dialogue on the quest map by pressing the 'SKIP' button. | By pressing ‘SKIP’. | By pressing ‘SKIP’. |
| 176 | `multifieldqa_en_e` | `token_f1` | 0.229 | 0.229 | +0.000 | Privacy concerns and skepticism about its effectiveness. | Governor Rick Scott cited privacy concerns, expressed skepticism that the monitoring program would work, and raised the  | Governor Rick Scott cited privacy concerns, expressed skepticism that the monitoring program would work, and raised the  |
| 177 | `multifieldqa_en_e` | `token_f1` | 0.000 | 0.000 | +0.000 | 5. | Five | five |
| 178 | `multifieldqa_en_e` | `token_f1` | 0.833 | 0.556 | -0.278 | L = 8 and L = 14. | L = 6, L = 8, and L = 14 | L = 6, L = 8, and L = 14 Heisenberg chains with periodic boundary conditions |
| 179 | `multifieldqa_en_e` | `token_f1` | 0.800 | 1.000 | +0.200 | Low temperature scanning tunneling microscopy and spectroscopy (STM/STS). | Low-temperature scanning tunneling microscopy and spectroscopy (STM/STS) | Low temperature scanning tunneling microscopy and spectroscopy (STM/STS) |
| 180 | `multifieldqa_en_e` | `token_f1` | 0.091 | 0.091 | +0.000 | There are 14,520 attendees, including 7,152 chemical scientists, 5,059 students, 1,283 exhibitors, 119 precollege teache | 14,520 | 14,520 |
| 181 | `multifieldqa_en_e` | `token_f1` | 0.333 | 0.333 | +0.000 | No, it is not necessary. | No | No |
| 182 | `multifieldqa_en_e` | `token_f1` | 0.500 | 1.000 | +0.500 | Power-law functions. | Power-law distributions | Power-law functions |
| 183 | `multifieldqa_en_e` | `token_f1` | 0.250 | 0.190 | -0.060 | The main topic of the text is Iraq's politics and current situation. | The main topic of the text is the political, social, and humanitarian situation in Iraq as of late December 2010, includ | The main topic of the text is the Iraq War and its ongoing consequences in December 2010, including political instabilit |
| 184 | `multifieldqa_en_e` | `token_f1` | 0.065 | 0.065 | +0.000 | Flexibility. | The main advantage of a horizontal business model for mobile devices is flexibility, allowing vendors to offer a wide ra | The main advantage is flexibility; as costs drop and the market expands, it will be increasingly necessary for vendors l |
| 185 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Vitamins K3, K4, and K5. | Vitamins K3, K4, and K5 | vitamins K3, K4, and K5 |
| 186 | `multifieldqa_en_e` | `token_f1` | 0.411 | 0.264 | -0.147 | The relationships between catch per set and fishing behavior variables differ when comparing unstandardized CPUE and sta | The relationships between catch per set and fishing behavior variables differ because unstandardized CPUE (individuals p | Unstandardised CPUE (individuals per set) shows a positive relationship with number of hooks, engine power, and number o |
| 187 | `multifieldqa_en_e` | `token_f1` | 0.541 | 0.690 | +0.149 | As the transition probability increases, the learning rate initially rises and then declines. | The learning rate in the static agent rapidly rises as the transition probability increases from 0, peaks, and then slow | The learning rate rapidly rises as the transition probability increases from 0, peaks, and then slowly declines, eventua |
| 188 | `multifieldqa_en_e` | `token_f1` | 1.000 | 0.200 | -0.800 | "I have seen the Lord.". | "I have seen the Lord." | “I have seen the Lord”; and she told them that he had said these things to her. |
| 189 | `multifieldqa_en_e` | `token_f1` | 0.333 | 0.333 | +0.000 | Watt, one joule per second. | watt | watt |
| 190 | `multifieldqa_en_e` | `token_f1` | 0.095 | 0.095 | +0.000 | Yes, individual molecules of indeno[1,2-a]fluorene can switch between open-shell and closed-shell states by changing the | Yes | Yes |
| 191 | `multifieldqa_en_e` | `token_f1` | 0.170 | 0.131 | -0.039 | Severe anemia that begins even before birth. | Severe anemia beginning before birth, enlargement of the placenta, heart, liver, spleen, and adrenal glands, fluid accum | Severe anemia that begins even before birth; affected fetuses develop severe anemia as early as the first trimester of p |
| 192 | `multifieldqa_en_e` | `token_f1` | 0.393 | 0.300 | -0.093 | The sticking point in the political showdown over the budget is how much spending to cut. | The sticking points in the political showdown over the budget are disagreements over how much to cut spending, policy ri | The sticking points in the political showdown over the budget are how much spending to cut, policy riders such as regula |
| 193 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | 1766. | 1766 | 1766 |
| 194 | `multifieldqa_en_e` | `token_f1` | 0.960 | 0.960 | +0.000 | The time required to update the belief does not increase with the complexity of the environment. | The time required to update the robot's belief does not increase with the complexity of the environment. | The time required to update the robot's belief does not increase with the complexity of the environment. |
| 195 | `multifieldqa_en_e` | `token_f1` | 0.261 | 0.200 | -0.061 | Quill harmed states more than anticipated due to the Internet. | Justice Kennedy argued that the Internet had caused far-reaching systemic and structural changes in the economy, making  | Justice Kennedy argued that “[t]he Internet has caused far-reaching systemic and structural changes in the economy” and  |
| 196 | `multifieldqa_en_e` | `token_f1` | 0.261 | 0.750 | +0.489 | Nuclear liquid-gas transition in lattice QCD. | The main focus of the research paper is determining the nuclear liquid-gas transition in the strong coupling regime of l | The nuclear liquid-gas transition in the strong coupling regime of lattice QCD. |
| 197 | `multifieldqa_en_e` | `token_f1` | 0.129 | 0.167 | +0.038 | Using the vacuum Einstein equation and the Baez-Bunn form. | The function $\beta(r)$ is determined by applying the vacuum Einstein equations in the Baez-Bunn form—specifically, the  | The function $\beta(r)$ is determined by applying the vacuum Einstein equations in the Baez-Bunn form (\ref{EinsteinVacu |
| 198 | `multifieldqa_en_e` | `token_f1` | 0.727 | 0.727 | +0.000 | Legacies of Losing in American Politics and an expanded edition of The Rhetorical Presidency in the Princeton Classics s | Legacies of Losing in American Politics, with Nicole Mellow (University of Chicago Press, Fall 2017), and an expanded ed | Legacies of Losing in American Politics, with Nicole Mellow (University of Chicago Press, Fall 2017), and an expanded ed |
| 199 | `multifieldqa_en_e` | `token_f1` | 0.638 | 0.622 | -0.016 | SNNs have the potential to better model and explain the functional hierarchy and mechanisms of the visual system. | SNNs have high potential as promising candidates to better model and explain the functional hierarchy and mechanisms of  | SNNs could serve as promising candidates to better model and explain the functional hierarchy and mechanisms of the visu |
| 200 | `multifieldqa_en_e` | `token_f1` | 0.182 | 0.182 | +0.000 | The water depth in the Greater Ekofisk Area is 70-75 meters. | 70-75 metres | 70-75 metres |
| 201 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | SQuAD; SQuAD | SQuAD dataset | SQuAD dataset |
| 202 | `qasper_e` | `token_f1` | 0.800 | 0.800 | +0.000 | relation classification dataset of the SemEval 2010 task 8; SemEval 2010 task 8 BIBREF8 | SemEval 2010 task 8 dataset | SemEval 2010 task 8 dataset |
| 203 | `qasper_e` | `token_f1` | 0.158 | 0.133 | -0.025 | 2174000000, 989000000; 2174 million tokens for English and 989 million tokens for Russian | The English training corpus was the English Wikipedia dump from February 2017; the Russian training corpus was a concate | English Wikipedia dump from February 2017; Russian Wikipedia dump from December 2018 concatenated with the full Russian  |
| 204 | `qasper_e` | `token_f1` | 0.333 | 0.173 | -0.160 | Spearman correlation values of GM_KL model evaluated on the benchmark word similarity datasets.
Evaluation results of GM | The qualitative experiments involved listing nearest neighbors for query words and their component IDs to demonstrate se | The qualitative experiments performed on benchmark datasets are not explicitly described; the article only mentions qual |
| 205 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Using DSC loss improves the F1 score by +0.58 for MRPC and +0.73 for QQP; +0.58 | +0.58 for MRPC and +0.73 for QQP | +0.58 for MRPC and +0.73 for QQP |
| 206 | `qasper_e` | `token_f1` | 0.204 | 0.129 | -0.075 | reducing the variance of an estimator,  EGL method in BIBREF3 is almost the same as Eq. ( EQREF8 ), except the gradient' | They calculate variance from the model outputs using the Fisher Information Matrix, as indicated by the asymptotic distr | They calculate variance from the model outputs using the Fisher Information Matrix, where the asymptotic distribution of |
| 207 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | LSTM; LSTM | LSTM | LSTM |
| 208 | `qasper_e` | `token_f1` | 0.071 | 0.138 | +0.067 | These 8 tasks require different competencies and a different level of understanding of the document to be well answered | Natural language questions about hotel reviews that challenge relational reasoning competencies. | Natural language questions about hotel reviews that challenge 8 relational reasoning competencies. |
| 209 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | SVM, No-Answer Baseline (NA) , Word Count Baseline, Human Performance; No-Answer Baseline (NA), Word Count Baseline, Hum | Yes | Yes |
| 210 | `qasper_e` | `token_f1` | 0.667 | 1.000 | +0.333 | 53 documents; 53 documents | 53 | 53 documents |
| 211 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | from Food.com | Food.com | Food.com |
| 212 | `qasper_e` | `token_f1` | 0.396 | 0.392 | -0.004 | We also evaluate all five models on downstream tasks from the VecEval suite BIBREF13 , using only the tasks for which tr | They evaluate their resulting word embeddings using intrinsic evaluations (word similarity and word analogy tasks), down | They evaluate their resulting word embeddings using intrinsic evaluations (word similarity and word analogy tasks), down |
| 213 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Adv. Heart Disease, Adv. Lung Disease, Alcohol Abuse, Chronic Neurologic Dystrophies, Dementia, Depression, Developmenta | unanswerable | unanswerable |
| 214 | `qasper_e` | `token_f1` | 0.842 | 0.947 | +0.105 | 204 tokens; Most texts, however, range roughly from 150 to 250 tokens. | Most essays range roughly from 150 to 250 tokens. | Most texts range roughly from 150 to 250 tokens. |
| 215 | `qasper_e` | `token_f1` | 0.129 | 0.143 | +0.014 | (VVD shop_VV0 II, VVD shopping_VVG II); patterns for generating all types of errors | Patterns over words and part-of-speech (POS) tags, in the form of (incorrect phrase, correct phrase), including up to on | patterns over words and part-of-speech (POS) tags |
| 216 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | No; No | unanswerable | unanswerable |
| 217 | `qasper_e` | `token_f1` | 0.826 | 0.826 | +0.000 | Random Kitchen Sink method uses a kernel function to map data vectors to a space where linear separation is possible.; e | The Random Kitchen Sink (RKS) approach is a method that explicitly maps data vectors to a space where linear separation  | The Random Kitchen Sink (RKS) approach is a method that explicitly maps data vectors to a space where linear separation  |
| 218 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | BIBREF11 , BIBREF26  | BIBREF26 | BIBREF26 |
| 219 | `qasper_e` | `token_f1` | 0.170 | 0.125 | -0.045 | Combining  pattern based and Machine translation approaches gave the best overall F0.5 scores. It was 49.11 for FCE data | The combination of both error generation methods gave an absolute improvement of 4.3% in F0.5 on both datasets. | The combination of both methods gives an absolute improvement of 4.3% in F_0.5, without requiring any additional annotat |
| 220 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | None | unanswerable | unanswerable |
| 221 | `qasper_e` | `token_f1` | 0.750 | 0.667 | -0.083 | Individuals with legal training; Yes | Experts with legal training. | seven experts with legal training |
| 222 | `qasper_e` | `token_f1` | 0.600 | 0.651 | +0.051 | Maximum Entropy, Weighted Finite State Transducer (WFST),  support vector machines (SVM), conditional random fields (CRF | Lexicon-based approaches (e.g., Maximum Matching), machine learning-based approaches (e.g., Support Vector Machines, Con | Weighted Finite State Transducer (WFST), Neural Network, Support Vector Machine (SVM), Conditional Random Fields (CRF),  |
| 223 | `qasper_e` | `token_f1` | 0.467 | 0.438 | -0.029 | Stanford NER, spaCy 2.0 , recurrent model with a CRF top layer; Stanford NER, spaCy 2.0, recurrent model with a CRF top  | Stanford NER, spaCy 2.0, and a recurrent model similar to BIBREF13/BIBREF14 using bidirectional LSTM cells for character | Stanford NER, spaCy 2.0, and a recurrent model similar to BIBREF13, BIBREF14 that uses bidirectional LSTM cells for char |
| 224 | `qasper_e` | `token_f1` | 0.235 | 0.235 | +0.000 | WordNet BIBREF0, Freebase BIBREF1, WN18 (a subset of WordNet) BIBREF24 , FB15K (a subset of Freebase) BIBREF2 | WN18 and FB15K | WN18 and FB15K |
| 225 | `qasper_e` | `token_f1` | 0.500 | 0.500 | +0.000 |  LastStateRNN, AvgRNN, AttentionRNN; LastStateRNN, AvgRNN, AttentionRNN  | LastStateRNN | LastStateRNN |
| 226 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | personal attack, racism, and sexism; racism, sexism, personal attack, not specifically about any single topic | Personal attack, racism, and sexism | personal attack, racism, and sexism |
| 227 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Yes; Yes | Yes | yes |
| 228 | `qasper_e` | `token_f1` | 0.706 | 0.933 | +0.227 | BIBREF12 , BIBREF13; an existing, annotated Twitter dataset that was constructed based on a hierarchical model of depres | An existing, annotated Twitter dataset constructed based on a hierarchical model of depression-related symptoms, contain | an existing, annotated Twitter dataset that was constructed based on a hierarchical model of depression-related symptoms |
| 229 | `qasper_e` | `token_f1` | 0.786 | 0.667 | -0.119 | Nguni languages (zul, xho, nbl, ssw), Sotho languages (nso, sot, tsn); The Nguni languages are similar to each other, Th | The Nguni languages (zul, xho, nbl, ssw) and the Sotho languages (nso, sot, tsn) are similar to each other. | The Nguni languages (zul, xho, nbl, ssw) are similar to each other, and the Sotho languages (nso, sot, tsn) are similar  |
| 230 | `qasper_e` | `token_f1` | 0.667 | 1.000 | +0.333 | IMDb dataset of movie reviews; IMDb | IMDb dataset | IMDb dataset of movie reviews |
| 231 | `qasper_e` | `token_f1` | 0.842 | 0.800 | -0.042 | accuracy and F1-score of 89.6% and 89.2%, respectively; accuracy and F1-score of 89.6% and 89.2%, respectively | The system's performance was an accuracy and F1-score of 89.6% and 89.2%, respectively. | Accuracy of 89.6% and F1-score of 89.2% |
| 232 | `qasper_e` | `token_f1` | 0.857 | 0.857 | +0.000 | K-means, LEM BIBREF13, DPEMM BIBREF14; K-means, LEM, DPEMM | K-means, LEM, and DPEMM | K-means, LEM, and DPEMM |
| 233 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | English, German, Spanish, Mandarin, Polish, Russian, Korean and Serbian; English (Edinburgh), German (Berlin), Spanish ( | English, German, Spanish, Mandarin, Polish, Russian, Korean, and Serbian. | English, German, Spanish, Mandarin, Polish, Russian, Korean, and Serbian |
| 234 | `qasper_e` | `token_f1` | 0.385 | 0.800 | +0.415 | rupnik2016news; rupnik2016news, Deutsche Welle's news website | The datasets include a cluster-linking dataset adapted from rupnik2016news, and IDF scores were computed using a larger  | Deutsche Welle's news website (http://www.dw.com/) |
| 235 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Yes; Yes | No. | No. |
| 236 | `qasper_e` | `token_f1` | 0.545 | 0.645 | +0.100 | GloVe, BERT, Universal Sentence Encoder, TF-IDF, InferSent; Avg. GloVe embeddings, Avg. fast-text embeddings, Avg. BERT  | InferSent, Universal Sentence Encoder, average GloVe embeddings, BERT embeddings (averaged and CLS-token), Skip-Thought, | InferSent, Universal Sentence Encoder, average GloVe embeddings, average BERT embeddings, and BERT CLS-token output. |
| 237 | `qasper_e` | `token_f1` | 0.933 | 1.000 | +0.067 | MR, CR, SUBJ, MPQA, SST, TREC, MRPC; MR: Sentiment prediction for movie reviews snippets on a five start scale BIBREF25. | MR, CR, SUBJ, MPQA, SST, TREC, and MRPC. | MR, CR, SUBJ, MPQA, SST, TREC, MRPC |
| 238 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | 33,663; 33,663 distinct review keywords  | unanswerable | unanswerable |
| 239 | `qasper_e` | `token_f1` | 0.312 | 0.333 | +0.021 | using tweets that one has replied or quoted to as contextual information; text sequences of context tweets | Context tweets are proposed as additional features, where the text sequences of context tweets are directly used and con | Context tweets and Latent Topic Clustering (LTC) |
| 240 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | No; No | Yes | Yes |
| 241 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | No; No | unanswerable | unanswerable |
| 242 | `qasper_e` | `token_f1` | 0.242 | 0.167 | -0.076 | For SLC task, the "ltuorp" team  has the best performing  model (0.6323/0.6028/0.6649 for F1/P/R  respectively) and for  | The best-performing model among the authors' submissions is the ensemble+ of (r4, r7, r12) for SLC and ensemble+ of (II  | MIC-CIS ranked 3rd in FLC and 4th in SLC. |
| 243 | `qasper_e` | `token_f1` | 0.250 | 0.800 | +0.550 | DTA18, DTA19; Diachronic Usage Relatedness (DURel) gold standard data set | The corpus used for the task is the diachronic corpus pair DTA18 and DTA19 from the DTA corpus. | DTA18 and DTA19 |
| 244 | `qasper_e` | `token_f1` | 0.900 | 1.000 | +0.100 | 13,757; 10,898 articles, 17,794 tweets, and 13,757 crowdsourced question-answer pairs | The dataset includes 10,898 articles, 17,794 tweets, and 13,757 crowdsourced question-answer pairs. | 10,898 articles, 17,794 tweets, and 13,757 crowdsourced question-answer pairs |
| 245 | `qasper_e` | `token_f1` | 0.966 | 0.966 | +0.000 | KNN
RF
SVM
MLP;  K Nearest Neighbors (KNN), Random Forest (RF), Support Vector Machine (SVM), Multi-layer Perceptron (ML | K Nearest Neighbors (KNN), Random Forest (RF), Support Vector Machine (SVM), and Multi-layer Perceptron (MLP) | K Nearest Neighbors (KNN), Random Forest (RF), Support Vector Machine (SVM), and Multi-layer Perceptron (MLP) |
| 246 | `qasper_e` | `token_f1` | 0.533 | 0.538 | +0.004 | They use two independent convolutional and max-pooling layers on (1) a combination of the left context, the left entity  | They obtain the new context representation by splitting the contexts into three disjoint regions (left, middle, and righ | They obtain the new context representation by splitting the contexts into three disjoint regions (left, middle, right) b |
| 247 | `qasper_e` | `token_f1` | 0.217 | 0.207 | -0.010 | An output layer for each task; Multi-tasking is addressed by neural sequence tagger based on LSTM-CRF and linguistic fea | Multi-granularity architecture jointly performs sentence-level and fragment-level classification with weighted loss, whi | Multi-granularity design jointly performs FLC and SLC with FastTextWordEmb and BERTSentEmb, adding binary sentence class |
| 248 | `qasper_e` | `token_f1` | 0.780 | 0.842 | +0.062 | which contains over 45,000 scholarly articles, including over 33,000 with full text, about COVID-19, SARS-CoV-2, and rel | The CORD-19 dataset is the COVID-19 Open Research Dataset, containing over 45,000 scholarly articles, including over 33, | the COVID-19 Open Research Dataset, containing over 45,000 scholarly articles, including over 33,000 with full text, abo |
| 249 | `qasper_e` | `token_f1` | 0.267 | 0.000 | -0.267 | 26972; 26972 sentences | The real-life dataset consists of supervisor assessment text from 4528 employees, containing 26972 sentences. | 4528 employees |
| 250 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Unanswerable; Unanswerable | The state of the art methods are neural network-based approaches to grammar induction, including models that learn tree  | neural network-based approaches to grammar induction BIBREF14 , BIBREF15 , BIBREF16 , BIBREF17 |
| 251 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | grandfather | Great-grandfather | Great-grandfather |
| 252 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | duck | duck | duck |
| 253 | `hotpotqa_e` | `token_f1` | 0.000 | 1.000 | +1.000 | Cleveland, Ohio | Washington, D.C. | Cleveland, Ohio |
| 254 | `hotpotqa_e` | `token_f1` | 1.000 | 0.000 | -1.000 | Honeysuckle | Honeysuckle | Quesnelia |
| 255 | `hotpotqa_e` | `token_f1` | 0.000 | 1.000 | +1.000 | Castle of Frankenstein | Right On! | Castle of Frankenstein |
| 256 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Sam Taylor | Sam Taylor | Sam Taylor |
| 257 | `hotpotqa_e` | `token_f1` | 0.500 | 0.500 | +0.000 | City of Newcastle | Newcastle | Newcastle |
| 258 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Deutzia | Deutzia | Deutzia |
| 259 | `hotpotqa_e` | `token_f1` | 0.400 | 0.400 | +0.000 | former tennis player | tennis players | tennis players |
| 260 | `hotpotqa_e` | `token_f1` | 0.750 | 0.750 | +0.000 | American reality television series | American reality television shows | American reality television shows |
| 261 | `hotpotqa_e` | `token_f1` | 0.000 | 1.000 | +1.000 | yes | No | Yes |
| 262 | `hotpotqa_e` | `token_f1` | 0.667 | 0.667 | +0.000 | in 2000 | 2000 | 2000 |
| 263 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Middle Palaeolithic period | Middle Palaeolithic period | Middle Palaeolithic period |
| 264 | `hotpotqa_e` | `token_f1` | 0.667 | 0.667 | +0.000 | XXIV Summer Universiade | 2007 Summer Universiade | 2007 Summer Universiade |
| 265 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | yes | Yes | Yes |
| 266 | `hotpotqa_e` | `token_f1` | 0.400 | 0.400 | +0.000 | Echeveria | Both Alopecurus and Echeveria | Both Alopecurus and Echeveria |
| 267 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | yes | Yes | Yes |
| 268 | `hotpotqa_e` | `token_f1` | 0.632 | 0.632 | +0.000 | poi, Kalua pig, poke, lomi salmon, opihi, haupia | poi, kālua puaʻa (kālua pig), poke, lomi salmon, ʻopihi, and haupia | poi, kālua puaʻa (kālua pig), poke, lomi salmon, ʻopihi, and haupia |
| 269 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | 12+3/4 mi northeast of Liverpool | 11½ miles (19 km) | 11½ miles (19 km) |
| 270 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Ferdi Taygan | Ferdi Taygan | Ferdi Taygan |
| 271 | `hotpotqa_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Costa | Albert Costa | Albert Costa |
| 272 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | no | No | No |
| 273 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | heavy metal band | bands | bands |
| 274 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Dennis Potter. | Dennis Potter | Dennis Potter |
| 275 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | no | No | No |
| 276 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | professional tennis player. | Professional tennis player | professional tennis player |
| 277 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | tennis | Tennis | Tennis |
| 278 | `hotpotqa_e` | `token_f1` | 0.400 | 1.000 | +0.600 | Ericsson Stadium | Mount Smart Stadium | Ericsson Stadium |
| 279 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | 8,648 | 8,648 | 8,648 |
| 280 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Les Temps modernes | Les Temps Modernes | Les Temps Modernes |
| 281 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Aksel Sandemose | Aksel Sandemose | Aksel Sandemose |
| 282 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Luger P08 | Luger P08 | Luger P08 |
| 283 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Dulwich | Dulwich | Dulwich |
| 284 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Jean Acker | Jean Acker | Jean Acker |
| 285 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | 1990 | 1990 | 1990 |
| 286 | `hotpotqa_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Hills | Adelaide Hills | Adelaide Hills |
| 287 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | tennis | Tennis | Tennis |
| 288 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Kurt Gerron | Kurt Gerron | Kurt Gerron |
| 289 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | yes | Yes | Yes |
| 290 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Marlborough | Marlborough | Marlborough |
| 291 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | The Ten-Year Lunch | The Ten-Year Lunch | The Ten-Year Lunch |
| 292 | `hotpotqa_e` | `token_f1` | 0.667 | 0.667 | +0.000 | director | film director | film director |
| 293 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | 179 women | 459 | 459 |
| 294 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | yes | Yes | Yes |
| 295 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | yes | Yes | Yes |
| 296 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | B. Reeves Eason | B. Reeves Eason | B. Reeves Eason |
| 297 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Polypodium | Polypodium | Polypodium |
| 298 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Albert | Albert | Albert |
| 299 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Leslie Goodwins | Leslie Goodwins | Leslie Goodwins |
| 300 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | A1 Recordings | Epic Records | Epic Records |

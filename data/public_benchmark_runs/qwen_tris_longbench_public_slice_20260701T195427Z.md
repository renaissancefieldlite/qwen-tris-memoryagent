# Qwen Tris LongBench Public Slice - qwen_tris_longbench_public_slice_20260701T195427Z

- Benchmark: `LongBench public data.zip`
- Provider: `qwen-cloud`
- Model: `qwen-plus`
- Items: `299`
- Skipped provider-blocked rows: `1`
- Condition A mean: `0.574`
- Condition B mean: `0.666`
- Delta: `+0.092`

## Boundary

Public LongBench smoke slice. This is not a full LongBench leaderboard claim; it is a source-backed answer-key accuracy receipt that can scale to larger slices.

## Conditions

- Condition A: baseline Qwen prompt-only answer discipline
- Condition B: Qwen Tris stable-state answer discipline

## Family Totals

- `passage_retrieval_en_e`: n=49 A=1.000 B=1.000 delta=+0.000
- `passage_count_e`: n=50 A=0.341 B=0.344 delta=+0.004
- `trec_e`: n=50 A=0.280 B=0.740 delta=+0.460
- `multifieldqa_en_e`: n=50 A=0.615 B=0.624 delta=+0.009
- `qasper_e`: n=50 A=0.508 B=0.569 delta=+0.062
- `hotpotqa_e`: n=50 A=0.707 B=0.726 delta=+0.018

## Skipped Provider-Blocked Rows

- row 32 `passage_retrieval_en_e` condition `baseline` _id `a1d308c5c355e0fdb4ba546280e459a5a50b696a3a6eb10b`: provider returned data_inspection_failed

## Rows

| # | Dataset | Metric | A | B | Delta | Gold | A prediction | B prediction |
|---:|---|---|---:|---:|---:|---|---|---|
| 1 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 6 | Paragraph 6 | Paragraph 6 |
| 2 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 1 | Paragraph 1 | Paragraph 1 |
| 3 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 3 | Paragraph 3 | Paragraph 3 |
| 4 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 1 | Paragraph 1 | Paragraph 1 |
| 5 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 5 | Paragraph 5 | Paragraph 5 |
| 6 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 12 | Paragraph 12 | Paragraph 12 |
| 7 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 7 | Paragraph 7 | Paragraph 7 |
| 8 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 1 | Paragraph 1 | Paragraph 1 |
| 9 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 2 | Paragraph 2 | Paragraph 2 |
| 10 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 6 | Paragraph 6 | Paragraph 6 |
| 11 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 11 | Paragraph 11 | Paragraph 11 |
| 12 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 4 | Paragraph 4 | Paragraph 4 |
| 13 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 9 | Paragraph 9 | Paragraph 9 |
| 14 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 8 | Paragraph 8 | Paragraph 8 |
| 15 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 2 | Paragraph 2 | Paragraph 2 |
| 16 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 4 | Paragraph 4 | Paragraph 4 |
| 17 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 3 | Paragraph 3 | Paragraph 3 |
| 18 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 9 | Paragraph 9 | Paragraph 9 |
| 19 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 4 | Paragraph 4 | Paragraph 4 |
| 20 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 1 | Paragraph 1 | Paragraph 1 |
| 21 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 2 | Paragraph 2 | Paragraph 2 |
| 22 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 6 | Paragraph 6 | Paragraph 6 |
| 23 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 3 | Paragraph 3 | Paragraph 3 |
| 24 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 1 | Paragraph 1 | Paragraph 1 |
| 25 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 7 | Paragraph 7 | Paragraph 7 |
| 26 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 10 | Paragraph 10 | Paragraph 10 |
| 27 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 2 | Paragraph 2 | Paragraph 2 |
| 28 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 5 | Paragraph 5 | Paragraph 5 |
| 29 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 10 | Paragraph 10 | Paragraph 10 |
| 30 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 4 | Paragraph 4 | Paragraph 4 |
| 31 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 10 | Paragraph 10 | Paragraph 10 |
| 33 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 7 | Paragraph 7 | Paragraph 7 |
| 34 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 9 | Paragraph 9 | Paragraph 9 |
| 35 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 3 | Paragraph 3 | Paragraph 3 |
| 36 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 8 | Paragraph 8 | Paragraph 8 |
| 37 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 10 | Paragraph 10 | Paragraph 10 |
| 38 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 9 | Paragraph 9 | Paragraph 9 |
| 39 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 10 | Paragraph 10 | Paragraph 10 |
| 40 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 11 | Paragraph 11 | Paragraph 11 |
| 41 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 8 | Paragraph 8 | Paragraph 8 |
| 42 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 6 | Paragraph 6 | Paragraph 6 |
| 43 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 3 | Paragraph 3 | Paragraph 3 |
| 44 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 5 | Paragraph 5 | Paragraph 5 |
| 45 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 12 | Paragraph 12 | Paragraph 12 |
| 46 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 11 | Paragraph 11 | Paragraph 11 |
| 47 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 2 | Paragraph 2 | Paragraph 2 |
| 48 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 6 | Paragraph 6 | Paragraph 6 |
| 49 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 2 | Paragraph 2 | Paragraph 2 |
| 50 | `passage_retrieval_en_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | Paragraph 5 | Paragraph 5 | Paragraph 5 |
| 51 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 6 | 5 | 5 |
| 52 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 10 | 7 | 7 |
| 53 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 4 | 3 | 3 |
| 54 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 6 | 5 | 5 |
| 55 | `passage_count_e` | `official_numeric_fraction` | 0.029 | 0.030 | +0.001 | 12 | Let's carefully analyze the 18 paragraphs and identify duplicates.  We'll group identical paragraphs by content. Since e | Let's carefully analyze the 18 paragraphs and identify duplicates.  We'll group identical paragraphs by content. Note: W |
| 56 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 8 | 4 | 4 |
| 57 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 9 | 7 | 7 |
| 58 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 7 | 7 | 7 |
| 59 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 60 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.045 | +0.045 | 9 | 5 | We are given 11 paragraphs and asked to count how many **unique** (non-duplicate) paragraphs there are.  Let’s compare t |
| 61 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 7 | 7 | 7 |
| 62 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.045 | +0.045 | 7 | 5 | We are given 12 paragraphs and asked to count how many **unique** (non-duplicate) paragraphs there are.  Let’s compare t |
| 63 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 0.043 | -0.957 | 6 | 6 | We are given 13 paragraphs and asked to count how many **unique** (non-duplicate) paragraphs there are.  Let’s group ide |
| 64 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 65 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 6 | 6 | 6 |
| 66 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 2 | 3 | 3 |
| 67 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 4 | 3 | 3 |
| 68 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 69 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 8 | 6 | 6 |
| 70 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 4 | 4 | 4 |
| 71 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 9 | 8 | 8 |
| 72 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 73 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 7 | 5 | 5 |
| 74 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 10 | 7 | 6 |
| 75 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 3 | 4 | 4 |
| 76 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 5 | 5 | 5 |
| 77 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 13 | 7 | 7 |
| 78 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 79 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 80 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 8 | 5 | 5 |
| 81 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 5 | 5 | 5 |
| 82 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 4 | 3 | 3 |
| 83 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 84 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 10 | 4 | 4 |
| 85 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 16 | 9 | 9 |
| 86 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 5 | 5 | 5 |
| 87 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 5 | 4 | 4 |
| 88 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 1.000 | +1.000 | 5 | 6 | 5 |
| 89 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 9 | 4 | 4 |
| 90 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 9 | 7 | 7 |
| 91 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 11 | 7 | 7 |
| 92 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 11 | 8 | 8 |
| 93 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 8 | 5 | 5 |
| 94 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 95 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 8 | 6 | 6 |
| 96 | `passage_count_e` | `official_numeric_fraction` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 97 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 9 | 4 | 4 |
| 98 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 9 | 5 | 6 |
| 99 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.045 | +0.045 | 17 | 10 | Let's carefully compare all 17 paragraphs to identify duplicates.  We'll go one by one and group identical paragraphs.   |
| 100 | `passage_count_e` | `official_numeric_fraction` | 0.000 | 0.000 | +0.000 | 7 | 5 | 5 |
| 101 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Definition of something | Type: Definition of something | Definition of something |
| 102 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Date | Type: Date | Date |
| 103 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Number of something | Type: Number of something | Number of something |
| 104 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Animal | Type: Definition of something | Definition of something |
| 105 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | City | Type: City | City |
| 106 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Individual | Type: Individual | Individual |
| 107 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Equivalent term | Type: Equivalent term | Definition of something |
| 108 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Element and substance | Type: Other entity | Other entity |
| 109 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Description of something | Type: Description of something | Description of something |
| 110 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 111 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Date | Date | Date |
| 112 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Definition of something | Type: Definition of something | Definition of something |
| 113 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Other location | Type: Other location | Other location |
| 114 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Expression abbreviated | Expression abbreviated | Expression abbreviated |
| 115 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Date | Type: Date | Date |
| 116 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Other location | Type: Other location | Other location |
| 117 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Definition of something | Type: Definition of something | Definition of something |
| 118 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Date | Date | Date |
| 119 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Country | Country | Country |
| 120 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Manner of an action | Type: Other entity | Other entity |
| 121 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Other entity | Type: Invention, book and other creative piece | Invention, book and other creative piece |
| 122 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Individual | Individual | Individual |
| 123 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Element and substance | Type: Color | Color |
| 124 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Other location | Type: Animal | Other entity |
| 125 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 126 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 127 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | City | Type: City | City |
| 128 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Group or organization of person | Type: Invention, book and other creative piece | Invention, book and other creative piece |
| 129 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 130 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Lasting time of somethin | Type: Number of something | Number of something |
| 131 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Currency name | Type: Product | Product |
| 132 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Date | Date | Date |
| 133 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Lasting time of somethin | Type: Number of something | Number of something |
| 134 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Vehicle | Type: Other entity | Other entity |
| 135 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Definition of something | Type: Definition of something | Definition of something |
| 136 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Other location | Type: Other location | Other location |
| 137 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Color | Type: Color | Color |
| 138 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 139 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Distance, linear measure | Number of something | Number of something |
| 140 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Percent, fraction | Type: Percent, fraction | Percent, fraction |
| 141 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 142 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Definition of something | Type: Definition of something | Definition of something |
| 143 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Date | Type: Date | Date |
| 144 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Other location | Type: Other location | Other location |
| 145 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 146 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 147 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Speed | Type: Number of something | Speed |
| 148 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Element and substance | Type: Element and substance | Element and substance |
| 149 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Other location | Type: Other location | Other location |
| 150 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Element and substance | Type: Element and substance | Element and substance |
| 151 | `multifieldqa_en_e` | `token_f1` | 0.600 | 0.700 | +0.100 | Exposure to sunlight or strong light may cause permanent yellow spot damage on the screen. | Permanent yellow spot damage on the screen. | Exposure to direct sunlight or other strong light sources may cause permanent yellow spot damage on the screen, and such |
| 152 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Vice Admiral. | Vice Admiral | Vice Admiral |
| 153 | `multifieldqa_en_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Sir Richard. | None of the text mentions Ralph Rokebye having a brother. | No brother is mentioned for Ralph Rokebye in the text. |
| 154 | `multifieldqa_en_e` | `token_f1` | 0.750 | 0.750 | +0.000 | South West Ultras fan club. | South West Ultras | South West Ultras |
| 155 | `multifieldqa_en_e` | `token_f1` | 0.222 | 0.222 | +0.000 | It is recommended to have at least a 2x2 meter space for using the VR headset. | At least 2×2 meters | at least 2×2 meters |
| 156 | `multifieldqa_en_e` | `token_f1` | 0.182 | 0.167 | -0.015 | It depends on the value of x, either 0 or (6x^2cos(x^2)+sin(x^2))/(3(x^2)^(1/3)). | $$ f'\left(x\right)  =  \begin{cases}  \frac{6x^2\cos{\left(x^2\right)}+\sin{\left(x^2\right)}}{3\sqrt[3]{x^2}}, & \mbox | \begin{equation*} f'\left(x\right)  =  \begin{cases}  \frac{6x^2\cos{\left(x^2\right)}+\sin{\left(x^2\right)}}{3\sqrt[3] |
| 157 | `multifieldqa_en_e` | `token_f1` | 0.737 | 0.737 | +0.000 | In 2009, Brooksley Born received the John F. Kennedy Profiles in Courage Award. | John F. Kennedy Profiles in Courage Award | John F. Kennedy Profiles in Courage Award |
| 158 | `multifieldqa_en_e` | `token_f1` | 0.182 | 0.364 | +0.182 | Margaret Way started self-publishing her books as e-books in 2013. | 2013 | Beginning in 2013, Margaret began to self-publish, releasing her first "e-book" mid-July. |
| 159 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Long Term Capital Management (LTCM). | Long Term Capital Management (LTCM) | Long Term Capital Management (LTCM) |
| 160 | `multifieldqa_en_e` | `token_f1` | 0.000 | 0.286 | +0.286 | It is well described by the Gaussian theory. | $m \sim t^{1/2}$ | The dynamical behaviour of the anisotropic order parameter $m$ following a quench to the critical point is well describe |
| 161 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | June 1, 1999. | June 1, 1999 | June 1, 1999 |
| 162 | `multifieldqa_en_e` | `token_f1` | 0.800 | 1.000 | +0.200 | 23 September. | 23 September 2017 | 23 September |
| 163 | `multifieldqa_en_e` | `token_f1` | 0.273 | 0.240 | -0.033 | The maximum velocity scales with the square root of the amplitude. | The maximum velocity has a linear relationship with amplitude for small amplitudes in compressible flows, transitioning  | The maximum velocity has a linear dependence on amplitude for compressible flows at small amplitudes ($\|\triangle n/n_0\| |
| 164 | `multifieldqa_en_e` | `token_f1` | 1.000 | 0.857 | -0.143 | The normalized least mean square (NLMS) algorithm. | Normalized least mean square (NLMS) algorithm | The normalized least mean square (NLMS) algorithm is engaged. |
| 165 | `multifieldqa_en_e` | `token_f1` | 0.478 | 0.274 | -0.205 | The momentum space curl of the interlayer Berry connection polarizability generates the crossed nonlinear dynamical Hall | The interlayer Berry connection polarizability (BCP) is the band geometric quantity whose momentum-space curl is the ori | The interlayer Berry connection polarizability (BCP) is significant because its momentum space curl constitutes the band |
| 166 | `multifieldqa_en_e` | `token_f1` | 0.250 | 0.250 | +0.000 | The first white settlement in McPherson County was Fuller's Ranch, established by Charles O. Fuller. | Fuller's Ranch | Fuller's Ranch |
| 167 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | McPherson. | McPherson | McPherson |
| 168 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | McPherson County is located in the U.S. state of Kansas. | McPherson County is located in the U.S. state of Kansas. | McPherson County is located in the U.S. state of Kansas. |
| 169 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Jacob C. Landau. | Jacob C. Landau | Jacob C. Landau |
| 170 | `multifieldqa_en_e` | `token_f1` | 1.000 | 0.667 | -0.333 | BERT, RoBERTa, ELECTRA, GPT-2, and XLM-RoBERTa. | BERT, RoBERTa, ELECTRA, GPT-2, and XLM-RoBERTa. | BERT, RoBERTa, ELECTRA, GPT-2, XLM-RoBERTa, Spanish BERT, Portuguese BERT |
| 171 | `multifieldqa_en_e` | `token_f1` | 0.737 | 0.917 | +0.180 | The club's headquarters are located on Jivani Street 2 of the Malatia-Sebastia District, Yerevan. | Jivani Street 2 of the Malatia-Sebastia District, Yerevan | The club headquarters are located on Jivani Street 2 of the Malatia-Sebastia District, Yerevan. |
| 172 | `multifieldqa_en_e` | `token_f1` | 0.471 | 0.500 | +0.029 | Margaret Way was born in Brisbane and died in Cleveland, Queensland, Australia. | Brisbane, Queensland, Australia; Cleveland, Queensland | Brisbane and Cleveland, Queensland |
| 173 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | FC Banants. | FC Banants | FC Banants |
| 174 | `multifieldqa_en_e` | `token_f1` | 0.000 | 0.000 | +0.000 | In the 2013-2014 season. | 2013–14 | 2013–14 |
| 175 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | 30,223. | 30,223 | 30,223 |
| 176 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Four. | Four | Four |
| 177 | `multifieldqa_en_e` | `token_f1` | 0.444 | 0.444 | +0.000 | Goodwin became a Naval aviator in January 1929. | January 1929 | January 1929 |
| 178 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | 85.61%. | 85.61% | 85.61% |
| 179 | `multifieldqa_en_e` | `token_f1` | 0.973 | 1.000 | +0.027 | Sustained viral gene delivery through core-shell fibers and Gene transfer to hemophilia A mice via oral delivery of FVII | Sustained viral gene delivery through core-shell fibers   Gene transfer to hemophilia A mice via oral delivery of FVIII- | Sustained viral gene delivery through core-shell fibers and Gene transfer to hemophilia A mice via oral delivery of FVII |
| 180 | `multifieldqa_en_e` | `token_f1` | 0.000 | 0.000 | +0.000 | They won their first game with a score of 15-3. | 1–0 | 15–3 |
| 181 | `multifieldqa_en_e` | `token_f1` | 1.000 | 0.800 | -0.200 | October 2001. | October 2001 | In October 2001 |
| 182 | `multifieldqa_en_e` | `token_f1` | 1.000 | 0.706 | -0.294 | The normalized least mean square (NLMS) algorithm. | Normalized least mean square (NLMS) algorithm | The normalized least mean square (NLMS) algorithm is engaged in the PLMS-PPIC method. |
| 183 | `multifieldqa_en_e` | `token_f1` | 0.625 | 0.625 | +0.000 | O(t, L_{\parallel}; S_\Delta) = L_{\parallel}^{-\beta/[\nu(1+\Delta)]} \tilde f_O(t/L_{\parallel}^{z/(1+\Delta)}; S_\Del | $O (t, L_{\parallel} ; S_\Delta) = L_{\parallel}^{-\beta/[\nu(1+\Delta)]} \tilde f_O (t/L_{\parallel}^{z/(1+\Delta)} ; S | $O (t, L_{\parallel} ; S_\Delta) = L_{\parallel}^{-\beta/[\nu(1+\Delta)]} \tilde f_O (t/L_{\parallel}^{z/(1+\Delta)} ; S |
| 184 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | VC-10 Squadron. | VC-10 Squadron | VC-10 Squadron |
| 185 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Del Bigtree and his team at ICAN. | Del Bigtree and his team at ICAN | Del Bigtree and his team at ICAN |
| 186 | `multifieldqa_en_e` | `token_f1` | 0.261 | 0.138 | -0.123 | The conclusion was that fruit consumption may provide a protective effect for mercury exposure in Amazonian riparians. | The conclusion of the study was that frequent consumption of high mercury seafood (tuna steak, marlin, swordfish, or sha | Fatigue may be associated with eating high mercury fish, but the sample size is small. |
| 187 | `multifieldqa_en_e` | `token_f1` | 0.000 | 0.000 | +0.000 | 使用安装包安装Ganache；打开程序，用户可以从显示的界面中查看账户、区块、交易和日志；点击“设置”，用户可以设置绑定的ip和端口、账户数量以及gas限制等，点击“restart”后设置生效。此时，Ganache已经在本机运行了一个以太坊 | 使用安装包安装Ganache，然后打开程序即可启动。 | 1. 使用安装包安装即可。   2. 打开程序后，会显示界面，用户可以查看账户（默认创建10个账户）、区块、交易和日志。   3. 点击“设置”，设置绑定的ip和端口（设为8545即可）、账户数量以及gas限制等，点击“restart”后设 |
| 188 | `multifieldqa_en_e` | `token_f1` | 0.714 | 0.714 | +0.000 | After attacking Jacobo at a workers' strike, Ngotho loses his job and Njoroge's family is forced to move. | Ngotho loses his job and Njoroge’s family is forced to move. | Ngotho loses his job and Njoroge’s family is forced to move. |
| 189 | `multifieldqa_en_e` | `token_f1` | 0.462 | 0.462 | +0.000 | KSTP switched to a sports radio format on February 15, 2010. | February 15, 2010 | February 15, 2010 |
| 190 | `multifieldqa_en_e` | `token_f1` | 0.308 | 0.308 | +0.000 | The best performing model for the Spanish language in Track-1 was Spanish BERT. | Spanish BERT | Spanish BERT |
| 191 | `multifieldqa_en_e` | `token_f1` | 0.722 | 0.550 | -0.172 | Infall rate is 2-5 times smaller and gas density is 2-5 times smaller. | The infall rate is 2-5 times smaller, and the gas density is 2-5 times smaller in the region close to the black hole com | Compared to non-magnetized accretion, infall rate is 2–5 times smaller depending on outer magnetization, and gas density |
| 192 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Lasa, Gitastrophe, and Shadoks. | Lasa, Gitastrophe, and Shadoks | Lasa, Gitastrophe, and Shadoks |
| 193 | `multifieldqa_en_e` | `token_f1` | 0.600 | 0.727 | +0.127 | Margaret Way wrote more than 120 novels. | More than 120 | more than 120 novels |
| 194 | `multifieldqa_en_e` | `token_f1` | 0.227 | 0.123 | -0.104 | By using a propagator in the latent space. | The framework captures the reduced-order dynamics using a propagator in a complex-valued latent space, where each latent | The framework captures the reduced-order dynamics by employing a propagator in the latent space—a continuous ODE in the  |
| 195 | `multifieldqa_en_e` | `token_f1` | 0.429 | 0.529 | +0.101 | Online documentation, QuecPython community, online support: QQ group 445121768. | Users can go to the QuecPython官网文档中心, QuecPython 社区, official QQ group (445121768), or contact online support for troubl | Users can refer to the official website online documentation, visit the QuecPython Community for searching, exchanging,  |
| 196 | `multifieldqa_en_e` | `token_f1` | 0.000 | 0.632 | +0.632 | McPherson County was established as a county in 1867. | 1870 | McPherson County was regularly organized as a county in the spring of 1870. |
| 197 | `multifieldqa_en_e` | `token_f1` | 0.247 | 0.327 | +0.081 | This research paper proposed an approach based on approximating the posterior distribution with an isotropic Gaussian di | The proposed approach is to approximate the posterior distribution $ p({\bf w}_k\|y_{1:k}) $ in a linear-Gaussian state-s | The proposed approach is approximating the posterior distribution $p({\bf w}_k\|y_{1:k})$ with an isotropic Gaussian dist |
| 198 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Four years. | Four years | Four years |
| 199 | `multifieldqa_en_e` | `token_f1` | 0.167 | 0.167 | +0.000 | Yes, DUO has 9.57 instances per image while COCO contains 7.7. | Yes | Yes |
| 200 | `multifieldqa_en_e` | `token_f1` | 0.889 | 1.000 | +0.111 | The Tevatron Collider Run II started in March 2002 and is expected to continue until the end of this decade. | The Tevatron Collider Run II started in March 2002 and is expected to end at the end of this decade. | The Tevatron Collider Run II started in March 2002 and is expected to continue until the end of this decade. |
| 201 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li |
| 202 | `qasper_e` | `token_f1` | 0.600 | 0.800 | +0.200 | the series of posts that trigger an intervention | The latent context used to predict instructor intervention is the series of posts that trigger an intervention. | latent context is the series of posts that trigger an intervention |
| 203 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | F-score, Kappa; Unanswerable | F-score and Kappa statistics | F-score and Kappa statistics |
| 204 | `qasper_e` | `token_f1` | 0.200 | 0.214 | +0.014 | (i) models that use plain stacked LSTMs, (ii) models with different INLINEFORM0, (iii) models without INLINEFORM1, (iv)  | The baselines were plain stacked LSTMs. | plain stacked LSTMs |
| 205 | `qasper_e` | `token_f1` | 0.000 | 1.000 | +1.000 | Yes; Unanswerable | No | unanswerable |
| 206 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | No | No | No |
| 207 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Yes; No | No | No |
| 208 | `qasper_e` | `token_f1` | 0.533 | 0.480 | -0.053 | SemEval-2016 Challenge Task 5 BIBREF27 , BIBREF28;  English reviews ,  restaurant reviews from four different languages  | Four datasets were used in evaluation: Spanish, Turkish, Dutch, and Russian restaurant reviews from SemEval-2016 Challen | SemEval-2016 Challenge Task 5 restaurant reviews datasets in Spanish, Turkish, Dutch, and Russian. |
| 209 | `qasper_e` | `token_f1` | 0.414 | 0.414 | +0.000 | 7.36% on accuracy and 9.69% on F1 score; it has 0.024 improvement in accuracy comparing to ELMO Only and  0.006 improvem | The article reports that adding topic information (Topic Only setting) to the base model improved accuracy by 7.36% and  | The article reports that adding topic information (Topic Only setting) to the base model improved accuracy by 7.36% and  |
| 210 | `qasper_e` | `token_f1` | 0.160 | 0.222 | +0.062 | They use text transcription.; both | They use both: they use the released transcripts of the IEMOCAP dataset and also process the audio data using an ASR sys | They use both: released transcripts of the IEMOCAP dataset and ASR-processed transcripts derived from the audio. |
| 211 | `qasper_e` | `token_f1` | 0.857 | 0.857 | +0.000 | CLUTO, Carrot2 Lingo; simple clustering algorithm which uses the cosine similarity between word embeddings | CLUTO and Carrot2 Lingo | CLUTO and Carrot2 Lingo |
| 212 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Bert + Unanswerable; CNN, BERT | BERT | BERT |
| 213 | `qasper_e` | `token_f1` | 0.200 | 0.333 | +0.133 | pivoting, pivoting$_{\rm m}$; firstly translates a source language into the pivot language which is later translated to  | Pivot-based baselines are the pivoting and pivot-synthetic methods. | pivoting and pivot-synthetic |
| 214 | `qasper_e` | `token_f1` | 0.364 | 0.444 | +0.081 | Friends, EmotionPush; EmotionLines BIBREF6 | EmotionLines dataset, which consists of the Friends and EmotionPush subsets. | EmotionLines (Friends and EmotionPush), Twitter emotion dataset |
| 215 | `qasper_e` | `token_f1` | 0.135 | 0.135 | +0.000 | three experimental setups with different numbers of speakers in the evaluation set, three experimental setups with diffe | Several evaluation protocols for each part of the database, allowing researchers to investigate performance in various s | Several evaluation protocols for each part of the database, allowing researchers to investigate performance in various s |
| 216 | `qasper_e` | `token_f1` | 0.286 | 0.260 | -0.026 | pays attentions to adjacent characters and casts a localness relationship between the characters as a fixed Gaussian wei | Gaussian-masked directional multi-head attention works by combining a Gaussian weight matrix, which encodes localness ba | Gaussian-masked directional multi-head attention combines a Gaussian weight matrix $G$, which encodes localness relation |
| 217 | `qasper_e` | `token_f1` | 0.077 | 0.200 | +0.123 | No data. Pretrained model is used. | Monolingual data (e.g., Wikipedias) and, for some experiments, parallel corpora (e.g., United Nations Parallel Corpus, I | monolingual data (e.g., Wikipedias) |
| 218 | `qasper_e` | `token_f1` | 0.118 | 0.154 | +0.036 | For certain POS tags, e.g. VERB, PRON.; most word alignments only involve one or a few words, attention can be distribut | Attention is different from alignment in cases involving verbs, where attention captures context words influencing trans | Attention is different from alignment in cases where it captures information beyond translational equivalence, such as f |
| 219 | `qasper_e` | `token_f1` | 1.000 | 0.211 | -0.789 | RNN;  Recurrent Neural Network (RNN) | Recurrent Neural Network (RNN) | RNN with two 2D-convolutional layers, seven bi-directional recurrent layers, and a fully-connected layer with softmax ac |
| 220 | `qasper_e` | `token_f1` | 0.500 | 0.500 | +0.000 | CNN modelBIBREF0, Stanford CRF modelBIBREF21; Bam et al. SVM, Ma and Hovy w/glove, Lample et al. w/fastText, Lample et a | Stanford CRF model | Stanford CRF model |
| 221 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Unanswerable | unanswerable | unanswerable |
| 222 | `qasper_e` | `token_f1` | 0.200 | 0.200 | +0.000 | about 500; Unanswerable | Around 500 different workers were involved in the annotation. | Around 500 different workers were involved in the annotation. |
| 223 | `qasper_e` | `token_f1` | 0.952 | 0.909 | -0.043 | linear SVM, bidirectional Long Short-Term-Memory (BiLSTM), Convolutional Neural Network (CNN); linear SVM, bidirectional | Linear SVM, bidirectional Long Short-Term-Memory (BiLSTM), and Convolutional Neural Network (CNN) | linear SVM, bidirectional Long Short-Term-Memory (BiLSTM) model, Convolutional Neural Network (CNN) model |
| 224 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | BiLSTM, BiLSTM-CNN, BiLSTM-CRF, BiLSTM-CNN-CRF; BiLSTMBIBREF14, BiLSTM+CNNBIBREF20, BiLSTM+CRFBIBREF1, BiLSTM+CNN+CRFBIB | BiLSTM, BiLSTM+CNN, BiLSTM+CRF, BiLSTM+CNN+CRF, CNN, and Stanford CRF | BiLSTM, BiLSTM+CNN, BiLSTM+CRF, BiLSTM+CNN+CRF, CNN, and Stanford CRF |
| 225 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Zero Resource Toolkit (ZRTools) BIBREF7 | Through unsupervised term discovery (UTD) and acoustic unit discovery (AUD), which operate directly on raw speech withou | Through unsupervised term discovery (UTD) for word-like units and acoustic unit discovery (AUD) for phoneme-like units. |
| 226 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | BERTbase; BERTbase | BERTbase model | BERTbase model |
| 227 | `qasper_e` | `token_f1` | 0.038 | 0.069 | +0.031 | Answer with content missing: (LVL1, LVL2, LVL3) 
- Stanford CoreNLP
- Optical Character Recognition (OCR) system, ParsCI | TopicRank, WINGNUS, KP-Miner, TF-IDF, and another unspecified model (the article states five models were re-implemented, | five keyphrase extraction models: two commonly used baselines, a resource-lean unsupervised graph-based ranking approach |
| 228 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Yes; Yes | Yes | yes |
| 229 | `qasper_e` | `token_f1` | 0.667 | 1.000 | +0.333 | MIMIC-III; MIMIC-III | MIMIC-III dataset | MIMIC-III |
| 230 | `qasper_e` | `token_f1` | 0.138 | 0.308 | +0.170 | Level A: 14100 Tweets
Level B: 4640 Tweets
Level C: 4089 Tweets | The dataset contains 14,100 tweets total, but the article does not specify the length of the dataset for each step of th | 14,100 tweets |
| 231 | `qasper_e` | `token_f1` | 0.108 | 0.000 | -0.108 | it captures other information rather than only the translational equivalent in the case of verbs; Alignment points of th | Attention captures context words influencing the current word translation, such as adjectives and determiners for nouns, | context words influencing the current word translation |
| 232 | `qasper_e` | `token_f1` | 0.766 | 0.829 | +0.063 | BOW-LR, BOW-RF. TFIDF-RF, TextCNN, C-TextCNN; bag-of-words (BOW), term frequency–inverse document frequency (TFIDF), neu | The baselines were bag-of-words (BOW), term frequency–inverse document frequency (TFIDF), and neural-based word embeddin | bag-of-words (BOW), term frequency–inverse document frequency (TFIDF), neural-based word embedding, Logistic Regression  |
| 233 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Unanswerable; 48,705 | The article does not specify a fixed number of tags they look at; it evaluates recommendations for different values of I | The article does not specify a fixed number of tags they look at; it evaluates recommendations for different values of I |
| 234 | `qasper_e` | `token_f1` | 0.333 | 0.667 | +0.333 | follow the architecture in berard2018end, but have 3 decoder layers like that in pino2019harnessing | The ASR and ST models follow the architecture in berard2018end with 3 decoder layers, and the MT model uses a Transforme | berard2018end architecture with 3 decoder layers like pino2019harnessing |
| 235 | `qasper_e` | `token_f1` | 0.833 | 0.833 | +0.000 |  Penn Treebank, WikiText2; Penn Treebank (PTB) , WikiText2 (WT-2) | Penn Treebank (PTB) and WikiText2 (WT-2) datasets | Penn Treebank (PTB) and WikiText2 (WT-2) datasets |
| 236 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | No; No | unanswerable | unanswerable |
| 237 | `qasper_e` | `token_f1` | 0.605 | 0.605 | +0.000 | While there has been existing work on reducing NLP model vocabulary sizes BIBREF15, distillation techniques cannot utili | Because they require the student and teacher models to share the same vocabulary and output space. | Because they require the student and teacher models to share the same vocabulary and output space. |
| 238 | `qasper_e` | `token_f1` | 0.154 | 0.154 | +0.000 | using word2vec to create features that are used as input to the SVM; use the word2vec algorithm, create several unsuperv | word2vec | word2vec |
| 239 | `qasper_e` | `token_f1` | 0.872 | 0.723 | -0.148 | ancient Chinese history records in several dynasties (about 1000BC-200BC) and articles written by celebrities of that er | The ancient Chinese dataset comes from ancient Chinese history records in several dynasties (about 1000BC-200BC) and art | 1.7K bilingual ancient-modern Chinese articles collected from the internet, with a large part coming from ancient Chines |
| 240 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | No | unanswerable | unanswerable |
| 241 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | words embeddings, style, and morality features; words embeddings, style, and morality features | Words embeddings, style, and morality features. | words embeddings, style, and morality features |
| 242 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | United Nations Parallel Corpus, IIT Bombay corpus, OpenSubtitles 2018 | XNLI dataset and Universal Dependencies v2.4 | XNLI dataset and Universal Dependencies v2.4 |
| 243 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Unanswerable; English | English | unanswerable |
| 244 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | No; No | No | no |
| 245 | `qasper_e` | `token_f1` | 0.643 | 0.947 | +0.305 | 45,000 scholarly articles, including over 33,000 with full text | The collection of COVID-19 literature is the CORD-19 dataset, which contains over 45,000 scholarly articles, including o | over 45,000 scholarly articles, including over 33,000 with full text |
| 246 | `qasper_e` | `token_f1` | 0.516 | 0.533 | +0.017 | support vector machine classifier (SVM), logistic regression classifier (LR), Naive Bayes classifier (NB), random forest | TF-IDF-based classifiers (SVM, LR, NB, RF), CNN, LSTM, LSTM-soft, and LSTM-self. | TF-IDF (SVM, LR, NB, RF), CNN, LSTM, LSTM-soft, and LSTM-self |
| 247 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | 1913 signals; Unanswerable | unanswerable | unanswerable |
| 248 | `qasper_e` | `token_f1` | 0.457 | 0.800 | +0.343 | Co-Reference Resolution, Query Generation, Retrieval Model, Result Generation; Co-Reference Resolution, Query Generation | The different modules in Macaw include actions (e.g., search, question answering), co-reference resolution, query genera | Macaw's modules include co-reference resolution, query generation, retrieval model, and result generation. |
| 249 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Unanswerable | unanswerable | unanswerable |
| 250 | `qasper_e` | `token_f1` | 0.000 | 1.000 | +1.000 | Unanswerable; Unanswerable | The article mentions variability with respect to "dialects" but does not specify particular accents present in the corpu | unanswerable |
| 251 | `hotpotqa_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Yanzhou | Yanzhou District | Yanzhou District |
| 252 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | McLaren Vale | McLaren Vale | McLaren Vale |
| 253 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Oberschleißheim | Munich | Munich |
| 254 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | yes | Yes | Yes |
| 255 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Sinclair Hill | Robert Z. Leonard | Robert Z. Leonard |
| 256 | `hotpotqa_e` | `token_f1` | 0.500 | 0.500 | +0.000 | Kew, Melbourne, Australia | Kew | Kew |
| 257 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Herbert Ross | Herbert Ross | Herbert Ross |
| 258 | `hotpotqa_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Emilio Ángel Sánchez Vicario | Emilio Sánchez | Emilio Sánchez |
| 259 | `hotpotqa_e` | `token_f1` | 0.800 | 0.800 | +0.000 | Oldham County, Kentucky | Oldham County | Oldham County |
| 260 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | very little | Very little | Very little |
| 261 | `hotpotqa_e` | `token_f1` | 0.500 | 0.500 | +0.000 | the best known globetrotters | globetrotters | globetrotters |
| 262 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | North Sea | North Sea | North Sea |
| 263 | `hotpotqa_e` | `token_f1` | 0.250 | 0.250 | +0.000 | a genus of flowering plant in the Lardizabalaceae family | Lardizabalaceae | Lardizabalaceae |
| 264 | `hotpotqa_e` | `token_f1` | 0.000 | 0.800 | +0.800 | Gareth Huw Evans | Pierre Chenal | Gareth Evans |
| 265 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | European route E 22 | E22 | E22 |
| 266 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Mulberry | Mulberry | Mulberry |
| 267 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | no | No | No |
| 268 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | University of Missouri | University of Missouri | University of Missouri |
| 269 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | WANH | None of the radio stations listed serve the Lakes Region (Belknap County, etc.). | WVNH |
| 270 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Orange County | Orange County | Orange County |
| 271 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Crocosmia | Crocosmia | Crocosmia |
| 272 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | William Cavendish, 7th Duke of Devonshire | William Cavendish, 7th Duke of Devonshire | William Cavendish, 7th Duke of Devonshire |
| 273 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Gambaga | Gambaga | Gambaga |
| 274 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | My Boss, My Hero | My Boss, My Hero | My Boss, My Hero |
| 275 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | the Netherlands | Dutch | Dutch |
| 276 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Division of Cook | Division of Cook | Division of Cook |
| 277 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | The Snowman | The Snowman | The Snowman |
| 278 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Timanfaya National Park | Timanfaya National Park | Timanfaya National Park |
| 279 | `hotpotqa_e` | `token_f1` | 0.250 | 0.000 | -0.250 | Albany Great Danes baseball team | Binghamton and Albany | Binghamton |
| 280 | `hotpotqa_e` | `token_f1` | 0.500 | 0.500 | +0.000 | Karakoram mountain range | Karakoram | Karakoram |
| 281 | `hotpotqa_e` | `token_f1` | 0.952 | 0.190 | -0.762 | George Clooney, Thekla Reuten, Violante Placido, Irina Björklund, and Paolo Bonacelli | George Clooney, Thekla Reuten, Violante Placido, Irina Björklund, Paolo Bonacelli | George Clooney, John Neville, Ray Smith, Cyril Luckham, Derek Godfrey |
| 282 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Dusty Dvoracek | None of the former nose tackles listed in the passages announced ESPN College Football Friday Primetime in 2017. | None of the passages state that any former nose tackle announced ESPN College Football Friday Primetime in 2017. |
| 283 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | September 23, 1935 | September 23, 1935 | September 23, 1935 |
| 284 | `hotpotqa_e` | `token_f1` | 0.727 | 0.727 | +0.000 | professional wrestler, actor, and hip hop musician | professional wrestler and actor | professional wrestler and actor |
| 285 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Amberley Village | Amberley Village | Amberley Village |
| 286 | `hotpotqa_e` | `token_f1` | 0.800 | 0.800 | +0.000 | architect Michael Graves | Michael Graves | Michael Graves |
| 287 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Tim Cluess | Tim Cluess | Tim Cluess |
| 288 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Apium | Apium | Apium |
| 289 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Marino Girolami | Marino Girolami | Marino Girolami |
| 290 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | American educator, writer, | None | None |
| 291 | `hotpotqa_e` | `token_f1` | 0.000 | 0.500 | +0.500 | intelligent design | Young earth creationism | young earth creationism and intelligent design |
| 292 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Knowlton Hall | Knowlton Hall | Knowlton Hall |
| 293 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Washington, D.C. | Washington, D.C. | Washington, D.C. |
| 294 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | tennis player | tennis player | tennis player |
| 295 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | no | No | No |
| 296 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Pope John X | Pope John X | Pope John X |
| 297 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Overijssel | Overijssel | Overijssel |
| 298 | `hotpotqa_e` | `token_f1` | 0.375 | 0.375 | +0.000 | prevent the opposing team from scoring goals | To stop attacks during the game and prevent the opposition from scoring. | To stop attacks during the game and prevent the opposition from scoring. |
| 299 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Godspell | Godspell | Godspell |
| 300 | `hotpotqa_e` | `token_f1` | 0.364 | 1.000 | +0.636 | The Fatima Mansions | The Fatima Mansions had more members when they were formed. | The Fatima Mansions |

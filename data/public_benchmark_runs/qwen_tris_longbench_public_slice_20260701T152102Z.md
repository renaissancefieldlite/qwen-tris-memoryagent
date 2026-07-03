# Qwen Tris LongBench Public Slice - qwen_tris_longbench_public_slice_20260701T152102Z

- Benchmark: `LongBench public data.zip`
- Provider: `qwen-cloud`
- Model: `qwen-plus`
- Items: `100`
- Skipped provider-blocked rows: `0`
- Condition A mean: `0.519`
- Condition B mean: `0.496`
- Delta: `-0.023`

## Boundary

Public LongBench smoke slice. This is not a full LongBench leaderboard claim; it is a source-backed answer-key accuracy receipt that can scale to larger slices.

## Conditions

- Condition A: baseline Qwen prompt-only answer discipline
- Condition B: Qwen Tris stable-state answer discipline

## Family Totals

- `passage_count_e`: n=50 A=0.340 B=0.280 delta=-0.060
- `hotpotqa_e`: n=50 A=0.698 B=0.712 delta=+0.015

## Rows

| # | Dataset | Metric | A | B | Delta | Gold | A prediction | B prediction |
|---:|---|---|---:|---:|---:|---|---|---|
| 1 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 6 | 5 | 4 |
| 2 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 10 | 7 | 7 |
| 3 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 4 | 3 | 3 |
| 4 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 6 | 5 | 4 |
| 5 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 12 | Let's carefully compare all 18 paragraphs to identify duplicates.  We'll group identical paragraphs by content (ignoring | 6 |
| 6 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 8 | 4 | 3 |
| 7 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 9 | 7 | 7 |
| 8 | `passage_count_e` | `numeric_accuracy` | 1.000 | 0.000 | -1.000 | 7 | 7 | 8 |
| 9 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 10 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 9 | 4 | 5 |
| 11 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 7 | 7 | 7 |
| 12 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 7 | 5 | 4 |
| 13 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 6 | 5 | 4 |
| 14 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 15 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 6 | 6 | 6 |
| 16 | `passage_count_e` | `numeric_accuracy` | 0.000 | 1.000 | +1.000 | 2 | 3 | 2 |
| 17 | `passage_count_e` | `numeric_accuracy` | 1.000 | 0.000 | -1.000 | 4 | 4 | 3 |
| 18 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 19 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 8 | 6 | 6 |
| 20 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 4 | 4 | 4 |
| 21 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 9 | 8 | 7 |
| 22 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 23 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 7 | 5 | 4 |
| 24 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 10 | 7 | 5 |
| 25 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 3 | 4 | 4 |
| 26 | `passage_count_e` | `numeric_accuracy` | 1.000 | 0.000 | -1.000 | 5 | 5 | 4 |
| 27 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 13 | 8 | 7 |
| 28 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 29 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 30 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 8 | 5 | 5 |
| 31 | `passage_count_e` | `numeric_accuracy` | 1.000 | 0.000 | -1.000 | 5 | 5 | 4 |
| 32 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 4 | 3 | 3 |
| 33 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 34 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 10 | 4 | 6 |
| 35 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 16 | 9 | 8 |
| 36 | `passage_count_e` | `numeric_accuracy` | 1.000 | 0.000 | -1.000 | 5 | 5 | 4 |
| 37 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 5 | 4 | 4 |
| 38 | `passage_count_e` | `numeric_accuracy` | 0.000 | 1.000 | +1.000 | 5 | 6 | 5 |
| 39 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 9 | 4 | 4 |
| 40 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 9 | 7 | 7 |
| 41 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 11 | 7 | 7 |
| 42 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 11 | 8 | 8 |
| 43 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 8 | 5 | 5 |
| 44 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 45 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 8 | 6 | 5 |
| 46 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 47 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 9 | 4 | 4 |
| 48 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 9 | 6 | 6 |
| 49 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 17 | Let's carefully compare all 17 paragraphs to identify duplicates.  We'll go one by one and group identical or near-ident | 10 |
| 50 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 7 | 5 | 6 |
| 51 | `hotpotqa_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Yanzhou | Yanzhou District | Yanzhou District |
| 52 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | McLaren Vale | McLaren Vale | McLaren Vale |
| 53 | `hotpotqa_e` | `token_f1` | 0.000 | 1.000 | +1.000 | Oberschleißheim | Munich | Oberschleißheim |
| 54 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | yes | Yes | Yes |
| 55 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Sinclair Hill | Robert Z. Leonard | Robert Z. Leonard |
| 56 | `hotpotqa_e` | `token_f1` | 0.500 | 0.500 | +0.000 | Kew, Melbourne, Australia | Kew | Kew |
| 57 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Herbert Ross | Herbert Ross | Herbert Ross |
| 58 | `hotpotqa_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Emilio Ángel Sánchez Vicario | Emilio Sánchez | Emilio Sánchez |
| 59 | `hotpotqa_e` | `token_f1` | 0.800 | 0.800 | +0.000 | Oldham County, Kentucky | Oldham County | Oldham County |
| 60 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | very little | Very little | Very little |
| 61 | `hotpotqa_e` | `token_f1` | 0.500 | 0.500 | +0.000 | the best known globetrotters | globetrotters | globetrotters |
| 62 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | North Sea | North Sea | North Sea |
| 63 | `hotpotqa_e` | `token_f1` | 0.250 | 0.250 | +0.000 | a genus of flowering plant in the Lardizabalaceae family | Lardizabalaceae | Lardizabalaceae |
| 64 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Gareth Huw Evans | Pierre Chenal | Pierre Chenal |
| 65 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | European route E 22 | E22 | E22 |
| 66 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Mulberry | Mulberry | Mulberry |
| 67 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | no | No | No |
| 68 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | University of Missouri | University of Missouri | University of Missouri |
| 69 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | WANH | None of the radio stations listed serve the Lakes Region (which comprises all of Belknap County, among others). | WVNH |
| 70 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Orange County | Orange County | Orange County |
| 71 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Crocosmia | Crocosmia | Crocosmia |
| 72 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | William Cavendish, 7th Duke of Devonshire | William Cavendish, 7th Duke of Devonshire | William Cavendish, 7th Duke of Devonshire |
| 73 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Gambaga | Gambaga | Gambaga |
| 74 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | My Boss, My Hero | My Boss, My Hero | My Boss, My Hero |
| 75 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | the Netherlands | Dutch | Dutch |
| 76 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Division of Cook | Division of Cook | Division of Cook |
| 77 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | The Snowman | The Snowman | The Snowman |
| 78 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Timanfaya National Park | Timanfaya National Park | Timanfaya National Park |
| 79 | `hotpotqa_e` | `token_f1` | 0.333 | 0.250 | -0.083 | Albany Great Danes baseball team | Albany | Binghamton and Albany |
| 80 | `hotpotqa_e` | `token_f1` | 0.500 | 0.500 | +0.000 | Karakoram mountain range | Karakoram | Karakoram |
| 81 | `hotpotqa_e` | `token_f1` | 0.190 | 0.000 | -0.190 | George Clooney, Thekla Reuten, Violante Placido, Irina Björklund, and Paolo Bonacelli | George Clooney, Ray Smith, Cyril Luckham, Derek Godfrey, John Neville | John Neville, Ray Smith, Cyril Luckham, Derek Godfrey, Ann Bell |
| 82 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Dusty Dvoracek | None of the former nose tackles listed announced ESPN College Football Friday Primetime in 2017. | None of the provided passages state that any former nose tackle announced ESPN College Football Friday Primetime in 2017 |
| 83 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | September 23, 1935 | September 23, 1935 | September 23, 1935 |
| 84 | `hotpotqa_e` | `token_f1` | 0.727 | 0.727 | +0.000 | professional wrestler, actor, and hip hop musician | professional wrestler and actor | professional wrestler and actor |
| 85 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Amberley Village | Amberley Village | Amberley Village |
| 86 | `hotpotqa_e` | `token_f1` | 0.800 | 0.800 | +0.000 | architect Michael Graves | Michael Graves | Michael Graves |
| 87 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Tim Cluess | Tim Cluess | Tim Cluess |
| 88 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Apium | Apium | Apium |
| 89 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Marino Girolami | Marino Girolami | Marino Girolami |
| 90 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | American educator, writer, | None | Academic pursuit |
| 91 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | intelligent design | Young earth creationism | young earth creationism |
| 92 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Knowlton Hall | Knowlton Hall | Knowlton Hall |
| 93 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Washington, D.C. | Washington, D.C. | Washington, D.C. |
| 94 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | tennis player | tennis player | tennis player |
| 95 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | no | No | No |
| 96 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Pope John X | Pope John X | Pope John X |
| 97 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Overijssel | Overijssel | Overijssel |
| 98 | `hotpotqa_e` | `token_f1` | 0.375 | 0.375 | +0.000 | prevent the opposing team from scoring goals | To stop attacks during the game and prevent the opposition from scoring. | To stop attacks during the game and prevent the opposition from scoring. |
| 99 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Godspell | Godspell | Godspell |
| 100 | `hotpotqa_e` | `token_f1` | 0.571 | 0.571 | +0.000 | The Fatima Mansions | The Fatima Mansions had more members. | The Fatima Mansions had more members. |

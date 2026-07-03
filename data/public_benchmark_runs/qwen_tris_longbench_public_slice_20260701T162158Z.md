# Qwen Tris LongBench Public Slice - qwen_tris_longbench_public_slice_20260701T162158Z

- Benchmark: `LongBench public data.zip`
- Provider: `qwen-cloud`
- Model: `qwen-plus`
- Items: `50`
- Skipped provider-blocked rows: `0`
- Condition A mean: `0.696`
- Condition B mean: `0.688`
- Delta: `-0.008`

## Boundary

Public LongBench smoke slice. This is not a full LongBench leaderboard claim; it is a source-backed answer-key accuracy receipt that can scale to larger slices.

## Conditions

- Condition A: baseline Qwen prompt-only answer discipline
- Condition B: Qwen Tris stable-state answer discipline

## Family Totals

- `hotpotqa_e`: n=50 A=0.696 B=0.688 delta=-0.008

## Rows

| # | Dataset | Metric | A | B | Delta | Gold | A prediction | B prediction |
|---:|---|---|---:|---:|---:|---|---|---|
| 1 | `hotpotqa_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Yanzhou | Yanzhou District | Yanzhou District |
| 2 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | McLaren Vale | McLaren Vale | McLaren Vale |
| 3 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Oberschleißheim | Munich | Munich |
| 4 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | yes | Yes | Yes |
| 5 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Sinclair Hill | Robert Z. Leonard | Robert Z. Leonard |
| 6 | `hotpotqa_e` | `token_f1` | 0.500 | 0.500 | +0.000 | Kew, Melbourne, Australia | Kew | Kew |
| 7 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Herbert Ross | Herbert Ross | Herbert Ross |
| 8 | `hotpotqa_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Emilio Ángel Sánchez Vicario | Emilio Sánchez | Emilio Sánchez |
| 9 | `hotpotqa_e` | `token_f1` | 0.800 | 0.800 | +0.000 | Oldham County, Kentucky | Oldham County | Oldham County |
| 10 | `hotpotqa_e` | `token_f1` | 1.000 | 0.571 | -0.429 | very little | Very little | very little differences in elevation |
| 11 | `hotpotqa_e` | `token_f1` | 0.500 | 0.500 | +0.000 | the best known globetrotters | globetrotters | globetrotters |
| 12 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | North Sea | North Sea | North Sea |
| 13 | `hotpotqa_e` | `token_f1` | 0.250 | 0.250 | +0.000 | a genus of flowering plant in the Lardizabalaceae family | Lardizabalaceae | Lardizabalaceae |
| 14 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Gareth Huw Evans | Pierre Chenal | Pierre Chenal |
| 15 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | European route E 22 | E22 | E22 |
| 16 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Mulberry | Mulberry | Mulberry |
| 17 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | no | No | No |
| 18 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | University of Missouri | University of Missouri | University of Missouri |
| 19 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | WANH | None of the radio stations listed serve the Lakes Region (Belknap County, etc.). | WVNH |
| 20 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Orange County | Orange County | Orange County |
| 21 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Crocosmia | Crocosmia | Crocosmia |
| 22 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | William Cavendish, 7th Duke of Devonshire | William Cavendish, 7th Duke of Devonshire | William Cavendish, 7th Duke of Devonshire |
| 23 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Gambaga | Gambaga | Gambaga |
| 24 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | My Boss, My Hero | My Boss, My Hero | My Boss, My Hero |
| 25 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | the Netherlands | Dutch | Dutch |
| 26 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Division of Cook | Division of Cook | Division of Cook |
| 27 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | The Snowman | The Snowman | The Snowman |
| 28 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Timanfaya National Park | Timanfaya National Park | Timanfaya National Park |
| 29 | `hotpotqa_e` | `token_f1` | 0.250 | 0.250 | +0.000 | Albany Great Danes baseball team | Binghamton and Albany | Binghamton and Albany |
| 30 | `hotpotqa_e` | `token_f1` | 0.500 | 0.500 | +0.000 | Karakoram mountain range | Karakoram | Karakoram |
| 31 | `hotpotqa_e` | `token_f1` | 0.190 | 0.000 | -0.190 | George Clooney, Thekla Reuten, Violante Placido, Irina Björklund, and Paolo Bonacelli | George Clooney, Ray Smith, Cyril Luckham, Derek Godfrey, John Neville | John Neville, Ray Smith, Cyril Luckham, Derek Godfrey, Ann Bell |
| 32 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Dusty Dvoracek | None of the former nose tackles listed in the passages announced ESPN College Football Friday Primetime in 2017. | None of the passages state that any former nose tackle announced ESPN College Football Friday Primetime in 2017. |
| 33 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | September 23, 1935 | September 23, 1935 | September 23, 1935 |
| 34 | `hotpotqa_e` | `token_f1` | 0.727 | 0.000 | -0.727 | professional wrestler, actor, and hip hop musician | Professional wrestler and actor | rapper |
| 35 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Amberley Village | Amberley Village | Amberley Village |
| 36 | `hotpotqa_e` | `token_f1` | 0.800 | 0.800 | +0.000 | architect Michael Graves | Michael Graves | Michael Graves |
| 37 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Tim Cluess | Tim Cluess | Tim Cluess |
| 38 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Apium | Apium | Apium |
| 39 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Marino Girolami | Marino Girolami | Marino Girolami |
| 40 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | American educator, writer, | None | Academic pursuit |
| 41 | `hotpotqa_e` | `token_f1` | 0.000 | 0.500 | +0.500 | intelligent design | Young earth creationism | young earth creationism and intelligent design |
| 42 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Knowlton Hall | Knowlton Hall | Knowlton Hall |
| 43 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Washington, D.C. | Washington, D.C. | Washington, D.C. |
| 44 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | tennis player | tennis player | tennis player |
| 45 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | no | No | No |
| 46 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Pope John X | Pope John X | Pope John X |
| 47 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Overijssel | Overijssel | Overijssel |
| 48 | `hotpotqa_e` | `token_f1` | 0.375 | 0.375 | +0.000 | prevent the opposing team from scoring goals | To stop attacks during the game and prevent the opposition from scoring. | To stop attacks during the game and prevent the opposition from scoring. |
| 49 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Godspell | Godspell | Godspell |
| 50 | `hotpotqa_e` | `token_f1` | 0.571 | 1.000 | +0.429 | The Fatima Mansions | The Fatima Mansions had more members. | The Fatima Mansions |

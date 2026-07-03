# Qasper Lock Receipt - qwen_tris_qasper_lock_20260701T172350Z

- Benchmark: `LongBench public data.zip`
- Dataset: `qasper_e`
- Provider: `qwen-cloud`
- Model: `qwen-plus`
- Type: derived lock receipt from two adjacent Qasper-only receipts; no additional model calls
- Items: `100`
- Skipped provider-blocked rows: `0`
- Condition A baseline mean: `0.488`
- Condition B Qwen Tris mean: `0.532`
- Delta: `+0.044`
- Wins / losses / ties: `30 / 17 / 53`

## Source Receipts

- `rows_1_50`: `data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T172019Z.json` A=0.494 B=0.545 delta=+0.051 skipped=0
- `rows_51_100`: `data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T171624Z.json` A=0.483 B=0.519 delta=+0.036 skipped=0

## Read

Qasper is locked as a positive LongBench-E public proof lane across two adjacent 50-row windows under the same repaired Qasper answer discipline. Remaining failure mode: answer-span selection can still miss the requested numeric/entity span on some rows, so do not claim solved-all-rows.

## Remaining Failure Modes

- Wrong numeric target when a question asks for real-life dataset size or corpus size.
- Over-expansion on questions that only want a label/acronym/name.
- Occasional wrong support span when article contains nearby competing model/team/dataset results.

## Biggest Positive Deltas

- `qasper_rows_1_50` row `50` delta `+1.000` gold: Unanswerable; Unanswerable | A: The article mentions variability with respect to "dialects" but does not specify which accents are present in the corpus. | B: unanswerable
- `qasper_rows_1_50` row `33` delta `+1.000` gold: Unanswerable; 48,705 | A: The article does not specify a fixed number of tags they look at; it evaluates recommendations for different values of "k" (number of recommended tags), with figures showing result | B: unanswerable
- `qasper_rows_1_50` row `45` delta `+0.852` gold: 45,000 scholarly articles, including over 33,000 with full text | A: The collection of COVID-19 literature consists of 2081 articles and about 360,000 sentences. | B: over 45,000 scholarly articles, including over 33,000 with full text
- `qasper_rows_51_100` row `43` delta `+0.550` gold: DTA18, DTA19; Diachronic Usage Relatedness (DURel) gold standard data set | A: The corpus used for the task is the diachronic corpus pair DTA18 and DTA19 from the DTA corpus. | B: DTA18 and DTA19
- `qasper_rows_1_50` row `34` delta `+0.333` gold: follow the architecture in berard2018end, but have 3 decoder layers like that in pino2019harnessing | A: The ASR and ST models follow the architecture in berard2018end with 3 decoder layers, and the MT model uses a Transformer base architecture with 3 encoder layers, 3 decoder layers, | B: berard2018end architecture with 3 decoder layers like pino2019harnessing
- `qasper_rows_51_100` row `30` delta `+0.333` gold: IMDb dataset of movie reviews; IMDb | A: IMDb dataset | B: IMDb dataset of movie reviews
- `qasper_rows_51_100` row `10` delta `+0.333` gold: 53 documents; 53 documents | A: 53 | B: 53 documents
- `qasper_rows_1_50` row `48` delta `+0.315` gold: Co-Reference Resolution, Query Generation, Retrieval Model, Result Generation; Co-Reference Resolution, Query Generation, Retrieval Model, Result Generation | A: Macaw's modules include actions (e.g., search, question answering), co-reference resolution, query generation, retrieval model, result generation, and user interfaces (e.g., File I | B: Macaw's modules include co-reference resolution, query generation, retrieval model, and result generation.

## Biggest Negative Deltas

- `qasper_rows_1_50` row `19` delta `-0.789` gold: RNN;  Recurrent Neural Network (RNN) | A: Recurrent Neural Network (RNN) | B: RNN with two 2D-convolutional layers, seven bi-directional recurrent layers, and a fully-connected layer with softmax activation
- `qasper_rows_1_50` row `29` delta `-0.533` gold: MIMIC-III; MIMIC-III | A: MIMIC-III dataset | B: MIMIC-III database, specifically 55,177 discharge reports and 4,475 discharge addendums for 41,127 distinct patients.
- `qasper_rows_51_100` row `49` delta `-0.267` gold: 26972; 26972 sentences | A: The real-life dataset consists of supervisor assessment text from 4528 employees, containing 26972 sentences. | B: 4528 employees
- `qasper_rows_1_50` row `8` delta `-0.165` gold: SemEval-2016 Challenge Task 5 BIBREF27 , BIBREF28;  English reviews ,  restaurant reviews from four different languages (Spanish, Turkish, Dutch, Russian) | A: The evaluation used restaurant reviews from four languages (Spanish, Turkish, Dutch, Russian) from SemEval-2016 Challenge Task 5, and an English corpus. | B: SemEval-2016 Challenge Task 5 restaurant reviews datasets in Spanish, Turkish, Dutch, and Russian.
- `qasper_rows_1_50` row `4` delta `-0.149` gold: (i) models that use plain stacked LSTMs, (ii) models with different INLINEFORM0, (iii) models without INLINEFORM1, (iv) models that integrate lower contexts via | A: The baselines were models that use plain stacked LSTMs. | B: plain stacked LSTMs
- `qasper_rows_1_50` row `31` delta `-0.108` gold: it captures other information rather than only the translational equivalent in the case of verbs; Alignment points of the POS tags. | A: Attention captures context words influencing the current word translation, such as adjectives and determiners for nouns, and auxiliary verbs, adverbs, subjects, and objects for ver | B: context words influencing the current word translation
- `qasper_rows_51_100` row `21` delta `-0.083` gold: Individuals with legal training; Yes | A: Experts with legal training. | B: seven experts with legal training
- `qasper_rows_1_50` row `14` delta `-0.078` gold: Friends, EmotionPush; EmotionLines BIBREF6 | A: EmotionLines dataset, which consists of the Friends and EmotionPush subsets. | B: EmotionLines (Friends and EmotionPush), Twitter emotion dataset, and Friends TV show scripts.

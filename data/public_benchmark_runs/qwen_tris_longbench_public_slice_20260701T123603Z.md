# Qwen Tris LongBench Public Slice - qwen_tris_longbench_public_slice_20260701T123603Z

- Benchmark: `LongBench public data.zip`
- Provider: `qwen-cloud`
- Model: `qwen-plus`
- Items: `60`
- Condition A mean: `0.565`
- Condition B mean: `0.587`
- Delta: `+0.022`

## Boundary

Public LongBench smoke slice. This is not a full LongBench leaderboard claim; it is a source-backed answer-key accuracy receipt that can scale to larger slices.

## Conditions

- Condition A: baseline Qwen prompt-only answer discipline
- Condition B: Qwen Tris stable-state answer discipline

## Family Totals

- `passage_retrieval_en_e`: n=10 A=1.000 B=1.000 delta=+0.000
- `passage_count_e`: n=10 A=0.000 B=0.000 delta=+0.000
- `trec_e`: n=10 A=0.800 B=0.900 delta=+0.100
- `multifieldqa_en_e`: n=10 A=0.520 B=0.514 delta=-0.006
- `qasper_e`: n=10 A=0.497 B=0.555 delta=+0.059
- `hotpotqa_e`: n=10 A=0.575 B=0.555 delta=-0.020

## Rows

| # | Dataset | Metric | A | B | Delta | Gold | A prediction | B prediction |
|---:|---|---|---:|---:|---:|---|---|---|
| 1 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 6 | Paragraph 6 | Paragraph 6 |
| 2 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 1 | Paragraph 1 | Paragraph 1 |
| 3 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 3 | Paragraph 3 | Paragraph 3 |
| 4 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 1 | Paragraph 1 | Paragraph 1 |
| 5 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 5 | Paragraph 5 | Paragraph 5 |
| 6 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 12 | Paragraph 12 | Paragraph 12 |
| 7 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 7 | Paragraph 7 | Paragraph 7 |
| 8 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 1 | Paragraph 1 | Paragraph 1 |
| 9 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 2 | Paragraph 2 | Paragraph 2 |
| 10 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 6 | Paragraph 6 | Paragraph 6 |
| 11 | `passage_count_e` | `token_f1` | 0.000 | 0.000 | +0.000 | 6 | 9 | passage_count_e |
| 12 | `passage_count_e` | `token_f1` | 0.000 | 0.000 | +0.000 | 10 | 3 | 0 |
| 13 | `passage_count_e` | `token_f1` | 0.000 | 0.000 | +0.000 | 4 | Bacardi 151 | passage_count_e |
| 14 | `passage_count_e` | `token_f1` | 0.000 | 0.000 | +0.000 | 6 | 1 | 0 |
| 15 | `passage_count_e` | `token_f1` | 0.000 | 0.000 | +0.000 | 12 | The context does not provide information to answer the question. | passage_count_e |
| 16 | `passage_count_e` | `token_f1` | 0.000 | 0.000 | +0.000 | 8 | 0 | passage_count_e |
| 17 | `passage_count_e` | `token_f1` | 0.000 | 0.000 | +0.000 | 9 | 6 | passage_count_e |
| 18 | `passage_count_e` | `token_f1` | 0.000 | 0.000 | +0.000 | 7 | No context provided to answer the question. | passage_count_e |
| 19 | `passage_count_e` | `token_f1` | 0.000 | 0.000 | +0.000 | 3 | 4 | 4 |
| 20 | `passage_count_e` | `token_f1` | 0.000 | 0.000 | +0.000 | 9 | 2 | passage_count_e |
| 21 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 22 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Date | Date | Date |
| 23 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Number of something | Number of something | Number of something |
| 24 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Animal | Other entity | Other entity |
| 25 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | City | City | City |
| 26 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Individual | Individual | Individual |
| 27 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Equivalent term | Equivalent term | Equivalent term |
| 28 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Element and substance | Element and substance | Element and substance |
| 29 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Description of something | Techniques and method | Description of something |
| 30 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 31 | `multifieldqa_en_e` | `token_f1` | 1.000 | 0.903 | -0.097 | Exposure to sunlight or strong light may cause permanent yellow spot damage on the screen. | Exposure to sunlight or strong light may cause permanent yellow spot damage on the screen. | Exposure to direct sunlight or other strong light sources may cause permanent yellow spot damage on the screen. |
| 32 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Vice Admiral. | Vice Admiral | Vice Admiral |
| 33 | `multifieldqa_en_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Sir Richard. | Ralph Rokebye's brother was William Rokeby. | No evidence in the context identifies Ralph Rokebye's brother. |
| 34 | `multifieldqa_en_e` | `token_f1` | 0.750 | 0.750 | +0.000 | South West Ultras fan club. | South West Ultras | South West Ultras |
| 35 | `multifieldqa_en_e` | `token_f1` | 0.222 | 0.222 | +0.000 | It is recommended to have at least a 2x2 meter space for using the VR headset. | At least 2×2 meters. | At least 2×2 meters |
| 36 | `multifieldqa_en_e` | `token_f1` | 0.182 | 0.167 | -0.015 | It depends on the value of x, either 0 or (6x^2cos(x^2)+sin(x^2))/(3(x^2)^(1/3)). | $$ f'\left(x\right)  =  \begin{cases}  \frac{6x^2\cos{\left(x^2\right)}+\sin{\left(x^2\right)}}{3\sqrt[3]{x^2}}, & \mbox | \begin{equation*} f'\left(x\right)  =  \begin{cases}  \frac{6x^2\cos{\left(x^2\right)}+\sin{\left(x^2\right)}}{3\sqrt[3] |
| 37 | `multifieldqa_en_e` | `token_f1` | 0.737 | 0.737 | +0.000 | In 2009, Brooksley Born received the John F. Kennedy Profiles in Courage Award. | John F. Kennedy Profiles in Courage Award | John F. Kennedy Profiles in Courage Award |
| 38 | `multifieldqa_en_e` | `token_f1` | 0.308 | 0.364 | +0.056 | Margaret Way started self-publishing her books as e-books in 2013. | Beginning in 2013 | Beginning in 2013, Margaret began to self-publish, releasing her first "e-book" mid-July. |
| 39 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Long Term Capital Management (LTCM). | Long Term Capital Management (LTCM) | Long Term Capital Management (LTCM) |
| 40 | `multifieldqa_en_e` | `token_f1` | 0.000 | 0.000 | +0.000 | It is well described by the Gaussian theory. | $m \sim t^{1/2}$ | $m \sim t^{1/2}$ |
| 41 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li |
| 42 | `qasper_e` | `token_f1` | 0.600 | 0.600 | +0.000 | the series of posts that trigger an intervention | The latent context used to predict instructor intervention is the series of posts that trigger an intervention. | The latent context used to predict instructor intervention is "the series of posts that trigger an intervention." |
| 43 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | F-score, Kappa; Unanswerable | F-score and Kappa statistics | F-score and Kappa statistics |
| 44 | `qasper_e` | `token_f1` | 0.200 | 0.200 | +0.000 | (i) models that use plain stacked LSTMs, (ii) models with different INLINEFORM0, (iii) models without INLINEFORM1, (iv)  | The baselines were plain stacked LSTMs. | The baselines were plain stacked LSTMs. |
| 45 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Yes; Unanswerable | No, jiant is compatible only with Python (requires Python 3.5 or later). | No. |
| 46 | `qasper_e` | `token_f1` | 0.061 | 1.000 | +0.939 | No | No. The experts are domain experts with legal training, not real-world users. The context states that questions were eli | No. |
| 47 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Yes; No | No. | No. |
| 48 | `qasper_e` | `token_f1` | 0.538 | 0.480 | -0.058 | SemEval-2016 Challenge Task 5 BIBREF27 , BIBREF28;  English reviews ,  restaurant reviews from four different languages  | Four restaurant review datasets from SemEval-2016 Challenge Task 5: Spanish, Turkish, Dutch, and Russian. | SemEval-2016 Challenge Task 5 restaurant reviews datasets in Spanish, Turkish, Dutch, and Russian. |
| 49 | `qasper_e` | `token_f1` | 0.706 | 0.414 | -0.292 | 7.36% on accuracy and 9.69% on F1 score; it has 0.024 improvement in accuracy comparing to ELMO Only and  0.006 improvem | 7.36% improvement in accuracy and 9.69% in F1 score. | The context states that adding topic information (Topic Only setting) to the base model improved accuracy by 7.36% and F |
| 50 | `qasper_e` | `token_f1` | 0.194 | 0.194 | +0.000 | They use text transcription.; both | They use both: they use the released transcripts of the IEMOCAP dataset and also process the audio data using an ASR sys | They use both: they use released transcripts of the IEMOCAP dataset and also process audio data using an ASR system (Goo |
| 51 | `hotpotqa_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Yanzhou | Yanzhou District | Yanzhou District |
| 52 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | McLaren Vale | McLaren Vale | McLaren Vale |
| 53 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Oberschleißheim | Munich | Munich |
| 54 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | yes | Yes | Yes |
| 55 | `hotpotqa_e` | `token_f1` | 0.174 | 0.016 | -0.158 | Sinclair Hill | Robert Z. Leonard is younger. He was born on October 7, 1889, while Sinclair Hill was born on June 10, 1896. | Robert Z. Leonard is younger. Sinclair Hill was born on 10 June 1896, and Robert Z. Leonard was born on 7 October 1889.  |
| 56 | `hotpotqa_e` | `token_f1` | 0.500 | 0.500 | +0.000 | Kew, Melbourne, Australia | Kew | Kew |
| 57 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Herbert Ross | Herbert Ross | Herbert Ross |
| 58 | `hotpotqa_e` | `token_f1` | 0.167 | 0.125 | -0.042 | Emilio Ángel Sánchez Vicario | Emilio Sánchez is older. He was born on 29 May 1965, while Andrei Olhovskiy was born on 15 April 1966. | Emilio Sánchez is older.   Supporting evidence: Passage 6 states Emilio Sánchez was born on 29 May 1965; Passage 4 state |
| 59 | `hotpotqa_e` | `token_f1` | 0.800 | 0.800 | +0.000 | Oldham County, Kentucky | Oldham County | Oldham County |
| 60 | `hotpotqa_e` | `token_f1` | 0.444 | 0.444 | +0.000 | very little | The circuit has very little differences in elevation. | The circuit has very little differences in elevation. |

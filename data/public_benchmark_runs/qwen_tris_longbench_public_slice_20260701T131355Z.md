# Qwen Tris LongBench Public Slice - qwen_tris_longbench_public_slice_20260701T131355Z

- Benchmark: `LongBench public data.zip`
- Provider: `qwen-cloud`
- Model: `qwen-plus`
- Items: `150`
- Condition A mean: `0.578`
- Condition B mean: `0.597`
- Delta: `+0.020`

## Boundary

Public LongBench smoke slice. This is not a full LongBench leaderboard claim; it is a source-backed answer-key accuracy receipt that can scale to larger slices.

## Conditions

- Condition A: baseline Qwen prompt-only answer discipline
- Condition B: Qwen Tris stable-state answer discipline

## Family Totals

- `passage_retrieval_en_e`: n=25 A=1.000 B=1.000 delta=+0.000
- `passage_count_e`: n=25 A=0.360 B=0.280 delta=-0.080
- `trec_e`: n=25 A=0.320 B=0.560 delta=+0.240
- `multifieldqa_en_e`: n=25 A=0.627 B=0.605 delta=-0.022
- `qasper_e`: n=25 A=0.504 B=0.504 delta=+0.001
- `hotpotqa_e`: n=25 A=0.655 B=0.635 delta=-0.020

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
| 11 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 11 | Paragraph 11 | Paragraph 11 |
| 12 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 4 | Paragraph 4 | Paragraph 4 |
| 13 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 9 | Paragraph 9 | Paragraph 9 |
| 14 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 8 | Paragraph 8 | Paragraph 8 |
| 15 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 2 | Paragraph 2 | Paragraph 2 |
| 16 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 4 | Paragraph 4 | Paragraph 4 |
| 17 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 3 | Paragraph 3 | Paragraph 3 |
| 18 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 9 | Paragraph 9 | Paragraph 9 |
| 19 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 4 | Paragraph 4 | Paragraph 4 |
| 20 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 1 | Paragraph 1 | Paragraph 1 |
| 21 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 2 | Paragraph 2 | Paragraph 2 |
| 22 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 6 | Paragraph 6 | Paragraph 6 |
| 23 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 3 | Paragraph 3 | Paragraph 3 |
| 24 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 1 | Paragraph 1 | Paragraph 1 |
| 25 | `passage_retrieval_en_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Paragraph 7 | Paragraph 7 | Paragraph 7 |
| 26 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 6 | 5 | 5 |
| 27 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 10 | 7 | 5 |
| 28 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 4 | 3 | 3 |
| 29 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 6 | 5 | 4 |
| 30 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 12 | Let's carefully compare all 18 paragraphs to identify duplicates.  We'll group identical paragraphs by content (ignoring | 7 |
| 31 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 8 | 4 | 4 |
| 32 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 9 | 7 | 7 |
| 33 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 7 | 7 | 7 |
| 34 | `passage_count_e` | `numeric_accuracy` | 1.000 | 0.000 | -1.000 | 3 | 3 | 4 |
| 35 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 9 | 5 | 5 |
| 36 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 7 | 7 | 7 |
| 37 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 7 | 5 | 4 |
| 38 | `passage_count_e` | `numeric_accuracy` | 1.000 | 0.000 | -1.000 | 6 | 6 | 5 |
| 39 | `passage_count_e` | `numeric_accuracy` | 1.000 | 0.000 | -1.000 | 2 | 2 | 3 |
| 40 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 6 | 6 | 6 |
| 41 | `passage_count_e` | `numeric_accuracy` | 0.000 | 1.000 | +1.000 | 2 | 3 | 2 |
| 42 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 4 | 3 | 3 |
| 43 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 44 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 8 | 6 | 6 |
| 45 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 4 | 4 | 4 |
| 46 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 9 | 8 | 7 |
| 47 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 48 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 7 | 4 | 6 |
| 49 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 10 | 7 | 7 |
| 50 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 3 | 4 | 4 |
| 51 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 52 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Date | Type: Date | Date |
| 53 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Number of something | Type: Number of something | Number of something |
| 54 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Animal | Type: Definition of something | Definition of something |
| 55 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | City | Type: City | City |
| 56 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Individual | Type: Individual | Individual |
| 57 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Equivalent term | Type: Equivalent term | Type: Equivalent term |
| 58 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Element and substance | Type: Other entity | Food |
| 59 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Description of something | Type: Description of something | Description of something |
| 60 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 61 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Date | Date | Date |
| 62 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Definition of something | Type: Definition of something | Type: Definition of something |
| 63 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Other location | Type: Other location | Type: Other location |
| 64 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Expression abbreviated | Expression abbreviated | Expression abbreviated |
| 65 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Date | Type: Date | Type: Date |
| 66 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Other location | Type: Other location | Type: Other location |
| 67 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Definition of something | Type: Definition of something | Definition of something |
| 68 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Date | Date | Date |
| 69 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Country | Country | Country |
| 70 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Manner of an action | Type: Other entity | Type: Other entity |
| 71 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Other entity | Type: Invention, book and other creative piece | Invention, book and other creative piece |
| 72 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Individual | Individual | Individual |
| 73 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Element and substance | Type: Color | Type: Color |
| 74 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Other location | Planet | Planet |
| 75 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 76 | `multifieldqa_en_e` | `token_f1` | 0.600 | 0.600 | +0.000 | Exposure to sunlight or strong light may cause permanent yellow spot damage on the screen. | Permanent yellow spot damage on the screen. | Permanent yellow spot damage on the screen. |
| 77 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Vice Admiral. | Vice Admiral | Vice Admiral |
| 78 | `multifieldqa_en_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Sir Richard. | None of the text mentions Ralph Rokebye having a brother. | No brother is mentioned for Ralph Rokebye in the text. |
| 79 | `multifieldqa_en_e` | `token_f1` | 0.750 | 0.750 | +0.000 | South West Ultras fan club. | South West Ultras | South West Ultras |
| 80 | `multifieldqa_en_e` | `token_f1` | 0.222 | 0.222 | +0.000 | It is recommended to have at least a 2x2 meter space for using the VR headset. | At least 2×2 meters | At least 2×2 meters |
| 81 | `multifieldqa_en_e` | `token_f1` | 0.182 | 0.182 | +0.000 | It depends on the value of x, either 0 or (6x^2cos(x^2)+sin(x^2))/(3(x^2)^(1/3)). | $$ f'\left(x\right)  =  \begin{cases}  \frac{6x^2\cos{\left(x^2\right)}+\sin{\left(x^2\right)}}{3\sqrt[3]{x^2}}, & \mbox | $$ f'\left(x\right)  =  \begin{cases}  \frac{6x^2\cos{\left(x^2\right)}+\sin{\left(x^2\right)}}{3\sqrt[3]{x^2}}, & \mbox |
| 82 | `multifieldqa_en_e` | `token_f1` | 0.737 | 0.737 | +0.000 | In 2009, Brooksley Born received the John F. Kennedy Profiles in Courage Award. | John F. Kennedy Profiles in Courage Award | John F. Kennedy Profiles in Courage Award |
| 83 | `multifieldqa_en_e` | `token_f1` | 0.182 | 0.182 | +0.000 | Margaret Way started self-publishing her books as e-books in 2013. | 2013 | 2013 |
| 84 | `multifieldqa_en_e` | `token_f1` | 1.000 | 0.889 | -0.111 | Long Term Capital Management (LTCM). | Long Term Capital Management (LTCM) | Long Term Capital Management |
| 85 | `multifieldqa_en_e` | `token_f1` | 0.000 | 0.000 | +0.000 | It is well described by the Gaussian theory. | $m \sim t^{1/2}$ | $m \sim t^{1/2}$ |
| 86 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | June 1, 1999. | June 1, 1999 | June 1, 1999 |
| 87 | `multifieldqa_en_e` | `token_f1` | 0.800 | 0.800 | +0.000 | 23 September. | 23 September 2017 | 23 September 2017 |
| 88 | `multifieldqa_en_e` | `token_f1` | 0.273 | 0.273 | +0.000 | The maximum velocity scales with the square root of the amplitude. | The maximum velocity has a linear relationship with amplitude for small amplitudes in compressible flows, transitioning  | The maximum velocity has a linear relationship with amplitude for small amplitudes in compressible flows, transitioning  |
| 89 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | The normalized least mean square (NLMS) algorithm. | Normalized least mean square (NLMS) algorithm | Normalized least mean square (NLMS) algorithm |
| 90 | `multifieldqa_en_e` | `token_f1` | 0.478 | 0.431 | -0.047 | The momentum space curl of the interlayer Berry connection polarizability generates the crossed nonlinear dynamical Hall | The interlayer Berry connection polarizability (BCP) is the band geometric quantity whose momentum-space curl is the ori | The interlayer Berry connection polarizability (BCP) is the band geometric quantity whose momentum-space curl gives rise |
| 91 | `multifieldqa_en_e` | `token_f1` | 0.250 | 0.250 | +0.000 | The first white settlement in McPherson County was Fuller's Ranch, established by Charles O. Fuller. | Fuller's Ranch | Fuller's Ranch |
| 92 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | McPherson. | McPherson | McPherson |
| 93 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | McPherson County is located in the U.S. state of Kansas. | McPherson County is located in the U.S. state of Kansas. | McPherson County is located in the U.S. state of Kansas. |
| 94 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Jacob C. Landau. | Jacob C. Landau | Jacob C. Landau |
| 95 | `multifieldqa_en_e` | `token_f1` | 1.000 | 0.667 | -0.333 | BERT, RoBERTa, ELECTRA, GPT-2, and XLM-RoBERTa. | BERT, RoBERTa, ELECTRA, GPT-2, and XLM-RoBERTa. | BERT, RoBERTa, ELECTRA, GPT-2, XLM-RoBERTa, Spanish BERT, Portuguese BERT |
| 96 | `multifieldqa_en_e` | `token_f1` | 0.737 | 0.737 | +0.000 | The club's headquarters are located on Jivani Street 2 of the Malatia-Sebastia District, Yerevan. | Jivani Street 2 of the Malatia-Sebastia District, Yerevan | Jivani Street 2 of the Malatia-Sebastia District, Yerevan |
| 97 | `multifieldqa_en_e` | `token_f1` | 0.471 | 0.400 | -0.071 | Margaret Way was born in Brisbane and died in Cleveland, Queensland, Australia. | Brisbane, Queensland, Australia; Cleveland, Queensland | Brisbane; Cleveland, Queensland |
| 98 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | FC Banants. | FC Banants | FC Banants |
| 99 | `multifieldqa_en_e` | `token_f1` | 0.000 | 0.000 | +0.000 | In the 2013-2014 season. | 2013–14 | 2013–2014 |
| 100 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | 30,223. | 30,223 | 30,223 |
| 101 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li |
| 102 | `qasper_e` | `token_f1` | 0.600 | 0.600 | +0.000 | the series of posts that trigger an intervention | The latent context used to predict instructor intervention is the series of posts that trigger an intervention. | The latent context used to predict instructor intervention is the series of posts that trigger an intervention. |
| 103 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | F-score, Kappa; Unanswerable | F-score and Kappa statistics | F-score and Kappa statistics |
| 104 | `qasper_e` | `token_f1` | 0.200 | 0.214 | +0.014 | (i) models that use plain stacked LSTMs, (ii) models with different INLINEFORM0, (iii) models without INLINEFORM1, (iv)  | The baselines were plain stacked LSTMs. | Plain stacked LSTMs. |
| 105 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Yes; Unanswerable | No | No |
| 106 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | No | No | No |
| 107 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Yes; No | No | No |
| 108 | `qasper_e` | `token_f1` | 0.645 | 0.538 | -0.107 | SemEval-2016 Challenge Task 5 BIBREF27 , BIBREF28;  English reviews ,  restaurant reviews from four different languages  | The evaluation used restaurant reviews from four languages (Spanish, Turkish, Dutch, Russian) from SemEval-2016 Challeng | Four restaurant review datasets from SemEval-2016 Challenge Task 5: Spanish, Turkish, Dutch, and Russian. |
| 109 | `qasper_e` | `token_f1` | 0.412 | 0.400 | -0.012 | 7.36% on accuracy and 9.69% on F1 score; it has 0.024 improvement in accuracy comparing to ELMO Only and  0.006 improvem | The article reports that adding topic information (Topic Only setting) improved accuracy by 7.36% and F1 score by 9.69%  | The article reports that adding topic information (Topic Only setting) improved accuracy by 7.36% and F1 score by 9.69%  |
| 110 | `qasper_e` | `token_f1` | 0.160 | 0.160 | +0.000 | They use text transcription.; both | They use both: they use the released transcripts of the IEMOCAP dataset and also process the audio data using an ASR sys | They use both: they use the released transcripts of the IEMOCAP dataset and also process the audio data using an ASR sys |
| 111 | `qasper_e` | `token_f1` | 0.857 | 0.857 | +0.000 | CLUTO, Carrot2 Lingo; simple clustering algorithm which uses the cosine similarity between word embeddings | CLUTO and Carrot2 Lingo | CLUTO and Carrot2 Lingo |
| 112 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Bert + Unanswerable; CNN, BERT | BERT | BERT |
| 113 | `qasper_e` | `token_f1` | 0.200 | 0.200 | +0.000 | pivoting, pivoting$_{\rm m}$; firstly translates a source language into the pivot language which is later translated to  | Pivot-based baselines are the pivoting and pivot-synthetic methods. | Pivot-based baselines are the pivoting and pivot-synthetic methods. |
| 114 | `qasper_e` | `token_f1` | 0.364 | 0.400 | +0.036 | Friends, EmotionPush; EmotionLines BIBREF6 | EmotionLines dataset, which consists of the Friends and EmotionPush subsets. | EmotionLines dataset, consisting of Friends and EmotionPush subsets. |
| 115 | `qasper_e` | `token_f1` | 0.135 | 0.268 | +0.133 | three experimental setups with different numbers of speakers in the evaluation set, three experimental setups with diffe | Several evaluation protocols for each part of the database, allowing researchers to investigate performance in various s | Several evaluation protocols are provided for each part of the database, including experimental setups with different nu |
| 116 | `qasper_e` | `token_f1` | 0.286 | 0.293 | +0.008 | pays attentions to adjacent characters and casts a localness relationship between the characters as a fixed Gaussian wei | Gaussian-masked directional multi-head attention works by combining a Gaussian weight matrix, which encodes localness ba | Gaussian-masked directional multi-head attention combines Gaussian weights based on character distance with directional  |
| 117 | `qasper_e` | `token_f1` | 0.077 | 0.077 | +0.000 | No data. Pretrained model is used. | Monolingual data (e.g., Wikipedias) and, for some experiments, parallel corpora (e.g., United Nations Parallel Corpus, I | Monolingual data (e.g., Wikipedias) and, for some experiments, parallel corpora (e.g., United Nations Parallel Corpus, I |
| 118 | `qasper_e` | `token_f1` | 0.140 | 0.080 | -0.060 | For certain POS tags, e.g. VERB, PRON.; most word alignments only involve one or a few words, attention can be distribut | Attention is different from alignment in cases involving verbs, pronouns, and particles, where attention is more distrib | Attention is different from alignment in cases involving verbs, where attention captures information beyond translationa |
| 119 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | RNN;  Recurrent Neural Network (RNN) | Recurrent Neural Network (RNN) | Recurrent Neural Network (RNN) |
| 120 | `qasper_e` | `token_f1` | 0.500 | 0.500 | +0.000 | CNN modelBIBREF0, Stanford CRF modelBIBREF21; Bam et al. SVM, Ma and Hovy w/glove, Lample et al. w/fastText, Lample et a | Stanford CRF model | Stanford CRF model |
| 121 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Unanswerable | unanswerable | unanswerable |
| 122 | `qasper_e` | `token_f1` | 0.200 | 0.200 | +0.000 | about 500; Unanswerable | Around 500 different workers were involved in the annotation. | Around 500 different workers were involved in the annotation. |
| 123 | `qasper_e` | `token_f1` | 0.818 | 0.818 | +0.000 | linear SVM, bidirectional Long Short-Term-Memory (BiLSTM), Convolutional Neural Network (CNN); linear SVM, bidirectional | Linear SVM, bidirectional Long Short-Term Memory (BiLSTM), and Convolutional Neural Network (CNN) | Linear SVM, bidirectional Long Short-Term Memory (BiLSTM), and Convolutional Neural Network (CNN). |
| 124 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | BiLSTM, BiLSTM-CNN, BiLSTM-CRF, BiLSTM-CNN-CRF; BiLSTMBIBREF14, BiLSTM+CNNBIBREF20, BiLSTM+CRFBIBREF1, BiLSTM+CNN+CRFBIB | BiLSTM, BiLSTM+CNN, BiLSTM+CRF, BiLSTM+CNN+CRF, CNN, and Stanford CRF | BiLSTM, BiLSTM+CNN, BiLSTM+CRF, BiLSTM+CNN+CRF, CNN, and Stanford CRF |
| 125 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Zero Resource Toolkit (ZRTools) BIBREF7 | Through unsupervised term discovery (UTD) for word-like units and acoustic unit discovery (AUD) using variational Bayesi | Through unsupervised term discovery (UTD) for word-like units and acoustic unit discovery (AUD) for phoneme-like units. |
| 126 | `hotpotqa_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Yanzhou | Yanzhou District | Yanzhou District |
| 127 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | McLaren Vale | McLaren Vale | McLaren Vale |
| 128 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Oberschleißheim | Munich | Munich |
| 129 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | yes | Yes | Yes |
| 130 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Sinclair Hill | Robert Z. Leonard | Robert Z. Leonard |
| 131 | `hotpotqa_e` | `token_f1` | 0.500 | 0.500 | +0.000 | Kew, Melbourne, Australia | Kew | Kew |
| 132 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Herbert Ross | Herbert Ross | Herbert Ross |
| 133 | `hotpotqa_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Emilio Ángel Sánchez Vicario | Emilio Sánchez | Emilio Sánchez |
| 134 | `hotpotqa_e` | `token_f1` | 0.800 | 0.800 | +0.000 | Oldham County, Kentucky | Oldham County | Oldham County |
| 135 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | very little | Very little | Very little |
| 136 | `hotpotqa_e` | `token_f1` | 0.500 | 0.500 | +0.000 | the best known globetrotters | globetrotters | globetrotters |
| 137 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | North Sea | North Sea | North Sea |
| 138 | `hotpotqa_e` | `token_f1` | 0.250 | 0.250 | +0.000 | a genus of flowering plant in the Lardizabalaceae family | Lardizabalaceae | Lardizabalaceae |
| 139 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Gareth Huw Evans | Pierre Chenal | Pierre Chenal |
| 140 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | European route E 22 | E22 | E22 |
| 141 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Mulberry | Mulberry | Mulberry |
| 142 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | no | No | No |
| 143 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | University of Missouri | University of Missouri | University of Missouri |
| 144 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | WANH | None of the radio stations listed serve the Lakes Region (which comprises all of Belknap County, among others). The radi | WVNH |
| 145 | `hotpotqa_e` | `token_f1` | 1.000 | 0.500 | -0.500 | Orange County | Orange County | Bay County |
| 146 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Crocosmia | Crocosmia | Crocosmia |
| 147 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | William Cavendish, 7th Duke of Devonshire | William Cavendish, 7th Duke of Devonshire | William Cavendish, 7th Duke of Devonshire |
| 148 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Gambaga | Gambaga | Gambaga |
| 149 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | My Boss, My Hero | My Boss, My Hero | My Boss, My Hero |
| 150 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | the Netherlands | Dutch | Dutch |

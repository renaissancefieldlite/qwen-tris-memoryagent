# Qwen Tris LongBench Public Slice - qwen_tris_longbench_public_slice_20260701T143102Z

- Benchmark: `LongBench public data.zip`
- Provider: `qwen-cloud`
- Model: `qwen-plus`
- Items: `150`
- Condition A mean: `0.571`
- Condition B mean: `0.676`
- Delta: `+0.105`

## Boundary

Public LongBench smoke slice. This is not a full LongBench leaderboard claim; it is a source-backed answer-key accuracy receipt that can scale to larger slices.

## Conditions

- Condition A: baseline Qwen prompt-only answer discipline
- Condition B: Qwen Tris stable-state answer discipline

## Family Totals

- `passage_retrieval_en_e`: n=25 A=1.000 B=1.000 delta=+0.000
- `passage_count_e`: n=25 A=0.320 B=0.440 delta=+0.120
- `trec_e`: n=25 A=0.320 B=0.720 delta=+0.400
- `multifieldqa_en_e`: n=25 A=0.627 B=0.641 delta=+0.014
- `qasper_e`: n=25 A=0.502 B=0.599 delta=+0.097
- `hotpotqa_e`: n=25 A=0.655 B=0.655 delta=+0.000

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
| 27 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 10 | 7 | 6 |
| 28 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 4 | 3 | 3 |
| 29 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 6 | 4 | 4 |
| 30 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 12 | Let's go through the paragraphs and identify duplicates.  We have 18 paragraphs. We need to find how many are unique — i | 6 |
| 31 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 8 | 4 | 3 |
| 32 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 9 | 7 | 7 |
| 33 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 7 | 7 | 7 |
| 34 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 35 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 9 | 5 | 5 |
| 36 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 7 | 7 | 7 |
| 37 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 7 | 5 | 4 |
| 38 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 6 | 5 | 5 |
| 39 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 40 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 6 | 6 | 6 |
| 41 | `passage_count_e` | `numeric_accuracy` | 0.000 | 1.000 | +1.000 | 2 | 3 | 2 |
| 42 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 4 | 3 | 3 |
| 43 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 44 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 8 | 6 | 7 |
| 45 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 4 | 4 | 4 |
| 46 | `passage_count_e` | `numeric_accuracy` | 0.000 | 1.000 | +1.000 | 9 | 8 | 9 |
| 47 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 48 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 7 | 4 | 6 |
| 49 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 10 | 6 | 5 |
| 50 | `passage_count_e` | `numeric_accuracy` | 0.000 | 1.000 | +1.000 | 3 | 4 | 3 |
| 51 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 52 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Date | Type: Date | Date |
| 53 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Number of something | Type: Number of something | Number of something |
| 54 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Animal | Definition of something | Definition of something |
| 55 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | City | Type: City | City |
| 56 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Individual | Type: Individual | Individual |
| 57 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Equivalent term | Type: Equivalent term | Definition of something |
| 58 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Element and substance | Type: Other entity | Food |
| 59 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Description of something | Type: Description of something | Description of something |
| 60 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 61 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Date | Date | Date |
| 62 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Definition of something | Type: Definition of something | Definition of something |
| 63 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Other location | Type: Other location | Other location |
| 64 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Expression abbreviated | Expression abbreviated | Expression abbreviated |
| 65 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Date | Type: Date | Date |
| 66 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Other location | Type: Other location | Other location |
| 67 | `trec_e` | `accuracy` | 0.000 | 1.000 | +1.000 | Definition of something | Type: Definition of something | Definition of something |
| 68 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Date | Date | Date |
| 69 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Country | Country | Country |
| 70 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Manner of an action | Type: Other entity | Other entity |
| 71 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Other entity | Type: Invention, book and other creative piece | Invention, book and other creative piece |
| 72 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Individual | Individual | Individual |
| 73 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Element and substance | Type: Color | Color |
| 74 | `trec_e` | `accuracy` | 0.000 | 0.000 | +0.000 | Other location | Planet | Other entity |
| 75 | `trec_e` | `accuracy` | 1.000 | 1.000 | +0.000 | Definition of something | Definition of something | Definition of something |
| 76 | `multifieldqa_en_e` | `token_f1` | 0.600 | 0.903 | +0.303 | Exposure to sunlight or strong light may cause permanent yellow spot damage on the screen. | Permanent yellow spot damage on the screen. | Exposure to direct sunlight or other strong light sources may cause permanent yellow spot damage on the screen. |
| 77 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Vice Admiral. | Vice Admiral | Vice Admiral |
| 78 | `multifieldqa_en_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Sir Richard. | None of the text mentions Ralph Rokebye having a brother. | Ralph Rokebye's brother was William Rokeby. |
| 79 | `multifieldqa_en_e` | `token_f1` | 0.750 | 0.750 | +0.000 | South West Ultras fan club. | South West Ultras | South West Ultras |
| 80 | `multifieldqa_en_e` | `token_f1` | 0.222 | 0.222 | +0.000 | It is recommended to have at least a 2x2 meter space for using the VR headset. | At least 2×2 meters | at least 2×2 meters |
| 81 | `multifieldqa_en_e` | `token_f1` | 0.182 | 0.167 | -0.015 | It depends on the value of x, either 0 or (6x^2cos(x^2)+sin(x^2))/(3(x^2)^(1/3)). | $$ f'\left(x\right)  =  \begin{cases}  \frac{6x^2\cos{\left(x^2\right)}+\sin{\left(x^2\right)}}{3\sqrt[3]{x^2}}, & \mbox | \begin{equation*} f'\left(x\right)  =  \begin{cases}  \frac{6x^2\cos{\left(x^2\right)}+\sin{\left(x^2\right)}}{3\sqrt[3] |
| 82 | `multifieldqa_en_e` | `token_f1` | 0.737 | 0.737 | +0.000 | In 2009, Brooksley Born received the John F. Kennedy Profiles in Courage Award. | John F. Kennedy Profiles in Courage Award | John F. Kennedy Profiles in Courage Award |
| 83 | `multifieldqa_en_e` | `token_f1` | 0.182 | 0.364 | +0.182 | Margaret Way started self-publishing her books as e-books in 2013. | 2013 | Beginning in 2013, Margaret began to self-publish, releasing her first "e-book" mid-July. |
| 84 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Long Term Capital Management (LTCM). | Long Term Capital Management (LTCM) | Long Term Capital Management (LTCM) |
| 85 | `multifieldqa_en_e` | `token_f1` | 0.000 | 0.286 | +0.286 | It is well described by the Gaussian theory. | $m \sim t^{1/2}$ | The dynamical behaviour of the anisotropic order parameter $m$ following a quench to the critical point is well describe |
| 86 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | June 1, 1999. | June 1, 1999 | June 1, 1999 |
| 87 | `multifieldqa_en_e` | `token_f1` | 0.800 | 1.000 | +0.200 | 23 September. | 23 September 2017 | 23 September |
| 88 | `multifieldqa_en_e` | `token_f1` | 0.316 | 0.152 | -0.164 | The maximum velocity scales with the square root of the amplitude. | The maximum velocity has a linear relationship with amplitude for small amplitudes in compressible flows, and a square r | The maximum velocity has a linear dependence on amplitude for compressible flows at small amplitudes ($\|\triangle n/n_0\| |
| 89 | `multifieldqa_en_e` | `token_f1` | 1.000 | 0.857 | -0.143 | The normalized least mean square (NLMS) algorithm. | Normalized least mean square (NLMS) algorithm | The normalized least mean square (NLMS) algorithm is engaged. |
| 90 | `multifieldqa_en_e` | `token_f1` | 0.435 | 0.261 | -0.174 | The momentum space curl of the interlayer Berry connection polarizability generates the crossed nonlinear dynamical Hall | The interlayer Berry connection polarizability (BCP) is the fundamental band geometric quantity whose momentum-space cur | The interlayer Berry connection polarizability (BCP) is significant because its momentum-space curl constitutes the band |
| 91 | `multifieldqa_en_e` | `token_f1` | 0.250 | 0.250 | +0.000 | The first white settlement in McPherson County was Fuller's Ranch, established by Charles O. Fuller. | Fuller's Ranch | Fuller's Ranch |
| 92 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | McPherson. | McPherson | McPherson |
| 93 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | McPherson County is located in the U.S. state of Kansas. | McPherson County is located in the U.S. state of Kansas. | McPherson County is located in the U.S. state of Kansas. |
| 94 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Jacob C. Landau. | Jacob C. Landau | Jacob C. Landau |
| 95 | `multifieldqa_en_e` | `token_f1` | 1.000 | 0.667 | -0.333 | BERT, RoBERTa, ELECTRA, GPT-2, and XLM-RoBERTa. | BERT, RoBERTa, ELECTRA, GPT-2, and XLM-RoBERTa. | BERT, RoBERTa, ELECTRA, GPT-2, XLM-RoBERTa, Spanish BERT, Portuguese BERT |
| 96 | `multifieldqa_en_e` | `token_f1` | 0.737 | 0.917 | +0.180 | The club's headquarters are located on Jivani Street 2 of the Malatia-Sebastia District, Yerevan. | Jivani Street 2 of the Malatia-Sebastia District, Yerevan | The club headquarters are located on Jivani Street 2 of the Malatia-Sebastia District, Yerevan. |
| 97 | `multifieldqa_en_e` | `token_f1` | 0.471 | 0.500 | +0.029 | Margaret Way was born in Brisbane and died in Cleveland, Queensland, Australia. | Brisbane, Queensland, Australia; Cleveland, Queensland | Brisbane and Cleveland, Queensland |
| 98 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | FC Banants. | FC Banants | FC Banants |
| 99 | `multifieldqa_en_e` | `token_f1` | 0.000 | 0.000 | +0.000 | In the 2013-2014 season. | 2013–14 | 2013–2014 |
| 100 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | 30,223. | 30,223 | 30,223 |
| 101 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li |
| 102 | `qasper_e` | `token_f1` | 0.600 | 0.800 | +0.200 | the series of posts that trigger an intervention | The latent context used to predict instructor intervention is the series of posts that trigger an intervention. | latent context is the series of posts that trigger an intervention |
| 103 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | F-score, Kappa; Unanswerable | F-score and Kappa statistics | F-score and Kappa statistics |
| 104 | `qasper_e` | `token_f1` | 0.200 | 0.214 | +0.014 | (i) models that use plain stacked LSTMs, (ii) models with different INLINEFORM0, (iii) models without INLINEFORM1, (iv)  | The baselines were plain stacked LSTMs. | plain stacked LSTMs |
| 105 | `qasper_e` | `token_f1` | 0.000 | 1.000 | +1.000 | Yes; Unanswerable | No | unanswerable |
| 106 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | No | No | No |
| 107 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Yes; No | No | no |
| 108 | `qasper_e` | `token_f1` | 0.645 | 0.500 | -0.145 | SemEval-2016 Challenge Task 5 BIBREF27 , BIBREF28;  English reviews ,  restaurant reviews from four different languages  | The evaluation used restaurant reviews from four languages (Spanish, Turkish, Dutch, Russian) from SemEval-2016 Challeng | SemEval-2016 Challenge Task 5 restaurant reviews in Spanish, Turkish, Dutch, and Russian |
| 109 | `qasper_e` | `token_f1` | 0.400 | 1.000 | +0.600 | 7.36% on accuracy and 9.69% on F1 score; it has 0.024 improvement in accuracy comparing to ELMO Only and  0.006 improvem | The article reports that adding topic information (Topic Only setting) improved accuracy by 7.36% and F1 score by 9.69%  | 7.36% on accuracy and 9.69% on F1 score |
| 110 | `qasper_e` | `token_f1` | 0.148 | 0.222 | +0.074 | They use text transcription.; both | They use both: released transcripts of the IEMOCAP dataset and also process audio data using an ASR system (Google Cloud | They use both: released transcripts of the IEMOCAP dataset and ASR-processed transcripts derived from the audio. |
| 111 | `qasper_e` | `token_f1` | 0.857 | 1.000 | +0.143 | CLUTO, Carrot2 Lingo; simple clustering algorithm which uses the cosine similarity between word embeddings | CLUTO and Carrot2 Lingo | CLUTO, Carrot2 Lingo |
| 112 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Bert + Unanswerable; CNN, BERT | BERT | BERT |
| 113 | `qasper_e` | `token_f1` | 0.200 | 0.333 | +0.133 | pivoting, pivoting$_{\rm m}$; firstly translates a source language into the pivot language which is later translated to  | Pivot-based baselines are the pivoting and pivot-synthetic methods. | pivoting and pivot-synthetic |
| 114 | `qasper_e` | `token_f1` | 0.364 | 0.800 | +0.436 | Friends, EmotionPush; EmotionLines BIBREF6 | EmotionLines dataset, which consists of the Friends and EmotionPush subsets. | Friends and EmotionPush |
| 115 | `qasper_e` | `token_f1` | 0.135 | 0.046 | -0.089 | three experimental setups with different numbers of speakers in the evaluation set, three experimental setups with diffe | Several evaluation protocols for each part of the database, allowing researchers to investigate performance in various s | Several evaluation protocols for each part of the database. |
| 116 | `qasper_e` | `token_f1` | 0.286 | 0.274 | -0.012 | pays attentions to adjacent characters and casts a localness relationship between the characters as a fixed Gaussian wei | Gaussian-masked directional multi-head attention works by combining a Gaussian weight matrix, which encodes localness ba | It combines Gaussian weights based on character distance with directional triangular masks and multi-head attention to e |
| 117 | `qasper_e` | `token_f1` | 0.077 | 0.083 | +0.006 | No data. Pretrained model is used. | Monolingual data (e.g., Wikipedias) and, for some experiments, parallel corpora (e.g., United Nations Parallel Corpus, I | Monolingual data (e.g., Wikipedias) and, optionally, parallel data (e.g., United Nations Parallel Corpus, IIT Bombay cor |
| 118 | `qasper_e` | `token_f1` | 0.179 | 0.176 | -0.002 | For certain POS tags, e.g. VERB, PRON.; most word alignments only involve one or a few words, attention can be distribut | Attention is different from alignment in cases involving verbs, pronouns, and particles, where attention is more distrib | In cases involving verbs, pronouns, and particles, where attention is more distributed and captures context beyond direc |
| 119 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | RNN;  Recurrent Neural Network (RNN) | Recurrent Neural Network (RNN) | RNN |
| 120 | `qasper_e` | `token_f1` | 0.500 | 0.500 | +0.000 | CNN modelBIBREF0, Stanford CRF modelBIBREF21; Bam et al. SVM, Ma and Hovy w/glove, Lample et al. w/fastText, Lample et a | Stanford CRF model | Stanford CRF model |
| 121 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Unanswerable | unanswerable | unanswerable |
| 122 | `qasper_e` | `token_f1` | 0.200 | 0.500 | +0.300 | about 500; Unanswerable | Around 500 different workers were involved in the annotation. | Around 500 |
| 123 | `qasper_e` | `token_f1` | 0.769 | 0.462 | -0.308 | linear SVM, bidirectional Long Short-Term-Memory (BiLSTM), Convolutional Neural Network (CNN); linear SVM, bidirectional | Linear SVM, bidirectional Long Short-Term-Memory (BiLSTM), and Convolutional Neural Network (CNN) models are used in the | SVM, BiLSTM, CNN |
| 124 | `qasper_e` | `token_f1` | 0.667 | 0.727 | +0.061 | BiLSTM, BiLSTM-CNN, BiLSTM-CRF, BiLSTM-CNN-CRF; BiLSTMBIBREF14, BiLSTM+CNNBIBREF20, BiLSTM+CRFBIBREF1, BiLSTM+CNN+CRFBIB | BiLSTM, BiLSTM+CNN, BiLSTM+CRF, BiLSTM+CNN+CRF, CNN, and Stanford CRF | BiLSTM, BiLSTM+CNN, BiLSTM+CRF, BiLSTM+CNN+CRF, CNN, Stanford CRF |
| 125 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Zero Resource Toolkit (ZRTools) BIBREF7 | Through unsupervised term discovery (UTD) and acoustic unit discovery (AUD). | Through unsupervised term discovery (UTD) and acoustic unit discovery (AUD). |
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
| 144 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | WANH | None of the radio stations listed serve the Lakes Region (which comprises all of Belknap County, among others). | WVNH |
| 145 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Orange County | Orange County | Orange County |
| 146 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Crocosmia | Crocosmia | Crocosmia |
| 147 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | William Cavendish, 7th Duke of Devonshire | William Cavendish, 7th Duke of Devonshire | William Cavendish, 7th Duke of Devonshire |
| 148 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Gambaga | Gambaga | Gambaga |
| 149 | `hotpotqa_e` | `token_f1` | 1.000 | 1.000 | +0.000 | My Boss, My Hero | My Boss, My Hero | My Boss, My Hero |
| 150 | `hotpotqa_e` | `token_f1` | 0.000 | 0.000 | +0.000 | the Netherlands | Dutch | Dutch |

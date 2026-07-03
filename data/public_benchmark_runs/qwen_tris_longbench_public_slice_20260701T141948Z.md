# Qwen Tris LongBench Public Slice - qwen_tris_longbench_public_slice_20260701T141948Z

- Benchmark: `LongBench public data.zip`
- Provider: `qwen-cloud`
- Model: `qwen-plus`
- Items: `25`
- Condition A mean: `0.511`
- Condition B mean: `0.560`
- Delta: `+0.049`

## Boundary

Public LongBench smoke slice. This is not a full LongBench leaderboard claim; it is a source-backed answer-key accuracy receipt that can scale to larger slices.

## Conditions

- Condition A: baseline Qwen prompt-only answer discipline
- Condition B: Qwen Tris stable-state answer discipline

## Family Totals

- `qasper_e`: n=25 A=0.511 B=0.560 delta=+0.049

## Rows

| # | Dataset | Metric | A | B | Delta | Gold | A prediction | B prediction |
|---:|---|---|---:|---:|---:|---|---|---|
| 1 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li |
| 2 | `qasper_e` | `token_f1` | 0.600 | 0.800 | +0.200 | the series of posts that trigger an intervention | The latent context used to predict instructor intervention is the series of posts that trigger an intervention. | latent context is the series of posts that trigger an intervention |
| 3 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | F-score, Kappa; Unanswerable | F-score and Kappa statistics | F-score and Kappa statistics |
| 4 | `qasper_e` | `token_f1` | 0.200 | 0.214 | +0.014 | (i) models that use plain stacked LSTMs, (ii) models with different INLINEFORM0, (iii) models without INLINEFORM1, (iv)  | The baselines were plain stacked LSTMs. | plain stacked LSTMs |
| 5 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Yes; Unanswerable | No | No |
| 6 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | No | No | No |
| 7 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Yes; No | No | no |
| 8 | `qasper_e` | `token_f1` | 0.645 | 0.480 | -0.165 | SemEval-2016 Challenge Task 5 BIBREF27 , BIBREF28;  English reviews ,  restaurant reviews from four different languages  | The evaluation used restaurant reviews from four languages (Spanish, Turkish, Dutch, Russian) from SemEval-2016 Challeng | SemEval-2016 Challenge Task 5 restaurant reviews datasets in Spanish, Turkish, Dutch, and Russian |
| 9 | `qasper_e` | `token_f1` | 0.412 | 1.000 | +0.588 | 7.36% on accuracy and 9.69% on F1 score; it has 0.024 improvement in accuracy comparing to ELMO Only and  0.006 improvem | The article reports that adding topic information (Topic Only setting) improved accuracy by 7.36% and F1 score by 9.69%  | 7.36% on accuracy and 9.69% on F1 score |
| 10 | `qasper_e` | `token_f1` | 0.174 | 0.222 | +0.048 | They use text transcription.; both | They use both: released transcripts of the IEMOCAP dataset and also process audio data using an ASR system to retrieve t | They use both: released transcripts of the IEMOCAP dataset and ASR-processed transcripts derived from the audio. |
| 11 | `qasper_e` | `token_f1` | 0.857 | 1.000 | +0.143 | CLUTO, Carrot2 Lingo; simple clustering algorithm which uses the cosine similarity between word embeddings | CLUTO and Carrot2 Lingo | CLUTO, Carrot2 Lingo |
| 12 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Bert + Unanswerable; CNN, BERT | BERT | BERT |
| 13 | `qasper_e` | `token_f1` | 0.200 | 0.333 | +0.133 | pivoting, pivoting$_{\rm m}$; firstly translates a source language into the pivot language which is later translated to  | Pivot-based baselines are the pivoting and pivot-synthetic methods. | pivoting and pivot-synthetic |
| 14 | `qasper_e` | `token_f1` | 0.364 | 0.800 | +0.436 | Friends, EmotionPush; EmotionLines BIBREF6 | EmotionLines dataset, which consists of the Friends and EmotionPush subsets. | Friends and EmotionPush |
| 15 | `qasper_e` | `token_f1` | 0.135 | 0.046 | -0.089 | three experimental setups with different numbers of speakers in the evaluation set, three experimental setups with diffe | Several evaluation protocols for each part of the database, allowing researchers to investigate performance in various s | Several evaluation protocols for each part of the database. |
| 16 | `qasper_e` | `token_f1` | 0.280 | 0.274 | -0.006 | pays attentions to adjacent characters and casts a localness relationship between the characters as a fixed Gaussian wei | Gaussian-masked directional multi-head attention works by combining a Gaussian weight matrix, which encodes localness re | It combines Gaussian weights based on character distance with directional triangular masks and multi-head attention to e |
| 17 | `qasper_e` | `token_f1` | 0.077 | 0.077 | +0.000 | No data. Pretrained model is used. | Monolingual data (e.g., Wikipedias) and, for some experiments, parallel corpora (e.g., United Nations Parallel Corpus, I | Monolingual data (e.g., Wikipedias) and, for some experiments, parallel corpora (e.g., United Nations Parallel Corpus, I |
| 18 | `qasper_e` | `token_f1` | 0.233 | 0.235 | +0.003 | For certain POS tags, e.g. VERB, PRON.; most word alignments only involve one or a few words, attention can be distribut | Attention is different from alignment in cases involving verbs, pronouns, and particles, where attention is more distrib | In cases involving verbs, pronouns, and particles, where attention is more distributed and captures context words beyond |
| 19 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | RNN;  Recurrent Neural Network (RNN) | Recurrent Neural Network (RNN) | RNN |
| 20 | `qasper_e` | `token_f1` | 0.500 | 0.500 | +0.000 | CNN modelBIBREF0, Stanford CRF modelBIBREF21; Bam et al. SVM, Ma and Hovy w/glove, Lample et al. w/fastText, Lample et a | Stanford CRF model | Stanford CRF model |
| 21 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Unanswerable | unanswerable | unanswerable |
| 22 | `qasper_e` | `token_f1` | 0.333 | 0.500 | +0.167 | about 500; Unanswerable | Around 500 different workers. | Around 500 |
| 23 | `qasper_e` | `token_f1` | 0.769 | 0.462 | -0.308 | linear SVM, bidirectional Long Short-Term-Memory (BiLSTM), Convolutional Neural Network (CNN); linear SVM, bidirectional | Linear SVM, bidirectional Long Short-Term-Memory (BiLSTM), and Convolutional Neural Network (CNN) models are used in the | SVM, BiLSTM, CNN |
| 24 | `qasper_e` | `token_f1` | 0.667 | 0.727 | +0.061 | BiLSTM, BiLSTM-CNN, BiLSTM-CRF, BiLSTM-CNN-CRF; BiLSTMBIBREF14, BiLSTM+CNNBIBREF20, BiLSTM+CRFBIBREF1, BiLSTM+CNN+CRFBIB | BiLSTM, BiLSTM+CNN, BiLSTM+CRF, BiLSTM+CNN+CRF, CNN, and Stanford CRF | BiLSTM, BiLSTM+CNN, BiLSTM+CRF, BiLSTM+CNN+CRF, CNN, Stanford CRF |
| 25 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Zero Resource Toolkit (ZRTools) BIBREF7 | Through unsupervised term discovery (UTD) for word-like units and acoustic unit discovery (AUD) for phoneme-like units. | Through unsupervised term discovery (UTD) and acoustic unit discovery (AUD). |

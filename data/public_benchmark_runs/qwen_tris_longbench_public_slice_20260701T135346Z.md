# Qwen Tris LongBench Public Slice - qwen_tris_longbench_public_slice_20260701T135346Z

- Benchmark: `LongBench public data.zip`
- Provider: `qwen-cloud`
- Model: `qwen-plus`
- Items: `50`
- Condition A mean: `0.394`
- Condition B mean: `0.436`
- Delta: `+0.043`

## Boundary

Public LongBench smoke slice. This is not a full LongBench leaderboard claim; it is a source-backed answer-key accuracy receipt that can scale to larger slices.

## Conditions

- Condition A: baseline Qwen prompt-only answer discipline
- Condition B: Qwen Tris stable-state answer discipline

## Family Totals

- `passage_count_e`: n=25 A=0.280 B=0.360 delta=+0.080
- `qasper_e`: n=25 A=0.507 B=0.513 delta=+0.006

## Rows

| # | Dataset | Metric | A | B | Delta | Gold | A prediction | B prediction |
|---:|---|---|---:|---:|---:|---|---|---|
| 1 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 6 | 5 | 5 |
| 2 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 10 | 7 | 6 |
| 3 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 4 | 3 | 3 |
| 4 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 6 | 5 | 4 |
| 5 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 12 | Let's go through the 18 paragraphs and identify duplicates.  We need to compare each paragraph carefully for exact textu | 7 |
| 6 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 8 | 4 | 4 |
| 7 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 9 | 7 | 7 |
| 8 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 7 | 7 | 7 |
| 9 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 10 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 9 | We are given 11 paragraphs and asked to count how many **unique** (non-duplicate) paragraphs there are.  Let’s compare t | 5 |
| 11 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 7 | 7 | 7 |
| 12 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 7 | 5 | 4 |
| 13 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 6 | 5 | 4 |
| 14 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 15 | `passage_count_e` | `numeric_accuracy` | 0.000 | 1.000 | +1.000 | 6 | 5 | 6 |
| 16 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 2 | 3 | 3 |
| 17 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 4 | 3 | 3 |
| 18 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 2 | 2 | 2 |
| 19 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 8 | 6 | 7 |
| 20 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 4 | 4 | 4 |
| 21 | `passage_count_e` | `numeric_accuracy` | 0.000 | 1.000 | +1.000 | 9 | 7 | 9 |
| 22 | `passage_count_e` | `numeric_accuracy` | 1.000 | 1.000 | +0.000 | 3 | 3 | 3 |
| 23 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 7 | 5 | 6 |
| 24 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 10 | 6 | 5 |
| 25 | `passage_count_e` | `numeric_accuracy` | 0.000 | 0.000 | +0.000 | 3 | 4 | 4 |
| 26 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li |
| 27 | `qasper_e` | `token_f1` | 0.600 | 0.800 | +0.200 | the series of posts that trigger an intervention | The latent context used to predict instructor intervention is the series of posts that trigger an intervention. | The latent context is the series of posts that trigger an intervention. |
| 28 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | F-score, Kappa; Unanswerable | F-score and Kappa statistics | F-score and Kappa statistics |
| 29 | `qasper_e` | `token_f1` | 0.200 | 0.214 | +0.014 | (i) models that use plain stacked LSTMs, (ii) models with different INLINEFORM0, (iii) models without INLINEFORM1, (iv)  | The baselines were plain stacked LSTMs. | plain stacked LSTMs |
| 30 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Yes; Unanswerable | No | No |
| 31 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | No | No | No |
| 32 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Yes; No | No | No |
| 33 | `qasper_e` | `token_f1` | 0.645 | 0.583 | -0.062 | SemEval-2016 Challenge Task 5 BIBREF27 , BIBREF28;  English reviews ,  restaurant reviews from four different languages  | The evaluation used restaurant reviews from four languages (Spanish, Turkish, Dutch, Russian) from SemEval-2016 Challeng | Spanish, Turkish, Dutch, and Russian restaurant reviews from SemEval-2016 Challenge Task 5. |
| 34 | `qasper_e` | `token_f1` | 0.412 | 0.941 | +0.529 | 7.36% on accuracy and 9.69% on F1 score; it has 0.024 improvement in accuracy comparing to ELMO Only and  0.006 improvem | The article reports that adding topic information (Topic Only setting) improved accuracy by 7.36% and F1 score by 9.69%  | 7.36% improvement on accuracy and 9.69% on F1 score |
| 35 | `qasper_e` | `token_f1` | 0.160 | 0.222 | +0.062 | They use text transcription.; both | They use both: they use the released transcripts of the IEMOCAP dataset and also process the audio data using an ASR sys | They use both: released transcripts of the IEMOCAP dataset and ASR-processed transcripts derived from the audio. |
| 36 | `qasper_e` | `token_f1` | 0.857 | 0.857 | +0.000 | CLUTO, Carrot2 Lingo; simple clustering algorithm which uses the cosine similarity between word embeddings | CLUTO and Carrot2 Lingo | CLUTO and Carrot2 Lingo |
| 37 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Bert + Unanswerable; CNN, BERT | BERT | BERT |
| 38 | `qasper_e` | `token_f1` | 0.200 | 0.333 | +0.133 | pivoting, pivoting$_{\rm m}$; firstly translates a source language into the pivot language which is later translated to  | Pivot-based baselines are the pivoting and pivot-synthetic methods. | pivoting and pivot-synthetic |
| 39 | `qasper_e` | `token_f1` | 0.364 | 0.267 | -0.097 | Friends, EmotionPush; EmotionLines BIBREF6 | EmotionLines dataset, which consists of the Friends and EmotionPush subsets. | EmotionLines dataset, consisting of Friends and EmotionPush subsets; Twitter dataset for ChatBERT pre-training. |
| 40 | `qasper_e` | `token_f1` | 0.135 | 0.135 | +0.000 | three experimental setups with different numbers of speakers in the evaluation set, three experimental setups with diffe | Several evaluation protocols for each part of the database, allowing researchers to investigate performance in various s | Several evaluation protocols for each part of the database, allowing researchers to investigate performance in various s |
| 41 | `qasper_e` | `token_f1` | 0.283 | 0.179 | -0.103 | pays attentions to adjacent characters and casts a localness relationship between the characters as a fixed Gaussian wei | Gaussian-masked directional multi-head attention works by combining a Gaussian weight matrix, which encodes localness re | It combines Gaussian weights based on character distance with scaled dot-product attention via Hadamard product, and use |
| 42 | `qasper_e` | `token_f1` | 0.077 | 0.077 | +0.000 | No data. Pretrained model is used. | Monolingual data (e.g., Wikipedias) and, for some experiments, parallel corpora (e.g., United Nations Parallel Corpus, I | Monolingual data (e.g., Wikipedias) and, for some experiments, parallel corpora (e.g., United Nations Parallel Corpus, I |
| 43 | `qasper_e` | `token_f1` | 0.233 | 0.185 | -0.047 | For certain POS tags, e.g. VERB, PRON.; most word alignments only involve one or a few words, attention can be distribut | Attention is different from alignment in cases involving verbs, pronouns, and particles, where attention is more distrib | Attention is different from alignment in cases involving verbs, pronouns, and particles, where attention is more distrib |
| 44 | `qasper_e` | `token_f1` | 1.000 | 0.211 | -0.789 | RNN;  Recurrent Neural Network (RNN) | Recurrent Neural Network (RNN) | RNN with two 2D-convolutional layers, seven bi-directional recurrent layers, and a fully-connected layer with softmax ac |
| 45 | `qasper_e` | `token_f1` | 0.500 | 0.500 | +0.000 | CNN modelBIBREF0, Stanford CRF modelBIBREF21; Bam et al. SVM, Ma and Hovy w/glove, Lample et al. w/fastText, Lample et a | Stanford CRF model | Stanford CRF model |
| 46 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Unanswerable | unanswerable | unanswerable |
| 47 | `qasper_e` | `token_f1` | 0.200 | 0.500 | +0.300 | about 500; Unanswerable | Around 500 different workers were involved in the annotation. | Around 500 |
| 48 | `qasper_e` | `token_f1` | 0.818 | 0.818 | +0.000 | linear SVM, bidirectional Long Short-Term-Memory (BiLSTM), Convolutional Neural Network (CNN); linear SVM, bidirectional | Linear SVM, bidirectional Long Short-Term Memory (BiLSTM), and Convolutional Neural Network (CNN) | Linear SVM, bidirectional Long Short-Term Memory (BiLSTM), and Convolutional Neural Network (CNN). |
| 49 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | BiLSTM, BiLSTM-CNN, BiLSTM-CRF, BiLSTM-CNN-CRF; BiLSTMBIBREF14, BiLSTM+CNNBIBREF20, BiLSTM+CRFBIBREF1, BiLSTM+CNN+CRFBIB | BiLSTM, BiLSTM+CNN, BiLSTM+CRF, BiLSTM+CNN+CRF, CNN, and Stanford CRF | BiLSTM, BiLSTM+CNN, BiLSTM+CRF, BiLSTM+CNN+CRF, CNN, and Stanford CRF |
| 50 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Zero Resource Toolkit (ZRTools) BIBREF7 | Through unsupervised term discovery (UTD) and acoustic unit discovery (AUD) frameworks operating directly on raw speech. | Through unsupervised term discovery (UTD) and acoustic unit discovery (AUD). |

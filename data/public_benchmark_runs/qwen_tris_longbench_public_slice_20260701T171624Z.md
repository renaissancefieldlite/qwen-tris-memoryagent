# Qwen Tris LongBench Public Slice - qwen_tris_longbench_public_slice_20260701T171624Z

- Benchmark: `LongBench public data.zip`
- Provider: `qwen-cloud`
- Model: `qwen-plus`
- Items: `50`
- Skipped provider-blocked rows: `0`
- Condition A mean: `0.483`
- Condition B mean: `0.519`
- Delta: `+0.036`

## Boundary

Public LongBench smoke slice. This is not a full LongBench leaderboard claim; it is a source-backed answer-key accuracy receipt that can scale to larger slices.

## Conditions

- Condition A: baseline Qwen prompt-only answer discipline
- Condition B: Qwen Tris stable-state answer discipline

## Family Totals

- `qasper_e`: n=50 A=0.483 B=0.519 delta=+0.036

## Rows

| # | Dataset | Metric | A | B | Delta | Gold | A prediction | B prediction |
|---:|---|---|---:|---:|---:|---|---|---|
| 1 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | SQuAD; SQuAD | SQuAD dataset | SQuAD dataset |
| 2 | `qasper_e` | `token_f1` | 0.800 | 0.800 | +0.000 | relation classification dataset of the SemEval 2010 task 8; SemEval 2010 task 8 BIBREF8 | SemEval 2010 task 8 dataset | SemEval 2010 task 8 dataset |
| 3 | `qasper_e` | `token_f1` | 0.158 | 0.133 | -0.025 | 2174000000, 989000000; 2174 million tokens for English and 989 million tokens for Russian | The English training corpus was the English Wikipedia dump from February 2017; the Russian training corpus was a concate | English Wikipedia dump from February 2017; Russian Wikipedia dump from December 2018 concatenated with the full Russian  |
| 4 | `qasper_e` | `token_f1` | 0.333 | 0.364 | +0.030 | Spearman correlation values of GM_KL model evaluated on the benchmark word similarity datasets.
Evaluation results of GM | The qualitative experiments involved listing nearest neighbors for query words and their component IDs to demonstrate se | Qualitative experiments involved listing nearest neighbours for query words and component IDs on the SCWS dataset. |
| 5 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Using DSC loss improves the F1 score by +0.58 for MRPC and +0.73 for QQP; +0.58 | +0.58 for MRPC and +0.73 for QQP | +0.58 for MRPC and +0.73 for QQP |
| 6 | `qasper_e` | `token_f1` | 0.167 | 0.136 | -0.031 | reducing the variance of an estimator,  EGL method in BIBREF3 is almost the same as Eq. ( EQREF8 ), except the gradient' | They calculate variance from the model outputs by minimizing the expected variance of the estimator over the test set, u | They calculate variance from the model outputs using the Fisher Information Matrix, where the asymptotic distribution of |
| 7 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | LSTM; LSTM | LSTM | LSTM |
| 8 | `qasper_e` | `token_f1` | 0.071 | 0.138 | +0.067 | These 8 tasks require different competencies and a different level of understanding of the document to be well answered | Natural language questions about hotel reviews that challenge relational reasoning competencies. | Natural language questions about hotel reviews that challenge 8 relational reasoning competencies. |
| 9 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | SVM, No-Answer Baseline (NA) , Word Count Baseline, Human Performance; No-Answer Baseline (NA), Word Count Baseline, Hum | Yes | Yes |
| 10 | `qasper_e` | `token_f1` | 0.667 | 1.000 | +0.333 | 53 documents; 53 documents | 53 | 53 documents |
| 11 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | from Food.com | Food.com | Food.com |
| 12 | `qasper_e` | `token_f1` | 0.396 | 0.392 | -0.004 | We also evaluate all five models on downstream tasks from the VecEval suite BIBREF13 , using only the tasks for which tr | They evaluate their resulting word embeddings using intrinsic evaluations (word similarity and word analogy tasks), down | They evaluate their resulting word embeddings using intrinsic evaluations (word similarity and word analogy tasks), down |
| 13 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Adv. Heart Disease, Adv. Lung Disease, Alcohol Abuse, Chronic Neurologic Dystrophies, Dementia, Depression, Developmenta | unanswerable | unanswerable |
| 14 | `qasper_e` | `token_f1` | 0.947 | 0.947 | +0.000 | 204 tokens; Most texts, however, range roughly from 150 to 250 tokens. | Most texts range roughly from 150 to 250 tokens. | Most texts range roughly from 150 to 250 tokens. |
| 15 | `qasper_e` | `token_f1` | 0.129 | 0.143 | +0.014 | (VVD shop_VV0 II, VVD shopping_VVG II); patterns for generating all types of errors | Patterns over words and part-of-speech (POS) tags, in the form of (incorrect phrase, correct phrase), including up to on | patterns over words and part-of-speech (POS) tags |
| 16 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | No; No | unanswerable | unanswerable |
| 17 | `qasper_e` | `token_f1` | 0.826 | 0.826 | +0.000 | Random Kitchen Sink method uses a kernel function to map data vectors to a space where linear separation is possible.; e | The Random Kitchen Sink (RKS) approach is a method that explicitly maps data vectors to a space where linear separation  | The Random Kitchen Sink (RKS) approach is a method that explicitly maps data vectors to a space where linear separation  |
| 18 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | BIBREF11 , BIBREF26  | BIBREF26 | BIBREF26 |
| 19 | `qasper_e` | `token_f1` | 0.128 | 0.125 | -0.003 | Combining  pattern based and Machine translation approaches gave the best overall F0.5 scores. It was 49.11 for FCE data | The combination of both error generation methods gives an absolute improvement of 4.3% in F0.5 on both datasets. | The combination of both methods gives an absolute improvement of 4.3% in F_0.5, without requiring any additional annotat |
| 20 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | None | unanswerable | unanswerable |
| 21 | `qasper_e` | `token_f1` | 0.750 | 0.667 | -0.083 | Individuals with legal training; Yes | Experts with legal training. | seven experts with legal training |
| 22 | `qasper_e` | `token_f1` | 0.471 | 0.651 | +0.181 | Maximum Entropy, Weighted Finite State Transducer (WFST),  support vector machines (SVM), conditional random fields (CRF | Lexicon-based approaches (e.g., Maximum Matching), machine learning-based methods (e.g., Support Vector Machines, Condit | Weighted Finite State Transducer (WFST), Neural Network, Support Vector Machine (SVM), Conditional Random Fields (CRF),  |
| 23 | `qasper_e` | `token_f1` | 0.467 | 0.467 | +0.000 | Stanford NER, spaCy 2.0 , recurrent model with a CRF top layer; Stanford NER, spaCy 2.0, recurrent model with a CRF top  | Stanford NER, spaCy 2.0, and a recurrent model similar to BIBREF13/BIBREF14 using bidirectional LSTM cells for character | Stanford NER, spaCy 2.0, and a recurrent model similar to BIBREF13/BIBREF14 using bidirectional LSTM cells for character |
| 24 | `qasper_e` | `token_f1` | 0.235 | 0.235 | +0.000 | WordNet BIBREF0, Freebase BIBREF1, WN18 (a subset of WordNet) BIBREF24 , FB15K (a subset of Freebase) BIBREF2 | WN18 and FB15K | WN18 and FB15K |
| 25 | `qasper_e` | `token_f1` | 0.500 | 0.500 | +0.000 |  LastStateRNN, AvgRNN, AttentionRNN; LastStateRNN, AvgRNN, AttentionRNN  | LastStateRNN | LastStateRNN |
| 26 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | personal attack, racism, and sexism; racism, sexism, personal attack, not specifically about any single topic | Personal attack, racism, and sexism | personal attack, racism, and sexism |
| 27 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Yes; Yes | Yes | Yes |
| 28 | `qasper_e` | `token_f1` | 0.706 | 0.933 | +0.227 | BIBREF12 , BIBREF13; an existing, annotated Twitter dataset that was constructed based on a hierarchical model of depres | An existing, annotated Twitter dataset constructed based on a hierarchical model of depression-related symptoms, contain | an existing, annotated Twitter dataset that was constructed based on a hierarchical model of depression-related symptoms |
| 29 | `qasper_e` | `token_f1` | 0.786 | 0.786 | +0.000 | Nguni languages (zul, xho, nbl, ssw), Sotho languages (nso, sot, tsn); The Nguni languages are similar to each other, Th | The Nguni languages (zul, xho, nbl, ssw) and the Sotho languages (nso, sot, tsn) are similar to each other. | The Nguni languages (zul, xho, nbl, ssw) and the Sotho languages (nso, sot, tsn) are similar to each other. |
| 30 | `qasper_e` | `token_f1` | 0.667 | 1.000 | +0.333 | IMDb dataset of movie reviews; IMDb | IMDb dataset | IMDb dataset of movie reviews |
| 31 | `qasper_e` | `token_f1` | 0.842 | 0.800 | -0.042 | accuracy and F1-score of 89.6% and 89.2%, respectively; accuracy and F1-score of 89.6% and 89.2%, respectively | The system's performance was an accuracy and F1-score of 89.6% and 89.2%, respectively. | Accuracy of 89.6% and F1-score of 89.2%. |
| 32 | `qasper_e` | `token_f1` | 0.857 | 0.857 | +0.000 | K-means, LEM BIBREF13, DPEMM BIBREF14; K-means, LEM, DPEMM | K-means, LEM, and DPEMM | K-means, LEM, and DPEMM |
| 33 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | English, German, Spanish, Mandarin, Polish, Russian, Korean and Serbian; English (Edinburgh), German (Berlin), Spanish ( | English, German, Spanish, Mandarin, Polish, Russian, Korean, and Serbian | English, German, Spanish, Mandarin, Polish, Russian, Korean, and Serbian |
| 34 | `qasper_e` | `token_f1` | 0.714 | 0.800 | +0.086 | rupnik2016news; rupnik2016news, Deutsche Welle's news website | Deutsche Welle's news website and a dataset adapted from rupnik2016news. | Deutsche Welle's news website (http://www.dw.com/) |
| 35 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Yes; Yes | No | No |
| 36 | `qasper_e` | `token_f1` | 0.609 | 0.645 | +0.036 | GloVe, BERT, Universal Sentence Encoder, TF-IDF, InferSent; Avg. GloVe embeddings, Avg. fast-text embeddings, Avg. BERT  | InferSent, Universal Sentence Encoder, average GloVe embeddings, Skip-Thought, BERT embeddings (averaged and CLS-token), | InferSent, Universal Sentence Encoder, average GloVe embeddings, average BERT embeddings, and BERT CLS-token output. |
| 37 | `qasper_e` | `token_f1` | 0.933 | 1.000 | +0.067 | MR, CR, SUBJ, MPQA, SST, TREC, MRPC; MR: Sentiment prediction for movie reviews snippets on a five start scale BIBREF25. | MR, CR, SUBJ, MPQA, SST, TREC, and MRPC | MR, CR, SUBJ, MPQA, SST, TREC, MRPC |
| 38 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | 33,663; 33,663 distinct review keywords  | unanswerable | unanswerable |
| 39 | `qasper_e` | `token_f1` | 0.211 | 0.333 | +0.123 | using tweets that one has replied or quoted to as contextual information; text sequences of context tweets | Context tweets and Latent Topic Clustering (LTC) are proposed as additional features and context. | Context tweets and Latent Topic Clustering (LTC) |
| 40 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | No; No | Yes | Yes |
| 41 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | No; No | unanswerable | unanswerable |
| 42 | `qasper_e` | `token_f1` | 0.222 | 0.215 | -0.007 | For SLC task, the "ltuorp" team  has the best performing  model (0.6323/0.6028/0.6649 for F1/P/R  respectively) and for  | The best-performing model among the authors' submissions is the ensemble+ of (r4, r7, r12) for SLC and ensemble+ of (II  | The best-performing model among the authors' submissions is the ensemble+ of (r4, r7, r12) for SLC with F1=0.673, and th |
| 43 | `qasper_e` | `token_f1` | 0.250 | 0.800 | +0.550 | DTA18, DTA19; Diachronic Usage Relatedness (DURel) gold standard data set | The corpus used for the task is the diachronic corpus pair DTA18 and DTA19 from the DTA corpus. | DTA18 and DTA19 |
| 44 | `qasper_e` | `token_f1` | 0.900 | 1.000 | +0.100 | 13,757; 10,898 articles, 17,794 tweets, and 13,757 crowdsourced question-answer pairs | The dataset includes 10,898 articles, 17,794 tweets, and 13,757 crowdsourced question-answer pairs. | 10,898 articles, 17,794 tweets, and 13,757 crowdsourced question-answer pairs |
| 45 | `qasper_e` | `token_f1` | 0.966 | 0.966 | +0.000 | KNN
RF
SVM
MLP;  K Nearest Neighbors (KNN), Random Forest (RF), Support Vector Machine (SVM), Multi-layer Perceptron (ML | K Nearest Neighbors (KNN), Random Forest (RF), Support Vector Machine (SVM), and Multi-layer Perceptron (MLP) | K Nearest Neighbors (KNN), Random Forest (RF), Support Vector Machine (SVM), and Multi-layer Perceptron (MLP) |
| 46 | `qasper_e` | `token_f1` | 0.469 | 0.543 | +0.074 | They use two independent convolutional and max-pooling layers on (1) a combination of the left context, the left entity  | They obtain the new context representation by splitting the contexts into three disjoint regions (left, middle, right) b | They obtain the new context representation by splitting the contexts into three disjoint regions (left, middle, right) b |
| 47 | `qasper_e` | `token_f1` | 0.269 | 0.203 | -0.066 | An output layer for each task; Multi-tasking is addressed by neural sequence tagger based on LSTM-CRF and linguistic fea | Multi-granularity architecture jointly performs sentence-level and fragment-level classification with shared representat | Multi-granularity design jointly performs FLC and SLC with FastTextWordEmb and BERTSentEmb, adding binary sentence class |
| 48 | `qasper_e` | `token_f1` | 0.780 | 0.878 | +0.098 | which contains over 45,000 scholarly articles, including over 33,000 with full text, about COVID-19, SARS-CoV-2, and rel | The CORD-19 dataset is the COVID-19 Open Research Dataset, containing over 45,000 scholarly articles, including over 33, | The COVID-19 Open Research Dataset (CORD-19), which contains over 45,000 scholarly articles, including over 33,000 with  |
| 49 | `qasper_e` | `token_f1` | 0.267 | 0.000 | -0.267 | 26972; 26972 sentences | The real-life dataset consists of supervisor assessment text from 4528 employees, containing 26972 sentences. | 4528 employees |
| 50 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Unanswerable; Unanswerable | The state of the art methods are neural network-based approaches to grammar induction, including models like PRPN, ON, a | neural network-based approaches to grammar induction BIBREF14 , BIBREF15 , BIBREF16 , BIBREF17 |

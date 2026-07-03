# Qwen Tris LongBench Public Slice - qwen_tris_longbench_public_slice_20260701T172019Z

- Benchmark: `LongBench public data.zip`
- Provider: `qwen-cloud`
- Model: `qwen-plus`
- Items: `50`
- Skipped provider-blocked rows: `0`
- Condition A mean: `0.494`
- Condition B mean: `0.545`
- Delta: `+0.051`

## Boundary

Public LongBench smoke slice. This is not a full LongBench leaderboard claim; it is a source-backed answer-key accuracy receipt that can scale to larger slices.

## Conditions

- Condition A: baseline Qwen prompt-only answer discipline
- Condition B: Qwen Tris stable-state answer discipline

## Family Totals

- `qasper_e`: n=50 A=0.494 B=0.545 delta=+0.051

## Rows

| # | Dataset | Metric | A | B | Delta | Gold | A prediction | B prediction |
|---:|---|---|---:|---:|---:|---|---|---|
| 1 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li | FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Li |
| 2 | `qasper_e` | `token_f1` | 0.600 | 0.600 | +0.000 | the series of posts that trigger an intervention | The latent context used to predict instructor intervention is the series of posts that trigger an intervention. | The latent context used to predict instructor intervention is "the series of posts that trigger an intervention". |
| 3 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | F-score, Kappa; Unanswerable | F-score and Kappa statistics | F-score and Kappa statistics |
| 4 | `qasper_e` | `token_f1` | 0.364 | 0.214 | -0.149 | (i) models that use plain stacked LSTMs, (ii) models with different INLINEFORM0, (iii) models without INLINEFORM1, (iv)  | The baselines were models that use plain stacked LSTMs. | plain stacked LSTMs |
| 5 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Yes; Unanswerable | No | no |
| 6 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | No | No | No |
| 7 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Yes; No | No | No |
| 8 | `qasper_e` | `token_f1` | 0.645 | 0.480 | -0.165 | SemEval-2016 Challenge Task 5 BIBREF27 , BIBREF28;  English reviews ,  restaurant reviews from four different languages  | The evaluation used restaurant reviews from four languages (Spanish, Turkish, Dutch, Russian) from SemEval-2016 Challeng | SemEval-2016 Challenge Task 5 restaurant reviews datasets in Spanish, Turkish, Dutch, and Russian. |
| 9 | `qasper_e` | `token_f1` | 0.400 | 0.424 | +0.024 | 7.36% on accuracy and 9.69% on F1 score; it has 0.024 improvement in accuracy comparing to ELMO Only and  0.006 improvem | The article reports that adding topic information (Topic Only setting) improved accuracy by 7.36% and F1 score by 9.69%  | The article reports that adding topic information (Topic Only setting) improved accuracy by 7.36% and F1 score by 9.69%  |
| 10 | `qasper_e` | `token_f1` | 0.174 | 0.222 | +0.048 | They use text transcription.; both | They use both: released transcripts of the IEMOCAP dataset and also process audio data using an ASR system to retrieve t | They use both: released transcripts of the IEMOCAP dataset and ASR-processed transcripts derived from the audio. |
| 11 | `qasper_e` | `token_f1` | 0.857 | 0.857 | +0.000 | CLUTO, Carrot2 Lingo; simple clustering algorithm which uses the cosine similarity between word embeddings | CLUTO and Carrot2 Lingo | CLUTO and Carrot2 Lingo |
| 12 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | Bert + Unanswerable; CNN, BERT | BERT | BERT |
| 13 | `qasper_e` | `token_f1` | 0.200 | 0.333 | +0.133 | pivoting, pivoting$_{\rm m}$; firstly translates a source language into the pivot language which is later translated to  | Pivot-based baselines are the pivoting and pivot-synthetic methods. | pivoting and pivot-synthetic |
| 14 | `qasper_e` | `token_f1` | 0.364 | 0.286 | -0.078 | Friends, EmotionPush; EmotionLines BIBREF6 | EmotionLines dataset, which consists of the Friends and EmotionPush subsets. | EmotionLines (Friends and EmotionPush), Twitter emotion dataset, and Friends TV show scripts. |
| 15 | `qasper_e` | `token_f1` | 0.135 | 0.135 | +0.000 | three experimental setups with different numbers of speakers in the evaluation set, three experimental setups with diffe | Several evaluation protocols for each part of the database, allowing researchers to investigate performance in various s | Several evaluation protocols for each part of the database, allowing researchers to investigate performance in various s |
| 16 | `qasper_e` | `token_f1` | 0.306 | 0.280 | -0.026 | pays attentions to adjacent characters and casts a localness relationship between the characters as a fixed Gaussian wei | Gaussian-masked directional multi-head attention works by combining a Gaussian weight matrix, which emphasizes adjacent  | Gaussian-masked directional multi-head attention works by combining a Gaussian weight matrix $G$, which encodes localnes |
| 17 | `qasper_e` | `token_f1` | 0.077 | 0.250 | +0.173 | No data. Pretrained model is used. | Monolingual data (e.g., Wikipedias) and, for some experiments, parallel corpora (e.g., United Nations Parallel Corpus, I | monolingual data |
| 18 | `qasper_e` | `token_f1` | 0.179 | 0.163 | -0.015 | For certain POS tags, e.g. VERB, PRON.; most word alignments only involve one or a few words, attention can be distribut | Attention is different from alignment in cases involving verbs, pronouns, and particles, where attention is more distrib | Attention is different from alignment in cases where it captures information beyond translational equivalence, such as f |
| 19 | `qasper_e` | `token_f1` | 1.000 | 0.211 | -0.789 | RNN;  Recurrent Neural Network (RNN) | Recurrent Neural Network (RNN) | RNN with two 2D-convolutional layers, seven bi-directional recurrent layers, and a fully-connected layer with softmax ac |
| 20 | `qasper_e` | `token_f1` | 0.500 | 0.500 | +0.000 | CNN modelBIBREF0, Stanford CRF modelBIBREF21; Bam et al. SVM, Ma and Hovy w/glove, Lample et al. w/fastText, Lample et a | Stanford CRF model | Stanford CRF model |
| 21 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Unanswerable | unanswerable | unanswerable |
| 22 | `qasper_e` | `token_f1` | 0.200 | 0.200 | +0.000 | about 500; Unanswerable | Around 500 different workers were involved in the annotation. | Around 500 different workers were involved in the annotation. |
| 23 | `qasper_e` | `token_f1` | 0.818 | 0.909 | +0.091 | linear SVM, bidirectional Long Short-Term-Memory (BiLSTM), Convolutional Neural Network (CNN); linear SVM, bidirectional | Linear SVM, bidirectional Long Short-Term Memory (BiLSTM), and Convolutional Neural Network (CNN) | linear SVM, bidirectional Long Short-Term-Memory (BiLSTM) model, Convolutional Neural Network (CNN) model |
| 24 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | BiLSTM, BiLSTM-CNN, BiLSTM-CRF, BiLSTM-CNN-CRF; BiLSTMBIBREF14, BiLSTM+CNNBIBREF20, BiLSTM+CRFBIBREF1, BiLSTM+CNN+CRFBIB | BiLSTM, BiLSTM+CNN, BiLSTM+CRF, BiLSTM+CNN+CRF, CNN, and Stanford CRF | BiLSTM, BiLSTM+CNN, BiLSTM+CRF, BiLSTM+CNN+CRF, CNN, and Stanford CRF |
| 25 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Zero Resource Toolkit (ZRTools) BIBREF7 | Through unsupervised term discovery (UTD) and acoustic unit discovery (AUD), which operate directly on raw speech withou | Through unsupervised term discovery (UTD) for word-like units and acoustic unit discovery (AUD) for phoneme-like units. |
| 26 | `qasper_e` | `token_f1` | 0.667 | 0.667 | +0.000 | BERTbase; BERTbase | BERTbase model | BERTbase model |
| 27 | `qasper_e` | `token_f1` | 0.038 | 0.069 | +0.031 | Answer with content missing: (LVL1, LVL2, LVL3) 
- Stanford CoreNLP
- Optical Character Recognition (OCR) system, ParsCI | TopicRank, WINGNUS, KP-Miner, TF-IDF, and another unspecified model (the article states five models were re-implemented, | five keyphrase extraction models: two commonly used baselines, a resource-lean unsupervised graph-based ranking approach |
| 28 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Yes; Yes | Yes | yes |
| 29 | `qasper_e` | `token_f1` | 0.667 | 0.133 | -0.533 | MIMIC-III; MIMIC-III | MIMIC-III dataset | MIMIC-III database, specifically 55,177 discharge reports and 4,475 discharge addendums for 41,127 distinct patients. |
| 30 | `qasper_e` | `token_f1` | 0.000 | 0.216 | +0.216 | Level A: 14100 Tweets
Level B: 4640 Tweets
Level C: 4089 Tweets | unanswerable | The dataset contains 14,100 tweets, with hierarchical annotation across three levels (A, B, C), but the article does not |
| 31 | `qasper_e` | `token_f1` | 0.108 | 0.000 | -0.108 | it captures other information rather than only the translational equivalent in the case of verbs; Alignment points of th | Attention captures context words influencing the current word translation, such as adjectives and determiners for nouns, | context words influencing the current word translation |
| 32 | `qasper_e` | `token_f1` | 0.766 | 0.829 | +0.063 | BOW-LR, BOW-RF. TFIDF-RF, TextCNN, C-TextCNN; bag-of-words (BOW), term frequency–inverse document frequency (TFIDF), neu | The baselines were bag-of-words (BOW), term frequency–inverse document frequency (TFIDF), and neural-based word embeddin | bag-of-words (BOW), term frequency–inverse document frequency (TFIDF), neural-based word embedding, Logistic Regression  |
| 33 | `qasper_e` | `token_f1` | 0.000 | 1.000 | +1.000 | Unanswerable; 48,705 | The article does not specify a fixed number of tags they look at; it evaluates recommendations for different values of " | unanswerable |
| 34 | `qasper_e` | `token_f1` | 0.333 | 0.667 | +0.333 | follow the architecture in berard2018end, but have 3 decoder layers like that in pino2019harnessing | The ASR and ST models follow the architecture in berard2018end with 3 decoder layers, and the MT model uses a Transforme | berard2018end architecture with 3 decoder layers like pino2019harnessing |
| 35 | `qasper_e` | `token_f1` | 0.833 | 0.833 | +0.000 |  Penn Treebank, WikiText2; Penn Treebank (PTB) , WikiText2 (WT-2) | Penn Treebank (PTB) and WikiText2 (WT-2) datasets | Penn Treebank (PTB) and WikiText2 (WT-2) datasets |
| 36 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | No; No | unanswerable | unanswerable |
| 37 | `qasper_e` | `token_f1` | 0.605 | 0.605 | +0.000 | While there has been existing work on reducing NLP model vocabulary sizes BIBREF15, distillation techniques cannot utili | Because they require the student and teacher models to share the same vocabulary and output space. | Because they require the student and teacher models to share the same vocabulary and output space. |
| 38 | `qasper_e` | `token_f1` | 0.154 | 0.154 | +0.000 | using word2vec to create features that are used as input to the SVM; use the word2vec algorithm, create several unsuperv | word2vec | word2vec |
| 39 | `qasper_e` | `token_f1` | 0.667 | 0.723 | +0.057 | ancient Chinese history records in several dynasties (about 1000BC-200BC) and articles written by celebrities of that er | The ancient Chinese dataset comes from 1.7K bilingual ancient-modern Chinese articles collected from the internet, prima | 1.7K bilingual ancient-modern Chinese articles collected from the internet, with a large part coming from ancient Chines |
| 40 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | No | unanswerable | unanswerable |
| 41 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | words embeddings, style, and morality features; words embeddings, style, and morality features | Words embeddings, style, and morality features. | words embeddings, style, and morality features |
| 42 | `qasper_e` | `token_f1` | 0.000 | 0.000 | +0.000 | United Nations Parallel Corpus, IIT Bombay corpus, OpenSubtitles 2018 | XNLI dataset and Universal Dependencies v2.4 | XNLI dataset and Universal Dependencies v2.4 |
| 43 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Unanswerable; English | unanswerable | unanswerable |
| 44 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | No; No | No | no |
| 45 | `qasper_e` | `token_f1` | 0.095 | 0.947 | +0.852 | 45,000 scholarly articles, including over 33,000 with full text | The collection of COVID-19 literature consists of 2081 articles and about 360,000 sentences. | over 45,000 scholarly articles, including over 33,000 with full text |
| 46 | `qasper_e` | `token_f1` | 0.444 | 0.533 | +0.089 | support vector machine classifier (SVM), logistic regression classifier (LR), Naive Bayes classifier (NB), random forest | The proposed model is compared to TF-IDF-based classifiers (SVM, LR, NB, RF), CNN, LSTM, LSTM-soft, and LSTM-self. | TF-IDF (SVM, LR, NB, RF), CNN, LSTM, LSTM-soft, and LSTM-self |
| 47 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | 1913 signals; Unanswerable | unanswerable | unanswerable |
| 48 | `qasper_e` | `token_f1` | 0.485 | 0.800 | +0.315 | Co-Reference Resolution, Query Generation, Retrieval Model, Result Generation; Co-Reference Resolution, Query Generation | Macaw's modules include actions (e.g., search, question answering), co-reference resolution, query generation, retrieval | Macaw's modules include co-reference resolution, query generation, retrieval model, and result generation. |
| 49 | `qasper_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Unanswerable | unanswerable | unanswerable |
| 50 | `qasper_e` | `token_f1` | 0.000 | 1.000 | +1.000 | Unanswerable; Unanswerable | The article mentions variability with respect to "dialects" but does not specify which accents are present in the corpus | unanswerable |

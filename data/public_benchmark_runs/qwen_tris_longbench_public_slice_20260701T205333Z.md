# Qwen Tris LongBench Public Slice - qwen_tris_longbench_public_slice_20260701T205333Z

- Benchmark: `LongBench public data.zip`
- Provider: `qwen-cloud`
- Model: `qwen-plus`
- Items: `50`
- Skipped provider-blocked rows: `0`
- Condition A mean: `0.482`
- Condition B mean: `0.531`
- Delta: `+0.049`

## Boundary

Public LongBench smoke slice. This is not a full LongBench leaderboard claim; it is a source-backed answer-key accuracy receipt that can scale to larger slices.

## Conditions

- Condition A: baseline Qwen prompt-only answer discipline
- Condition B: Qwen Tris stable-state answer discipline

## Family Totals

- `multifieldqa_en_e`: n=50 A=0.482 B=0.531 delta=+0.049

## Rows

| # | Dataset | Metric | A | B | Delta | Gold | A prediction | B prediction |
|---:|---|---|---:|---:|---:|---|---|---|
| 1 | `multifieldqa_en_e` | `token_f1` | 0.200 | 0.200 | +0.000 | The focus of the study was on the reactive radical ethynyl (C$_2$H). | C$_2$H | C$_2$H |
| 2 | `multifieldqa_en_e` | `token_f1` | 0.500 | 1.000 | +0.500 | Other toxic products. | Other toxic products, rather than against saline (genuine placebo). | other toxic products |
| 3 | `multifieldqa_en_e` | `token_f1` | 0.533 | 0.533 | +0.000 | The authors used simulated data and real data from a wireless MISO channel. | Simulated and real data | simulated and real data |
| 4 | `multifieldqa_en_e` | `token_f1` | 0.341 | 0.439 | +0.098 | Verifying other meta-information such as patient's gender, age, race, etc. | Applying the findings to non-Japanese EHRs, verifying other meta-information (e.g., patient's gender, age, race, religio | Developing a robust and flexible research infrastructure to conduct a more large scale cross-sectional study, verifying  |
| 5 | `multifieldqa_en_e` | `token_f1` | 0.125 | 0.000 | -0.125 | The three subsets are V+, V0, and V-, determined by the Kullback-Leibler information distance. | V⁺, V₀, and V⁻ | V⁺, V₀, V⁻ |
| 6 | `multifieldqa_en_e` | `token_f1` | 0.647 | 0.957 | +0.309 | $\int f'(u) \psi^2 \le \int \| \nabla \psi\|^2, \forall \psi \in C_c^2$. | A solution $ u $ of $ -\Delta u = f(u) $ in $ \mathbb{R}^N $ is stable if   $$ \int f'(u) \psi^2 \le \int \| \nabla \psi\| | $\int f'(u) \psi^2 \le \int \| \nabla \psi\|^2, \qquad \forall \psi \in C_c^2$ |
| 7 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | 21. | 21 | 21 |
| 8 | `multifieldqa_en_e` | `token_f1` | 0.000 | 1.000 | +1.000 | 48V. | 20V | 48V |
| 9 | `multifieldqa_en_e` | `token_f1` | 0.667 | 0.667 | +0.000 | The Wallace electorate. | Wallace | Wallace |
| 10 | `multifieldqa_en_e` | `token_f1` | 0.600 | 0.600 | +0.000 | The paper was published on 7 March 2023. | 7 March 2023 | 7 March 2023 |
| 11 | `multifieldqa_en_e` | `token_f1` | 0.222 | 0.222 | +0.000 | Weep Not, Child was first published in 1964. | 1964 | 1964 |
| 12 | `multifieldqa_en_e` | `token_f1` | 0.516 | 0.222 | -0.294 | Multiple vacuum processing apparatuses are arranged in parallel. | The vacuum processing system is configured with multiple vacuum processing apparatuses arranged in parallel, where all v | parallel |
| 13 | `multifieldqa_en_e` | `token_f1` | 0.483 | 0.583 | +0.101 | NFPA and FPSA greatly outperform GMRES and DSA. | NFPA and FPSA vastly outperform GMRES and DSA in runtime and iteration counts by orders of magnitude for all tested case | NFPA and FPSA vastly outperform GMRES and DSA in runtime and iterations by orders of magnitude. |
| 14 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Romance novels and women's fiction. | Romance novels and women's fiction | romance novels and women's fiction |
| 15 | `multifieldqa_en_e` | `token_f1` | 0.667 | 0.667 | +0.000 | URPC2017, URPC2018, URPC2019, URPC2020_ZJ and URPC2020_DL. | URPC2017 and URPC2018 | URPC2017 and URPC2018 |
| 16 | `multifieldqa_en_e` | `token_f1` | 0.000 | 0.000 | +0.000 | Unknown. | No. | Nothing can give a solid proof of the existence of heaven and hell, yet, nothing can disprove it either. |
| 17 | `multifieldqa_en_e` | `token_f1` | 0.875 | 0.875 | +0.000 | He became deputy prime minister and minister of finance. | Deputy Prime Minister and Minister of Finance | Deputy Prime Minister and Minister of Finance |
| 18 | `multifieldqa_en_e` | `token_f1` | 0.600 | 0.133 | -0.467 | The generative interactive model used in the method is called the Coupled Generalized Dynamic Bayesian Network (C-GDBN). | Coupled Generalized Dynamic Bayesian Network (C-GDBN) | C-GDBN |
| 19 | `multifieldqa_en_e` | `token_f1` | 0.121 | 0.556 | +0.434 | It uses a content-recognition module or algorithm. | A media application determines the context of an event using a content-recognition module or algorithm that may employ t | A media application uses a content-recognition module or algorithm to determine the context of an event. |
| 20 | `multifieldqa_en_e` | `token_f1` | 0.200 | 0.237 | +0.037 | Smartphones are more compact and power constrained. | Smartphones are more compact and power-constrained (limited to ~1W), require integrated cellular modems, and have strict | Smartphones are far more compact and power constrained, with SoCs limited to around 1W, while tablets have a much greate |
| 21 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | 172. | 172 | 172 |
| 22 | `multifieldqa_en_e` | `token_f1` | 0.514 | 0.800 | +0.286 | An unsupervised method based on the information bottleneck and contrastive learning. | The main methodology used in the research is an unsupervised method based on the information bottleneck, combining compo | Unsupervised method based on the information bottleneck |
| 23 | `multifieldqa_en_e` | `token_f1` | 0.486 | 0.783 | +0.296 | The longerons bow up from the building surface, forming a "banana" shape. | The problem is that the once straight longerons bow up from the building surface, forming an unacceptable "banana" shape | The problem is that the once straight longerons bow up from the building surface, forming a "banana" shape. |
| 24 | `multifieldqa_en_e` | `token_f1` | 0.061 | 0.111 | +0.051 | The belief entropy decreases more steadily. | The time required to update the robot's belief does not increase with the complexity of the environment (e.g., number of | The time required to update the robot's belief does not increase with the complexity of the environment. |
| 25 | `multifieldqa_en_e` | `token_f1` | 0.286 | 0.286 | +0.000 | Players can skip dialogue on the quest map by pressing the 'SKIP' button. | By pressing ‘SKIP’. | by pressing ‘SKIP’ |
| 26 | `multifieldqa_en_e` | `token_f1` | 0.229 | 0.276 | +0.047 | Privacy concerns and skepticism about its effectiveness. | Governor Rick Scott cited privacy concerns, expressed skepticism that the monitoring program would work, and raised the  | privacy concerns, skepticism that the monitoring program would work, and concern that taxpayers would be left with a $50 |
| 27 | `multifieldqa_en_e` | `token_f1` | 1.000 | 0.000 | -1.000 | 5. | 5 | five |
| 28 | `multifieldqa_en_e` | `token_f1` | 0.833 | 0.727 | -0.106 | L = 8 and L = 14. | L = 6, L = 8, and L = 14 | L = 6, L = 8, L = 14 |
| 29 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Low temperature scanning tunneling microscopy and spectroscopy (STM/STS). | Low temperature scanning tunneling microscopy and spectroscopy (STM/STS) | low temperature scanning tunneling microscopy and spectroscopy (STM/STS) |
| 30 | `multifieldqa_en_e` | `token_f1` | 0.091 | 0.091 | +0.000 | There are 14,520 attendees, including 7,152 chemical scientists, 5,059 students, 1,283 exhibitors, 119 precollege teache | 14,520 | 14,520 |
| 31 | `multifieldqa_en_e` | `token_f1` | 0.333 | 0.333 | +0.000 | No, it is not necessary. | No | No |
| 32 | `multifieldqa_en_e` | `token_f1` | 0.500 | 1.000 | +0.500 | Power-law functions. | Power-law distributions | power-law functions |
| 33 | `multifieldqa_en_e` | `token_f1` | 0.255 | 0.133 | -0.121 | The main topic of the text is Iraq's politics and current situation. | The main topic of the text is the political, social, and humanitarian situation in Iraq as of late December 2010, includ | Iraq War and its aftermath |
| 34 | `multifieldqa_en_e` | `token_f1` | 0.065 | 1.000 | +0.935 | Flexibility. | The main advantage of a horizontal business model for mobile devices is flexibility, allowing vendors to offer a wide ra | flexibility |
| 35 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | Vitamins K3, K4, and K5. | Vitamins K3, K4, and K5 | vitamins K3, K4, and K5 |
| 36 | `multifieldqa_en_e` | `token_f1` | 0.385 | 0.275 | -0.110 | The relationships between catch per set and fishing behavior variables differ when comparing unstandardized CPUE and sta | The relationships between catch per set and fishing behavior variables differ for different measures of CPUE because uns | Unstandardised CPUE (individuals per set) shows positive relationships with number of hooks, engine power, and number of |
| 37 | `multifieldqa_en_e` | `token_f1` | 0.541 | 0.690 | +0.149 | As the transition probability increases, the learning rate initially rises and then declines. | The learning rate in the static agent rapidly rises as the transition probability increases from 0, peaks, and then slow | The learning rate rapidly rises as the transition probability increases from 0, peaks, then slowly declines and eventual |
| 38 | `multifieldqa_en_e` | `token_f1` | 1.000 | 0.500 | -0.500 | "I have seen the Lord.". | "I have seen the Lord." | “I have seen the Lord” |
| 39 | `multifieldqa_en_e` | `token_f1` | 0.333 | 0.333 | +0.000 | Watt, one joule per second. | watt | watt |
| 40 | `multifieldqa_en_e` | `token_f1` | 0.095 | 0.095 | +0.000 | Yes, individual molecules of indeno[1,2-a]fluorene can switch between open-shell and closed-shell states by changing the | Yes | Yes |
| 41 | `multifieldqa_en_e` | `token_f1` | 0.174 | 0.167 | -0.007 | Severe anemia that begins even before birth. | Severe anemia beginning before birth, enlarged placenta, heart, liver, spleen, and adrenal glands, fluid accumulation th | Severe anemia beginning before birth, placental and organ enlargement (heart, liver, spleen, adrenal glands), fluid accu |
| 42 | `multifieldqa_en_e` | `token_f1` | 0.500 | 0.429 | -0.071 | The sticking point in the political showdown over the budget is how much spending to cut. | The sticking points in the political showdown over the budget are disagreements over how much to cut spending, policy ri | How much spending to cut and policy riders, especially over abortion and regulating greenhouse gases. |
| 43 | `multifieldqa_en_e` | `token_f1` | 1.000 | 1.000 | +0.000 | 1766. | 1766 | 1766 |
| 44 | `multifieldqa_en_e` | `token_f1` | 0.960 | 0.960 | +0.000 | The time required to update the belief does not increase with the complexity of the environment. | The time required to update the robot's belief does not increase with the complexity of the environment. | The time required to update the robot's belief does not increase with the complexity of the environment. |
| 45 | `multifieldqa_en_e` | `token_f1` | 0.245 | 0.200 | -0.045 | Quill harmed states more than anticipated due to the Internet. | Justice Kennedy argued that the Internet had caused far-reaching systemic and structural changes in the economy, making  | Justice Kennedy argued that “[t]he Internet has caused far-reaching systemic and structural changes in the economy” and  |
| 46 | `multifieldqa_en_e` | `token_f1` | 0.261 | 0.750 | +0.489 | Nuclear liquid-gas transition in lattice QCD. | The main focus of the research paper is determining the nuclear liquid-gas transition in the strong coupling regime of l | Nuclear liquid-gas transition in the strong coupling regime of lattice QCD |
| 47 | `multifieldqa_en_e` | `token_f1` | 0.133 | 0.222 | +0.089 | Using the vacuum Einstein equation and the Baez-Bunn form. | The function $\beta(r)$ is determined by applying the vacuum Einstein equations in the simplified Baez-Bunn form—specifi | From the simplified form of the vacuum Einstein equations (\ref{EinsteinVacuum}) applied to a test ball in free fall alo |
| 48 | `multifieldqa_en_e` | `token_f1` | 0.727 | 0.545 | -0.182 | Legacies of Losing in American Politics and an expanded edition of The Rhetorical Presidency in the Princeton Classics s | Legacies of Losing in American Politics, with Nicole Mellow (University of Chicago Press, Fall 2017), and an expanded ed | Legacies of Losing in American Politics |
| 49 | `multifieldqa_en_e` | `token_f1` | 0.625 | 0.788 | +0.163 | SNNs have the potential to better model and explain the functional hierarchy and mechanisms of the visual system. | SNNs have the potential to serve as promising candidates to better model and explain the functional hierarchy and mechan | SNNs could serve as promising candidates to better model and explain the functional hierarchy and mechanisms of the visu |
| 50 | `multifieldqa_en_e` | `token_f1` | 0.182 | 0.182 | +0.000 | The water depth in the Greater Ekofisk Area is 70-75 meters. | 70-75 metres | 70-75 metres |

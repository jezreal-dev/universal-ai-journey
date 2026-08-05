# Lecture Notes – AI and Ethics

---

## 🏛️ Lecture 1: Introduction to AI & Ethical Frameworks

### 1. Survey of Normative Ethical Frameworks

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                                Normative Ethics Taxonomy                                 │
├─────────────────────┬────────────────────────────────────┬───────────────────────────────┤
│ Framework           │ Core Principle                     │ Application to AI Systems     │
├─────────────────────┼────────────────────────────────────┼───────────────────────────────┤
│ 1. Deontology       │ Duty-based rules & moral rights    │ Hard constraints, safety guard│
│                     │ (Kant's Categorical Imperative)    │ rails, privacy compliance     │
├─────────────────────┼────────────────────────────────────┼───────────────────────────────┤
│ 2. Utilitarianism   │ Consequentialism: Maximize net     │ Welfare optimization, Pareto  │
│                     │ expected utility for all beings    │ efficiency, risk-benefit trade│
├─────────────────────┼────────────────────────────────────┼───────────────────────────────┤
│ 3. Virtue Ethics    │ Cultivating moral character traits │ Value alignment, honesty,     │
│                     │ (honesty, fairness, prudence)      │ human-centric AI design       │
└─────────────────────┴────────────────────────────────────┴───────────────────────────────┘
```

---

### 2. Taxonomy of 4 Sources of Algorithmic Bias

Bias in AI systems does not stem solely from flawed code; it arises at multiple stages of the data and modeling lifecycle:

```
Raw World Dynamics ──► [1. Historical Bias] ──► Data Collection ──► [2. Sampling Bias]
                                                                        │
Model Deployment   ◄── [4. Aggregation Bias] ◄── Feature Eng.   ◄── [3. Measurement Bias]
```

1. **Historical Bias**: Pre-existing structural societal inequities reflected in historical data, even if sampled perfectly (e.g. historical mortgage redlining or hiring disparities).
2. **Sampling Bias**: Non-representative sampling where certain demographic sub-populations are under-represented or over-represented in training sets.
3. **Measurement Bias**: Use of flawed or proxy features that correlate differently with outcomes across groups (e.g. using arrest records as a proxy for actual crime commission).
4. **Aggregation Bias**: Fitting a single universal model to heterogeneous populations when distinct sub-groups require distinct functional relationships.

---

### 3. The 3 Fundamental Criteria of Fairness

Let $X$ denote features, $A \in \{0, 1\}$ denote protected demographic attribute, $Y \in \{0, 1\}$ denote ground truth label, and $\hat{Y} \in \{0, 1\}$ denote model prediction.

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                            3 Fundamental Fairness Criteria                               │
├───────────────────┬────────────────────────────────────────┬─────────────────────────────┤
│ Criterion         │ Formal Mathematical Condition          │ Common Name                 │
├───────────────────┼────────────────────────────────────────┼─────────────────────────────┤
│ 1. Independence   │ P(Y_hat=1 | A=0) = P(Y_hat=1 | A=1)    │ Demographic Parity          │
├───────────────────┼────────────────────────────────────────┼─────────────────────────────┤
│ 2. Separation     │ P(Y_hat=1 | A=0, Y=y) =                │ Equalized Odds /            │
│                   │ P(Y_hat=1 | A=1, Y=y)  forall y        │ Error Rate Parity           │
├───────────────────┼────────────────────────────────────────┼─────────────────────────────┤
│ 3. Sufficiency    │ P(Y=1 | A=0, Y_hat=y) =                │ Predictive Parity /         │
│                   │ P(Y=1 | A=1, Y_hat=y)  forall y        │ Calibration Within Groups   │
└───────────────────┴────────────────────────────────────────┴─────────────────────────────┘
```

---

## ⚖️ Lecture 2: AI Fairness & Impossibility Theorems

### 1. The COMPAS Case Study & Error Rate Disparities

In judicial risk assessment, the COMPAS system evaluated 2-year recidivism risk. Audit by ProPublica revealed a sharp conflict between fairness definitions:

* **Calibration (Sufficiency)**: COMPAS was well-calibrated across races ($P(\text{Recidivate} \mid \text{Score} = k)$ was similar for Black and white defendants).
* **Error Rate Parity (Separation)**: COMPAS severely violated Separation:
  * **False Positive Rate (FPR)**: Black non-recidivists were misclassified as high risk at twice the rate of white non-recidivists ($\sim 45\%$ vs. $\sim 23\%$).
  * **False Negative Rate (FNR)**: White recidivists were misclassified as low risk at twice the rate of Black recidivists ($\sim 48\%$ vs. $\sim 28\%$).

---

### 2. Chouldechova & Kleinberg Impossibility Theorems

**Theorem (Kleinberg et al. 2016, Chouldechova 2017)**:  
Suppose base rates differ across demographic groups ($P(Y=1 \mid A=0) \neq P(Y=1 \mid A=1)$). Then a prediction model $f(X, A)$ **CANNOT** satisfy Sufficiency (Calibration) and Separation (Equal FPR & Equal FNR) simultaneously, unless the classifier achieves $100\%$ perfect accuracy ($FPR = 0, FNR = 0$).

#### Mathematical Proof Outline
Positive Predictive Value ($PPV$) is related to $TPR = 1 - FNR$, $FPR$, and Base Rate $p = P(Y=1)$:

$$PPV = \frac{TPR \cdot p}{TPR \cdot p + FPR \cdot (1 - p)} = \frac{(1 - FNR) \cdot p}{(1 - FNR) \cdot p + FPR \cdot (1 - p)}$$

If $FPR_0 = FPR_1$ and $FNR_0 = FNR_1$, but $p_0 \neq p_1$, then:

$$PPV_0 = \frac{(1 - FNR) \cdot p_0}{(1 - FNR) \cdot p_0 + FPR \cdot (1 - p_0)} \neq \frac{(1 - FNR) \cdot p_1}{(1 - FNR) \cdot p_1 + FPR \cdot (1 - p_1)} = PPV_1$$

Hence, equal error rates mathematically force unequal calibration when base rates differ!

---

## 🎯 Lecture 3: AI & The Alignment Problem

### 1. Misspecified Desires & Objective Functions

When optimizing complex machine learning models, optimizing an incomplete proxy reward function leads to severe unintended consequences:

* **Goodhart's Law**: *"When a measure becomes a target, it ceases to be a good measure."*
* **Reward Hacking**: Agents exploit loopholes in reward functions to maximize score without fulfilling intended goals (e.g. a boat racing agent driving in circles to collect points instead of finishing the race).
* **Cobra Effect**: Perverse incentives where policies produce the exact opposite of intended outcomes.

---

### 2. Modern AI Alignment Methods (RLHF, DPO, Constitutional AI)

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                               Modern LLM Alignment Pipeline                              │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ Pretrained LLM ──► Supervised Fine-Tuning (SFT) ──► Preference Optimization (RLHF / DPO)│
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

1. **RLHF (Reinforcement Learning from Human Feedback)**:
   - Train a Reward Model $R_\psi(x, y)$ on human pairwise preferences $(y_w \succ y_l)$.
   - Optimize policy $\pi_\theta$ using PPO with a KL-divergence penalty against initial reference policy $\pi_{\text{ref}}$:
   
   $$\max_\theta \mathbb{E}_{(x, y) \sim \mathcal{D}} \left[ R_\psi(x, y) \right] - \beta D_{\text{KL}}\left(\pi_\theta(y \mid x) \parallel \pi_{\text{ref}}(y \mid x)\right)$$

2. **DPO (Direct Preference Optimization)**:
   - Eliminates explicit reward model training by analytically solving for the optimal policy under the Bradley-Terry preference model:
   
   $$\mathcal{L}_{\text{DPO}}(\theta) = -\mathbb{E}_{(x, y_w, y_l)} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w \mid x)}{\pi_{\text{ref}}(y_w \mid x)} - \beta \log \frac{\pi_\theta(y_l \mid x)}{\pi_{\text{ref}}(y_l \mid x)} \right) \right]$$

3. **Constitutional AI (RLAIF)**:
   - Replaces human feedback with automated AI critiques evaluated against a written "Constitution" of principles.

---

### 3. Social Choice Theory & Arrow's Impossibility Theorem

When aligning AI systems with diverse human populations, preference aggregation encounters fundamental social choice limitations:

**Arrow's Impossibility Theorem**: For any preference aggregation rule combining individual preference orderings over $\ge 3$ outcomes, no social welfare function can satisfy all 3 axioms simultaneously:
1. **Unanimity (Pareto Efficiency)**: If everyone prefers $X$ over $Y$, society prefers $X$ over $Y$.
2. **Non-dictatorship**: No single individual's preferences dictate the societal outcome.
3. **Independence of Irrelevant Alternatives (IIA)**: The relative ranking of $X$ and $Y$ depends only on individual preferences between $X$ and $Y$, not a third alternative $Z$.

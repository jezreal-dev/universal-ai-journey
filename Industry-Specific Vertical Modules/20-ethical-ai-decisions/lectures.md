# Lecture Notes – Ethical AI for Decisions in Today's World

---

## ⚖️ Lecture 1: Data, Models, Decisions, and Ethical Foundations

### 1. The Data-Model-Decision Pipeline & Feedback Loops

AI-driven decision systems operate as closed-loop feedback environments rather than static one-way functions:

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                            Data-Model-Decision Closed Pipeline                           │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ Real-World System ──► Raw Data X, y ──► Model Predictive Training ──► Predictions y_hat │
│        ▲                                                                    │            │
│        └──────────── Feedback Loop ◄── Real-World Action & Policy ◄─────────┘            │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

* **Data ($X, y$)**: Historical observations, noisy signals, and social proxies.
* **Model ($\hat{y} = f(X)$)**: Statistical patterns mapping inputs to predictions.
* **Decision ($D(\hat{y})$)**: Policy rules determining real-world actions (e.g. loan approval, bail release, hiring selection).
* **Feedback Loop**: Actions alter future system states, generating self-reinforcing training data (e.g. denying loans prevents observing whether rejected applicants would have paid).

---

### 2. Normative Ethical Frameworks

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                             Normative Ethical Paradigms                                  │
├─────────────────────┬────────────────────────────────────┬───────────────────────────────┤
│ Paradigm            │ Core Principle                     │ Application in AI Systems     │
├─────────────────────┼────────────────────────────────────┼───────────────────────────────┤
│ 1. Deontology       │ Duty-based; adherence to moral     │ Absolute procedural constraints│
│                     │ rules regardless of outcomes       │ (e.g. banning protected features)│
├─────────────────────┼────────────────────────────────────┼───────────────────────────────┤
│ 2. Utilitarianism   │ Maximize overall net utility across│ Objective function expected   │
│                     │ all affected individuals           │ payoff optimization           │
├─────────────────────┼────────────────────────────────────┼───────────────────────────────┤
│ 3. Consequentialism │ Evaluate actions strictly by the   │ Measuring real-world impact   │
│                     │ quality of their results           │ metrics (false arrest rates)  │
└─────────────────────┴────────────────────────────────────┴───────────────────────────────┘
```

---

## 🔍 Lecture 2: Causes of Unintended Consequences

### 1. Noise, Uncertainty, and Biased Proxies

When true target variables $y$ (e.g. true job performance, true creditworthiness) are unobservable, models rely on **biased proxies** $\tilde{y}$ (e.g. supervisor ratings, past arrest records):

$$\tilde{y}_i = y_i + \delta_{G(i)} + \epsilon_i$$

Where $\delta_{G(i)}$ represents group-systemic bias and $\epsilon_i$ represents unobserved noise.

---

### 2. Interplay of Optimization and Prediction

Combining machine learning predictions $\hat{y}$ with downstream optimization algorithms creates severe systemic vulnerabilities:

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                             Optimization & Prediction Failures                           │
├───────────────────────┬──────────────────────────────────┬───────────────────────────────┤
│ Phenomenon            │ Core Mechanism                   │ Real-World Impact             │
├───────────────────────┼──────────────────────────────────┼───────────────────────────────┤
│ 1. Goodhart's Law     │ "When a measure becomes a target,│ Gaming of predictive metrics  │
│                       │ it ceases to be a good measure"  │ by subjects                   │
├───────────────────────┼──────────────────────────────────┼───────────────────────────────┤
│ 2. Lucas Critique     │ Historical correlations collapse │ Model failure under policy    │
│                       │ when underlying policies change  │ regime shifts                 │
├───────────────────────┼──────────────────────────────────┼───────────────────────────────┤
│ 3. Unobserved         │ Outcomes for rejected entities   │ Selective labels contaminate  │
│    Counterfactuals    │ are never observed               │ future retraining sets        │
└───────────────────────┴──────────────────────────────────┴───────────────────────────────┘
```

---

## 🛠️ Lecture 3: Strategies for Ethical Decision-Making

### 1. Group Residual Bias Correction

For demographic group $g \in G$, residual prediction error is defined as:

$$\text{Bias}_g = \mathbb{E}\left[ \hat{y}_i - y_i \mid G(i) = g \right] = \frac{1}{N_g} \sum_{i \in Group_g} (\hat{y}_i - y_i)$$

Applying group-specific recentering yields unbiased point estimates:

$$\hat{y}_{i, \text{corrected}} = \hat{y}_i - \text{Bias}_{G(i)}$$

---

### 2. Conformal Prediction Intervals & Poset Selection

Rather than relying on single point predictions $\hat{y}_i$, **Conformal Prediction** provides distribution-free prediction intervals $C(X_i)$ with guaranteed finite-sample coverage $(1-\alpha)$:

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                         Conformal Poset Selection Architecture                           │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ Candidate i ──► Point Prediction y_hat_i ──► Conformal Interval [Lower_i, Upper_i]       │
│                                                                  │                       │
│ Selected Candidates ◄── Lower_i >= Threshold Tau ────────────────┘                       │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Interval Bound Derivation
Given empirical quantile $q_{1-\alpha}$ of absolute calibration residuals $R_i = |y_i - \hat{y}_{i, \text{corrected}}|$:

$$C(X_i) = \left[ \hat{y}_{i, \text{corrected}} - q_{1-\alpha}, \; \hat{y}_{i, \text{corrected}} + q_{1-\alpha} \right]$$

#### Poset Lower Bound Selection Rule
In applicant screening, candidates are selected into a Partially Ordered Set (Poset) if their lower interval bound meets or exceeds selection threshold $\tau$:

$$\text{Select Candidate } i \iff \hat{y}_{i, \text{lower}} = \hat{y}_{i, \text{corrected}} - q_{1-\alpha} \ge \tau$$

---

### 3. Multi-Objective Pareto Optimization

When balancing competing objectives (e.g. operational cost $J_{\text{cost}}$ vs. spatial access disparity $J_{\text{equity}}$):

$$\min_{\theta} \; \mathcal{L}(\theta) = w \cdot J_{\text{cost}}(\theta) + (1 - w) \cdot J_{\text{equity}}(\theta), \quad w \in [0, 1]$$

Varying weight parameter $w$ traces out the **Pareto Optimal Frontier**, illustrating non-dominated decision choices.

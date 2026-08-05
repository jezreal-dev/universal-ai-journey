# Assignment Solutions – Ethical AI for Decisions in Today's World

---

## 📝 Assignment 1: Algorithmic Auditing, Conformal Intervals & Pareto Solutions

### 📌 Problem 1 — Algorithmic Parole Auditing & Selective Labels

#### Question Formulation
A state judicial system deploys a risk assessment model to predict recidivism for parole decisions. If the judge denies parole to high-risk individuals, recidivism outcomes for released individuals are observed, but recidivism for incarcerated individuals remains unobserved. What is this methodological flaw called, and how does it distort future model retraining?

#### Verified Solution & Explanation
* **Correct Answer**: **Selective Labels / Unobserved Counterfactual Problem.**
* **Explanation**: Because recidivism is only observed for released individuals, the training dataset suffers from selective label bias. If high-risk individuals are systematically detained, the model never learns whether interventions or post-release programs would have lowered their true recidivism risk.

---

### 📌 Problem 2 — Label Bias Recentering Calculation

#### Question Formulation
In an automated resume screening pipeline, performance ratings for Group A (privileged) have zero mean bias ($\text{Bias}_A = 0.0$), while ratings for Group B (unprivileged) are systematically under-predicted by 4.5 points ($\text{Bias}_B = -4.5$). If an unadjusted model outputs predictions $\hat{y}_A = 72.0$ and $\hat{y}_B = 68.0$, calculate the bias-corrected point predictions.

#### Verified Solution & Explanation
* **Formula**:

$$\hat{y}_{i, \text{corrected}} = \hat{y}_i - \text{Bias}_{G(i)}$$

* **Calculation**:
  - $\hat{y}_{A, \text{corrected}} = 72.0 - 0.0 = \mathbf{72.0}$
  - $\hat{y}_{B, \text{corrected}} = 68.0 - (-4.5) = 68.0 + 4.5 = \mathbf{72.5}$

```python
y_hat_A, bias_A = 72.0, 0.0
y_hat_B, bias_B = 68.0, -4.5

y_corr_A = y_hat_A - bias_A
y_corr_B = y_hat_B - bias_B

print(f"Corrected Score Group A: {y_corr_A:.1f}")
print(f"Corrected Score Group B: {y_corr_B:.1f}")
```

---

### 📌 Problem 3 — Conformal Prediction Interval Derivation

#### Question Formulation
A conformal calibration set produces a 90% empirical error quantile $q_{0.90} = 5.2$. For an applicant with a bias-corrected score $\hat{y}_{\text{corrected}} = 78.0$, derive the 90% conformal prediction interval $C(X)$ and determine if the applicant meets a lower-bound Poset selection threshold $\tau = 72.0$.

#### Verified Solution & Explanation
* **Interval Bounds**:

$$C(X) = [\hat{y}_{\text{corrected}} - q_{0.90}, \; \hat{y}_{\text{corrected}} + q_{0.90}] = [78.0 - 5.2, \; 78.0 + 5.2] = \mathbf{[72.8, \; 83.2]}$$

* **Poset Lower Bound Check**:

$$\hat{y}_{\text{lower}} = 72.8 \ge \tau = 72.0 \implies \mathbf{\text{Applicant Selected Into Poset}}$$

```python
y_corr = 78.0
q_90 = 5.2
tau = 72.0

lower_bound = y_corr - q_90
upper_bound = y_corr + q_90
is_selected = lower_bound >= tau

print(f"Conformal Interval: [{lower_bound:.1f}, {upper_bound:.1f}]")
print(f"Poset Selected? {is_selected} (Lower Bound {lower_bound:.1f} >= Tau {tau:.1f})")
```

---

### 📌 Problem 4 — Multi-Objective Facility Location Trade-Offs

#### Question Formulation
Why is selecting a single "optimal" facility location plan impossible when balancing municipal operational cost against spatial accessibility disparity across neighborhoods?

#### Verified Solution & Explanation
* **Correct Answer**: **Because the objectives are strictly competing. Minimizing total municipal cost concentrates facilities in high-density areas, increasing spatial travel disparity for rural/marginalized neighborhoods.**
* **Strategic Solution**: **Construct the Pareto Optimal Frontier of non-dominated solutions, allowing policymakers to select a point that explicitly encodes community values.**

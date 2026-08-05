# Assignment Solutions – AI and Ethics

---

## 📝 Assignment 1: Algorithmic Fairness, Bias & Alignment Solutions

### 📌 Problem 1 — $\alpha$-Bias Evaluation in Bar Exam Pass Rates

#### Question Formulation
A bar exam dataset is defined to be $\alpha$-biased if the difference in pass rates between Group W and Group B is at least $\alpha = 0.10$. In the data, $60\%$ of Group W pass and $45\%$ of Group B pass. Which statement best describes $\alpha$-bias?

#### Verified Solution & Explanation
* **Correct Answer**: **The dataset is $\alpha$-biased because the pass-rate difference ($0.15$) is at least $\alpha = 0.10$.**
* **Derivation**: Pass Rate Group W = $0.60$, Pass Rate Group B = $0.45$. Pass Rate Delta = $0.60 - 0.45 = 0.15$. Since $0.15 \ge 0.10 = \alpha$, the dataset satisfies the mathematical condition for $\alpha$-bias.

```python
pass_W = 0.60
pass_B = 0.45
alpha = 0.10

delta = pass_W - pass_B
is_alpha_biased = delta >= alpha
print(f"Pass Rate Delta: {delta:.2f} | Alpha: {alpha} | Is Alpha-Biased? {is_alpha_biased}")
```

---

### 📌 Problem 2 — Proxy Variables & Predictive Policing Feedback Loops

#### Question Formulation
A city wants to justify its predictive policing system by noting that it does not explicitly use race or neighborhood as input features. Based on Lecture 2, why is this reasoning flawed?

#### Verified Solution & Explanation
* **Correct Answer**: **Because correlated variables and feedback loops can still amplify bias.**
* **Explanation**: Excluding explicit protected attributes ("fairness through unawareness") fails because proxy variables (e.g. income, prior stops, arrest history) correlate strongly with race, and automated dispatch models generate self-fulfilling feedback loops that concentrate police presence in targeted communities.

---

### 📌 Problem 3 — Label Flipping Optimization in Fairness Logistic Regression

#### Question Formulation
In fairness-aware logistic regression, labels may be flipped using $Y'_i = Y_i (1 - 2 Z_i)$. What happens when $Z_i = 1$?

#### Verified Solution & Explanation
* **Correct Answer**: **The label is flipped (positive $\rightarrow$ negative or negative $\rightarrow$ positive).**
* **Derivation**: For binary labels $Y_i \in \{-1, +1\}$, when $Z_i = 1$, the factor $1 - 2(1) = -1$. Thus $Y'_i = -Y_i$, inverting the ground truth label.

```python
def label_flip(Y_i, Z_i):
    return Y_i * (1 - 2 * Z_i)

print("Positive label with Z=1:", label_flip(1, 1))   # Returns -1 (Flipped)
print("Negative label with Z=1:", label_flip(-1, 1))  # Returns +1 (Flipped)
```

---

### 📌 Problem 4 — Decision Boundary Interventions in Audit Trees

#### Question Formulation
In Lecture 2, label flips are often described as occurring near the decision boundary... How would this typically appear in the audit tree?

#### Verified Solution & Explanation
* **Correct Answer**: **Splits on variables such as test scores, prior counts, or age at values close to decision thresholds.**
* **Explanation**: Optimal classification audit trees that isolate boundary label flips partition the dataset on continuous predictive variables near their critical cutoff thresholds, identifying individuals close to the decision boundary who benefit from fairness recourse.

---

### 📌 Problem 5 — COMPAS & $\epsilon$-Demographic Parity Criteria

#### Question Formulation
Two students are discussing the COMPAS example. Student A says the model is fair because Black and white defendants have similar false positive rates. Student B says the model is fair because Black and white defendants are labeled 'high risk' at similar rates. If $\epsilon$-demographic parity is the fairness criterion being enforced, which student's reasoning aligns with the lecture?

#### Verified Solution & Explanation
* **Correct Answer**: **Student B, because $\epsilon$-demographic parity constrains the rate of positive predictions across groups.**
* **Explanation**: $\epsilon$-Demographic Parity requires equal positive prediction rates $P(\hat{Y}=1 \mid A=a)$ across groups (Student B). Student A describes Equalized Odds / False Positive Rate equality.

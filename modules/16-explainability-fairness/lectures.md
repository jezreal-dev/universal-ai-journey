# Lecture Notes – Explainability & Fairness in AI

---

## 🔍 Lecture 1: Explainable AI (XAI)

### 1. The Imperative for AI Transparency

As machine learning models transition from auxiliary analytics to autonomous decision-makers in clinical diagnostics, financial lending, and judicial risk assessment, opacity becomes a critical liability.

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                             Explainability vs. Accuracy Trade-Off                        │
├──────────────────────┬────────────────────────────┬──────────────────────────────────────┤
│ Model Family         │ Interpretability           │ Predictive Performance (Capacity)    │
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ Linear / Logistic    │ High (Intrinsic Weights)   │ Low to Moderate                      │
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ Decision Trees       │ High (Visual Rules)        │ Moderate                             │
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ XGBoost / Ensembles  │ Moderate (Post-hoc SHAP)   │ High                                 │
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ Deep Neural Networks │ Low (Black-Box Tensors)    │ Very High ⭐                         │
└──────────────────────┴────────────────────────────┴──────────────────────────────────────┘
```

---

### 2. Taxonomy of Explanation Paradigms

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                              Explanation Scope & Scope Taxonomy                          │
├───────────────────┬──────────────────────────────────────────────────────────────────────┤
│ 1. Global         │ Explains overall model behavior across the entire dataset.           │
├───────────────────┼──────────────────────────────────────────────────────────────────────┤
│ 2. Local          │ Explains a single prediction for a specific individual instance.     │
├───────────────────┼──────────────────────────────────────────────────────────────────────┤
│ 3. Counterfactual │ Specifies minimal feature changes needed to flip a model decision.   │
└───────────────────┴──────────────────────────────────────────────────────────────────────┘
```

---

### 3. SHAP (Shapley Additive exPlanations)

Grounded in cooperative game theory, **SHAP** allocates fair feature attributions by measuring a feature's marginal contribution across all possible feature sub-coalitions $S \subseteq F \setminus \{i\}$:

$$\phi_i(v) = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} \left[ v(S \cup \{i\}) - v(S) \right]$$

* $|F|$: Total number of features.
* $S$: Subset of features excluding feature $i$.
* $v(S) = \mathbb{E}[f(x) \mid x_S]$: Value function representing expected model output given subset $S$.

#### Fundamental Axioms of SHAP
1. **Efficiency**: $\sum_{i=1}^{|F|} \phi_i = f(x) - \mathbb{E}[f(x)]$. (Attributions sum to total prediction delta).
2. **Symmetry**: If $v(S \cup \{i\}) = v(S \cup \{j\})$ for all $S$, then $\phi_i = \phi_j$.
3. **Dummy (Null Player)**: If $v(S \cup \{i\}) = v(S)$ for all $S$, then $\phi_i = 0$.
4. **Additivity**: For combined models $f + g$, $\phi_i(f + g) = \phi_i(f) + \phi_i(g)$.

---

### 4. LIME (Local Interpretable Model-Agnostic Explanations)

**LIME** constructs a linear surrogate model $g \in G$ locally around a target instance $x$ by minimizing a local fidelity loss penalized by model complexity:

$$\arg\min_{g \in G} \mathcal{L}(f, g, \pi_x) + \Omega(g)$$

* $f(x)$: Original complex black-box model.
* $g(z')$: Interpretable surrogate model (e.g. sparse linear model).
* $\pi_x(z) = \exp\left(-\frac{D(x, z)^2}{\sigma^2}\right)$: Exponential distance kernel measuring proximity to $x$.
* $\Omega(g)$: Complexity penalty (e.g. non-zero feature count limit).

---

## ⚖️ Lecture 2: AI & Fairness

### 1. Demographic Parity ($\epsilon$-Demographic Parity)

**Demographic Parity** requires that a model's positive decision rate be independent of a protected demographic attribute $A \in \{0, 1\}$ (e.g. sex, race):

$$P(\hat{Y} = 1 \mid A = 0) = P(\hat{Y} = 1 \mid A = 1)$$

#### Disparate Impact Ratio (DPR - Four-Fifths Rule)
$$DPR = \frac{P(\hat{Y} = 1 \mid A = 0)}{P(\hat{Y} = 1 \mid A = 1)} \ge 0.80$$

If $DPR < 0.80$, the decision pipeline is legally flagged for **disparate impact**.

---

### 2. Equalized Odds & Equal Opportunity

1. **Equalized Odds**: Requires equal True Positive Rates (TPR) AND equal False Positive Rates (FPR) across groups:

$$P(\hat{Y} = 1 \mid A = 0, Y = y) = P(\hat{Y} = 1 \mid A = 1, Y = y) \quad \forall y \in \{0, 1\}$$

2. **Equal Opportunity**: Relaxes Equalized Odds to mandate equal True Positive Rates only:

$$P(\hat{Y} = 1 \mid A = 0, Y = 1) = P(\hat{Y} = 1 \mid A = 1, Y = 1)$$

---

### 3. COMPAS Case Study & The Pareto Accuracy-Fairness Frontier

```
   Predictive Accuracy
         ▲
    1.0  │         * Unconstrained Model (Max Accuracy, Low Fairness)
         │        /
    0.8  │       * Fairlearn Mitigated Model (Balanced)
         │      /
    0.6  │     * Equal Odds Enforced Model (High Fairness, Reduced Accuracy)
         │    /
         └─────────────────────────────────────────────────────► Demographic Parity (DPR)
             0.2        0.4        0.6        0.8        1.0
```

Enforcing strict demographic parity constraints on historical data containing systemic bias shifts the model along a **Pareto Frontier**, where increasing group equity introduces a marginal reduction in overall accuracy.

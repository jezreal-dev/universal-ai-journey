# Module Overview – Explainability & Fairness in AI

📅 **Status**: Completed  
🎓 **MIT Open Learning via 3MTT**  
📌 **Module Folder**: `modules/16-explainability-fairness`  
📓 **Recitation & Assignment Notebooks**: [notebooks/mod15_rec1.ipynb](notebooks/mod15_rec1.ipynb) \| [notebooks/mod15_assign1.ipynb](notebooks/mod15_assign1.ipynb)  
📊 **Dataset**: [data/heart.csv](data/heart.csv)

---

## 🌟 Executive Summary

Welcome to **Explainability & Fairness in AI**, the capstone module of the MIT Universal AI Track. As artificial intelligence models are deployed in high-stakes domains—such as healthcare diagnostics, credit scoring, judicial sentencing, and hiring—black-box neural predictions can no longer be accepted without rigorous auditing.

This module explores the mathematical foundations, algorithmic methods, and auditing frameworks required to ensure AI systems are transparent, auditable, and non-discriminatory:
* **Explainable AI (XAI)**: Intrinsic vs. Post-hoc interpretability, Global vs. Local explanations, and Counterfactual recourses.
* **Feature Attribution Mathematics**: **SHAP (Shapley Additive exPlanations)** grounded in cooperative game theory, and **LIME (Local Interpretable Model-agnostic Explanations)** local surrogate models.
* **Computer Vision & Multimodal Interpretability**: Grad-CAM visual heatmaps and Integrated Gradients.
* **Algorithmic Fairness Metrics**: **Demographic Parity** ($\epsilon$-demographic parity, $\alpha$-bias ratio), **Equalized Odds**, and Disparate Impact Ratio ($DPR \ge 0.80$, Four-Fifths Rule).
* **Bias Mitigation & Pareto Frontiers**: Constrained optimization techniques (Fairlearn) and the Pareto trade-off between predictive accuracy and group equity (COMPAS Recidivism Case Study).

---

## 🎯 Key Learning Goals

By completing this module, we have achieved the following core capabilities:

1. **XAI Taxonomies**: Mastered the distinctions between Intrinsic (interpretable-by-design) vs. Post-hoc (after-the-fact) explanations, and Global (model-wide) vs. Local (instance-level) attributions.
2. **Game-Theoretic Feature Attribution (SHAP)**: Derived Shapley marginal contribution values ($\phi_i$), satisfying Efficiency, Symmetry, Dummy, and Additivity axioms.
3. **Local Surrogate Interpretability (LIME)**: Formulated local surrogate loss functions ($\mathcal{L}(f, g, \pi_x) + \Omega(g)$) to approximate complex decision boundaries locally around target samples.
4. **Counterfactual Recourses**: Generated actionable counterfactual explanations specifying minimal feature modifications required to alter adverse model decisions.
5. **Algorithmic Fairness Auditing**: Evaluated Demographic Parity Ratio ($DPR = \frac{P(\hat{Y}=1 \mid A=0)}{P(\hat{Y}=1 \mid A=1)}$) and Equalized Odds across protected demographic attributes (e.g. sex, age).
6. **Fairness-Constrained Optimization**: Implemented constrained Logistic Regression and Fairlearn mitigations to resolve disparate impact while analyzing the Pareto accuracy-fairness trade-off curve.

---

## 🗺️ Module Architecture & File Guide

* 📖 [lectures.md](lectures.md) — Lossless, mathematically rigorous breakdown of Lectures 1–2 covering Explainable AI (SHAP/LIME) and Algorithmic Fairness (Demographic Parity, Equalized Odds, COMPAS Case Study).
* 🧪 [recitations.md](recitations.md) — Comprehensive hands-on notes and Python code synthesizing MIT Recitation 1 (SHAP tabular summaries, LIME text explanations, PyTorch Grad-CAM visual heatmaps).
* 📓 [notebooks/](notebooks/) — Archived interactive Jupyter Notebooks:
  * [mod15_rec1.ipynb](notebooks/mod15_rec1.ipynb) — Recitation 1: Multi-Modal Explainable AI Methods.
  * [mod15_assign1.ipynb](notebooks/mod15_assign1.ipynb) — Assignment 1: Clinical Heart Disease Prediction, SHAP Attribution, Counterfactuals & Demographic Parity Auditing.
* 📝 [assignments.md](assignments.md) — Complete problem formulations, verified solutions, and Python code for Assignment 1 (Parts 1–4).
* 🎯 [conclusion.md](conclusion.md) — Comprehensive Explainability & Fairness Technology Taxonomy table and Full MIT Universal AI Track Graduation Summary.

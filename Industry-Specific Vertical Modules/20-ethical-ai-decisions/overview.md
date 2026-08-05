# Module Overview – Ethical AI for Decisions in Today's World

📅 **Status**: Completed  
🎓 **MIT Open Learning via 3MTT**  
📌 **Module Folder**: `modules/20-ethical-ai-decisions`  
📖 **Source File**: [source_lecture.md](source_lecture.md)  
💻 **Notebook Resource**: [uaiedm1_rec1.ipynb](notebooks/uaiedm1_rec1.ipynb)  
📚 **Research Paper**: [ssrn-3444283.pdf](resources/ssrn-3444283.pdf)

---

## 🌟 Executive Summary

Welcome to **Ethical AI for Decisions in Today's World**, an industry-specific vertical module in the MIT Universal AI Track. As artificial intelligence models transition from passive prediction engines into active decision-making systems, understanding the end-to-end **Data-Model-Decision Pipeline** and its self-reinforcing feedback loops is essential.

This module provides a lossless, mathematically rigorous exploration of algorithmic ethics, decision science, and uncertainty management:
* **The Data-Model-Decision Pipeline**: Deconstructing how raw observations generate predictive models, how predictions drive real-world actions, and how decisions alter future data distributions.
* **Causes of Unintended Consequences**: Analyzing statistical noise, missing data, biased proxies, unobserved counterfactuals, Goodhart's Law, the Lucas Critique, and misaligned objective functions.
* **Conformal Prediction & Bias Correction**: Formulating group-dependent residual bias corrections ($\text{Bias}_g = \mathbb{E}[\hat{y} - y \mid G=g]$) and distribution-free conformal prediction intervals ($[\hat{y}_{\text{corrected}} - q_{1-\alpha}, \hat{y}_{\text{corrected}} + q_{1-\alpha}]$) with guaranteed empirical coverage.
* **Poset Selection Filtering**: Screening candidates under uncertainty using Partially Ordered Set (Poset) lower bounds ($\hat{y}_{\text{lower}} \ge \tau$) to prevent false negative exclusion of unprivileged groups.
* **Multi-Objective Value Alignment**: Balancing competing social objectives (efficiency vs. spatial access equity) in facility location and resource allocation along Pareto optimal frontiers.

---

## 🎯 Key Learning Goals

By completing this module, we have achieved the following core capabilities:

1. **Pipeline Diagnosis**: Mapped the end-to-end Data-Model-Decision pipeline to identify feedback loops, unobserved counterfactuals, and systemic bias injection points.
2. **Group-Dependent Bias Derivation**: Calculated residual prediction bias across demographic groups and implemented group-specific recentering transformations ($\hat{y}_{\text{corrected}} = \hat{y} - \text{Bias}_g$).
3. **Conformal Prediction Intervals**: Derived distribution-free conformal prediction intervals $C(X) = [\hat{y} - q_{1-\alpha}, \hat{y} + q_{1-\alpha}]$, guaranteeing $(1-\alpha)$ coverage under finite-sample distributions.
4. **Poset Selection Implementation**: Built Partially Ordered Set (Poset) decision filters using lower interval bounds to preserve high-potential applicants from under-represented backgrounds.
5. **Multi-Objective Pareto Optimization**: Formulated multi-objective loss functions to navigate trade-offs between average operational cost and maximum spatial access disparity.
6. **Algorithmic Auditing**: Conducted empirical fairness audits on hiring, criminal justice parole, and credit scoring pipelines.

---

## 🗺️ Module Architecture & File Guide

* 📖 [lectures.md](lectures.md) — Lossless breakdown of Lectures 1–3 covering Data-Model-Decision Pipelines, Normative Ethics (Deontology, Utilitarianism, Consequentialism), Causes of Unintended Harm (Noise, Proxies, Goodhart's Law), and Strategies for Responsible AI (Conformal Prediction, Posets, Pareto Tradeoffs).
* 🧪 [recitations.md](recitations.md) — Applied notes and Python code implementations for Fair Hiring using Bias-Corrected Conformal Intervals, Poset Selection, and Multi-Objective Facility Location.
* 📝 [assignments.md](assignments.md) — Problem formulations, verified solutions, and Python code for algorithmic parole auditing, label bias correction, conformal prediction coverage, and spatial resource allocation.
* 🎯 [conclusion.md](conclusion.md) — Comprehensive Ethical AI & Decision Science Technology Taxonomy table and Full Program Completion Summary.

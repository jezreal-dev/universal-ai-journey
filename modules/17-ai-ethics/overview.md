# Module Overview – AI and Ethics

📅 **Status**: Completed  
🎓 **MIT Open Learning via 3MTT**  
📌 **Module Folder**: `modules/17-ai-ethics`  
📖 **Source File**: [source_lecture.md](source_lecture.md)

---

## 🌟 Executive Summary

Welcome to **AI and Ethics**, a foundational governance module in the MIT Universal AI Track. As artificial intelligence models transition from passive analytics to active decision-making agents in credit scoring, criminal sentencing, healthcare, and autonomous text/image generation, ethical alignment and fairness become central engineering requirements.

This module provides a lossless, mathematically rigorous exploration of AI ethics, algorithmic bias, and value alignment:
* **Normative Ethical Frameworks**: Deontology (duty-based rules), Utilitarianism (consequentialist welfare maximization), and Virtue Ethics (character-focused principles).
* **Taxonomy of 4 Bias Sources**: Historical Bias (structural societal inequities), Sampling Bias (non-representative training distributions), Measurement Bias (flawed proxy metrics), and Aggregation Bias (one-size-fits-all model assumptions).
* **3 Core Criteria of Fairness**: **Independence** (Demographic Parity), **Separation** (Equalized Odds / Error Rate Parity), and **Sufficiency** (Predictive Parity / Calibration).
* **Impossibility Theorems**: Formal mathematical proof (**Chouldechova & Kleinberg Impossibility Theorems**) demonstrating that Independence, Separation, and Sufficiency cannot hold simultaneously when base rates differ across demographic groups.
* **AI Alignment & Social Choice Theory**: Objective misspecification (Goodhart's Law, Cobra Effect), alignment algorithms (**RLHF**, **DPO**, **Constitutional AI / RLAIF**), and **Arrow's Impossibility Theorem** governing preference aggregation.

---

## 🎯 Key Learning Goals

By completing this module, we have achieved the following core capabilities:

1. **Ethical Framework Mapping**: Evaluated machine learning deployment scenarios through Deontological, Utilitarian, and Virtue Ethics lenses.
2. **Bias Diagnostics**: Identified and categorized the 4 root sources of bias across data collection, feature engineering, and model aggregation.
3. **Fairness Criteria Formulation**: Defined mathematical formulations for Independence ($P(\hat{Y}=1 \mid A=a) = P(\hat{Y}=1 \mid A=b)$), Separation ($P(\hat{Y}=1 \mid A=a, Y=y) = P(\hat{Y}=1 \mid A=b, Y=y)$), and Sufficiency ($P(Y=1 \mid A=a, \hat{Y}=y) = P(Y=1 \mid A=b, \hat{Y}=y)$).
4. **Impossibility Theorem Proof**: Derived the mathematical conflict proving why calibration and equal error rates are mutually exclusive under unequal group base rates.
5. **Alignment Optimization**: Formulated loss functions for Reinforcement Learning from Human Feedback (**RLHF**) and Direct Preference Optimization (**DPO**).
6. **Social Choice Theory**: Applied **Arrow's Impossibility Theorem** to evaluate preference aggregation in multi-stakeholder AI alignment.

---

## 🗺️ Module Architecture & File Guide

* 📖 [lectures.md](lectures.md) — Lossless breakdown of Lectures 1–3 covering Ethics Survey, 4 Bias Sources, 3 Fairness Criteria, Impossibility Theorems, COMPAS Case Study, RLHF/DPO Alignment, and Social Choice Theory.
* 🧪 [recitations.md](recitations.md) — Applied hands-on notes and Python code implementations for Demographic Parity auditing, Equalized Odds evaluation, Calibration curve calculation, and DPO loss functions.
* 📝 [assignments.md](assignments.md) — Problem formulations, verified solutions, and Python code for AI Ethics & Fairness scenarios ($\alpha$-bias, proxy variable feedback loops, boundary label flipping, COMPAS trade-offs).
* 🎯 [conclusion.md](conclusion.md) — Comprehensive AI Ethics Technology Taxonomy table and Full Program Completion Summary.

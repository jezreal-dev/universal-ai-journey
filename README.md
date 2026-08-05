# MIT Universal AI Training Journey

![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![License MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Graduation Status](https://img.shields.io/badge/Graduation-100%25%20Complete-brightgreen.svg)

A structured log and portfolio documenting my progression through the **MIT Open Learning "Universal AI" program**, completed under the **3MTT initiative**. This repository serves as a reference for theoretical notes, conceptual milestones, and practical Python implementations across machine learning, descriptive statistics, and deep learning pipelines.

---

## 🛠️ Tech Stack & Focus Areas

*   **Languages & Environments**: Python (WSL Ubuntu), Jupyter Notebooks, Git / GitHub
*   **Scientific Computing**: NumPy, Pandas, Descriptive Statistics
*   **Data Visualization**: Seaborn, Matplotlib, Spatial Mapping (Choropleths/Projections)
*   **Modeling Paradigms**: Decision Trees, Random Forests, Ensemble Learning, Supervised & Unsupervised Learning

```bash
# System Quickstart & Environment Setup
git clone https://github.com/jezreal-dev/universal-ai-journey.git
cd universal-ai-journey
source .venv/bin/activate
```

```python
# System Onboarding & Environment Verification
import sys, numpy as np, pandas as pd, torch

print(f"Python {sys.version.split()[0]} | NumPy {np.__version__} | Pandas {pd.__version__} | PyTorch {torch.__version__}")
print("WSL Environment Check: OK ✅")
```

---

## 📂 Applied Labs & Scripts

This repository contains active coding workspaces and scripts built during the program assignments:
*   [check_corr_matrix.py](scripts/check_corr_matrix.py) — Pivots, cleans, and analyzes correlation metrics on raw health risk datasets (BRFSS).
*   [analyse_assignments.py](modules/05-supervised-unsupervised-learning/code/analyse_assignments.py) — Performs OLS regression and out-of-sample prediction diagnostics on state demographic and climate change datasets.
*   [Python Part 1 Labs](modules/02-python-part1/code) — Implementations of expressions, list processing, and procedural logic algorithms.
*   [Python Part 2 Labs](modules/03-python-part2/code) — Object-oriented modeling, CSV parsing, and supervised classification tests (Titanic prediction).

---

## 🗺️ Curriculum Roadmap & Logs

<details open>
<summary><b>Completed Modules (May - June 2026)</b></summary>

| Module | Core Concepts & Labs | Documentation & Artifacts |
| :--- | :--- | :--- |
| **0. Introduction to Universal AI** | AI Paradigms, ML Loops (Perceive-Reason-Act), Ethics & Fairness | [Overview](modules/01-intro-universal-ai/overview.md) / [Lectures](modules/01-intro-universal-ai/lectures.md) / [Recitations](modules/01-intro-universal-ai/recitations.md) / [Assignments](modules/01-intro-universal-ai/assignments.md) / [Conclusion](modules/01-intro-universal-ai/conclusion.md) |
| **1. Python Coding, Part 1** | Procedural flow, logic/conditionals, loops, nested lists, and testing/debugging workflows | [Overview](modules/02-python-part1/overview.md) / [Lectures](modules/02-python-part1/lectures.md) / [Recitations](modules/02-python-part1/recitations.md) / [Assignments](modules/02-python-part1/assignments.md) / [Conclusion](modules/02-python-part1/conclusion.md) |
| **2. Python Coding, Part 2** | Dictionaries, NumPy & Pandas integration, OOP (Classes/Types), and Decision Trees / Random Forests | [Overview](modules/03-python-part2/overview.md) / [Lectures](modules/03-python-part2/lectures.md) / [Recitations](modules/03-python-part2/recitations.md) / [Assignments](modules/03-python-part2/assignments.md) / [Conclusion](modules/03-python-part2/conclusion.md) |
| **3. Data Analytics & Machine Learning** | Data Lifecycle, Descriptive Statistics (Simpson's Paradox), Spatial Mapping, Reproducible Pipelines, Visualization (Data-Ink Ratio) | [Overview](modules/04-data-analytics-ml/overview.md) / [Lectures](modules/04-data-analytics-ml/lectures.md) / [Recitations](modules/04-data-analytics-ml/recitations.md) / [Assignments](modules/04-data-analytics-ml/assignments.md) / [Conclusion](modules/04-data-analytics-ml/conclusion.md) |
| **4. Supervised & Unsupervised Learning** | Linear & Logistic Regression (Framingham), Decision Trees (CART), Performance Metrics (ROC/AUC), Clustering (K-means/Hierarchical), Interpretable Clustering | [Overview](modules/05-supervised-unsupervised-learning/overview.md) / [Lectures](modules/05-supervised-unsupervised-learning/lectures.md) / [Recitations](modules/05-supervised-unsupervised-learning/recitations.md) / [Assignments](modules/05-supervised-unsupervised-learning/assignments.md) \| [A1](modules/05-supervised-unsupervised-learning/assignment_1.md) \| [A2](modules/05-supervised-unsupervised-learning/assignment_2.md) \| [A3](modules/05-supervised-unsupervised-learning/assignment_3.md) / [Conclusion](modules/05-supervised-unsupervised-learning/conclusion.md) |
| **5. Foundations of Neural Networks** | Perceptrons, Multilayer networks, Structured vs. Unstructured Data, Underfitting/Overfitting, Generalization, Embeddings | [Overview](modules/06-foundations-neural-networks/overview.md) / [Lectures](modules/06-foundations-neural-networks/lectures.md) / [Recitations](modules/06-foundations-neural-networks/recitations.md) / [Assignments](modules/06-foundations-neural-networks/assignments.md) / [Conclusion](modules/06-foundations-neural-networks/conclusion.md) |
| **6. Hands-On Deep Learning** | Keras & PyTorch fundamentals, FNN/CNN architectures, hyperparameter tuning, loss optimization | [Overview](modules/07-hands-on-deep-learning/overview.md) / [Lectures](modules/07-hands-on-deep-learning/lectures.md) / [Recitations](modules/07-hands-on-deep-learning/recitations.md) / [Assignments](modules/07-hands-on-deep-learning/assignments.md) / [Conclusion](modules/07-hands-on-deep-learning/conclusion.md) |
| **7. Deep Learning & Computer Vision** | Convolutional networks, max-pooling, spatial feature extraction, MobileNetV2 transfer learning, fine-tuning | [Overview](modules/08-deep-learning-and-computer-vision/overview.md) / [Lectures](modules/08-deep-learning-and-computer-vision/lectures.md) / [Recitations](modules/08-deep-learning-and-computer-vision/recitations.md) / [Assignments](modules/08-deep-learning-and-computer-vision/assignments.md) / [Conclusion](modules/08-deep-learning-and-computer-vision/conclusion.md) |
| **8. Data-Driven Prescriptive AI** | From predictions to prescriptions, $P^2$ stochastic optimization, Optimal Policy Trees (OPT), $OP^2T$ model routing, Rejection Learning, Fairness Diagnostics, Prescriptive Neural Networks (PNN), Mirrored OCTs | [Overview](modules/09-data-driven-prescriptive-ai/overview.md) / [Lectures](modules/09-data-driven-prescriptive-ai/lectures.md) / [Recitations](modules/09-data-driven-prescriptive-ai/recitations.md) / [Assignments](modules/09-data-driven-prescriptive-ai/assignments.md) / [Conclusion](modules/09-data-driven-prescriptive-ai/conclusion.md) |
| **9. Model-Driven Prescriptive AI (Part 1)** | Decision variables, Objectives, Constraints, Linear Programming, Simplex algorithm, Airline Revenue Management (Shadow Prices), Shortest Path, Assignment Matching, Minimum Cost Network Flows (Total Unimodularity), WFP Multi-Commodity & Dietary LP | [Overview](modules/10-model-driven-prescriptive-ai-part1/overview.md) / [Lectures](modules/10-model-driven-prescriptive-ai-part1/lectures.md) / [Recitations](modules/10-model-driven-prescriptive-ai-part1/recitations.md) / [Assignments](modules/10-model-driven-prescriptive-ai-part1/assignments.md) / [Conclusion](modules/10-model-driven-prescriptive-ai-part1/conclusion.md) |
| **10. Model-Driven Prescriptive AI (Part 2)** | Mixed-Integer Optimization (MIO/MILP), Facility Location (Vaccine Distribution), Branch-and-Bound, Multi-Objective Optimization, Pareto Frontiers (School Bus Routing), Nonlinear Optimization (NLO), Convexity, Gradient Descent, Mini-Batch Stochastic Gradient Descent (SGD) | [Overview](modules/11-model-driven-prescriptive-ai-part2/overview.md) / [Lectures](modules/11-model-driven-prescriptive-ai-part2/lectures.md) / [Recitations](modules/11-model-driven-prescriptive-ai-part2/recitations.md) / [Assignments](modules/11-model-driven-prescriptive-ai-part2/assignments.md) / [Conclusion](modules/11-model-driven-prescriptive-ai-part2/conclusion.md) |
| **11. Large Language Models** | Autoregressive generation, Tokenization (BPE/WordPiece), Scaled Dot-Product Attention, Multi-Head Attention, Pretraining vs Fine-tuning vs Prompting, Decoding Samplers (Greedy, Temperature Softmax, Top-k, Top-p), Prompting Strategies (Zero-Shot, Few-Shot, CoT), Internal Reasoning (o1), Alignment (RLHF/DPO), Mixture of Experts (MoE) | [Overview](modules/12-large-language-models/overview.md) / [Lectures](modules/12-large-language-models/lectures.md) / [Recitations](modules/12-large-language-models/recitations.md) / [Assignments](modules/12-large-language-models/assignments.md) / [Conclusion](modules/12-large-language-models/conclusion.md) |
| **12. Generative AI & Creativity** | Task augmentation vs. automation, Economic productivity impact, Divergent/Convergent thinking, Combinatorial/Exploratory/Transformational creativity, Centaur vs. Cyborg collaboration, MIT Solve screening pipeline, Forward/Reverse Diffusion Models ($q(x_t \mid x_{t-1})$), UNet Denoising Loss ($\mathcal{L}_{\text{simple}}$), CLIP Multimodal Contrastive Alignment ($\mathcal{L}_{\text{CLIP}}$), Stable Diffusion v1.5, BLIP image captioning, Prompt styles & CFG parameter tuning | [Overview](modules/13-generative-ai-creativity/overview.md) / [Lectures](modules/13-generative-ai-creativity/lectures.md) / [Recitations](modules/13-generative-ai-creativity/recitations.md) / [Assignments](modules/13-generative-ai-creativity/assignments.md) / [Conclusion](modules/13-generative-ai-creativity/conclusion.md) |
| **13. Multimodal AI** | 6 Core Challenges (Representation, Translation, Alignment, Fusion, Co-learning, Reasoning), HAIM Healthcare Framework (EHR + CXR + ECG + Notes Text), Early vs Intermediate vs Late Fusion, LMM Adapters ($\mathbf{h}_{\text{adapter}}$), Prefix Tuning, Multimodal Hurricane Forecasting, XGBoost & PyTorch Deep Fusion, AUROC & Modality Ablation Studies | [Overview](modules/14-multimodal-ai/overview.md) / [Lectures](modules/14-multimodal-ai/lectures.md) / [Recitations](modules/14-multimodal-ai/recitations.md) / [Assignments](modules/14-multimodal-ai/assignments.md) / [Conclusion](modules/14-multimodal-ai/conclusion.md) |
| **14. LLM-Based Agents & Compound AI** | Symbolic AI Engines (RDF Triples $\langle s, p, o \rangle$, SPARQL, Ontologies), Compound AI Systems (Neurosymbolic Architecture), Retrieval-Augmented Generation (RAG Pipeline), Fixed vs Sliding vs Semantic Chunking, Dense Cosine Similarity ($S_C$), Sparse BM25, Hybrid RRF Search, RAG Topologies (Standard, Contextual, Graph, Agentic RAG), Autonomous ReAct Execution Loops (`Thought -> Action -> Observation -> Answer`) | [Overview](modules/15-llm-based-agents/overview.md) / [Lectures](modules/15-llm-based-agents/lectures.md) / [Recitations](modules/15-llm-based-agents/recitations.md) / [Assignments](modules/15-llm-based-agents/assignments.md) / [Conclusion](modules/15-llm-based-agents/conclusion.md) |
| **15. Explainability & Fairness in AI** | Intrinsic vs Post-hoc XAI, Global vs Local vs Counterfactual Explanations, SHAP (Shapley Additive Attributions $\phi_i$), LIME (Local Surrogate Models), Grad-CAM Heatmaps, Demographic Parity ($\epsilon$-demographic parity), Equalized Odds, Disparate Impact Ratio ($DPR \ge 0.80$), COMPAS Recidivism Case Study, Pareto Accuracy-Fairness Frontier | [Overview](modules/16-explainability-fairness/overview.md) / [Lectures](modules/16-explainability-fairness/lectures.md) / [Recitations](modules/16-explainability-fairness/recitations.md) / [Assignments](modules/16-explainability-fairness/assignments.md) / [Conclusion](modules/16-explainability-fairness/conclusion.md) |
| **16. AI and Ethics** | Normative Ethics (Deontology, Utilitarianism, Virtue Ethics), 4 Bias Sources (Historical, Sampling, Measurement, Aggregation), 3 Fairness Criteria (Independence, Separation, Sufficiency), Chouldechova & Kleinberg Impossibility Theorem, LLM Alignment (RLHF, DPO, Constitutional AI), Arrow's Impossibility Theorem | [Overview](modules/17-ai-ethics/overview.md) / [Lectures](modules/17-ai-ethics/lectures.md) / [Recitations](modules/17-ai-ethics/recitations.md) / [Assignments](modules/17-ai-ethics/assignments.md) / [Conclusion](modules/17-ai-ethics/conclusion.md) |
| **17. AI and Entrepreneurship** | Stevenson Paradigm ("pursuit of opportunity beyond resources controlled"), 5 Venture Evolution Stages, AI Product Lifecycles, Centaur vs Cyborg Team Topologies, GTM Motions (PLG vs SLG), Unit Economics ($LTV/CAC \ge 3.0x$, Payback $\le 12m$), The AI & Entrepreneurship Paradox & Moat Strategy | [Overview](Industry-Specific%20Vertical%20Modules/18-ai-entrepreneurship/overview.md) / [Lectures](Industry-Specific%20Vertical%20Modules/18-ai-entrepreneurship/lectures.md) / [Recitations](Industry-Specific%20Vertical%20Modules/18-ai-entrepreneurship/recitations.md) / [Assignments](Industry-Specific%20Vertical%20Modules/18-ai-entrepreneurship/assignments.md) / [Conclusion](Industry-Specific%20Vertical%20Modules/18-ai-entrepreneurship/conclusion.md) |
| **18. AI and Finance** | Financial Intermediation vs Algorithmic Finance, Narrative vs Facts (Sentiment Analysis), Financial MDPs ($S, A, P, R, \gamma$), Multi-Armed Bandits (UCB1), Q-Learning Bellman Optimality, Deep Q-Networks (DQN), Limit Order Books & Market Impact, FinBERT, SEC Filing Parsing, Look-Ahead & Survivorship Bias Prevention | [Overview](Industry-Specific%20Vertical%20Modules/19-ai-finance/overview.md) / [Lectures](Industry-Specific%20Vertical%20Modules/19-ai-finance/lectures.md) / [Recitations](Industry-Specific%20Vertical%20Modules/19-ai-finance/recitations.md) / [Assignments](Industry-Specific%20Vertical%20Modules/19-ai-finance/assignments.md) / [Conclusion](Industry-Specific%20Vertical%20Modules/19-ai-finance/conclusion.md) |
| **19. Ethical AI for Decisions in Today's World** | Data-Model-Decision Pipeline, Feedback Loops, Normative Ethics (Deontology, Utilitarianism, Consequentialism), Causes of Unintended Harm (Biased Proxies, Goodhart's Law, Lucas Critique, Unobserved Counterfactuals), Group Residual Bias Correction ($\hat{y}_{\text{corrected}} = \hat{y} - \text{Bias}_g$), Distribution-Free Conformal Prediction Intervals ($C(X) = [\hat{y} \pm q_{1-\alpha}]$), Poset Lower-Bound Selection ($\hat{y}_{\text{lower}} \ge \tau$), Multi-Objective Pareto Facility Location | [Overview](Industry-Specific%20Vertical%20Modules/20-ethical-ai-decisions/overview.md) / [Lectures](Industry-Specific%20Vertical%20Modules/20-ethical-ai-decisions/lectures.md) / [Recitations](Industry-Specific%20Vertical%20Modules/20-ethical-ai-decisions/recitations.md) / [Assignments](Industry-Specific%20Vertical%20Modules/20-ethical-ai-decisions/assignments.md) / [Conclusion](Industry-Specific%20Vertical%20Modules/20-ethical-ai-decisions/conclusion.md) |

</details>

<details>
<summary><b>🎓 Graduation Status</b></summary>

- 🎉 **100% COMPLETE** — All 19 Core & Industry Vertical Modules Completed & Verified!

</details>

---

## 📈 Milestone Log

### 🗓️ May 2026
* **May 2026**: Program Enrollment & Cohort Onboarding
* **May 2026**: Completed *Introduction to Universal AI*
* **May 2026**: Completed *Python Coding, Part 1*
* **May 2026**: Completed *Python Coding, Part 2*

### 🗓️ June 2026
* **June 2026**: Completed *Foundations of Data Analytics & Machine Learning*
* **June 2026**: Completed *Supervised & Unsupervised Learning*

### 🗓️ July 2026
* **July 2026**: Completed *Foundations of Neural Networks*
* **July 2026**: Completed *Hands-On Deep Learning*
* **July 2026**: Completed *Deep Learning & Computer Vision*
* **July 2026**: Completed *Data-Driven Prescriptive AI*
* **July 2026**: Completed *Model-Driven Prescriptive AI Part 1*
* **July 2026**: Completed *Model-Driven Prescriptive AI Part 2*
* **July 2026**: Completed *Large Language Models*
* **July 2026**: Completed *Generative AI, the Future of Work, and Human Creativity*
* **July 2026**: Completed *Multimodal AI*

### 🗓️ August 2026
* **August 2026**: Completed *LLM-Based Agents & Compound AI Systems*
* **August 2026**: Completed *Explainability & Fairness in AI*
* **August 2026**: Completed *AI and Ethics*
* **August 2026**: Completed *AI and Entrepreneurship* (Industry Vertical)
* **August 2026**: Completed *AI and Finance* (Industry Vertical)
* **August 2026**: Completed *Ethical AI for Decisions in Today's World* (INDUSTRY VERTICAL MASTERY 🎉)


---

## 🔗 Quick Links & External Resources

*   **Dashboard**: [MIT Learn Portal](https://learn.mit.edu)
*   **Shared Drive**: [MIT Universal AI Resource Folder](https://drive.google.com/drive/folders/1QLZyC7nwjtBhlEApoT5pDmZHmr8evtWV?usp=drive_link)
*   **Support**: [3MTT Help Guide](https://3mttsupport.tawk.help)

---

## 🛡️ License

This repository is curated for personal documentation and portfolio presentation. Open source contributions or review are licensed under the [MIT License](LICENSE).
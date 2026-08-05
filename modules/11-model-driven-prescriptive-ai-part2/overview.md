# Module Overview – Model-Driven Prescriptive AI Part 2

📅 **Status**: Completed  
🎓 **MIT Open Learning via 3MTT**  
📌 **Module Folder**: `modules/11-model-driven-prescriptive-ai-part2`  
📓 **Recitation Notebooks**: [notebooks/mod10_rec2_pt1.ipynb](notebooks/mod10_rec2_pt1.ipynb) \| [notebooks/mod10_rec2_pt2.ipynb](notebooks/mod10_rec2_pt2.ipynb)

---

## 🌟 Executive Summary

Welcome to **Model-Driven Prescriptive AI Part 2**. Building directly upon the linear programming and network flow foundations established in Part 1, this module tackles the full complexity of real-world decision systems: **discrete choices**, **competing objectives**, **nonlinear physical behavior**, and **large-scale stochastic optimization**.

Learners explore how Mixed-Integer Optimization (MIO) guides critical facility placement (such as COVID-19 vaccine distribution), how Multi-Objective Optimization balances cost vs. equity (such as school bus routing), how Taylor series approximations simplify complex functions, and how Nonlinear Optimization and Stochastic Gradient Descent (SGD) power machine learning and neural network parameter fitting.

---

## 🎯 Key Learning Goals

By completing this module, we have achieved the following core capabilities:

1. **Mixed-Integer Optimization (MIO)**: Formulated binary decision variables ($y_j \in \{0, 1\}$) and logical linking constraints ($x_{ij} \le K_j y_j$) to model facility locations, fixed costs, and discrete operational choices (COVID-19 vaccine distribution).
2. **Branch-and-Bound Algorithm**: Understood how linear programming relaxations provide lower/upper bounds to prune search trees efficiently in integer programming solvers.
3. **Multi-Objective Optimization**: Modeled systems with non-commensurable, competing goals, generating **Pareto frontiers** via the weighted-sum and $\epsilon$-constraint methods (applied to Boston Public Schools bus routing and start-time selection), proving why the $\epsilon$-constraint method succeeds on non-convex Pareto boundaries where weighted-sum fails.
4. **Taylor Series Approximations**: Derived 1st and 2nd degree polynomial approximations ($f(x) \approx f(a) + f'(a)(x-a) + \frac{f''(a)}{2}(x-a)^2$) to simplify non-linear functions around operating points.
5. **Nonlinear Optimization (NLO) & KKT Conditions**: Defined unconstrained and constrained nonlinear problems, evaluating gradient vectors $\nabla f(\mathbf{x})$, Hessian matrices $\nabla^2 f(\mathbf{x})$, first/second-order optimality conditions (FONC/SONC/SOSC), and Karush-Kuhn-Tucker (KKT) conditions for constrained optimization.
6. **Convexity & Global Guarantees**: Differentiated between convex functions (where local minima are globally optimal) and non-convex landscapes, applying convex optimization to Ridge Regression.
7. **Stochastic Gradient Descent (SGD) & Neural Networks**: Formulated neural network parameter fitting as empirical risk minimization ($\min_{\mathbf{W}} f(\mathbf{W}) = \frac{1}{n} \sum \mathcal{L}(g(\mathbf{x}_i, \mathbf{W}), y_i)$), comparing Mini-Batch SGD against Full-Batch GD and implementing step-size decay schedules ($\alpha_k = \frac{\alpha_0}{1 + \gamma k}$) to achieve scalable convergence.

---

## 🗺️ Module Architecture & File Guide

* 📖 [lectures.md](lectures.md) — Detailed notes for Lectures 1–4, covering MIO facility placement, multi-objective Pareto trade-offs, Taylor series approximations, KKT conditions, and SGD learning rate schedules.
* 🧪 [recitations.md](recitations.md) — Comprehensive hands-on Python code for PuLP Mixed-Integer Facility Location, 1D Taylor approximations ($f(x) = \frac{1}{x}\sin(x)$), 2D quadratic gradient descent, and Mini-Batch SGD neural network fitting.
* 📓 [notebooks/](notebooks/) — Interactive Jupyter Notebooks from MIT Recitation 2:
  * [mod10_rec2_pt1.ipynb](notebooks/mod10_rec2_pt1.ipynb) — Taylor Approximations, Optimality Conditions & Gradient Descent Step Sizes.
  * [mod10_rec2_pt2.ipynb](notebooks/mod10_rec2_pt2.ipynb) — Stochastic Gradient Descent, Mini-Batch Variance & Neural Network Fitting.
* 📝 [assignments.md](assignments.md) — Verified problem formulations, solutions, and step-by-step mathematical proofs for Assignment 1 (Vaccine distribution & Bus routing) and Assignment 2 (Ridge Regression NLO & SGD hyperparameter tuning).
* 🎯 [conclusion.md](conclusion.md) — Comprehensive synthesis of discrete, multi-objective, and non-linear optimization, bridging model-driven AI to Large Language Model (LLM) loss minimization.

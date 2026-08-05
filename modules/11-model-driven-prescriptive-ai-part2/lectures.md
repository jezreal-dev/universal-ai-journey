# Lecture Notes – Model-Driven Prescriptive AI Part 2

---

## 🏗️ Lecture 1: Mixed Integer Optimization (MIO)

### 1. Overview & Case Study: COVID-19 Vaccine Distribution
Linear programming assumes decision variables are continuous. However, many real-world choices are discrete:
* Should a vaccination site be opened at candidate location $j$? ($y_j \in \{0, 1\}$)
* Should a flight route or bus trip be operated? ($z_{ij} \in \{0, 1\}$)

During the COVID-19 pandemic, public health authorities faced the **Facility Location & Distribution Problem**: selecting which vaccination sites to open to minimize total setup costs and patient travel times while satisfying site capacities.

---

### 2. Mathematical Formulation of Uncapacitated & Capacitated Facility Location

Let $I$ be the set of demand centers (population areas) and $J$ be candidate facility sites.
* $f_j$: Fixed cost to open facility site $j \in J$.
* $c_{ij}$: Transportation/travel cost per unit from facility $j$ to demand center $i$.
* $d_i$: Demand requirement of center $i$.
* $K_j$: Supply capacity of facility site $j$.

#### Decision Variables
* $y_j \in \{0, 1\}$: Binary variable indicating if facility $j$ is opened ($y_j = 1$) or not ($y_j = 0$).
* $x_{ij} \ge 0$: Amount of demand for center $i$ served by facility $j$.

#### Mixed-Integer Linear Program (MILP)

$$\begin{aligned}
\min_{\mathbf{x}, \mathbf{y}} \quad & \sum_{j \in J} f_j y_j + \sum_{i \in I} \sum_{j \in J} c_{ij} x_{ij} \\
\text{subject to} \quad & \sum_{j \in J} x_{ij} = d_i, \quad \forall i \in I \quad \text{(Demand Satisfaction)} \\
& \sum_{i \in I} x_{ij} \le K_j y_j, \quad \forall j \in J \quad \text{(Capacity & Linking Constraint)} \\
& x_{ij} \ge 0, \quad \forall i, j \\
& y_j \in \{0, 1\}, \quad \forall j \in J
\end{aligned}$$

#### Linking Constraints & Big-M Parameter Selection
The constraint $\sum_i x_{ij} \le K_j y_j$ acts as a **logical linking constraint**: if $y_j = 0$, no flow can originate from facility $j$ ($\sum_i x_{ij} \le 0$).

When explicit site capacity $K_j$ is unconstrained, a **Big-M parameter** is used:
$$x_{ij} \le M y_j \quad \text{where } M = \sum_{i \in I} d_i$$

* **Tightness of Relaxations**: Setting $M$ excessively large (e.g., $M = 10^9$) weakens the linear programming (LP) relaxation bounds, forcing the solver to expand far deeper Branch-and-Bound search trees. Tight bounds ($M = \sum d_i$) dramatically accelerate solution convergence.

---

### 3. Solving MIO: Branch-and-Bound Algorithm

Integer Optimization is NP-hard. Solvers utilize **Branch-and-Bound**:

```
                              [ Root Node: LP Relaxation ]
                                     (Lower Bound Z_LP)
                                     /                \
                                    /                  \
                              [y_1 = 0]              [y_1 = 1]
                             /         \            /         \
                       [y_2=0]       [y_2=1]    [y_2=0]     [y_2=1]
                          |             |          |           |
                       Feasible      Infeasible  Optimal    Pruned (Bound)
                      (Z = 120)                             (Z_LP >= 120)
```

1. **LP Relaxation**: Relax integer constraints $y_j \in \{0, 1\}$ to continuous bounds $0 \le y_j \le 1$. The resulting LP provides an absolute **lower bound** ($Z_{\text{LP}} \le Z_{\text{MIO}}^*$) for minimization.
2. **Branching**: Select a fractional variable (e.g., $y_1 = 0.6$) and split the search space into two subproblems ($y_1 = 0$ and $y_1 = 1$).
3. **Bounding & Pruning**: Prune subtrees if:
   * The subproblem is infeasible.
   * The subproblem yields an integer solution (updating the incumbent **upper bound**).
   * The subproblem's LP lower bound exceeds the incumbent integer upper bound ($Z_{\text{LP}} \ge Z_{\text{incumbent}}$).

---

## 🎯 Lecture 2: Multi-Objective Optimization

### 1. Case Study: School Bus Routing & Start Times
Public school districts (e.g., Boston Public Schools) manage hundreds of buses serving thousands of students across multiple schools. Decisions involve competing, non-commensurable goals:
1. **Cost Minimization**: Reduce fleet size and total miles driven.
2. **Student Welfare**: Minimize total bus ride duration and early pick-up times.
3. **Equity**: Ensure uniform ride times across different socioeconomic neighborhoods.

---

### 2. Formulating Multi-Objective Problems

Let $\mathbf{x} \in \Omega$ be the feasible decision vector. We have $k$ objective functions $f_1(\mathbf{x}), f_2(\mathbf{x}), \dots, f_k(\mathbf{x})$ to minimize simultaneously:

$$\min_{\mathbf{x} \in \Omega} \quad \mathbf{F}(\mathbf{x}) = \left( f_1(\mathbf{x}), f_2(\mathbf{x}), \dots, f_k(\mathbf{x}) \right)^T$$

#### Concept of Pareto Dominance
A solution $\mathbf{x}_1$ **dominates** $\mathbf{x}_2$ ($\mathbf{x}_1 \succ \mathbf{x}_2$) if:
1. $f_i(\mathbf{x}_1) \le f_i(\mathbf{x}_2)$ for all $i \in \{1, \dots, k\}$.
2. $f_j(\mathbf{x}_1) < f_j(\mathbf{x}_2)$ for at least one objective $j$.

#### The Pareto Frontier
The set of non-dominated feasible solutions forms the **Pareto Frontier** (trade-off curve). Moving along the Pareto frontier improves one objective only at the expense of worsening another.

```
  Objective 2 (Student Ride Time)
       ▲
       │   x_A (Short ride, high cost)
       │    \
       │     \____ Pareto Frontier (Non-dominated solutions)
       │          \
       │           \____ x_B (Low cost, longer ride)
       │                 
       │              * x_C (Dominated solution)
       └─────────────────────────────────────────► Objective 1 (Bus Fleet Cost)
```

---

### 3. Solution Methods for Multi-Objective LP/MIP

#### Method 1: Weighted-Sum Approach
Combine objectives into a single scalar function using weights $w_i > 0$ ($\sum w_i = 1$):

$$\min_{\mathbf{x} \in \Omega} \quad \sum_{i=1}^k w_i f_i(\mathbf{x})$$

* **Theoretical Limitation (Non-Convex Failure)**: The Weighted-Sum method **can only identify solutions on the convex hull** of the Pareto frontier. If the true Pareto frontier contains non-convex regions (indentations), no set of non-negative weights $w_i$ can generate Pareto points located within non-convex gaps.

#### Method 2: $\epsilon$-Constraint Method
Optimize primary objective $f_1(\mathbf{x})$ while bounding all other objectives $f_i(\mathbf{x}) \le \epsilon_i$:

$$\begin{aligned}
\min_{\mathbf{x} \in \Omega} \quad & f_1(\mathbf{x}) \\
\text{subject to} \quad & f_i(\mathbf{x}) \le \epsilon_i, \quad \forall i = 2, \dots, k
\end{aligned}$$

* **Advantage**: By systematically sweeping bound parameters $\epsilon_i$, the $\epsilon$-Constraint method **successfully discovers non-convex Pareto solutions** that Weighted-Sum skips.

#### Method 3: Lexicographic (Priority) Optimization
Order objectives by priority ($f_1 \gg f_2 \gg \dots \gg f_k$). Solve for $f_1^*$ first, then solve for $f_2$ subject to $f_1(\mathbf{x}) = f_1^*$, and repeat.

---

## 📈 Lecture 3: Continuous Nonlinear Optimization (NLO)

### 1. Continuous Nonlinear Optimization Formulations
When objective functions or constraints contain non-linear components:

$$\begin{aligned}
\min_{\mathbf{x} \in \mathbb{R}^n} \quad & f(\mathbf{x}) \\
\text{subject to} \quad & g_i(\mathbf{x}) \le 0, \quad i = 1, \dots, m \\
& h_j(\mathbf{x}) = 0, \quad j = 1, \dots, p
\end{aligned}$$

---

### 2. Taylor Series Approximations

Complex non-linear functions $f(\mathbf{x})$ can be locally approximated using Taylor expansions around point $\mathbf{a}$.

#### 1-D Taylor Expansion
$$f(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \dots = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x - a)^n$$

* **First-Degree (Linear) Approximation**: $P_1(x) = f(a) + f'(a)(x - a)$
* **Second-Degree (Quadratic) Approximation**: $P_2(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2}(x - a)^2$

#### Case Study Example: $f(x) = \frac{1}{x} \sin(x)$ on $(0, \infty)$
Derivatives via product rule:
$$\begin{aligned}
f'(x) &= \frac{\cos(x)}{x} - \frac{\sin(x)}{x^2} \\
f''(x) &= -\frac{\sin(x)}{x} - \frac{2\cos(x)}{x^2} + \frac{2\sin(x)}{x^3}
\end{aligned}$$
Evaluating at $a = 5$ provides a local quadratic parabola that closely tracks $f(x)$ near $x \in [4, 6]$.

---

### 3. Calculus Foundations: Gradients & Hessians

* **Gradient Vector**: $\nabla f(\mathbf{x}) = \left( \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \dots, \frac{\partial f}{\partial x_n} \right)^T \in \mathbb{R}^n$. Points in the direction of steepest increase.
* **Hessian Matrix**: $\nabla^2 f(\mathbf{x}) = \left[ \frac{\partial^2 f}{\partial x_i \partial x_j} \right]_{n \times n} \in \mathbb{R}^{n \times n}$. Captures local curvature.

---

### 4. Optimality Conditions

#### Unconstrained Optimality
* **First-Order Necessary Condition (FONC)**: If $\mathbf{x}^*$ is a local minimum of a differentiable function $f(\mathbf{x})$, then:
  $$\nabla f(\mathbf{x}^*) = \mathbf{0}$$
* **Second-Order Necessary Condition (SONC)**: The Hessian matrix at $\mathbf{x}^*$ must be Positive Semi-Definite (PSD):
  $$\nabla^2 f(\mathbf{x}^*) \succeq \mathbf{0} \quad (\mathbf{v}^T \nabla^2 f(\mathbf{x}^*) \mathbf{v} \ge 0, \forall \mathbf{v})$$
* **Second-Order Sufficient Condition (SOSC)**: If $\nabla f(\mathbf{x}^*) = \mathbf{0}$ and $\nabla^2 f(\mathbf{x}^*) \succ \mathbf{0}$ (Positive Definite), then $\mathbf{x}^*$ is a strict local minimum.

#### Constrained Optimality: Karush-Kuhn-Tucker (KKT) Conditions
For constrained problem $\min f(\mathbf{x}) \text{ s.t. } g_i(\mathbf{x}) \le 0, h_j(\mathbf{x}) = 0$, define the Lagrangian:
$$\mathcal{L}(\mathbf{x}, \boldsymbol{\mu}, \boldsymbol{\lambda}) = f(\mathbf{x}) + \sum_{i=1}^m \mu_i g_i(\mathbf{x}) + \sum_{j=1}^p \lambda_j h_j(\mathbf{x})$$

The KKT necessary conditions for local optimum $\mathbf{x}^*$ are:
1. **Stationarity**: $\nabla_\mathbf{x} \mathcal{L}(\mathbf{x}^*, \boldsymbol{\mu}^*, \boldsymbol{\lambda}^*) = \nabla f(\mathbf{x}^*) + \sum \mu_i^* \nabla g_i(\mathbf{x}^*) + \sum \lambda_j^* \nabla h_j(\mathbf{x}^*) = \mathbf{0}$
2. **Primal Feasibility**: $g_i(\mathbf{x}^*) \le 0 \, (\forall i), \quad h_j(\mathbf{x}^*) = 0 \, (\forall j)$
3. **Dual Feasibility**: $\mu_i^* \ge 0 \, (\forall i)$
4. **Complementary Slackness**: $\mu_i^* g_i(\mathbf{x}^*) = 0 \, (\forall i)$

---

### 5. Convexity & Global Guarantees

#### Convex Sets & Functions
* A function $f(\mathbf{x})$ is convex if for all $\mathbf{x}, \mathbf{y}$ and $\lambda \in [0, 1]$:
  $$f(\lambda \mathbf{x} + (1-\lambda)\mathbf{y}) \le \lambda f(\mathbf{x}) + (1-\lambda) f(\mathbf{y})$$

#### Fundamental Theorem of Convex Optimization
For any convex optimization problem (convex objective $f(\mathbf{x})$, convex feasible set $\Omega$), **every local minimum is a global minimum**.

---

### 6. Application: Ridge Regression & Gradient Descent

#### Ridge Regression Loss
$$\min_{\boldsymbol{\beta} \in \mathbb{R}^p} \quad \mathcal{L}(\boldsymbol{\beta}) = \frac{1}{2N} \|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|_2^2 + \frac{\lambda}{2} \|\boldsymbol{\beta}\|_2^2$$

Gradient: $\nabla_{\boldsymbol{\beta}} \mathcal{L}(\boldsymbol{\beta}) = -\frac{1}{N} \mathbf{X}^T (\mathbf{y} - \mathbf{X}\boldsymbol{\beta}) + \lambda \boldsymbol{\beta}$.  
Hessian: $\nabla^2 \mathcal{L}(\boldsymbol{\beta}) = \frac{1}{N} \mathbf{X}^T \mathbf{X} + \lambda \mathbf{I} \succ \mathbf{0}$, guaranteeing **strict convexity**.

#### Gradient Descent Update Rule
$$\mathbf{x}^{(k+1)} = \mathbf{x}^{(k)} - \alpha \nabla f(\mathbf{x}^{(k)})$$
where $\alpha > 0$ is the learning rate / step size.

---

## ⚡ Lecture 4: Stochastic Gradient Descent (SGD)

### 1. Neural Network Training as Empirical Risk Minimization
Training a machine learning or deep neural network model with parameters $\boldsymbol{\theta} \in \mathbb{R}^d$ on $N$ labeled samples $\{(\mathbf{x}_i, y_i)\}_{i=1}^N$ is framed as minimizing empirical risk:

$$\min_{\boldsymbol{\theta} \in \mathbb{R}^d} \quad f(\boldsymbol{\theta}) = \frac{1}{N} \sum_{i=1}^N \mathcal{L}_i(\boldsymbol{\theta})$$

where $\mathcal{L}_i(\boldsymbol{\theta}) = \ell(y_i, g(\mathbf{x}_i; \boldsymbol{\theta}))$ is the loss on sample $i$.

---

### 2. Full-Batch GD vs. Mini-Batch SGD

#### Full-Batch Gradient Descent (GD)
$$\boldsymbol{\theta}^{(k+1)} = \boldsymbol{\theta}^{(k)} - \alpha \left( \frac{1}{N} \sum_{i=1}^N \nabla \mathcal{L}_i(\boldsymbol{\theta}^{(k)}) \right)$$
* **Limitation**: Evaluates all $N$ samples per iteration ($\mathcal{O}(N \cdot d)$ complexity).

#### Mini-Batch Stochastic Gradient Descent (SGD)
Sample mini-batch $B_k \subset \{1, \dots, N\}$ of size $|B_k| = m \ll N$:

$$\boldsymbol{\theta}^{(k+1)} = \boldsymbol{\theta}^{(k)} - \alpha_k \left( \frac{1}{m} \sum_{i \in B_k} \nabla \mathcal{L}_i(\boldsymbol{\theta}^{(k)}) \right)$$

* **Unbiased Gradient Estimator**: $\mathbb{E}_{B_k} \left[ \frac{1}{m} \sum_{i \in B_k} \nabla \mathcal{L}_i(\boldsymbol{\theta}) \right] = \nabla f(\boldsymbol{\theta})$.
* **Efficiency**: Reduces per-iteration complexity to $\mathcal{O}(m \cdot d)$.

---

### 3. Step Size & Learning Rate Decay Schedules

To ensure convergence under mini-batch gradient variance, learning rates must satisfy the **Robbins-Monro Conditions**:

$$\sum_{k=1}^\infty \alpha_k = \infty \quad \text{and} \quad \sum_{k=1}^\infty \alpha_k^2 < \infty$$

#### Popular Learning Rate Decay Formula
$$\alpha_k = \frac{\alpha_0}{1 + \gamma k} \quad \text{or} \quad \alpha_k = \alpha_0 \cdot e^{-\gamma k}$$

---

### 4. Advanced Optimizer Variants

1. **Momentum SGD**: Incorporates past step inertia $\mathbf{v}^{(k)}$ to accelerate along narrow valleys:
   $$\mathbf{v}^{(k+1)} = \beta \mathbf{v}^{(k)} + \alpha \nabla f_{B_k}(\boldsymbol{\theta}^{(k)}), \quad \boldsymbol{\theta}^{(k+1)} = \boldsymbol{\theta}^{(k)} - \mathbf{v}^{(k+1)}$$
2. **RMSprop & Adam**: Adapts per-parameter step sizes using running estimates of first ($\mathbf{m}_t$) and second ($\mathbf{v}_t$) uncentered gradient moments.

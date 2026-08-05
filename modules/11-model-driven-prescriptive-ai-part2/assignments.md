# Assignment Notes & Solutions – Model-Driven Prescriptive AI Part 2

---

## 📝 Assignment 1: Mixed-Integer & Multi-Objective Optimization

### Overview
Assignment 1 covers discrete facility location choices in public health logistics and Pareto multi-objective trade-off analysis in urban transportation.

---

### Part 1: COVID-19 Vaccine Distribution Facility Location

#### Scenario
A regional health authority evaluates 3 candidate clinic sites ($J_1, J_2, J_3$) to distribute vaccines to 3 communities ($I_1, I_2, I_3$).
* Fixed setup costs: $f_1 = \$1,000$, $f_2 = \$1,200$, $f_3 = \$800$.
* Clinic capacities: $K_1 = 500$, $K_2 = 600$, $K_3 = 400$ doses.
* Community demands: $d_1 = 300$, $d_2 = 400$, $d_3 = 250$ doses (Total demand = 950 doses).
* Unit delivery costs ($c_{ij}$ per dose):

$$\mathbf{C} = \begin{pmatrix}
2 & 4 & 5 \\
3 & 1 & 4 \\
6 & 3 & 2
\end{pmatrix}$$

#### MILP Formulation

$$\begin{aligned}
\min_{\mathbf{x}, \mathbf{y}} \quad & 1000 y_1 + 1200 y_2 + 800 y_3 + \sum_{i=1}^3 \sum_{j=1}^3 c_{ij} x_{ij} \\
\text{subject to} \quad & \sum_{j=1}^3 x_{1j} = 300, \quad \sum_{j=1}^3 x_{2j} = 400, \quad \sum_{j=1}^3 x_{3j} = 250 \\
& \sum_{i=1}^3 x_{i1} \le 500 y_1, \quad \sum_{i=1}^3 x_{i2} \le 600 y_2, \quad \sum_{i=1}^3 x_{i3} \le 400 y_3 \\
& x_{ij} \ge 0, \quad y_j \in \{0, 1\}
\end{aligned}$$

#### Questions & Verified Solutions

* **Q1: What are the binary decision variables?**  
  *Solution*: $y_j \in \{0, 1\}$ for $j \in \{1, 2, 3\}$, where $y_j = 1$ if clinic site $j$ is opened, and $0$ otherwise.

* **Q2: Why are linking constraints required?**  
  *Solution*: Linking constraints ($\sum_i x_{ij} \le K_j y_j$) ensure that doses can only be shipped from site $j$ if site $j$ incurs its fixed setup cost ($y_j = 1$).

* **Q3: Solve for the optimal clinic opening decisions $\mathbf{y}^*$.**  
  *Solution*:  
  * Opening only $J_1$ and $J_3$: Capacity = $500 + 400 = 900 < 950$ (Infeasible).  
  * Opening $J_1$ and $J_2$: Capacity = $500 + 600 = 1100 \ge 950$. Fixed cost = $\$2,200$.  
  * Opening $J_2$ and $J_3$: Capacity = $600 + 400 = 1000 \ge 950$. Fixed cost = $\$2,000$.  
  * Optimal solution: Open **$J_2$ and $J_3$** ($y_1^* = 0, y_2^* = 1, y_3^* = 1$).

* **Q4: Optimal Shipping Allocation $\mathbf{x}^*$.**  
  *Solution*:  
  * Community $I_1$ ($d_1=300$): Ships from $J_2$ ($c_{12}=4$, $x_{12}=300$).  
  * Community $I_2$ ($d_2=400$): Ships from $J_2$ ($c_{22}=1$, $x_{22}=300$, reaching $J_2$ cap limit of 600) and $J_3$ ($c_{23}=4$, $x_{23}=100$).  
  * Community $I_3$ ($d_3=250$): Ships from $J_3$ ($c_{33}=2$, $x_{33}=250$).

* **Q5: Calculate Minimum Total Cost.**  
  *Solution*:  
  Fixed cost = $\$1,200 + \$800 = \$2,000$.  
  Shipping cost = $4(300) + 1(300) + 4(100) + 2(250) = 1200 + 300 + 400 + 500 = \$2,400$.  
  Total Cost = $2000 + 2400 = \mathbf{\$4,400}$.

---

### Part 2: School Bus Route Multi-Objective Trade-Off

#### Scenario
A school district evaluates 3 bus routing plans ($A, B, C$) across two objectives: Fleet Operating Cost ($f_1$ in thousands) and Average Student Ride Time ($f_2$ in minutes).

* Plan $A$: $f_1 = \$500\text{k}$, $f_2 = 45\text{ mins}$
* Plan $B$: $f_1 = \$650\text{k}$, $f_2 = 30\text{ mins}$
* Plan $C$: $f_1 = \$700\text{k}$, $f_2 = 35\text{ mins}$

#### Questions & Verified Solutions

* **Q1: Which plan is Pareto dominated?**  
  *Solution*: **Plan $C$** is strictly dominated by Plan $B$ ($f_1(B) = \$650\text{k} < \$700\text{k}$ and $f_2(B) = 30\text{ mins} < 35\text{ mins}$). Plan $C$ costs more AND takes longer.

* **Q2: Identify the Pareto Frontier.**  
  *Solution*: The Pareto frontier consists of non-dominated plans **$\text{Pareto} = \{A, B\}$**.

* **Q3: Weighted-Sum Selection.**  
  *Solution*: If the district assigns weight $w_1 = 0.6$ to cost and $w_2 = 0.4$ to ride time:  
  * Score($A$) = $0.6(500) + 0.4(45) = 300 + 18 = 318$.  
  * Score($B$) = $0.6(650) + 0.4(30) = 390 + 12 = 402$.  
  * **Plan $A$** achieves the lower weighted score.

---

## 💻 Assignment 2: Nonlinear Optimization & SGD Tuning

### Overview
Assignment 2 explores gradient calculations, convexity conditions, and mini-batch SGD hyperparameter sensitivity.

---

### Part 1: Convexity & Gradient Analysis for Ridge Regression

#### Loss Function
$$f(\beta_1, \beta_2) = \frac{1}{2}(\beta_1 - 2)^2 + (\beta_2 + 1)^2 + \frac{\lambda}{2}(\beta_1^2 + \beta_2^2) \quad \text{with } \lambda = 0.1$$

#### Questions & Verified Solutions

* **Q1: Compute the Gradient Vector $\nabla f(\beta_1, \beta_2)$.**  
  *Solution*:  
  $$\frac{\partial f}{\partial \beta_1} = (\beta_1 - 2) + 0.1 \beta_1 = 1.1 \beta_1 - 2$$
  $$\frac{\partial f}{\partial \beta_2} = 2(\beta_2 + 1) + 0.1 \beta_2 = 2.1 \beta_2 + 2$$
  $$\nabla f(\beta_1, \beta_2) = \begin{pmatrix} 1.1 \beta_1 - 2 \\ 2.1 \beta_2 + 2 \end{pmatrix}$$

* **Q2: Compute the Hessian Matrix $\nabla^2 f(\beta_1, \beta_2)$ and check convexity.**  
  *Solution*:  
  $$\nabla^2 f = \begin{pmatrix} 1.1 & 0 \\ 0 & 2.1 \end{pmatrix}$$
  Since eigenvalues are $\lambda_1 = 1.1 > 0$ and $\lambda_2 = 2.1 > 0$, the Hessian is **Positive Definite ($\nabla^2 f \succ \mathbf{0}$)** everywhere, guaranteeing strict convexity.

* **Q3: Calculate the Analytical Global Minimum $(\beta_1^*, \beta_2^*)$.**  
  *Solution*: Setting $\nabla f = \mathbf{0}$:  
  $$1.1 \beta_1^* - 2 = 0 \implies \beta_1^* = \frac{2}{1.1} = \mathbf{1.8182}$$
  $$2.1 \beta_2^* + 2 = 0 \implies \beta_2^* = -\frac{2}{2.1} = \mathbf{-0.9524}$$

---

### Part 2: Stochastic Gradient Descent (SGD) Hyperparameter Analysis

#### Scenario
Training a logistic regression classifier on $N = 10,000$ patient records using mini-batch SGD under different learning rates $\alpha_0 \in \{0.5, 0.01, 0.0001\}$ and batch sizes $m \in \{1, 64, 10000\}$.

#### Questions & Verified Solutions

* **Q1: Impact of Large Learning Rate ($\alpha_0 = 0.5$ without decay).**  
  *Solution*: The loss trajectory **diverges or oscillates wildly** near the minimum due to gradient steps overshooting the narrow valley.

* **Q2: Trade-off between Batch Size $m=1$ (Pure SGD) vs. $m=64$ (Mini-Batch SGD) vs. $m=10,000$ (Full-Batch GD).**  
  *Solution*:  
  * $m=1$: High gradient variance per step; fast per-iteration computation, but noisy convergence trajectory.  
  * $m=10,000$: Smooth loss curve, but extremely slow per-iteration time.  
  * $m=64$: **Optimal balance** between GPU vectorization speed and stochastic noise for escaping saddle points.

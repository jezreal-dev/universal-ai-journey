# Lecture Notes – Model-Driven Prescriptive AI Part 1

---

## 📚 Lecture 1: Introduction to Optimization

### 1. Overview & Conceptual Foundations
Optimization is the science and engineering of making the best possible decisions under explicit real-world constraints. In the broader AI landscape, analytics progresses through three distinct layers:
1. **Descriptive Analytics**: Data acquisition, management, and visualization (dashboards showing *what happened*).
2. **Predictive AI**: Machine learning, deep learning, and statistical inference (forecasting *what will happen*).
3. **Prescriptive AI**: Optimization, simulation, and decision systems (guiding *what action to take* to maximize value).

```
[ Data ] ──► [ Descriptive Analytics ] ──► [ Predictive AI ] ──► [ Prescriptive AI ] ──► [ System Value ]
                  (Dashboards)              (ML / Deep Learning)     (Optimization)
```

---

### 2. Optimization in Prediction vs. Prescription

Optimization plays a critical role in **both** predictive and prescriptive AI:

| AI Layer | Role of Optimization | Mathematical Task | Example Applications |
| :--- | :--- | :--- | :--- |
| **Predictive AI** (Model Fitting) | Parameter Estimation | Minimize loss function $\mathcal{L}(\theta) = \sum_{i} \ell(y_i, f(x_i; \theta))$ | OLS, Logistic Regression, CNN/Transformer weight optimization via Gradient Descent |
| **Prescriptive AI** (Decision Making) | Action Selection | Optimize objective $f(x)$ subject to system constraints $g_i(x) \le 0$ | Vehicle routing (UPS ORION), Airline fleet assignment, WFP food distribution |

#### Problem Complexity Spectrum
* **Prediction-Heavy Problems** (e.g., Loan Approval): High predictive complexity (estimating default risk), but straightforward action rule (if $\hat{p}_{\text{repay}} > \tau$, approve loan).
* **Prescription-Heavy Problems** (e.g., Power Grid Dispatch): High prescriptive complexity (spatiotemporal coupling across generators, line limits, ramp rates) even with near-perfect demand predictions.
* **Combined Problems** (e.g., Disaster Relief / Evacuation): Require deep predictive modeling (disaster trajectory) **and** complex multi-commodity network optimization (shelter allocation, medical supply routing).

---

### 3. Canonical Mathematical Formulation

An optimization model consists of three core components:
1. **Decision Variables**: $\mathbf{x} = (x_1, x_2, \dots, x_n) \in \mathbb{R}^n$ representing choices under controller control.
2. **Objective Function**: $f(\mathbf{x}): \mathbb{R}^n \to \mathbb{R}$ measuring cost, profit, energy, or service quality.
3. **Constraints**: Functions $g_i(\mathbf{x}) \le 0$ for $i=1, \dots, m$ defining the **feasible region** $\Omega = \{\mathbf{x} \in \mathbb{R}^n \mid g_i(\mathbf{x}) \le 0, \forall i\}$.

$$\begin{aligned}
\min_{\mathbf{x} \in \mathbb{R}^n} \quad & f(\mathbf{x}) \\
\text{subject to} \quad & g_i(\mathbf{x}) \le 0, \quad \forall i = 1, \dots, m
\end{aligned}$$

---

### 4. Taxonomy of Optimization Problems

```
                           ┌──────────────────────────────┐
                           │     Optimization Problems    │
                           └──────────────┬───────────────┘
                                          │
                  ┌───────────────────────┴───────────────────────┐
                  ▼                                               ▼
     ┌─────────────────────────┐                     ┌─────────────────────────┐
     │ Continuous Optimization │                     │  Discrete Optimization  │
     └────────────┬────────────┘                     └────────────┬────────────┘
                  │                                               │
        ┌─────────┴─────────┐                           ┌─────────┴─────────┐
        ▼                   ▼                           ▼                   ▼
┌───────────────┐   ┌───────────────┐           ┌───────────────┐   ┌───────────────┐
│ Linear (LP)   │   │Nonlinear (NLP)│           │ Integer (IP)  │   │ Mixed-Integer │
│  f, g linear  │   │ f or g curved │           │ x_j \in \mathbb{Z}│   │  (MIP/MILP)   │
└───────────────┘   └───────────────┘           └───────────────┘   └───────────────┘
```

1. **Linear Optimization (LP)**: Objective function $f(\mathbf{x}) = \mathbf{c}^T \mathbf{x}$ and constraints $\mathbf{A}\mathbf{x} \le \mathbf{b}$ are all linear. Convex, globally solvable via Simplex/Interior-point.
2. **Integer Optimization (IP / MILP)**: Some or all decision variables are restricted to integers ($x_j \in \mathbb{Z}$) or binary decisions ($x_j \in \{0, 1\}$). NP-hard, solved via Branch-and-Bound / Branch-and-Cut.
3. **Nonlinear Optimization (NLP)**: Objective or constraints contain non-linear terms. May be convex (global minimum reachable via gradient methods) or non-convex (multiple local minima).

---

### 5. Historical Foundations & Computational Evolution

* **1600s (Fermat & Newton)**: Single-variable calculus optimization ($\frac{df}{dx} = 0$).
* **1750s (Euler & Lagrange)**: Multi-variable unconstrained optimization via gradient ($\nabla f = \mathbf{0}$) and constrained optimization via Lagrangian multipliers ($\mathcal{L}(\mathbf{x}, \boldsymbol{\lambda}) = f(\mathbf{x}) + \boldsymbol{\lambda}^T \mathbf{g}(\mathbf{x})$).
* **1947 (George Dantzig)**: Development of the **Simplex Algorithm** for Linear Programming, revolutionizing industrial operations planning.
* **1990s–Present (Industrial Optimization at Scale)**: Enterprise routing and analytics, such as **UPS ORION** (On-Road Integrated Optimization and Navigation), saving over 100 million miles driven per year.

---

## ✈️ Lecture 2: Linear Optimization & Airline Revenue Management

### 1. Case Study: Network Revenue Management (RM)
Airlines must sell seats across complex flight networks with multiple fare classes (e.g., Business, Flexible Economy, Discount Economy) to maximize revenue under fixed aircraft capacities and uncertain demand.

#### Single-Flight vs. Network RM
* **Single-Flight Heuristic**: Manages each flight leg independently using nested booking limits (e.g., Littlewood's Rule / EMSR).
* **Network Revenue Management**: Jointly optimizes seat allocations across an entire hub-and-spoke network, taking into account multi-leg itineraries (e.g., BOS $\to$ ORD $\to$ LAX).

---

### 2. Mathematical Formulation of Network LP

Consider a flight network with flight legs $l \in L$ each with capacity $C_l$, and itineraries/fare products $j \in J$ with price $p_j$ and estimated demand $D_j$.
Let $A_{lj} = 1$ if itinerary $j$ uses flight leg $l$, and $0$ otherwise.
Decision variable: $x_j \ge 0$, number of seats sold for itinerary product $j$.

$$\begin{aligned}
\max_{\mathbf{x}} \quad & \sum_{j \in J} p_j x_j \\
\text{subject to} \quad & \sum_{j \in J} A_{lj} x_j \le C_l, \quad \forall l \in L \quad \text{(Leg Capacity Constraints)} \\
& 0 \le x_j \le D_j, \quad \forall j \in J \quad \text{(Demand Upper Bounds)}
\end{aligned}$$

---

### 3. Dual Variables & Shadow Prices

The dual variable $\pi_l \ge 0$ associated with leg constraint $\sum A_{lj} x_j \le C_l$ represents the **shadow price** (marginal value) of flight capacity:

$$\pi_l = \frac{\partial \text{Revenue}^*}{\partial C_l}$$

#### Strategic Managerial Insights:
* **Opportunity Cost**: Product $j$ should be accepted only if its price exceeds the sum of the shadow prices of the legs it consumes:
  $$p_j \ge \sum_{l \in L} A_{lj} \pi_l$$
* **Edge of Optimization**: Network LP prevents greedy over-booking of low-fare local passengers when high-fare connecting passengers generate higher network-wide revenue.

---

### 4. Geometry of Linear Programming & The Simplex Method

* **Convex Polyhedron**: The feasible set $\Omega = \{\mathbf{x} \ge \mathbf{0} \mid \mathbf{A}\mathbf{x} \le \mathbf{b}\}$ forms a convex polytope in $\mathbb{R}^n$.
* **Fundamental Theorem of LP**: If an optimal solution exists, at least one extreme point (corner point / vertex) of the feasible polyhedron is optimal.
* **Simplex Algorithm**:
  1. Start at an initial feasible vertex.
  2. Evaluate adjacent vertices along edge directions with positive reduced cost.
  3. Move along the improving edge until a new vertex is reached (pivot step).
  4. Terminate when all adjacent reduced costs are non-positive.

---

## 🌐 Lecture 3: Network Flows & Platform Matching

### 1. Network Platforms & Graph Representations
Many modern platforms (ride-hailing, cloud routing, logistics) map naturally onto directed graphs $G = (V, E)$ with nodes $V$ and directed edges $E$.

```
   (Node i) ────────── Edge (i, j) with cost c_ij, capacity u_ij ──────────► (Node j)
```

---

### 2. Shortest Path Problem

Find the minimum cost path from source node $s$ to destination node $t$.
Decision variable: $x_{ij} \in \{0, 1\}$, indicating whether edge $(i, j) \in E$ is traversed.

$$\begin{aligned}
\min_{\mathbf{x}} \quad & \sum_{(i,j) \in E} c_{ij} x_{ij} \\
\text{subject to} \quad & \sum_{j: (i,j) \in E} x_{ij} - \sum_{j: (j,i) \in E} x_{ji} = \begin{cases} 1 & \text{if } i = s \\ -1 & \text{if } i = t \\ 0 & \text{otherwise} \end{cases}, \quad \forall i \in V \\
& x_{ij} \ge 0, \quad \forall (i,j) \in E
\end{aligned}$$

---

### 3. Assignment Problem (Rideshare Platform Matching)

Match a set of drivers $K$ to a set of riders $R$ to minimize total pickup distance/time.
Decision variable: $x_{kr} \in \{0, 1\}$, indicating driver $k$ is assigned to rider $r$. Cost: $c_{kr}$.

$$\begin{aligned}
\min_{\mathbf{x}} \quad & \sum_{k \in K} \sum_{r \in R} c_{kr} x_{kr} \\
\text{subject to} \quad & \sum_{r \in R} x_{kr} \le 1, \quad \forall k \in K \quad \text{(Driver Capacity)} \\
& \sum_{k \in K} x_{kr} = 1, \quad \forall r \in R \quad \text{(Rider Service Requirement)} \\
& x_{kr} \ge 0, \quad \forall k, r
\end{aligned}$$

---

### 4. Minimum Cost Network Flow Problem (MCNFP)

The general network flow model unifies shortest path, assignment, and transportation problems.
Each node $i \in V$ has net supply/demand $b_i$ ($\sum b_i = 0$). Edge $(i,j)$ has cost $c_{ij}$ and capacity $u_{ij}$.

$$\begin{aligned}
\min_{\mathbf{x}} \quad & \sum_{(i,j) \in E} c_{ij} x_{ij} \\
\text{subject to} \quad & \sum_{j: (i,j) \in E} x_{ij} - \sum_{j: (j,i) \in E} x_{ji} = b_i, \quad \forall i \in V \quad \text{(Flow Conservation)} \\
& 0 \le x_{ij} \le u_{ij}, \quad \forall (i,j) \in E
\end{aligned}$$

#### Total Unimodularity (TU) Property
The node-arc incidence matrix $\mathbf{A}$ of a directed graph is **totally unimodular** (every square submatrix has determinant $-1, 0,$ or $+1$). Consequently, if supplies $b_i$ and capacities $u_{ij}$ are integer, solving the linear relaxation guarantees **pure integer optimal solutions** without requiring integer constraints!

---

## 🍲 Lecture 4: The Analytics of Zero Hunger

### 1. Humanitarian Supply Chain Context
The United Nations World Food Programme (WFP) delivers food assistance to over 100 million people annually. Logistics involve complex trade-offs across procurement options (local vs. global), transport modes (road, rail, sea), and strict nutritional guidelines.

---

### 2. Multi-Commodity Network Flow Model

Multiple distinct food commodities $k \in K$ (e.g., rice, beans, vegetable oil) share transport network capacity $u_{ij}$.

$$\begin{aligned}
\min_{\mathbf{x}} \quad & \sum_{k \in K} \sum_{(i,j) \in E} c_{ij}^k x_{ij}^k \\
\text{subject to} \quad & \sum_{j} x_{ij}^k - \sum_{j} x_{ji}^k = b_i^k, \quad \forall i \in V, \forall k \in K \quad \text{(Commodity Flow Balance)} \\
& \sum_{k \in K} x_{ij}^k \le u_{ij}, \quad \forall (i,j) \in E \quad \text{(Shared Arc Capacity)} \\
& x_{ij}^k \ge 0, \quad \forall (i,j), \forall k
\end{aligned}$$

---

### 3. Nutritionally-Constrained Diet Optimization

Let $N$ be the set of required nutrients (energy, protein, fat, iron, vitamins). Food commodity $k$ provides $a_{nk}$ units of nutrient $n$ per kg at cost $p_k$. Daily requirements: $[L_n, U_n]$.

$$\begin{aligned}
\min_{\mathbf{y}} \quad & \sum_{k \in K} p_k y_k \\
\text{subject to} \quad & L_n \le \sum_{k \in K} a_{nk} y_k \le U_n, \quad \forall n \in N \quad \text{(Nutritional Bounds)} \\
& y_k \ge 0, \quad \forall k \in K
\end{aligned}$$

---

### 4. Applied Impact & WFP Deployment
By integrating diet optimization directly into multi-commodity network flow models, WFP's **Optimus** platform achieved:
* **15%–20% reduction** in total supply chain procurement and delivery costs.
* **Expanded reach**, feeding millions more beneficiaries under fixed donor budgets.
* **Iterative refinement**: Model outputs guide real-time policy adjustments between local food procurement and international shipments.

# Assignment Notes & Solutions – Model-Driven Prescriptive AI Part 1

---

## 📝 Assignment 1: Linear Optimization & Airline Revenue Management

### Overview
Assignment 1 evaluates mastery of linear optimization principles, moving from single-period production planning to multi-leg airline network revenue management.

---

### Part 1: Production Planning & Resource Allocation

#### Scenario
A manufacturer produces two items ($P_1$ and $P_2$) utilizing Labor (hours) and Raw Material (kg).
* Profit per unit: $P_1 = \$40$, $P_2 = \$30$.
* Labor requirement: $P_1$ requires 2 hrs, $P_2$ requires 1 hr. Total available labor = 100 hrs.
* Material requirement: $P_1$ requires 1 kg, $P_2$ requires 2 kg. Total available material = 80 kg.

#### LP Formulation

$$\begin{aligned}
\max_{x_1, x_2 \ge 0} \quad & 40 x_1 + 30 x_2 \\
\text{subject to} \quad & 2 x_1 + x_2 \le 100 \quad \text{(Labor Constraint)} \\
& x_1 + 2 x_2 \le 80 \quad \text{(Material Constraint)}
\end{aligned}$$

#### Questions & Verified Solutions

* **Q1: What are the decision variables?**  
  *Solution*: $x_1$ = units of $P_1$ produced, $x_2$ = units of $P_2$ produced ($x_1, x_2 \ge 0$).

* **Q2: Write the objective function.**  
  *Solution*: Maximize $Z = 40x_1 + 30x_2$.

* **Q3: Identify the corner points (extreme points) of the feasible region.**  
  *Solution*: Intersecting constraint boundaries gives $(0,0)$, $(50,0)$, $(0,40)$, and the intersection of $2x_1+x_2=100$ and $x_1+2x_2=80 \implies (x_1^*, x_2^*) = (40, 20)$.

* **Q4: What is the optimal production quantity and maximum profit?**  
  *Solution*: $x_1^* = 40$, $x_2^* = 20$.  
  $Z^* = 40(40) + 30(20) = 1600 + 600 = \mathbf{\$2,200}$.

* **Q5: Calculate the shadow price of labor.**  
  *Solution*: Increasing labor by 1 unit to 101 gives system solution $(x_1^*, x_2^*) = (40.667, 19.667)$, $Z^* = 2216.67$. Shadow price $\pi_{\text{labor}} = \mathbf{\$16.67}$ per hour.

* **Q6: Calculate the shadow price of raw material.**  
  *Solution*: Increasing material by 1 unit to 81 gives $Z^* = 2206.67$. Shadow price $\pi_{\text{material}} = \mathbf{\$6.67}$ per kg.

* **Q7: Managerial Decision**: Should the plant buy 10 extra labor hours at \$10/hr?  
  *Solution*: **Yes**. Since shadow price ($\$16.67/hr$) > marginal cost ($\$10/hr$), net profit increases by $(16.67 - 10) \times 10 = \mathbf{\$66.70}$.

---

### Part 2: Airline Network Revenue Management

#### Scenario
An airline operates a hub network connecting Boston (BOS) $\to$ Chicago (ORD) $\to$ Los Angeles (LAX).
* Flight Leg 1 (BOS $\to$ ORD): Capacity = 150 seats.
* Flight Leg 2 (ORD $\to$ LAX): Capacity = 150 seats.

4 Fare Products:
1. Local BOS $\to$ ORD ($Q_1$): Price = \$200, Demand = 100 seats.
2. Local ORD $\to$ LAX ($Q_2$): Price = \$250, Demand = 120 seats.
3. Connecting BOS $\to$ LAX Discount ($Q_3$): Price = \$350, Demand = 80 seats.
4. Connecting BOS $\to$ LAX Full Fare ($Q_4$): Price = \$500, Demand = 50 seats.

#### LP Formulation

$$\begin{aligned}
\max_{x_1, x_2, x_3, x_4} \quad & 200 x_1 + 250 x_2 + 350 x_3 + 500 x_4 \\
\text{subject to} \quad & x_1 + x_3 + x_4 \le 150 \quad \text{(Leg 1 Capacity: BOS-ORD)} \\
& x_2 + x_3 + x_4 \le 150 \quad \text{(Leg 2 Capacity: ORD-LAX)} \\
& 0 \le x_1 \le 100, \quad 0 \le x_2 \le 120, \quad 0 \le x_3 \le 80, \quad 0 \le x_4 \le 50
\end{aligned}$$

#### Questions & Verified Solutions

* **Q1: Formulate the leg capacity constraints.**  
  *Solution*: Leg 1: $x_1 + x_3 + x_4 \le 150$; Leg 2: $x_2 + x_3 + x_4 \le 150$.

* **Q2–Q5: What is the optimal seat allocation vector $\mathbf{x}^*$?**  
  *Solution*:  
  * $x_4^* = 50$ (High fare connecting BOS-LAX, revenue \$500/seat).  
  * $x_3^* = 0$ (Discount connecting yields \$350, but local legs $Q_1+Q_2 = 200+250 = \$450 > \$350$).  
  * $x_1^* = 100$ (Local BOS-ORD, uses $150-50 = 100$ remaining Leg 1 seats).  
  * $x_2^* = 100$ (Local ORD-LAX, uses $150-50 = 100$ remaining Leg 2 seats).

* **Q6: Calculate Maximum Revenue.**  
  *Solution*: $Z^* = 200(100) + 250(100) + 350(0) + 500(50) = 20,000 + 25,000 + 25,000 = \mathbf{\$70,000}$.

* **Q7: Shadow Price of Leg 1 (BOS-ORD).**  
  *Solution*: Leg 1 is tight ($100 + 50 = 150$). Extra seat increases $x_1$ by 1 unit $\implies \pi_1 = \mathbf{\$200}$.

* **Q8: Shadow Price of Leg 2 (ORD-LAX).**  
  *Solution*: Leg 2 is tight ($100 + 50 = 150$). Extra seat increases $x_2$ by 1 unit $\implies \pi_2 = \mathbf{\$250}$.

* **Q9: Evaluate Opportunity Cost for Product $Q_3$.**  
  *Solution*: Marginal value of capacity on $Q_3$ path = $\pi_1 + \pi_2 = \$200 + \$250 = \$450$. Since $Q_3$ fare ($\$350$) < $\$450$, LP rejects $Q_3$ seats.

---

## 💻 Assignment 2: Network Flows & Cloud Operations

### Overview
Assignment 2 applies minimum cost network flow principles to server workload routing and data center traffic scheduling.

---

### Part 1: Cloud Server Workload Routing

#### Scenario
A cloud provider routes compute tasks from two entry gateways ($S_1, S_2$) through intermediate routers ($M_1, M_2$) to target processing centers ($T_1, T_2$).

* Gateway supplies: $b(S_1) = +50$, $b(S_2) = +30$.
* Center demands: $b(T_1) = -40$, $b(T_2) = -40$.
* Router flow balance: $b(M_1) = 0$, $b(M_2) = 0$.

Network Arc Costs & Capacities:

| Arc $(i, j)$ | Cost $c_{ij}$ (\$/unit) | Capacity $u_{ij}$ |
| :--- | :--- | :--- |
| $(S_1, M_1)$ | 2 | 40 |
| $(S_1, M_2)$ | 4 | 30 |
| $(S_2, M_1)$ | 3 | 30 |
| $(S_2, M_2)$ | 1 | 20 |
| $(M_1, T_1)$ | 2 | 50 |
| $(M_1, T_2)$ | 5 | 30 |
| $(M_2, T_1)$ | 6 | 20 |
| $(M_2, T_2)$ | 2 | 40 |

#### Network Flow Formulation

$$\begin{aligned}
\min_{\mathbf{x}} \quad & 2 x_{S1,M1} + 4 x_{S1,M2} + 3 x_{S2,M1} + 1 x_{S2,M2} + 2 x_{M1,T1} + 5 x_{M1,T2} + 6 x_{M2,T1} + 2 x_{M2,T2} \\
\text{subject to} \quad & x_{S1,M1} + x_{S1,M2} = 50 \\
& x_{S2,M1} + x_{S2,M2} = 30 \\
& (x_{S1,M1} + x_{S2,M1}) - (x_{M1,T1} + x_{M1,T2}) = 0 \\
& (x_{S1,M2} + x_{S2,M2}) - (x_{M2,T1} + x_{M2,T2}) = 0 \\
& x_{M1,T1} + x_{M2,T1} = 40 \\
& x_{M1,T2} + x_{M2,T2} = 40 \\
& 0 \le x_{ij} \le u_{ij}, \quad \forall (i,j)
\end{aligned}$$

#### Questions & Verified Solutions

* **Q1: What is the flow routed through $(S_2, M_2)$?**  
  *Solution*: Cost is lowest ($c = 1$, cap = 20). $x_{S2,M2}^* = \mathbf{20}$.

* **Q2: What is the optimal routing flow vector $\mathbf{x}^*$?**  
  *Solution*:  
  * $x_{S1,M1}^* = 40$, $x_{S1,M2}^* = 10$.  
  * $x_{S2,M1}^* = 10$, $x_{S2,M2}^* = 20$.  
  * $x_{M1,T1}^* = 40$, $x_{M1,T2}^* = 10$.  
  * $x_{M2,T1}^* = 0$, $x_{M2,T2}^* = 30$.

* **Q3: Calculate Total Minimum Network Routing Cost.**  
  *Solution*:  
  $\text{Cost} = 2(40) + 4(10) + 3(10) + 1(20) + 2(40) + 5(10) + 6(0) + 2(30) = 80 + 40 + 30 + 20 + 80 + 50 + 0 + 60 = \mathbf{\$360}$.

* **Q4: Total Unimodularity Verification.**  
  *Solution*: All optimal flow values $x_{ij}^*$ are pure integers because the node-arc incidence matrix is **Totally Unimodular** and all supply/demand bounds are integer.

---

### Part 2: Multi-Commodity Data Transfer Optimization

#### Scenario
Two data traffic classes (High Priority Video $K_1$, Low Priority File Sync $K_2$) share a backbone link with total capacity $U_{\text{link}} = 100$ Gbps. Video profit = \$10/Gbps, File profit = \$4/Gbps. Minimum video requirement = 40 Gbps.

#### Questions & Verified Solutions

* **Q1: Formulate the joint allocation model.**  
  *Solution*: Maximize $10 y_1 + 4 y_2$ subject to $y_1 + y_2 \le 100$, $y_1 \ge 40$, $y_2 \ge 0$.

* **Q2: Optimal Bandwidth Allocation & Maximum Revenue.**  
  *Solution*: Allocate maximum possible to high-margin Video ($y_1^* = 100$), $y_2^* = 0$. Revenue = $10(100) = \mathbf{\$1,000}$.

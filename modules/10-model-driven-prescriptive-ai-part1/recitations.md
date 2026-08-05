# Recitation Notes – Model-Driven Prescriptive AI Part 1

---

## 🔬 Recitation 1: Network Flows in Python

### 1. Overview & Setup
Taught by **Shriya Karam**, PhD candidate at MIT's Operations Research Center. This recitation bridges network optimization theory with hands-on Python implementations using `networkx` for graph modeling and `pulp` for linear programming formulations.

---

### 2. Recitation Section 1: Shortest Path Problem

#### Problem Scenario
Given a directed transport graph with nodes $V=\{A, B, C, D, E\}$ and edge travel times $c_{ij}$, determine the shortest route from source node $A$ to destination node $E$.

```
       (B) ─── 4 ───► (D)
     ▲  │              ▲  │
    2   │              │  │ 3
   ╱    3              1  ▼
(A)     ▼              │ (E)
   ╲    (C) ─── 5 ─────┘
    6  ▲
     ╲ │
      (D)
```

#### Python Implementation (`pulp` + `networkx`)

```python
import pulp
import networkx as nx

# Define graph structure
nodes = ['A', 'B', 'C', 'D', 'E']
edges = {
    ('A', 'B'): 2,
    ('A', 'D'): 6,
    ('B', 'C'): 3,
    ('B', 'D'): 4,
    ('C', 'E'): 5,
    ('D', 'C'): 1,
    ('D', 'E'): 3
}

# Create LP Problem
model = pulp.LpProblem("Shortest_Path_Problem", pulp.LpMinimize)

# Decision variables: x_ij in [0, 1]
x = pulp.LpVariable.dicts("flow", edges.keys(), lowBound=0, upBound=1, cat=pulp.LpContinuous)

# Objective Function: Minimize total travel time
model += pulp.lpSum([edges[e] * x[e] for e in edges.keys()]), "Total_Travel_Time"

# Flow Conservation Constraints: sum(out) - sum(in) = b_i
source, target = 'A', 'E'
for node in nodes:
    out_flow = pulp.lpSum([x[(i, j)] for (i, j) in edges.keys() if i == node])
    in_flow = pulp.lpSum([x[(i, j)] for (i, j) in edges.keys() if j == node])
    
    if node == source:
        model += (out_flow - in_flow == 1), f"Flow_Balance_{node}"
    elif node == target:
        model += (out_flow - in_flow == -1), f"Flow_Balance_{node}"
    else:
        model += (out_flow - in_flow == 0), f"Flow_Balance_{node}"

# Solve using CBC solver
model.solve(pulp.PULP_CBC_CMD(msg=False))

print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Minimum Travel Time: {pulp.value(model.objective)}")
for e in edges.keys():
    if x[e].varValue > 0.5:
        print(f"Path segment: {e[0]} -> {e[1]} (Cost: {edges[e]})")
```

---

### 3. Recitation Section 2: Rider-Driver Assignment Problem

#### Problem Scenario
A ride-hailing platform must match 3 available drivers $\{D_1, D_2, D_3\}$ to 3 requesting riders $\{R_1, R_2, R_3\}$. The pickup response time matrix (minutes) is given by:

$$\mathbf{C} = \begin{pmatrix}
4 & 7 & 3 \\
6 & 2 & 5 \\
5 & 8 & 4
\end{pmatrix}$$

#### Python Implementation (`pulp`)

```python
import pulp

drivers = ['D1', 'D2', 'D3']
riders = ['R1', 'R2', 'R3']

cost_matrix = {
    ('D1', 'R1'): 4, ('D1', 'R2'): 7, ('D1', 'R3'): 3,
    ('D2', 'R1'): 6, ('D2', 'R2'): 2, ('D2', 'R3'): 5,
    ('D3', 'R1'): 5, ('D3', 'R2'): 8, ('D3', 'R3'): 4
}

# LP Formulation
prob = pulp.LpProblem("Rider_Driver_Matching", pulp.LpMinimize)

# Decision Variables
assign = pulp.LpVariable.dicts("x", (drivers, riders), lowBound=0, upBound=1, cat=pulp.LpContinuous)

# Objective: Minimize total pickup response time
prob += pulp.lpSum([cost_matrix[d, r] * assign[d][r] for d in drivers for r in riders])

# Constraint 1: Each driver assigned to at most 1 rider
for d in drivers:
    prob += pulp.lpSum([assign[d][r] for r in riders]) <= 1, f"Driver_Limit_{d}"

# Constraint 2: Each rider matched to exactly 1 driver
for r in riders:
    prob += pulp.lpSum([assign[d][r] for d in drivers]) == 1, f"Rider_Requirement_{r}"

prob.solve(pulp.PULP_CBC_CMD(msg=False))

print(f"Optimal Total Pickup Time: {pulp.value(prob.objective)} minutes")
for d in drivers:
    for r in riders:
        if assign[d][r].varValue > 0.5:
            print(f"Driver {d} assigned to Rider {r} (Pickup time: {cost_matrix[d, r]} mins)")
```

---

### 4. Recitation Summary & Key Insights

1. **Continuous Relaxation Integrity**: Because node-arc incidence matrices are **Totally Unimodular (TU)**, configuring decision variables as continuous (`LpContinuous` in $[0, 1]$) yields exact binary integer solutions ($0$ or $1$) at significantly faster computational speeds.
2. **Greedy vs. Optimal Matching**: A greedy heuristic matching $D_1 \to R_3$ (3 mins), then $D_2 \to R_2$ (2 mins), leaves $D_3 \to R_1$ (5 mins), giving a total cost of $10$ mins. The global LP optimization achieves $D_1 \to R_1$ (4 mins), $D_2 \to R_2$ (2 mins), $D_3 \to R_3$ (4 mins), yielding a total cost of **10 mins** (and when supply/demand expands, LP avoids worst-case bottlenecks).

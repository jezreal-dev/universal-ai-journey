# Recitation Notes – Model-Driven Prescriptive AI Part 2

---

## 🔬 Recitation 1: Integer Optimization in Python (Facility Location)

### 1. Problem Description
Select which distribution centers to open among 3 candidate sites $\{J_1, J_2, J_3\}$ to serve 4 regional demand areas $\{I_1, I_2, I_3, I_4\}$.

* **Fixed Costs**: $f_1 = \$500$, $f_2 = \$750$, $f_3 = \$400$.
* **Capacities**: $K_1 = 100$, $K_2 = 150$, $K_3 = 80$.
* **Demands**: $d_1 = 30$, $d_2 = 40$, $d_3 = 50$, $d_4 = 20$ (Total = 140).

Unit Shipping Costs ($c_{ij}$):

$$\mathbf{C} = \begin{pmatrix}
4 & 6 & 9 \\
5 & 3 & 7 \\
8 & 4 & 3 \\
6 & 5 & 2
\end{pmatrix}$$

---

### 2. Python Implementation (`pulp`)

```python
import pulp

facilities = ['J1', 'J2', 'J3']
demands = ['I1', 'I2', 'I3', 'I4']

fixed_costs = {'J1': 500, 'J2': 750, 'J3': 400}
capacities = {'J1': 100, 'J2': 150, 'J3': 80}
demand_reqs = {'I1': 30, 'I2': 40, 'I3': 50, 'I4': 20}

ship_cost = {
    ('I1', 'J1'): 4, ('I1', 'J2'): 6, ('I1', 'J3'): 9,
    ('I2', 'J1'): 5, ('I2', 'J2'): 3, ('I2', 'J3'): 7,
    ('I3', 'J1'): 8, ('I3', 'J2'): 4, ('I3', 'J3'): 3,
    ('I4', 'J1'): 6, ('I4', 'J2'): 5, ('I4', 'J3'): 2,
}

# Create MILP problem
model = pulp.LpProblem("Facility_Location_MIO", pulp.LpMinimize)

# Decision Variables
y = pulp.LpVariable.dicts("open", facilities, cat=pulp.LpBinary)
x = pulp.LpVariable.dicts("ship", ((i, j) for i in demands for j in facilities), lowBound=0, cat=pulp.LpContinuous)

# Objective Function: Fixed Costs + Transportation Costs
model += (
    pulp.lpSum([fixed_costs[j] * y[j] for j in facilities]) +
    pulp.lpSum([ship_cost[i, j] * x[i, j] for i in demands for j in facilities])
), "Total_Cost"

# Constraint 1: Satisfy customer demands
for i in demands:
    model += pulp.lpSum([x[i, j] for j in facilities]) == demand_reqs[i], f"Demand_{i}"

# Constraint 2: Capacity & Logical Linking Constraint (sum_i x_ij <= K_j * y_j)
for j in facilities:
    model += pulp.lpSum([x[i, j] for i in demands]) <= capacities[j] * y[j], f"Capacity_Linking_{j}"

# Solve MILP using CBC Branch-and-Bound solver
model.solve(pulp.PULP_CBC_CMD(msg=False))

print(f"Optimal MILP Status: {pulp.LpStatus[model.status]}")
print(f"Minimum Total Cost: ${pulp.value(model.objective):,.2f}\n")

for j in facilities:
    if y[j].varValue > 0.5:
        print(f"Facility {j} is OPENED (Fixed cost: ${fixed_costs[j]})")
        for i in demands:
            if x[i, j].varValue > 0:
                print(f"  --> Shipping {x[i, j].varValue:.0f} units to {i}")
```

---

## 📈 Recitation 2 (Part 1): Taylor Approximations & Gradient Descent

### 1. Taylor Series Expansion of $f(x) = \frac{1}{x}\sin(x)$

#### Problem Setup
Given $f(x) = \frac{1}{x}\sin(x)$ defined on $(0, \infty)$, we compute Taylor approximations around point $a = 5$:

$$\begin{aligned}
f(a) &= \frac{\sin(a)}{a} \\
f'(a) &= \frac{\cos(a)}{a} - \frac{\sin(a)}{a^2} \\
f''(a) &= -\frac{\sin(a)}{a} - \frac{2\cos(a)}{a^2} + \frac{2\sin(a)}{a^3}
\end{aligned}$$

#### Python Visualization & Taylor Order Comparison

```python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) / x

def f_prime(x):
    return np.cos(x) / x - np.sin(x) / (x**2)

def f_double_prime(x):
    return -np.sin(x) / x - 2 * np.cos(x) / (x**2) + 2 * np.sin(x) / (x**3)

def taylor_approx_1st(x, a):
    return f(a) + f_prime(a) * (x - a)

def taylor_approx_2nd(x, a):
    return taylor_approx_1st(x, a) + 0.5 * f_double_prime(a) * ((x - a)**2)

# Generate points around a = 5
a = 5.0
x_vals = np.linspace(3.0, 7.0, 200)

plt.figure(figsize=(9, 5))
plt.plot(x_vals, f(x_vals), label="True f(x) = sin(x)/x", color="black", linewidth=2)
plt.plot(x_vals, taylor_approx_1st(x_vals, a), "--", label="1st Degree Taylor (Linear)", color="blue")
plt.plot(x_vals, taylor_approx_2nd(x_vals, a), ":", label="2nd Degree Taylor (Quadratic)", color="red", linewidth=2)
plt.scatter([a], [f(a)], color="green", zorder=5, label=f"Expansion Point a={a}")

plt.title("Taylor Expansion Approximations for f(x) = sin(x)/x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

---

### 2. Gradient Descent Step Size Sensitivity in 2D Quadratic Loss

```python
# 2D Quadratic Function: f(x1, x2) = 0.5 * x1^2 + 2.5 * x2^2
def quad_loss(x1, x2):
    return 0.5 * (x1**2) + 2.5 * (x2**2)

def quad_grad(x1, x2):
    return np.array([x1, 5.0 * x2])

def run_gradient_descent(alpha, iterations=20, start_pos=(4.0, 3.0)):
    x = np.array(start_pos, dtype=float)
    path = [x.copy()]
    for _ in range(iterations):
        grad = quad_grad(x[0], x[1])
        x -= alpha * grad
        path.append(x.copy())
    return np.array(path)

# Test Learning Rates
alphas = [0.05, 0.35, 0.42] # Slow crawl, optimal convergence, overshooting oscillation
paths = {lr: run_gradient_descent(lr) for lr in alphas}

for lr, path in paths.items():
    print(f"Learning Rate alpha = {lr}: Final Position = ({path[-1][0]:.4f}, {path[-1][1]:.4f}), Loss = {quad_loss(path[-1][0], path[-1][1]):.6f}")
```

---

## ⚡ Recitation 2 (Part 2): Mini-Batch SGD & Neural Network Fitting

### 1. Mini-Batch SGD vs. Full-Batch GD from Scratch

```python
import numpy as np

# Synthetic Dataset: N = 2000 samples, 5 features
np.random.seed(42)
N = 2000
d = 5
X = np.random.randn(N, d)
true_beta = np.array([2.5, -1.5, 0.8, 0.0, -3.0])
y = X.dot(true_beta) + 0.5 * np.random.randn(N)

def compute_loss(X, y, beta):
    return np.mean((X.dot(beta) - y) ** 2)

def mini_batch_sgd(X, y, batch_size=32, lr_0=0.1, gamma=0.005, epochs=15):
    N, d = X.shape
    beta = np.zeros(d)
    loss_history = []
    step = 0
    
    for epoch in range(epochs):
        perm = np.random.permutation(N)
        X_shuffled = X[perm]
        y_shuffled = y[perm]
        
        for i in range(0, N, batch_size):
            step += 1
            X_b = X_shuffled[i:i+batch_size]
            y_b = y_shuffled[i:i+batch_size]
            
            # Mini-batch gradient
            grad = (2.0 / len(y_b)) * X_b.T.dot(X_b.dot(beta) - y_b)
            
            # Learning rate decay schedule: lr = lr_0 / (1 + gamma * step)
            lr = lr_0 / (1.0 + gamma * step)
            beta -= lr * grad
            
        loss_history.append(compute_loss(X, y, beta))
        
    return beta, loss_history

beta_opt, losses = mini_batch_sgd(X, y, batch_size=32, epochs=15)

print("True Coefficients:     ", true_beta)
print("Estimated Coefficients:", np.round(beta_opt, 4))
print(f"Final Test MSE Loss:    {losses[-1]:.5f}")
```

---

### 2. Recitation Summary & Key Insights
1. **Taylor Expansion Precision**: Second-degree Taylor polynomial captures local function curvature ($\nabla^2 f$), expanding valid approximation radius significantly compared to first-degree linear tangent approximations.
2. **Learning Rate Stability**: In Mini-Batch SGD, applying step-size decay schedules ($\alpha_k = \frac{\alpha_0}{1 + \gamma k}$) dampens mini-batch sampling noise near optimum bounds, ensuring smooth gradient convergence.

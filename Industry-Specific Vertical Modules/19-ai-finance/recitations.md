# Recitation Notes – AI and Finance

---

## 🔬 Applied AI Finance & Quantitative Trading in Python

### 1. Q-Learning Algorithmic Trading Agent

This Python script implements a Q-Learning agent to automate buy, sell, and hold trading decisions on price time series data.

```python
import numpy as np
import pandas as pd

class QLearningTradingAgent:
    def __init__(self, n_states=10, n_actions=3, alpha=0.1, gamma=0.95, epsilon=0.1):
        self.n_states = n_states
        self.n_actions = n_actions # 0: Hold, 1: Buy, 2: Sell
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = np.zeros((n_states, n_actions))

    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.epsilon:
            return np.random.choice(self.n_actions) # Explore
        return np.argmax(self.q_table[state])       # Exploit

    def update(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.gamma * self.q_table[next_state, best_next_action]
        td_error = td_target - self.q_table[state, action]
        self.q_table[state, action] += self.alpha * td_error

# Synthetic Market Data Simulation
np.random.seed(42)
prices = 100 + np.cumsum(np.random.normal(0.05, 1.0, 500))
returns = pd.Series(prices).pct_change().fillna(0)

# Discretize states based on 5-day return quantiles
states = pd.qcut(returns.rolling(5).mean().fillna(0), q=10, labels=False)

agent = QLearningTradingAgent(n_states=10, n_actions=3)

# Training Loop
for step in range(len(prices) - 1):
    s = states[step]
    a = agent.choose_action(s)
    
    # Calculate Reward (PnL - transaction cost)
    r_pct = returns[step + 1]
    reward = r_pct if a == 1 else (-r_pct if a == 2 else 0.0)
    reward -= 0.0005 if a != 0 else 0.0 # Transaction cost penalty
    
    next_s = states[step + 1]
    agent.update(s, a, reward, next_s)

print("Trained Q-Table Sample (First 3 States):")
print(agent.q_table[:3])
```

---

### 2. Portfolio Backtesting & Annualized Sharpe Ratio Engine

```python
import numpy as np
import pandas as pd

def backtest_portfolio_strategy(daily_returns, risk_free_rate_annual=0.04):
    """
    Computes annualized return, annualized volatility, and Sharpe Ratio.
    """
    trading_days = 252
    rf_daily = risk_free_rate_annual / trading_days
    
    excess_returns = daily_returns - rf_daily
    mean_excess_return = np.mean(excess_returns)
    std_return = np.std(daily_returns, ddof=1)
    
    annualized_return = np.mean(daily_returns) * trading_days
    annualized_volatility = std_return * np.sqrt(trading_days)
    annualized_sharpe = (mean_excess_return / std_return) * np.sqrt(trading_days)
    
    return {
        'Annualized Return': f"{annualized_return * 100:.2f}%",
        'Annualized Volatility': f"{annualized_volatility * 100:.2f}%",
        'Annualized Sharpe Ratio': round(annualized_sharpe, 4)
    }

# Run Simulation
np.random.seed(42)
strategy_returns = np.random.normal(loc=0.0008, scale=0.012, size=252) # Strategy returns
results = backtest_portfolio_strategy(strategy_returns)

for metric, val in results.items():
    print(f"{metric}: {val}")
```

---

### 3. Summary of Core Quantitative Formulas

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                            Quantitative Financial Metrics Summary                        │
├──────────────────────────────┬───────────────────────────────────────────────────────────┤
│ Metric                       │ Mathematical Equation                                     │
├──────────────────────────────┼───────────────────────────────────────────────────────────┤
│ Annualized Sharpe Ratio      │ SR = [(E[R_p] - R_f) / std(R_p)] * sqrt(252)             │
├──────────────────────────────┼───────────────────────────────────────────────────────────┤
│ Bellman Optimality           │ Q(s,a) <= Q(s,a) + alpha * [r + gamma*max Q(s',a') - Q]   │
├──────────────────────────────┼───────────────────────────────────────────────────────────┤
│ UCB1 Bandit Bound            │ A_t = argmax [ Q_t(a) + c * sqrt(ln(t) / N_t(a)) ]        │
└──────────────────────────────┴───────────────────────────────────────────────────────────┘
```

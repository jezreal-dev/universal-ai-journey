# Assignment Solutions – AI and Finance

---

## 📝 Assignment 1: Quantitative Trading, RL & Financial NLP Solutions

### 📌 Problem 1 — Financial MDP Formulation

#### Question Formulation
An algorithmic trading team models an automated execution strategy as a Markov Decision Process (MDP). If the portfolio holds 500 shares of stock $X$, the stock price moves from $\$150$ to $\$152$, and the agent executes a sell order of 100 shares incurring a $\$5.00$ fixed transaction fee, define the state, action, and immediate PnL reward.

#### Verified Solution & Explanation
* **State ($S_t$)**: Current stock price $=\$150$, current inventory $= 500 \text{ shares}$.
* **Action ($A_t$)**: Sell 100 shares ($a_t = -100$).
* **Immediate PnL Reward ($R_{t+1}$)**: 

$$\Delta \text{Portfolio Value} = (500 \text{ shares}) \times (\$152 - \$150) - \$5.00 \text{ fee} = (500 \times \$2.00) - \$5.00 = \mathbf{\$995.00}$$

```python
initial_inventory = 500
price_t0 = 150.0
price_t1 = 152.0
transaction_fee = 5.0

pnl_reward = (initial_inventory * (price_t1 - price_t0)) - transaction_fee
print(f"Immediate PnL Reward: ${pnl_reward:.2f}")
```

---

### 📌 Problem 2 — Bellman Optimality Q-Learning Calculation

#### Question Formulation
A Q-learning trading agent in state $S_1$ (RSI indicator $< 30$, oversold) takes action $A_1$ (Buy 50 shares). The initial estimated Q-value is $Q(S_1, A_1) = 2.50$. The market yields an immediate reward $R = 0.80$, leading to new state $S_2$ where maximum estimated future action value is $\max_{a'} Q(S_2, a') = 4.00$. Given learning rate $\alpha = 0.20$ and discount factor $\gamma = 0.90$, calculate the updated $Q(S_1, A_1)$.

#### Verified Solution & Explanation
* **Bellman Formula**:

$$Q(s, a) \leftarrow Q(s, a) + \alpha \left[ R + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]$$

* **Calculation**:
  - $\text{TD Target} = R + \gamma \max Q(S_2, a') = 0.80 + (0.90 \times 4.00) = 0.80 + 3.60 = 4.40$
  - $\text{TD Error} = \text{TD Target} - Q(S_1, A_1) = 4.40 - 2.50 = 1.90$
  - $Q_{\text{updated}} = 2.50 + (0.20 \times 1.90) = 2.50 + 0.38 = \mathbf{2.88}$

```python
q_old = 2.50
reward = 0.80
max_q_next = 4.00
alpha = 0.20
gamma = 0.90

td_target = reward + (gamma * max_q_next)
q_updated = q_old + alpha * (td_target - q_old)

print(f"Updated Q(S1, A1): {q_updated:.4f}")
```

---

### 📌 Problem 3 — Annualized Sharpe Ratio Computation

#### Question Formulation
A quantitative trading strategy yields a mean daily return of $0.06\%$ with a daily standard deviation of $1.10\%$. Assuming a $3.0\%$ annual risk-free rate ($252$ trading days), evaluate the annualized Sharpe Ratio.

#### Verified Solution & Explanation
* **Calculation**:
  - Daily Risk-Free Rate = $\frac{0.03}{252} = 0.00011905$ ($0.0119\%$)
  - Mean Daily Excess Return = $0.0006 - 0.00011905 = 0.00048095$
  - Annualized Sharpe Ratio = $\frac{0.00048095}{0.0110} \times \sqrt{252} = 0.04372 \times 15.8745 = \mathbf{0.6941}$

```python
mean_daily_return = 0.0006
daily_std = 0.0110
annual_rf = 0.03
trading_days = 252

daily_rf = annual_rf / trading_days
excess_return = mean_daily_return - daily_rf
sharpe_ratio = (excess_return / daily_std) * np.sqrt(trading_days)

print(f"Annualized Sharpe Ratio: {sharpe_ratio:.4f}")
```

---

### 📌 Problem 4 — Quantitative Bias Mitigation

#### Question Formulation
A researcher backtests a financial LLM sentiment trading model on historical S&P 500 constituents from 2015 to 2025 using the list of S&P 500 companies active in 2025. Which critical bias is present, and how should it be corrected?

#### Verified Solution & Explanation
* **Correct Answer**: **Survivorship Bias. The dataset excludes companies that were delisted or went bankrupt between 2015 and 2025.**
* **Mitigation**: **Re-run the backtest using point-in-time historical constituent databases that explicitly include delisted, merged, and bankrupt companies.**

# Lecture Notes – AI and Finance

---

## 📈 Lecture 1: Fintech & Algorithmic Finance

### 1. Financial Intermediation & Algorithmic Transformation

The evolution of financial services has transitioned from traditional human intermediation to automated algorithmic execution:

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                           Evolution of Financial Execution                               │
├─────────────────────┬────────────────────────────────────┬───────────────────────────────┤
│ Era                 │ Primary Mechanics                  │ Core Technology               │
├─────────────────────┼────────────────────────────────────┼───────────────────────────────┤
│ 1. Traditional      │ Human brokers & manual order books │ Telephones & paper ledgers    │
├─────────────────────┼────────────────────────────────────┼───────────────────────────────┤
│ 2. Electronic       │ Automated order matching           │ FIX Protocol & electronic ECNs│
├─────────────────────┼────────────────────────────────────┼───────────────────────────────┤
│ 3. Quantitative     │ Rule-based statistical arbitrage   │ High-Frequency Trading (HFT)  │
├─────────────────────┼────────────────────────────────────┼───────────────────────────────┤
│ 4. AI & LLM Era     │ Sentiment NLP & RL execution agents│ FinBERT, DQNs, Deep RL        │
└─────────────────────┴────────────────────────────────────┴───────────────────────────────┘
```

---

### 2. Narrative vs. Facts: Sentiment vs. Fundamental Valuation

Financial asset prices are driven by two interacting forces:
1. **Fundamental Facts**: Balance sheet metrics (revenue, EBITDA, cash flow, debt ratios) extracted from financial filings.
2. **Market Narratives**: Perceptual signals and sentiment extracted from news feeds, social media, and earnings calls.

NLP systems convert unstructured market narratives into quantitative sentiment scores $S_t \in [-1, +1]$, combining sentiment signals with quantitative factors to generate alpha ($\alpha$).

---

## 🤖 Lecture 2: Reinforcement Learning in Finance

### 1. Financial Markov Decision Process (MDP)

Algorithmic trading and portfolio allocation are modeled as a Markov Decision Process defined by the tuple $(S, A, P, R, \gamma)$:

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                               Financial Trading MDP Pipeline                             │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ Environment (Market/Order Book) ──► State S_t (Prices, Indicators, Portfolio Inventory)  │
│          ▲                                                                     │         │
│          └────────────── Action A_t (Buy/Sell/Hold) ◄── RL Agent ◄─────────────┘         │
│                          Reward R_{t+1} (PnL / Sharpe Ratio)                             │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

* **State Space ($S_t$)**: Current asset prices, technical indicators (RMA, MACD), historical returns, and current portfolio inventory.
* **Action Space ($A_t$)**: Target position allocations $a_t \in [-1, +1]$ (Short, Cash, Long).
* **Reward Function ($R_t$)**: Change in portfolio value, risk-adjusted returns (Sharpe Ratio), or PnL penalized by transaction costs and volatility:

$$R_t = \Delta \text{PnL}_t - \lambda \cdot \sigma^2(R_t) - c \cdot |\Delta a_t|$$

---

### 2. Multi-Armed Bandits & Action Selection

In static or stationary trade selection, Multi-Armed Bandits balance exploration vs. exploitation:

#### UCB1 Action Selection Formula
$$A_t = \arg\max_{a \in A} \left[ Q_t(a) + c \sqrt{\frac{\ln t}{N_t(a)}} \right]$$

* $Q_t(a)$: Estimated mean return of action $a$.
* $N_t(a)$: Number of times action $a$ has been selected.
* $c$: Exploration constant balancing risk.

---

### 3. Q-Learning & Deep Q-Networks (DQN)

#### Bellman Optimality Update Equation
$$Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r_t + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]$$

In Deep Q-Networks (DQN), a deep neural network parametrized by $\theta$ approximates the optimal Q-function $Q(s, a; \theta)$, trained by minimizing the Mean Squared Bellman Error (MSBE):

$$\mathcal{L}(\theta) = \mathbb{E}_{\left(s, a, r, s'\right) \sim \mathcal{D}} \left[ \left( r + \gamma \max_{a'} Q(s', a'; \theta^-) - Q(s, a; \theta) \right)^2 \right]$$

---

### 4. "Trading to Learn": Order Book Execution & Market Impact

Executing large institutional orders requires minimizing **Market Impact** and **Slippage**:

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                            Limit Order Book & Execution Dynamics                         │
├─────────────────────┬────────────────────────────────────┬───────────────────────────────┤
│ Execution Strategy  │ Mechanics                          │ Market Impact Risk            │
├─────────────────────┼────────────────────────────────────┼───────────────────────────────┤
│ 1. TWAP             │ Time-Weighted Average Price        │ Constant rate; vulnerable to  │
│                     │ (fixed slices over time)           │ adverse selection             │
├─────────────────────┼────────────────────────────────────┼───────────────────────────────┤
│ 2. VWAP             │ Volume-Weighted Average Price      │ Follows historical volume     │
│                     │ (slices proportional to volume)    │ distribution profile          │
├─────────────────────┼────────────────────────────────────┼───────────────────────────────┤
│ 3. RL Market Making │ Adaptive limit/market order placement │ Optimizes bid-ask spread &    │
│                     │ using Deep Q-Learning              │ inventory risk (Almgren-Chriss)│
└─────────────────────┴────────────────────────────────────┴───────────────────────────────┘
```

---

## 📄 Lecture 3: Large Language Models in Finance

### 1. Financial NLP Architecture: FinBERT

General-purpose LLMs often struggle with financial terminology (e.g. "liability", "bullish", "impairment"). **FinBERT** is pre-trained on financial corpora (SEC filings, earnings transcripts, financial news) to perform domain-tuned sentiment classification:

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                             FinBERT Financial NLP Architecture                           │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ SEC 10-K / News ──► Tokenizer ──► Transformer Layers (Self-Attention) ──► Sentiment Output│
│                                                                        (Positive/Negative│
│                                                                         /Neutral)        │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 2. Common Quantitative Biases in AI Financial Models

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                            Quantitative Financial Model Biases                           │
├───────────────────┬────────────────────────────────────────┬─────────────────────────────┤
│ Bias Type         │ Description                            │ Mitigation Strategy         │
├───────────────────┼────────────────────────────────────────┼─────────────────────────────┤
│ 1. Look-Ahead     │ Including information in training that │ Strictly timestamp all data │
│    Bias           │ was unavailable at prediction time     │ features before backtesting │
├───────────────────┼────────────────────────────────────────┼─────────────────────────────┤
│ 2. Survivorship   │ Evaluating models only on companies    │ Include delisted and bankrupt│
│    Bias           │ that currently exist today             │ firms in historical datasets│
├───────────────────┼────────────────────────────────────────┼─────────────────────────────┤
│ 3. Overfitting /  │ Fitting noise in historical market     │ Out-of-sample testing and   │
│    Data Snooping  │ data through excessive factor search   │ Deflated Sharpe Ratio (DSR) │
└───────────────────┴────────────────────────────────────────┴─────────────────────────────┘
```

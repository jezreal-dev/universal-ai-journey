# Module Overview – AI and Finance

📅 **Status**: Completed  
🎓 **MIT Open Learning via 3MTT**  
📌 **Module Folder**: `modules/19-ai-finance`  
📖 **Source File**: [source_lecture.md](source_lecture.md)

---

## 🌟 Executive Summary

Welcome to **AI and Finance**, an industry-specific vertical module in the MIT Universal AI Track. Financial markets are undergoing a fundamental transformation—shifting from traditional human intermediation to algorithmic execution, automated sentiment extraction, and reinforcement learning-driven asset management.

This module provides a lossless, mathematically rigorous exploration of AI in quantitative finance, market microstructure, and financial NLP:
* **Fintech & Narrative-Driven Markets**: Analyzing how market narratives interact with fundamental valuation facts, NLP sentiment extraction from financial news, and factor investing in the age of LLMs.
* **Reinforcement Learning (RL) in Trading**: Modeling financial markets as Markov Decision Processes (MDP: $S, A, P, R, \gamma$), Multi-Armed Bandits ($\epsilon$-Greedy & UCB1 bounds), and Q-Learning / Deep Q-Networks (DQN) for optimal portfolio allocation and execution.
* **Market Microstructure & "Trading to Learn"**: Simulating limit order books, market impact, slippage, and automated market making under real-time inventory constraints.
* **Financial LLMs & Document Intelligence**: Domain-tuned language models (**FinBERT**), automated parsing of SEC 10-K/10-Q filings, earnings call transcript analysis, and credit risk assessment.
* **Risk & Regulatory Governance**: Mitigating financial hallucinations, look-ahead bias, survivorship bias, and ensuring compliance with SEC regulatory standards.

---

## 🎯 Key Learning Goals

By completing this module, we have achieved the following core capabilities:

1. **Financial MDP Formulation**: Formulated trading and portfolio management as Markov Decision Processes, defining state spaces (price history, indicators, inventory), action spaces (buy/sell/hold size), and reward functions (Sharpe ratio, PnL).
2. **Q-Learning & Bellman Optimality**: Derived and implemented Q-learning update equations ($Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s, a)]$) for automated execution algorithms.
3. **Multi-Armed Bandit Action Selection**: Applied UCB1 action selection bounds ($A_t = \arg\max \left[ Q(a) + c \sqrt{\frac{\ln t}{N(a)}} \right]$) to balance exploration and exploitation in financial decision-making.
4. **Financial NLP with FinBERT**: Extracted financial sentiment and risk disclosures from unstructured SEC filings and earnings call transcripts using domain-specialized transformers.
5. **Risk Metrics & Performance Backtesting**: Derived Annualized Sharpe Ratios ($SR = \frac{\mathbb{E}[R_p - R_f]}{\sigma_p} \sqrt{252}$) and evaluated quantitative backtests incorporating realistic transaction costs and market impact.
6. **Quantitative Bias Prevention**: Audit trading algorithms against look-ahead bias (using future information) and survivorship bias (ignoring delisted companies).

---

## 🗺️ Module Architecture & File Guide

* 📖 [lectures.md](lectures.md) — Lossless breakdown of Lectures 1–3 covering Fintech & AI, Reinforcement Learning (MDPs, Bandits, Q-Learning, DQNs, Market Impact), Financial LLMs (FinBERT), and Regulatory Compliance.
* 🧪 [recitations.md](recitations.md) — Applied notes and Python code implementations for Q-Learning trading agents, FinBERT SEC filing sentiment extraction, and Sharpe ratio backtesting engines.
* 📝 [assignments.md](assignments.md) — Problem formulations, verified solutions, and Python code for quantitative finance and RL portfolio case studies.
* 🎯 [conclusion.md](conclusion.md) — Comprehensive AI Finance Technology & Quantitative Taxonomy table and Full Program Completion Summary.

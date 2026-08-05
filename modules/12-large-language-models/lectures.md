# Lecture Notes – Large Language Models (LLMs)

---

## 🏗️ Lecture 1: Foundations of Large Language Models

### 1. Discriminative AI vs. Generative AI

Prior AI paradigms focused primarily on **discriminative modeling**: learning decision boundaries $P(Y \mid X)$ to map structured features $\mathbf{x} \in \mathbb{R}^d$ to labels $y$ (e.g., classification, regression, disease detection).

In contrast, **generative language modeling** models the joint probability distribution over unstructured token sequences, learning $P(X)$ to generate novel text content.

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             AI Modeling Paradigms                                │
├───────────────────────────────┬──────────────────────────────────────────────────┤
│ Discriminative Models         │ Maps input features X to label Y                 │
│ P(Y | X)                      │ (Decision Trees, OLS, Logistic Regression)       │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ Generative Language Models    │ Models sequence probabilities P(W_1, ..., W_T)   │
│ P(W_1, W_2, ..., W_T)         │ (Transformers, GPT, LLaMA, Mistral)              │
└───────────────────────────────┴──────────────────────────────────────────────────┘
```

---

### 2. Autoregressive Text Generation

An **Autoregressive Language Model** calculates the conditional probability of the next word $w_t$ appearing in a sequence given all preceding context words $w_1, w_2, \dots, w_{t-1}$.

Using the chain rule of probability, the joint likelihood of a text sequence $\mathbf{W} = (w_1, w_2, \dots, w_T)$ is factorized as:

$$P(\mathbf{W}) = P(w_1, w_2, \dots, w_T) = \prod_{t=1}^T P(w_t \mid w_1, w_2, \dots, w_{t-1})$$

#### Sequential Token Generation Loop
1. **Input Prompt**: $\mathbf{W}^{(0)} = (w_1, w_2, \dots, w_k)$.
2. **Probability Distribution**: Model outputs logits over vocabulary $V$, yields $P(w_{k+1} \mid \mathbf{W}^{(0)})$.
3. **Sampling / Selection**: Select token $w_{k+1}$ via decoding strategy.
4. **Append & Repeat**: Update prompt $\mathbf{W}^{(1)} = (\mathbf{W}^{(0)}, w_{k+1})$ and repeat until `<EOS>` token or maximum length $T_{\max}$ is reached.

---

### 3. Tokenization & Subwords

Computers process numbers, not raw text strings. **Tokenization** maps text into integer IDs.

To prevent vocabulary explosion while handling out-of-vocabulary (OOV) terms, modern LLMs utilize **Subword Tokenization** algorithms (e.g., Byte-Pair Encoding [BPE], WordPiece, Unigram):

$$\text{"unbreakable"} \longrightarrow \text{["un", "##break", "##able"]}$$

#### Key Tokenization Characteristics
* **Whole Words**: High-frequency terms (`"the"`, `"cat"`) map to single token IDs.
* **Subword Chunks**: Rare terms (`"unbreakable"`, `"xylophonic"`) are split into subword roots and affixes.
* **Fallback Characters**: Unknown characters fall back to individual ASCII/UTF-8 character IDs.
* **Space Preservation**: Identifiers preserve leading whitespace (e.g., GPT `ĠYork` vs `York`).

---

### 4. Empirical Scaling Laws

LLM performance improves predictably as a power law function of three parameters: model parameters ($N$), training dataset size ($D$), and total compute budget ($C$).

Kaplan et al. and Chinchilla scaling laws define empirical loss functions:

$$\mathcal{L}(N, D) = \left( \frac{N_c}{N} \right)^{\alpha_N} + \left( \frac{D_c}{D} \right)^{\alpha_D} + \mathcal{L}_0$$

* **Chinchilla Optimal Compute**: To optimize compute $C \approx 6 N D$, model parameter size $N$ and dataset token count $D$ must be scaled at equal rates.

---

### 5. Internal Reasoning & Alignment (RLHF & $o1$)

Pre-trained base LLMs ($P(w_t \mid w_{<t})$) predict raw internet continuation, often exhibiting toxic, biased, or evasive text. **Alignment** steers models toward human values (Helpful, Honest, Harmless).

#### Alignment Pipeline
1. **Supervised Fine-Tuning (SFT)**: Fine-tune base model on curated prompt-response pairs.
2. **Reward Modeling**: Train a reward model $R(\mathbf{x}, \mathbf{y}) \in \mathbb{R}$ on human preference rankings.
3. **Reinforcement Learning with Human Feedback (RLHF / PPO)**: Optimize policy model $\pi_\theta$ using Proximal Policy Optimization to maximize reward while penalizing drift from base model via KL divergence:

$$\max_\theta \mathbb{E}_{(\mathbf{x}, \mathbf{y}) \sim \mathcal{D}} \left[ R(\mathbf{x}, \mathbf{y}) - \beta D_{\text{KL}}(\pi_\theta(\mathbf{y} \mid \mathbf{x}) \parallel \pi_{\text{ref}}(\mathbf{y} \mid \mathbf{x})) \right]$$

#### Internal Reasoning Models ($o1$)
Models like OpenAI $o1$ replace instantaneous single-pass generation with an internal **chain-of-thought draft loop** prior to emitting final answer tokens, enabling complex reasoning verification.

---

## 🎯 Lecture 2: Architecture & Attention Mechanisms

### 1. The Q-K-V Library Analogy

Self-Attention allows each token in a sequence to dynamically weigh and extract relevant information from every other token.

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                         Query - Key - Value Analogy                              │
├───────────────────┬──────────────────────────────────────────────────────────────┤
│ Query (Q)         │ Research Question / Search Request                           │
│ Key (K)           │ Book Index / Title Tags in Library                           │
│ Value (V)         │ Actual Knowledge Content contained inside Books              │
└───────────────────┴──────────────────────────────────────────────────────────────┘
```

#### Attention Score Formulation
1. **Query Projection**: $\mathbf{Q} = \mathbf{X} \mathbf{W}_Q \in \mathbb{R}^{T \times d_k}$
2. **Key Projection**: $\mathbf{K} = \mathbf{X} \mathbf{W}_K \in \mathbb{R}^{T \times d_k}$
3. **Value Projection**: $\mathbf{V} = \mathbf{X} \mathbf{W}_V \in \mathbb{R}^{T \times d_v}$

---

### 2. Scaled Dot-Product Attention Derivation

The raw similarity between Query $i$ and Key $j$ is computed via dot product $\mathbf{q}_i \mathbf{k}_j^T$. Dividing by scaling factor $\sqrt{d_k}$ prevents gradient saturation in the softmax function for high dimensions $d_k$:

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left( \frac{\mathbf{Q} \mathbf{K}^T}{\sqrt{d_k}} \right) \mathbf{V}$$

#### Matrix Step-by-Step
$$\mathbf{A}_{\text{raw}} = \frac{\mathbf{Q} \mathbf{K}^T}{\sqrt{d_k}} \in \mathbb{R}^{T \times T}$$

$$\mathbf{A}_{\text{weights}} = \text{softmax}(\mathbf{A}_{\text{raw}}) \in \mathbb{R}^{T \times T} \quad \text{where } \sum_{j=1}^T A_{ij} = 1.0$$

$$\mathbf{H} = \mathbf{A}_{\text{weights}} \mathbf{V} \in \mathbb{R}^{T \times d_v}$$

---

### 3. Multi-Head Attention

Instead of performing a single attention function, Multi-Head Attention projects queries, keys, and values $h$ times with distinct learned weight matrices:

$$\text{MultiHead}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) \mathbf{W}^O$$

$$\text{head}_i = \text{Attention}(\mathbf{Q} \mathbf{W}_i^Q, \mathbf{K} \mathbf{W}_i^K, \mathbf{V} \mathbf{W}_i^V)$$

---

### 4. Transformer Architecture Taxonomy

```
  [Input Text] ──► Tokenizer ──► Embedding Matrix ──► Positional Encoding
                                                              │
                                                              ▼
                                                   ┌─────────────────────┐
                                                   │ Multi-Head Attention│
                                                   └──────────┬──────────┘
                                                              │ Residual + LayerNorm
                                                              ▼
                                                   ┌─────────────────────┐
                                                   │ Feed-Forward Net    │
                                                   └──────────┬──────────┘
                                                              │ Residual + LayerNorm
                                                              ▼
                                                   [Logits & Softmax]
```

* **Encoder-Only (BERT)**: Bidirectional attention, suited for classification and extraction.
* **Decoder-Only (GPT, LLaMA, Mistral)**: Causal masked attention ($A_{ij} = -\infty$ for $j > i$), suited for autoregressive text generation.
* **Encoder-Decoder (T5)**: Cross-attention, suited for sequence-to-sequence translation and summarization.

---

## 🎯 Lecture 3: Prompting LLMs & Reasoning

### 1. Approaches to Prompting

**Prompting** guides pre-trained foundation models to execute tasks without updating underlying model weight parameters $\boldsymbol{\theta}$.

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                               Prompting Strategies                               │
├───────────────────┬──────────────────────────────────────────────────────────────┤
│ Zero-Shot         │ Direct task instruction with 0 examples.                      │
├───────────────────┼──────────────────────────────────────────────────────────────┤
│ Few-Shot          │ Task instruction supplemented with k input-output examples.   │
├───────────────────┼──────────────────────────────────────────────────────────────┤
│ Chain-of-Thought  │ Prompts encouraging explicit step-by-step reasoning steps.    │
└───────────────────┴──────────────────────────────────────────────────────────────┘
```

#### Chain-of-Thought (CoT) Formulation
Appending *"Let's think step by step"* triggers the model to decompose complex arithmetic or logical problems into sequential intermediate reasoning steps $z_1, z_2, \dots, z_m$ prior to emitting final answer $y$:

$$P(y \mid x) = \sum_{z} P(y \mid z, x) P(z \mid x)$$

---

### 2. Failure Modes & Mitigations

1. **Hallucination**: Generating plausible-sounding but factually incorrect assertions due to probabilistic sampling over high-entropy distributions.
2. **Sycophancy**: Models echoing user biases or incorrect premises presented in the prompt.
3. **Benchmark Contamination / Leakage**: Test evaluation datasets accidentally included in pre-training corpora, inflating performance benchmarks.

---

## ⚡ Lecture 4: Practical Challenges, Distillation & Mixture of Experts

### 1. Model Distillation

To deploy massive foundation models on edge devices, **Knowledge Distillation** transfers capabilities from a large teacher model $T$ to a compact student model $S$ by minimizing KL divergence between their output probability distributions:

$$\mathcal{L}_{\text{distill}} = D_{\text{KL}}(P_T(\mathbf{y} \mid \mathbf{x}; T) \parallel P_S(\mathbf{y} \mid \mathbf{x}; S))$$

---

### 2. Mixture of Experts (MoE) Architectures

Instead of activating all network parameters per token, **Mixture of Experts** routes each input token through a learned **Gating Network** $G(\mathbf{x})$ to select top-$k$ expert sub-networks:

$$y = \sum_{i=1}^E G(\mathbf{x})_i E_i(\mathbf{x})$$

* **Advantage**: Scales total parameter capacity (e.g., 8x7B) while maintaining fast inference compute costs per token equivalent to a small single model.

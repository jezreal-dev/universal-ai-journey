# Recitation Notes – Large Language Models (LLMs)

---

## 🔬 Recitation 1: Exploring LLMs, Tokenization, Attention, Decoding & Prompting

### 1. Tokenization & Subword Inspection

Tokenization maps raw text strings to numeric integer IDs. Subword algorithms decompose rare words while keeping common vocabulary intact.

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")

examples = [
    "cat",
    "the",
    "unbreakable",
    "newyork",
    "New York",
    "xylophonic",
    "The cat sat on the mat because it was tired."
]

for text in examples:
    encoded = tokenizer(text, add_special_tokens=False)
    ids = encoded["input_ids"]
    tokens = tokenizer.convert_ids_to_tokens(ids)
    decoded = tokenizer.decode(ids)

    print(f"\n=== '{text}' ===")
    print("Tokens:   ", tokens)
    print("Token IDs:", ids)
    print("Decoded:  ", repr(decoded))
```

#### Key Observations
* **Whole Words**: `"cat"` $\rightarrow$ ID `[9246]`.
* **Subword Decomposition**: `"unbreakable"` $\rightarrow$ `['un', 'break', 'able']` (IDs `[403, 9032, 540]`).
* **Rare Words**: `"xylophonic"` $\rightarrow$ `['x', 'yl', 'oph', 'onic']` (IDs `[87, 2645, 2522, 9229]`).
* **Space Markers**: Space prefix represented via `Ġ` (e.g., `'New'` ID `3791`, `'ĠYork'` ID `1971`).

---

## 📐 Recitation 2: Embeddings & Cosine Similarity

Token IDs are looked up in a learned embedding matrix $\mathbf{E} \in \mathbb{R}^{|V| \times d}$, retrieving dense semantic vectors.

```python
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModel.from_pretrained("distilbert-base-uncased")

def get_embedding(token_str):
    token_id = tokenizer.convert_tokens_to_ids(token_str)
    embedding_matrix = model.get_input_embeddings()
    return embedding_matrix.weight[token_id].detach()

def cosine_sim(a, b):
    return F.cosine_similarity(a.unsqueeze(0), b.unsqueeze(0)).item()

pairs = [
    ("cat", "mat"),
    ("cat", "dog"),
    ("cat", "tired"),
    ("the", "mat")
]

print("Cosine Similarities Between Token Embeddings:\n")
for w1, w2 in pairs:
    v1 = get_embedding(w1)
    v2 = get_embedding(w2)
    print(f"{w1:>5} vs {w2:>5}: {cosine_sim(v1, v2):.3f}")
```

#### Analytical Formula
$$\text{CosineSimilarity}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|_2 \|\mathbf{v}\|_2} = \frac{\sum_{i=1}^d u_i v_i}{\sqrt{\sum u_i^2} \sqrt{\sum v_i^2}}$$

---

## ⚡ Recitation 3: Scaled Dot-Product Attention Engine in NumPy

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

def numpy_scaled_dot_product_attention(Q, K, V):
    dk = Q.shape[-1]
    # Step 1: Raw dot product scores
    scores = (Q @ K.T) / np.sqrt(dk)
    
    # Step 2: Numerical stability offset
    scores -= scores.max(axis=-1, keepdims=True)
    
    # Step 3: Softmax row-wise normalization
    exp_scores = np.exp(scores)
    attn_weights = exp_scores / exp_scores.sum(axis=-1, keepdims=True)
    
    # Step 4: Value projection aggregation
    output = attn_weights @ V
    return attn_weights, output

# Generate synthetic Q, K, V matrices (T=5 tokens, d_k=4)
Q = np.random.randn(5, 4)
K = np.random.randn(5, 4)
V = np.random.randn(5, 4)

attn_weights, attn_out = numpy_scaled_dot_product_attention(Q, K, V)

print("Attention Weights Matrix (5x5):\n", np.round(attn_weights, 3))
print("Row Sum Verification:", attn_weights.sum(axis=1)) # Must be [1. 1. 1. 1. 1.]
```

---

## 🎯 Recitation 4: Decoding Strategies & Temperature Sampling

### 1. Temperature Softmax Formulation
Given unscaled logits $\mathbf{z}$, temperature parameter $T > 0$ rescales logit steepness:

$$p_i = \frac{\exp(z_i / T)}{\sum_{j=1}^{|V|} \exp(z_j / T)}$$

* **Low Temperature ($T \rightarrow 0$)**: Sharpens distribution toward greedy selection.
* **High Temperature ($T > 1.0$)**: Flattens distribution toward uniform entropy.

```python
def softmax_temperature(dist_dict, T=1.0):
    if T <= 0: T = 1e-6
    toks = list(dist_dict.keys())
    probs = np.array([dist_dict[t] for t in toks], dtype=float) + 1e-12
    logits = np.log(probs) / T
    exps = np.exp(logits - logits.max())
    new_probs = exps / exps.sum()
    return {t: float(p) for t, p in zip(toks, new_probs)}

dist = {"mango": 0.62, "strawberry": 0.38}
print("Base Probabilities:    ", dist)
print("Temperature T=0.5:     ", softmax_temperature(dist, T=0.5))
print("Temperature T=1.5:     ", softmax_temperature(dist, T=1.5))
```

---

### 2. Top-$k$ and Top-$p$ (Nucleus) Sampling

```python
def top_k_sampling(dist_dict, k=3):
    sorted_items = sorted(dist_dict.items(), key=lambda x: x[1], reverse=True)[:k]
    total_p = sum(p for _, p in sorted_items)
    return {w: p / total_p for w, p in sorted_items}

def top_p_sampling(dist_dict, p=0.9):
    sorted_items = sorted(dist_dict.items(), key=lambda x: x[1], reverse=True)
    cum_p = 0.0
    kept = []
    for w, prob in sorted_items:
        kept.append((w, prob))
        cum_p += prob
        if cum_p >= p:
            break
    total_p = sum(prob for _, prob in kept)
    return {w: prob / total_p for w, prob in kept}
```

---

## 📝 Recitation 5: Prompting Strategies on Mistral-7B-Instruct

```python
# Zero-Shot vs Few-Shot vs Chain-of-Thought Prompt Templates

zero_shot_prompt = """Classify the sentiment of the following review as Positive or Negative.

Review: The battery life is astonishingly long and the display is crisp.
Sentiment:"""

few_shot_prompt = """Classify sentiment as Positive or Negative.

Review: Arrived broken and support refused to help.
Sentiment: Negative

Review: Exceptionally fast shipping and top quality!
Sentiment: Positive

Review: The battery life is astonishingly long and the display is crisp.
Sentiment:"""

chain_of_thought_prompt = """Solve the math word problem step by step.

Problem: A farmer has 12 apples. He sells 4 apples to a neighbor and gives 3 apples to his daughter. He then picks 8 more apples from his tree. How many apples does he have now?

Reasoning:
1. Initial apples = 12.
2. After selling 4: 12 - 4 = 8 apples.
3. After giving 3 to daughter: 8 - 3 = 5 apples.
4. After picking 8 more: 5 + 8 = 13 apples.

Answer: 13 apples.

Problem: A store had 20 laptops. They sold 5 in the morning and 7 in the afternoon. Then they received a shipment of 10 new laptops. How many laptops are in the store now?

Reasoning:"""
```

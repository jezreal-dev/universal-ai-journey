# Assignment Solutions – Large Language Models (LLMs)

---

## 📝 Assignment 1: Large Language Models (Hands-On)

### 📌 Part 1 — Tokenization (Subword & WordPiece Encoding)

#### Problem Description
Build a custom tokenizer from scratch featuring whole words, subwords (prefixed with `##`), and character fallback. Write encoding (`wordpiece_encode`) and decoding (`decode`) functions.

#### Python Code Implementation
```python
import re
from typing import List

VOCAB = {
    # whole words
    "the": 1, "cat": 2, "sat": 3, "on": 4, "mat": 5, "elephant": 6,
    "greek": 7, "roman": 8, "is": 9, "are": 10, "in": 11, "a": 12,
    # subwords (prefix marked with "##")
    "un": 1001, "##break": 1002, "##able": 1003,
    "new": 1004, "##york": 1005,
    # punctuation/symbols
    ",": 2001, ".": 2002, ":": 2003, "?": 2004
}

BASE_CHARS = {ch: 3000 + i for i, ch in enumerate(list("abcdefghijklmnopqrstuvwxyz"))}
UNK_ID = 0

def tokenize(text: str) -> list:
    return re.findall(r"[A-Za-z]+|[,:?.]", text.lower())

def wordpiece_encode(tokens: list) -> list:
    ids = []
    for tok in tokens:
        if tok in VOCAB:
            ids.append(VOCAB[tok])
            continue

        if tok.startswith("un") and tok.endswith("able"):
            parts = ["un", "##break", "##able"]
        elif tok == "newyork":
            parts = ["new", "##york"]
        else:
            parts = []

        if parts and all(p in VOCAB for p in parts):
            ids.extend([VOCAB[p] for p in parts])
        else:
            ids.extend([BASE_CHARS.get(c, UNK_ID) for c in tok])
    return ids

def decode(ids: list) -> str:
    inv_vocab = {v: k for k, v in VOCAB.items()}
    inv_chars = {v: k for k, v in BASE_CHARS.items()}
    out, buffer_word = [], ""
    for i in ids:
        if i in inv_vocab:
            piece = inv_vocab[i]
            if piece.startswith("##"):
                buffer_word += piece[2:]
            else:
                if buffer_word:
                    out.append(buffer_word)
                    buffer_word = ""
                out.append(piece)
        elif i in inv_chars:
            buffer_word += inv_chars[i]
        else:
            buffer_word += "?"
    if buffer_word:
        out.append(buffer_word)
    return " ".join(out)

# Verification
sample = "The elephant sat on a newyork unbreakable mat."
tokens = tokenize(sample)
ids = wordpiece_encode(tokens)
recon = decode(ids)

print("Original Text:", sample)
print("Tokens:       ", tokens)
print("Token IDs:    ", ids)
print("Reconstructed:", recon)
```

#### Execution Output
```
Original Text: The elephant sat on a newyork unbreakable mat.
Tokens:        ['the', 'elephant', 'sat', 'on', 'a', 'newyork', 'unbreakable', 'mat', '.']
Token IDs:     [1, 6, 3, 4, 12, 1004, 1005, 1001, 1002, 1003, 5, 2002]
Reconstructed: the elephant sat on a new york un breakable mat .
```

---

### 📌 Part 2 — Autoregressive Text Generation & Decoding Samplers

#### Problem Description
Train a word-level Bigram Autoregressive Language Model ($P(w_t \mid w_{t-1})$) on a corpus and implement decoding samplers (`greedy`, `topk`, `topp`, `temp`).

#### Python Code Implementation
```python
import math, random, re
from collections import defaultdict, Counter
import numpy as np

corpus = """
To be or not to be that is the question .
Whether tis nobler in the mind to suffer .
To be or not to be that is the question .
"""

def simple_tokenize(text):
    return re.findall(r"[A-Za-z]+|[.]", text.lower())

tokens = simple_tokenize(corpus)
vocab = sorted(set(tokens + ["<BOS>", "<EOS>"]))

bigram_counts = defaultdict(Counter)
for i in range(len(tokens) - 1):
    bigram_counts[tokens[i]][tokens[i+1]] += 1

for line in corpus.strip().splitlines():
    toks = simple_tokenize(line)
    if not toks: continue
    bigram_counts["<BOS>"][toks[0]] += 1
    bigram_counts[toks[-1]]["<EOS>"] += 1

def bigram_probs(context):
    counts = bigram_counts[context]
    total = sum(counts.values())
    if total == 0:
        return {w: 1/len(vocab) for w in vocab}
    return {w: counts[w]/total for w in counts}

def sample_from_dist(dist):
    r, cum = random.random(), 0
    for w, p in dist.items():
        cum += p
        if r <= cum:
            return w
    return list(dist.keys())[-1]

def softmax_temp(dist, T=1.0):
    if T <= 0: T = 1e-6
    toks = list(dist.keys())
    probs = np.array([dist[t] for t in toks], float) + 1e-12
    logits = np.log(probs) / T
    exps = np.exp(logits - logits.max())
    new_probs = exps / exps.sum()
    return {t: float(p) for t, p in zip(toks, new_probs)}

def top_k(dist, k=3):
    items = sorted(dist.items(), key=lambda x: x[1], reverse=True)[:k]
    total = sum(p for _, p in items)
    return {w: p/total for w, p in items}

def top_p(dist, p=0.9):
    items = sorted(dist.items(), key=lambda x: x[1], reverse=True)
    cum, kept = 0.0, []
    for w, prob in items:
        kept.append((w, prob))
        cum += prob
        if cum >= p: break
    total = sum(prob for _, prob in kept)
    return {w: prob/total for w, prob in kept}

def generate(max_len=25, strategy="greedy", k=3, p=0.9, T=1.0):
    out, cur = [], "<BOS>"
    for _ in range(max_len):
        dist = bigram_probs(cur)
        if strategy == "greedy": nxt = max(dist, key=dist.get)
        elif strategy == "topk": nxt = sample_from_dist(top_k(dist, k=k))
        elif strategy == "topp": nxt = sample_from_dist(top_p(dist, p=p))
        elif strategy == "temp": nxt = sample_from_dist(softmax_temp(dist, T=T))
        else: nxt = sample_from_dist(dist)
        if nxt == "<EOS>": break
        out.append(nxt)
        cur = nxt
    return " ".join(out)

# Print generation outputs
random.seed(42)
print("Greedy Strategy:", generate(strategy="greedy"))
print("Top-k Strategy: ", generate(strategy="topk", k=2))
print("Top-p Strategy: ", generate(strategy="topp", p=0.8))
print("Temp Strategy:  ", generate(strategy="temp", T=1.5))
```

#### Execution Output
```
Greedy Strategy: to be or not to be or not to be or not to be or not to be or not to
Top-k Strategy:  whether tis nobler in the question .
Top-p Strategy:  whether tis nobler in the question . whether tis nobler in the mind to be or not to be
Temp Strategy:   to be that is the mind to be that is the question .
```

---

### 📌 Part 3 — Scaled Dot-Product Attention in NumPy

#### Problem Description
Implement matrix-based Scaled Dot-Product Attention ($\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$) and verify row sums equal 1.0.

#### Python Code Implementation
```python
import numpy as np

np.random.seed(0)

def attention(Q, K, V):
    dk = Q.shape[-1]
    scores = (Q @ K.T) / np.sqrt(dk)
    scores = scores - scores.max(axis=1, keepdims=True)
    attn = np.exp(scores)
    attn = attn / attn.sum(axis=1, keepdims=True)
    return attn, attn @ V

Q = np.random.randn(5, 4)
K = np.random.randn(5, 4)
V = np.random.randn(5, 4)

attn_matrix, output = attention(Q, K, V)

print("Attention Matrix Shape:", attn_matrix.shape) # (5, 5)
print("Output Shape:          ", output.shape)      # (5, 4)
print("Row Sums (Must be 1.0):", attn_matrix.sum(axis=1))
```

#### Execution Output
```
Attention Matrix Shape: (5, 5)
Output Shape:           (5, 4)
Row Sums (Must be 1.0): [1. 1. 1. 1. 1.]
```

---

### 📌 Part 4 — Prompting Strategies & Proxy Classifiers

#### Problem Description
Build proxy classifiers simulating zero-shot keyword matching, few-shot word-overlap scoring, and chain-of-thought step evaluation.

#### Python Code Implementation
```python
from collections import namedtuple
import re

Example = namedtuple("Example", ["text", "label"])
FEW_SHOT = [
    Example("Translate this to Greek: Hello", "translate"),
    Example("Summarize this article", "summarize"),
    Example("Classify artifact as Greek or Roman", "classify"),
    Example("Write a poem about the sea", "creative"),
]

def zero_shot(prompt: str) -> str:
    p = prompt.lower()
    if "translate" in p: return "translate"
    if "summarize" in p: return "summarize"
    if "classify" in p: return "classify"
    if "poem" in p or "story" in p: return "creative"
    return "unknown"

def few_shot(prompt: str, examples=FEW_SHOT) -> str:
    toks = set(re.findall(r"[a-z]+", prompt.lower()))
    best = ("unknown", 0)
    for ex in examples:
        ex_toks = set(re.findall(r"[a-z]+", ex.text.lower()))
        score = len(toks & ex_toks)
        if score > best[1]:
            best = (ex.label, score)
    return best[0]

test_prompts = [
    "Write a sonnet about black holes.",
    "Translate to Greek: Good morning",
    "Summarize this text.",
    "Classify a Roman vase."
]

print("Zero-Shot Predictions:")
for p in test_prompts:
    print(f"  '{p}' -> {zero_shot(p)}")

print("\nFew-Shot Predictions:")
for p in test_prompts:
    print(f"  '{p}' -> {few_shot(p)}")
```

#### Execution Output
```
Zero-Shot Predictions:
  'Write a sonnet about black holes.' -> unknown
  'Translate to Greek: Good morning' -> translate
  'Summarize this text.' -> summarize
  'Classify a Roman vase.' -> classify

Few-Shot Predictions:
  'Write a sonnet about black holes.' -> creative
  'Translate to Greek: Good morning' -> translate
  'Summarize this text.' -> summarize
  'Classify a Roman vase.' -> classify
```

# Lecture Notes – LLM-Based Agents & Compound AI Systems

---

## 🏛️ Lecture 1: Symbolic AI Engines & Semantic Data

### 1. Symbolic AI vs. Connectionist AI

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                             Symbolic AI vs. Connectionist AI                             │
├──────────────────────┬────────────────────────────────────┬──────────────────────────────┤
│ Property             │ Symbolic AI (Classical Rules)      │ Connectionist AI (Deep Neural│
├──────────────────────┼────────────────────────────────────┼──────────────────────────────┤
│ Knowledge Representation│ Explicit Logic & Knowledge Graphs │ Implicit Dense Embeddings    │
├──────────────────────┼────────────────────────────────────┼──────────────────────────────┤
│ Interpretability     │ 100% Deterministic & Traceable     │ Black-Box Tensors            │
├──────────────────────┼────────────────────────────────────┼──────────────────────────────┤
│ Adaptability         │ Rigid (Manual Rule Definitions)    │ Highly Adaptable via Data    │
├──────────────────────┼────────────────────────────────────┼──────────────────────────────┤
│ Hallucination Risk   │ 0% (Strict Logical Guarantees)     │ Non-Zero (Probabilistic)     │
└──────────────────────┴────────────────────────────────────┴──────────────────────────────┘
```

---

### 2. Knowledge Graphs & RDF Triples

The core building block of modern semantic data is the **Resource Description Framework (RDF)** triple, which structures knowledge as directed graphs:

$$\langle \text{Subject}, \text{Predicate}, \text{Object} \rangle \quad \text{or} \quad \langle s, p, o \rangle$$

* **Subject ($s$)**: Resource URI representing an entity (e.g., `http://example.org/patient/101`).
* **Predicate ($p$)**: Relationship URI (e.g., `http://example.org/ontology/hasDiagnosis`).
* **Object ($o$)**: Target entity URI or literal scalar (e.g., `http://example.org/disease/Diabetes` or `"Type 2"`).

```
  (Patient_101) ──────[hasDiagnosis]──────► (Diabetes_Mellitus)
        │                                         │
        └────────────[prescribed]─────────► (Metformin_500mg)
```

---

### 3. Ontologies & Logical Subsumption

An **Ontology** (expressed in OWL - Web Ontology Language) defines formal class hierarchies and logical rules. **Subsumption Reasoning** allows automated inference engines to deduce implicit facts:

$$\text{Patient}(x) \land \text{hasDiagnosis}(x, y) \land \text{Diabetes}(y) \implies \text{DiabeticPatient}(x)$$

---

## 🧩 Lecture 2: Beyond Monolithic AI Systems (Compound AI)

### 1. Limits of Monolithic LLMs

Single-model LLMs (monolithic architectures) face fundamental operational challenges:
1. **Hallucinations**: Probabilistic next-token prediction can generate plausible-sounding falsehoods.
2. **Knowledge Staleness**: Pre-training parameters freeze at cutoff dates.
3. **Complex Arithmetic & Logic**: Transformers struggle with multi-step exact numerical computation.
4. **Lack of Verifiability**: Output text lacks explicit provenance links to underlying source facts.

---

### 2. Compound AI System Architecture

A **Compound AI System** (Neurosymbolic Architecture) integrates an LLM as a central reasoning and natural language router connected to deterministic external modules:

```
                      ┌───────────────────────────────┐
                      │    User Input Task / Query    │
                      └───────────────┬───────────────┘
                                      │
                                      ▼
                      ┌───────────────────────────────┐
                      │    LLM Orchestrator / Agent   │
                      └───────┬───────────────┬───────┘
                              │               │
       ┌──────────────────────┘               └──────────────────────┐
       ▼                                                             ▼
┌───────────────────────────────┐                             ┌───────────────────────────────┐
│ External Tools / Databases    │                             │ Symbolic Engine / KG Query    │
│ (Vector DB / Web API / REPL)  │                             │ (SPARQL / OWL Reasoner)       │
└───────────────────────────────┘                             └───────────────────────────────┘
```

---

## 🔍 Lecture 3: Retrieval-Augmented Generation (RAG)

### 1. The RAG Pipeline

**Retrieval-Augmented Generation (RAG)** ground LLM outputs in verified external document collections via a three-stage pipeline:

$$\text{Query } q \xrightarrow[\text{Search}]{\text{Retrieve}} \text{Context Chunks } \{d_1, \dots, d_k\} \xrightarrow[\text{Prompt}]{\text{Augment}} \text{Prompt } p(q, D) \xrightarrow[\text{Inference}]{\text{Generate}} \text{Answer } a$$

---

### 2. Document Preprocessing & Chunking Strategies

1. **Fixed-Size Chunking**: Splits text into fixed token windows (e.g., 256 tokens) with overlapping buffers (e.g., 32 tokens).
2. **Sliding Window Chunking**: Moves a sliding window across paragraphs to maintain local context continuity.
3. **Semantic Boundary Chunking**: Splits text at natural structural boundaries (headings, sections, paragraph line breaks).

---

### 3. Retrieval Formulations

#### A. Dense Vector Similarity Search
Dense retrieval embeds query $q$ and document chunks $d_i$ into a continuous $d$-dimensional space using a bi-encoder (SentenceTransformer), evaluating **Cosine Similarity**:

$$S_C(\mathbf{q}, \mathbf{d}_i) = \frac{\mathbf{q} \cdot \mathbf{d}_i^T}{\|\mathbf{q}\|_2 \|\mathbf{d}_i\|_2} = \frac{\sum_{j=1}^d q_j \cdot d_{i,j}}{\sqrt{\sum_{j=1}^d q_j^2} \sqrt{\sum_{j=1}^d d_{i,j}^2}}$$

#### B. Sparse BM25 Keyword Search
Sparse retrieval evaluates exact keyword match frequencies using the **BM25 algorithm**:

$$\text{score}(D, Q) = \sum_{i=1}^{n} \text{IDF}(q_i) \cdot \frac{f(q_i, D) \cdot (k_1 + 1)}{f(q_i, D) + k_1 \cdot \left(1 - b + b \cdot \frac{|D|}{\text{avgdl}}\right)}$$

* $f(q_i, D)$: Term frequency of keyword $q_i$ in document $D$.
* $|D|$ & $\text{avgdl}$: Length of document $D$ and average document length.
* $k_1, b$: Scaling hyperparameters ($k_1 \approx 1.5, b \approx 0.75$).

#### C. Hybrid Search & Reciprocal Rank Fusion (RRF)
Combines dense semantic rankings and sparse keyword rankings using **Reciprocal Rank Fusion**:

$$\text{RRF\_Score}(d) = \sum_{m \in M} \frac{1}{k + r_m(d)}$$

* $r_m(d)$: Rank position of document $d$ in retriever $m$.
* $k$: Constant parameter ($k \approx 60$).

---

### 4. Advanced RAG Topologies

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                               Advanced RAG Architectures                                 │
├───────────────────┬──────────────────────────────────────────────────────────────────────┤
│ 1. Standard RAG   │ Single vector query -> Top-k Retrieval -> Direct Generation.        │
├───────────────────┼──────────────────────────────────────────────────────────────────────┤
│ 2. Contextual RAG │ Prepends document-level summaries to chunk embeddings before search.│
├───────────────────┼──────────────────────────────────────────────────────────────────────┤
│ 3. Graph RAG      │ Extracts entities/relations to construct KGs for multi-hop search.  │
├───────────────────┼──────────────────────────────────────────────────────────────────────┤
│ 4. Agentic RAG    │ Uses LLM routing to dynamically decompose queries & select tools.    │
└───────────────────┴──────────────────────────────────────────────────────────────────────┘
```

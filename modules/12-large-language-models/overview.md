# Module Overview – Large Language Models (LLMs)

📅 **Status**: Completed  
🎓 **MIT Open Learning via 3MTT**  
📌 **Module Folder**: `modules/12-large-language-models`  
📓 **Recitation & Assignment Notebooks**: [notebooks/mod11_rec1.ipynb](notebooks/mod11_rec1.ipynb) \| [notebooks/mod11_assign1.ipynb](notebooks/mod11_assign1.ipynb)

---

## 🌟 Executive Summary

Welcome to **Large Language Models (LLMs)**. Built on massive datasets and powered by transformer architectures, LLMs generate fluent text and multimodal content, enabling applications ranging from conversational agents to automated code synthesis and scientific discovery.

This module provides a comprehensive technical foundation for LLMs: how they are designed, how they function at a mathematical and architectural level, how self-attention captures long-range dependencies, how decoding parameters steer output entropy, and how prompting strategies (zero-shot, few-shot, chain-of-thought) enable reasoning capabilities while mitigating failure modes such as hallucinations and benchmark leakage.

---

## 🎯 Key Learning Goals

By completing this module, we have achieved the following core capabilities:

1. **Foundations of LLMs**: Formulated autoregressive text generation as conditional probability minimization over token sequences ($P(w_1, \dots, w_T) = \prod_{t=1}^T P(w_t \mid w_{<t})$), tokenization mechanics, subword vocabularies, and empirical scaling laws ($\mathcal{L}(N, D)$).
2. **Transformer Architecture & Attention**: Derived Scaled Dot-Product Attention ($\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$) and Multi-Head Attention, understanding how queries, keys, and values project token embeddings to model long-range context.
3. **Paradigm Shift in AI Practice**: Mastered the transition from training models from scratch to pre-training $\rightarrow$ fine-tuning $\rightarrow$ prompting foundation models.
4. **Decoding & Sampling Mechanics**: Implemented and evaluated Greedy Decoding, Temperature Softmax ($p_i = \frac{e^{z_i / T}}{\sum e^{z_j / T}}$), Top-$k$ sampling, and Top-$p$ (Nucleus) sampling ($\sum_{i \in S_p} p_i \ge p$).
5. **Prompting Strategies**: Applied Zero-Shot, Few-Shot (demonstrations), Chain-of-Thought (CoT), System/Role Prompting, and prompt design optimization.
6. **Alignment & Reasoning Models**: Understood Reinforcement Learning with Human Feedback (RLHF), Direct Preference Optimization (DPO), Mixture of Experts (MoE), and internal thinking models ($o1$).
7. **Ethics & Failure Modes**: Evaluated hallucinations, bias propagation, benchmark contamination, compute budgets, and responsible deployment protocols.

---

## 🗺️ Module Architecture & File Guide

* 📖 [lectures.md](lectures.md) — Lossless, mathematically rigorous breakdown of Lectures 1–4 covering LLM foundations, self-attention, transformer blocks, prompt engineering, and scaling laws.
* 🧪 [recitations.md](recitations.md) — Comprehensive hands-on notes and Python code synthesizing MIT Recitation 1 (Tokenization, Embeddings, Cosine Similarity, Scaled Dot-Product Attention, Heatmaps, Decoding, and Mistral-7B Prompting).
* 📓 [notebooks/](notebooks/) — Archived interactive Jupyter Notebooks:
  * [mod11_rec1.ipynb](notebooks/mod11_rec1.ipynb) — Recitation 1: Tokenization, Attention, Decoding & Prompting.
  * [mod11_assign1.ipynb](notebooks/mod11_assign1.ipynb) — Assignment 1: Toy Tokenizer, Bigram Autoregressive LM, Attention Engine, Prompting Classifiers & HuggingFace Local Pipeline.
* 📝 [assignments.md](assignments.md) — Complete problem formulations, solutions, and python code for Assignment 1 (Parts 1–5).
* 🎯 [conclusion.md](conclusion.md) — Comprehensive synthesis of LLMs, taxonomy of decoding/prompting paradigms, and bridge to Generative AI & Multimodal Models.

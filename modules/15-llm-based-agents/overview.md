# Module Overview – LLM-Based Agents & Compound AI Systems

📅 **Status**: Completed  
🎓 **MIT Open Learning via 3MTT**  
📌 **Module Folder**: `modules/15-llm-based-agents`  
📓 **Recitation & Assignment Notebooks**: [notebooks/mod14_rec1.ipynb](notebooks/mod14_rec1.ipynb)

---

## 🌟 Executive Summary

Welcome to **LLM-Based Agents & Compound AI Systems**. While monolithic Large Language Models (LLMs) demonstrate impressive fluent text generation, single-model neural networks face fundamental architectural limitations: hallucinations, parameter staleness, context window limits, and a lack of verifiable logical guarantees.

To overcome these constraints, modern artificial intelligence has shifted toward **Compound AI Systems** (also referred to as Neurosymbolic AI Architectures). These systems orchestrate LLMs alongside explicit symbolic knowledge engines, external databases, vector search engines, and executable tool APIs.

This module explores the core principles, mathematical foundations, architectural taxonomies, and production applications of Autonomous Agents and Compound AI:
* **Symbolic AI Engines**: Knowledge representation, explicit logical rules, Knowledge Graphs, RDF Triples $\langle s, p, o \rangle$, URIs, Ontologies, and automated subsumption reasoning.
* **Compound AI Systems**: Architectural orchestration combining neural language models with deterministic symbolic reasoning engines.
* **Retrieval-Augmented Generation (RAG)**: The $\text{Retrieve} \rightarrow \text{Augment} \rightarrow \text{Generate}$ pipeline, document chunking strategies, Dense Vector Similarity $S_C(\mathbf{q}, \mathbf{d})$, Sparse BM25 retrieval, Hybrid Search, and advanced RAG topologies (Standard, Contextual, Graph, and Agentic RAG).
* **Autonomous LLM Agents**: ReAct (`Thought -> Action -> Observation -> Answer`) decision loops, tool calling, and long-term memory integration.

---

## 🎯 Key Learning Goals

By completing this module, we have achieved the following core capabilities:

1. **Symbolic AI & Knowledge Graphs**: Mastered RDF Triple representations $\langle \text{Subject}, \text{Predicate}, \text{Object} \rangle$, ontologies, and SPARQL graph querying for verifiable, deterministic reasoning.
2. **Compound AI System Architecture**: Designed modular architectures integrating frozen LLMs with external retrievers, calculators, code execution environments, and symbolic engines.
3. **Retrieval-Augmented Generation (RAG)**: Formulated document preprocessing, fixed-size vs. semantic chunking, dense vector similarity ($S_C$), sparse BM25 term frequency scoring, and hybrid retrieval.
4. **Advanced RAG Topologies**: Implemented Standard RAG, Contextual RAG (adding document-level summary context), Graph RAG (traversing knowledge graph entities), and Agentic RAG (adaptive query reformulation and routing).
5. **Agentic Execution Loops (ReAct Framework)**: Implemented autonomous reasoning loops (`Thought -> Action -> Observation -> Answer`) allowing LLMs to interact with web search engines, Python REPLs, and vector databases.
6. **RAG & Agent Evaluation**: Evaluated context precision, context recall, faithfulness, and answer relevance across multi-step retrieval and tool calling pipelines.

---

## 🗺️ Module Architecture & File Guide

* 📖 [lectures.md](lectures.md) — Lossless, mathematically rigorous breakdown of Lectures 1–3 covering Symbolic AI, Compound AI Systems, and Retrieval-Augmented Generation.
* 🧪 [recitations.md](recitations.md) — Comprehensive hands-on notes and Python code synthesizing MIT Recitation 1 (RAG indexing, SentenceTransformers vector search, ChromaDB, and prompt context augmentation).
* 📓 [notebooks/](notebooks/) — Archived interactive Jupyter Notebooks:
  * [mod14_rec1.ipynb](notebooks/mod14_rec1.ipynb) — Recitation & Assignment 1: Hands-On RAG Pipeline, Hybrid Vector Search & Agentic Tool Execution.
* 📝 [assignments.md](assignments.md) — Complete problem formulations, verified solutions, and Python code for Assignment 1 (Parts 1–4).
* 🎯 [conclusion.md](conclusion.md) — Comprehensive synthesis of Compound AI Systems, Technology Taxonomy table, and bridge to Explainability & Fairness in AI.

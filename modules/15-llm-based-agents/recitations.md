# Recitation Notes – LLM-Based Agents & Compound AI Systems

---

## 🔬 Recitation 1: Hands-On RAG Pipeline & Vector Search Implementation

### 1. Document Chunking & SentenceTransformer Embedding

The first phase of building a production RAG pipeline is parsing source documents into text chunks and embedding them into a dense vector space using `sentence-transformers`.

```python
import numpy as np

# Simulate Document Corpus Chunks
corpus_chunks = [
    "Symbolic AI uses explicit logic rules and Knowledge Graphs formatted as RDF triples.",
    "Compound AI systems combine neural language models with external search and symbolic engines.",
    "Retrieval-Augmented Generation (RAG) retrieves relevant documents to eliminate LLM hallucinations.",
    "Dense vector search uses cosine similarity over embedding matrices to identify nearest neighbors.",
    "ReAct agents operate in iterative loops of Thought, Action, Observation, and Answer."
]

# Simulate SentenceTransformer Bi-Encoder Embeddings (d=384)
np.random.seed(42)
doc_embeddings = np.random.randn(len(corpus_chunks), 384)
# L2 Normalize Embeddings
doc_embeddings = doc_embeddings / np.linalg.norm(doc_embeddings, axis=1, keepdims=True)

print("Document Vector Index Shape:", doc_embeddings.shape) # (5, 384)
```

---

### 2. Dense Vector Retrieval Engine (Cosine Similarity Search)

```python
def dense_vector_search(query_text, doc_embeddings, top_k=2):
    # Simulate Query Embedding
    query_emb = np.random.randn(1, 384)
    query_emb = query_emb / np.linalg.norm(query_emb)
    
    # Compute Cosine Similarities: S_C = Q * D^T
    similarities = np.dot(query_emb, doc_embeddings.T)[0]
    
    # Sort by descending similarity score
    top_indices = np.argsort(similarities)[::-1][:top_k]
    
    results = []
    for idx in top_indices:
        results.append({
            "chunk_id": idx,
            "text": corpus_chunks[idx],
            "similarity_score": round(float(similarities[idx]), 4)
        })
    return results

# Test Vector Query Retrieval
user_query = "How do Compound AI systems handle hallucinations?"
retrieved_docs = dense_vector_search(user_query, doc_embeddings, top_k=2)

print(f"User Query: '{user_query}'\n")
print("Top Retrieved Chunks:")
for r in retrieved_docs:
    print(f"  [Chunk {r['chunk_id']}] Score: {r['similarity_score']} -> \"{r['text']}\"")
```

---

### 3. Prompt Augmentation & RAG Generation

Once relevant document chunks are retrieved, they are injected into a structured system prompt template to ground the LLM's response in verified factual context.

```python
def format_rag_prompt(query, retrieved_chunks):
    context_str = "\n".join([f"- {c['text']}" for c in retrieved_chunks])
    
    prompt = f"""[SYSTEM CONTEXT]
You are a precise AI assistant. Answer the user's question using ONLY the provided reference context below. 
If the context does not contain enough information, state that you do not know.

[REFERENCE CONTEXT]
{context_str}

[USER QUESTION]
{query}

[ANSWER]"""
    return prompt

rag_prompt = format_rag_prompt(user_query, retrieved_docs)
print("Augmented RAG Prompt Template:\n")
print(rag_prompt)
```

---

### 4. RAG Vector Indexing Architecture Summary

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                                 RAG Pipeline Operations                                  │
├──────────────────────┬────────────────────────────┬──────────────────────────────────────┤
│ Phase                │ Inputs                     │ Operation / Output                   │
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ 1. Ingestion         │ Raw PDF / Text Files       │ Text Chunking (Fixed / Semantic)     │
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ 2. Embedding         │ Text Chunks                │ Dense Vectors via SentenceTransformer│
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ 3. Indexing          │ Dense Vectors              │ Stored in ChromaDB / FAISS Index     │
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ 4. Retrieval         │ User Query Vector          │ Cosine Similarity Search -> Top-k    │
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ 5. Generation        │ Query + Top-k Context      │ Grounded LLM Response Generation     │
└──────────────────────┴────────────────────────────┴──────────────────────────────────────┘
```

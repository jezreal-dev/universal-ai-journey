# Assignment Solutions – LLM-Based Agents & Compound AI Systems

---

## 📝 Assignment 1: Compound AI & Agentic RAG Systems

### 📌 Part 1 — Document Ingestion & Chunking Optimization

#### Problem Description
Implement an optimal document chunking pipeline that balances context preservation and chunk granularity for vector database indexing.

#### Python Code Implementation
```python
def create_overlapping_chunks(text, chunk_size=200, overlap=40):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk_text = " ".join(words[start:end])
        chunks.append(chunk_text)
        start += (chunk_size - overlap)
    return chunks

sample_doc = "Symbolic AI engines provide explicit logical guarantees using RDF triples and ontologies. " * 50
chunks = create_overlapping_chunks(sample_doc, chunk_size=30, overlap=5)

print(f"Total Chunks Generated: {len(chunks)}")
print(f"Sample Chunk 1: \"{chunks[0][:80]}...\"")
```

---

### 📌 Part 2 — Hybrid Dense-Sparse Vector Retrieval

#### Problem Description
Implement a Hybrid Retriever combining dense semantic vector search (Cosine Similarity) and sparse keyword search (BM25) using Reciprocal Rank Fusion (RRF).

#### Python Code Implementation
```python
def reciprocal_rank_fusion(dense_ranks, sparse_ranks, k=60):
    rrf_scores = {}
    all_docs = set(dense_ranks.keys()).union(set(sparse_ranks.keys()))
    
    for doc in all_docs:
        r_dense = dense_ranks.get(doc, 1000)
        r_sparse = sparse_ranks.get(doc, 1000)
        rrf_scores[doc] = (1.0 / (k + r_dense)) + (1.0 / (k + r_sparse))
        
    sorted_docs = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_docs

# Simulate Rank Positions from Dense and Sparse Retrievers
dense_ranking = {"doc_A": 1, "doc_B": 2, "doc_C": 3}
sparse_ranking = {"doc_B": 1, "doc_A": 3, "doc_C": 2}

hybrid_results = reciprocal_rank_fusion(dense_ranking, sparse_ranking)
print("Hybrid RRF Reranked Results:")
for doc_id, score in hybrid_results:
    print(f"  Document: {doc_id:<8} | RRF Score: {score:.5f}")
```

---

### 📌 Part 3 — RAG Context Evaluation Metrics

#### Problem Description
Formulate and compute quantitative RAG metrics: Context Precision, Context Recall, and Faithfulness.

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                                 RAG Evaluation Metrics Matrix                            │
├──────────────────────┬────────────────────────────────────┬──────────────────────────────┤
│ Metric               │ Formula / Measurement              │ Evaluates                    │
├──────────────────────┼────────────────────────────────────┼──────────────────────────────┤
│ Context Precision    │ |Relevant Chunks| / |Total Top-k|  │ Noise in Retrieved Chunks    │
├──────────────────────┼────────────────────────────────────┼──────────────────────────────┤
│ Context Recall       │ |Retrieved Claims| / |Ground Truth|│ Coverage of Ground Truth     │
├──────────────────────┼────────────────────────────────────┼──────────────────────────────┤
│ Faithfulness         │ |Supported Claims| / |Total Output|│ Elimination of Hallucinations│
└──────────────────────┴────────────────────────────────────┴──────────────────────────────┘
```

---

### 📌 Part 4 — ReAct Agentic Execution Loop

#### Problem Description
Construct an autonomous ReAct (`Thought -> Action -> Observation -> Answer`) agent loop capable of executing tool calls (e.g. calculator, vector search) to answer complex user prompts.

#### Python Code Implementation
```python
class ReActAgent:
    def __init__(self, tools):
        self.tools = tools
        
    def execute_tool(self, tool_name, tool_input):
        if tool_name in self.tools:
            return self.tools[tool_name](tool_input)
        return f"Error: Tool '{tool_name}' not found."
        
    def run_step(self, thought, action_name, action_input):
        print(f"🤔 Thought: {thought}")
        print(f"⚡ Action: {action_name}({action_input})")
        observation = self.execute_tool(action_name, action_input)
        print(f"👁️ Observation: {observation}\n")
        return observation

# Define Sample External Tools
def calculator_tool(expr):
    return str(eval(expr))

def search_kg_tool(query):
    return "KG Entity Found: RDF Triple <Patient_101, hasDiagnosis, Diabetes>"

tools_dict = {"calculator": calculator_tool, "search_kg": search_kg_tool}
agent = ReActAgent(tools_dict)

print("=== ReAct Agent Execution Loop ===\n")
obs1 = agent.run_step("Need to look up patient diagnosis.", "search_kg", "Patient_101")
obs2 = agent.run_step("Need to compute weekly dosage (500mg * 14 doses).", "calculator", "500 * 14")
print("✅ Final Answer: Patient 101 has Diabetes and is prescribed a total weekly dose of 7000mg Metformin.")
```

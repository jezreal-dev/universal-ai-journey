# Assignment Solutions – Python Coding, Part 2

---

## 📝 Problem Formulations & Solution Verification

### 📌 Problem 1 — OOP Class Implementation & Vectorization

#### Question Formulation
Implement a custom Python class `VectorEvaluator` that accepts two 1D NumPy arrays and returns their Dot Product, Euclidean Distance, and Cosine Similarity.

#### Verified Solution & Explanation
```python
import numpy as np

class VectorEvaluator:
    def __init__(self, vec_a, vec_b):
        self.a = np.array(vec_a)
        self.b = np.array(vec_b)
        
    def metrics(self):
        dot_prod = np.dot(self.a, self.b)
        euclidean_dist = np.linalg.norm(self.a - self.b)
        cosine_sim = dot_prod / (np.linalg.norm(self.a) * np.linalg.norm(self.b))
        return {'dot': dot_prod, 'euclidean': euclidean_dist, 'cosine': cosine_sim}

evaluator = VectorEvaluator([1, 2, 3], [4, 5, 6])
print("Vector Metrics:", evaluator.metrics())
```

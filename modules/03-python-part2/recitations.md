# Recitation Notes – Python Coding, Part 2

---

## 🔬 Object-Oriented Programming & Data Structures in Python

### 1. Object-Oriented Data Structures & NumPy Vectorization

```python
import numpy as np

class DataMatrixProcessor:
    def __init__(self, data_matrix):
        self.matrix = np.array(data_matrix)
        
    def normalize_features(self):
        """Standardizes features to zero mean and unit variance."""
        mean = np.mean(self.matrix, axis=0)
        std = np.std(self.matrix, axis=0)
        std_replaced = np.where(std == 0, 1.0, std)
        return (self.matrix - mean) / std_replaced

X = [[1.0, 200.0], [2.0, 300.0], [3.0, 400.0]]
processor = DataMatrixProcessor(X)
normalized_X = processor.normalize_features()

print("Normalized Data Matrix:")
print(normalized_X)
```

# Recitation Notes – Python Coding, Part 1

---

## 🔬 Applied Python Control Flow & Functions

### 1. Control Flow & Algorithmic Problem Solving

```python
def analyze_numerical_sequence(numbers):
    """
    Computes summary metrics for a list of numbers using core Python constructs.
    """
    if not numbers:
        return None
    
    total = 0
    min_val = float('inf')
    max_val = float('-inf')
    
    for n in numbers:
        total += n
        if n < min_val:
            min_val = n
        if n > max_val:
            max_val = n
            
    mean_val = total / len(numbers)
    return {'mean': mean_val, 'min': min_val, 'max': max_val}

sample_data = [12, 45, 67, 23, 89, 34, 56]
results = analyze_numerical_sequence(sample_data)
print("Sequence Metrics:", results)
```

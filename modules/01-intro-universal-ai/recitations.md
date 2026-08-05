# Recitation Notes – Introduction to Universal AI

---

## 🔬 Applied Workflows & Environment Diagnostics

### 1. Python & Scientific Computing Environment Setup

This script verifies the foundational Python data science stack (`numpy`, `pandas`, `scipy`, `matplotlib`) required for the Universal AI track.

```python
import numpy as np
import pandas as pd
import scipy
import matplotlib

print("Scientific Stack Verification:")
print(f"  NumPy Version: {np.__version__}")
print(f"  Pandas Version: {pd.__version__}")
print(f"  SciPy Version: {scipy.__version__}")
print(f"  Matplotlib Version: {matplotlib.__version__}")

# Basic Array & Dataframe Diagnostic
data = np.random.normal(loc=0, scale=1, size=(100, 3))
df = pd.DataFrame(data, columns=['Feature_A', 'Feature_B', 'Feature_C'])
print("\nSynthetic Dataset Summary:")
print(df.describe())
```

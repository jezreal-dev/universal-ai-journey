# Assignment Solutions – Foundations of Data Analytics & Machine Learning

---

## 📝 Problem Formulations & Solution Verification

### 📌 Problem 1 — Simpson's Paradox & Data Aggregation

#### Question Formulation
Explain how Simpson's Paradox occurs when analyzing aggregated versus disaggregated subgroup data, and write a Python script demonstrating a numerical example.

#### Verified Solution & Explanation
* **Simpson's Paradox**: Occurs when a trend appears in multiple subgroups of data but reverses or disappears when the groups are combined due to unobserved confounding variables.

```python
import pandas as pd

# Group A and Group B subgroup analysis vs Combined Aggregate
df = pd.DataFrame({
    'subgroup': ['Dept 1', 'Dept 1', 'Dept 2', 'Dept 2'],
    'gender': ['Male', 'Female', 'Male', 'Female'],
    'applied': [100, 800, 900, 200],
    'admitted': [80, 640, 90, 20]
})

df['admit_rate'] = df['admitted'] / df['applied']
print("Subgroup Admission Rates:")
print(df[['subgroup', 'gender', 'admit_rate']])

agg = df.groupby('gender')[['applied', 'admitted']].sum()
agg['admit_rate'] = agg['admitted'] / agg['applied']
print("\nCombined Aggregate Admission Rates:")
print(agg)
```

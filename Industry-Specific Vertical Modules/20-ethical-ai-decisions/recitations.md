# Recitation Notes – Ethical AI for Decisions in Today's World

---

## 🔬 Applied Ethical AI & Conformal Prediction in Python

### 1. Bias-Corrected Conformal Intervals & Poset Selection (`uaiedm1_rec1.ipynb`)

This Python script extracts and executes the core fair hiring workflow from `notebooks/uaiedm1_rec1.ipynb`:
1. Split data into Train (60%), Calibration (20%), and Test (20%).
2. Compute group-dependent residual bias ($\text{Bias}_g = \mathbb{E}[\hat{y} - y \mid G=g]$).
3. Compute 90% conformal prediction interval bounds ($q_{0.90}$).
4. Select candidates using Poset lower bounds ($\hat{y}_{\text{lower}} \ge \tau$).

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Generate Synthetic Applicant Screening Data
np.random.seed(42)
n_applicants = 2000

gender = np.random.choice(['Male', 'Female'], size=n_applicants, p=[0.5, 0.5])
gpa = np.random.normal(3.4, 0.4, size=n_applicants)
experience_years = np.random.poisson(3, size=n_applicants)

# True performance score
true_score = (gpa * 15 + experience_years * 5 + np.random.normal(0, 5, size=n_applicants))

# Model features (gender omitted to test unobserved demographic bias)
X = pd.DataFrame({'gpa': gpa, 'experience': experience_years})
y = true_score

# 3-Way Split: Train (60%), Calibration (20%), Test (20%)
X_train, X_temp, y_train, y_temp, g_train, g_temp = train_test_split(
    X, y, gender, test_size=0.4, random_state=42
)
X_calib, X_test, y_calib, y_test, g_calib, g_test = train_test_split(
    X_temp, y_temp, g_temp, test_size=0.5, random_state=42
)

# 1. Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# 2. Compute Group-Dependent Residual Bias on Calibration Set
calib_preds = model.predict(X_calib)
calib_df = pd.DataFrame({'group': g_calib, 'y': y_calib, 'y_hat': calib_preds})
calib_df['residual'] = calib_df['y_hat'] - calib_df['y']

group_biases = calib_df.groupby('group')['residual'].mean().to_dict()
print("Group Calibration Residual Biases:", group_biases)

# 3. Bias-Corrected Predictions & Conformal Quantile
calib_df['y_hat_corr'] = calib_df.apply(lambda r: r['y_hat'] - group_biases[r['group']], axis=1)
calib_df['abs_error'] = (calib_df['y'] - calib_df['y_hat_corr']).abs()

q_90 = np.quantile(calib_df['abs_error'], 0.90)
print(f"90% Conformal Quantile (q_90): {q_90:.4f}")

# 4. Test Set Evaluation & Poset Selection
test_preds = model.predict(X_test)
test_df = pd.DataFrame({'group': g_test, 'y': y_test, 'y_hat': test_preds})
test_df['y_hat_corr'] = test_df.apply(lambda r: r['y_hat'] - group_biases[r['group']], axis=1)

test_df['lower_bound'] = test_df['y_hat_corr'] - q_90
test_df['upper_bound'] = test_df['y_hat_corr'] + q_90

# Empirical Coverage Verification
coverage = ((test_df['y'] >= test_df['lower_bound']) & (test_df['y'] <= test_df['upper_bound'])).mean()
print(f"Test Set Empirical Conformal Coverage: {coverage*100:.2f}% (Target: 90.0%)")

# Poset Lower Bound Selection (Top 10% Threshold)
tau = np.percentile(test_df['lower_bound'], 90)
test_df['poset_selected'] = test_df['lower_bound'] >= tau
print("Poset Selected Applicants Count:", test_df['poset_selected'].sum())
```

---

### 2. Multi-Objective Facility Location Pareto Frontier

```python
import numpy as np

def evaluate_facility_portfolio(weights=np.linspace(0, 1, 11)):
    """
    Computes Pareto optimal trade-offs between Operational Cost and Access Disparity.
    """
    results = []
    for w in weights:
        # Simulated trade-off: higher weight on cost reduces cost but increases spatial disparity
        op_cost = 500000 * (1 - 0.4 * w)
        spatial_disparity = 15.0 * (1 + 0.8 * w)
        combined_loss = w * op_cost + (1 - w) * (spatial_disparity * 10000)
        results.append({'weight': round(w, 2), 'op_cost': op_cost, 'disparity': spatial_disparity})
    return results

print("Pareto Optimal Portfolio Sample:")
for row in evaluate_facility_portfolio()[:3]:
    print(row)
```

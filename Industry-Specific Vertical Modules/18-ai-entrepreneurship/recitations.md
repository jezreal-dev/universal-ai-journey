# Recitation Notes – AI and Entrepreneurship

---

## 🔬 Applied AI Venture Engineering & Financial Modeling

### 1. Automated GTM Lead Scoring Classifier

This Python script implements a Random Forest classifier to predict sales lead conversion probability, enabling AI-driven lead routing for sales teams.

```python
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

# Generate Synthetic Lead Data
np.random.seed(42)
n_leads = 1000

df_leads = pd.DataFrame({
    'website_visits': np.random.poisson(lam=12, size=n_leads),
    'docs_viewed': np.random.poisson(lam=4, size=n_leads),
    'api_keys_created': np.random.binomial(n=3, p=0.3, size=n_leads),
    'team_members_invited': np.random.poisson(lam=2, size=n_leads),
    'company_size': np.random.choice([10, 50, 200, 1000], size=n_leads)
})

# Conversion Target Signal
score = (df_leads['docs_viewed'] * 0.3 + 
         df_leads['api_keys_created'] * 0.8 + 
         df_leads['team_members_invited'] * 0.5)
df_leads['converted'] = (score > 2.5).astype(int)

X = df_leads.drop(columns=['converted'])
y = df_leads['converted']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=50, random_state=42)
clf.fit(X_train, y_train)

y_probs = clf.predict_proba(X_test)[:, 1]
print(f"Lead Scoring Model AUROC: {roc_auc_score(y_test, y_probs):.4f}")
```

---

### 2. Unit Economics Monte Carlo Simulator (LTV / CAC Ratio)

```python
import numpy as np

def simulate_unit_economics(n_simulations=5000):
    """
    Runs Monte Carlo simulation of LTV / CAC and Payback Period under uncertainty.
    """
    np.random.seed(42)
    
    # Stochastic Parameters
    arpu = np.random.normal(loc=500, scale=50, size=n_simulations)          # Monthly ARPU ($500 +/- 50)
    gross_margin = np.random.uniform(low=0.75, high=0.85, size=n_simulations)# 75-85% Margin
    monthly_churn = np.random.uniform(low=0.015, high=0.035, size=n_simulations)# 1.5-3.5% Churn
    cac = np.random.normal(loc=4000, scale=400, size=n_simulations)         # CAC ($4000 +/- 400)
    
    # Calculate Metrics
    ltv = (arpu * gross_margin) / monthly_churn
    ltv_cac_ratio = ltv / cac
    payback_months = cac / (arpu * gross_margin)
    
    print(f"Mean LTV: ${np.mean(ltv):,.2f}")
    print(f"Mean CAC: ${np.mean(cac):,.2f}")
    print(f"Mean LTV/CAC Ratio: {np.mean(ltv_cac_ratio):.2f}x")
    print(f"Probability of LTV/CAC >= 3.0x: {np.mean(ltv_cac_ratio >= 3.0) * 100:.1f}%")
    print(f"Mean Payback Period: {np.mean(payback_months):.1f} months")

simulate_unit_economics()
```

---

### 3. Summary of Financial Health Thresholds

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                             SaaS / AI Venture Financial Benchmarks                       │
├──────────────────────────────┬────────────────────────────┬──────────────────────────────┤
│ Metric                       │ Healthy Benchmark          │ Warning Threshold            │
├──────────────────────────────┼────────────────────────────┼──────────────────────────────┤
│ LTV / CAC Ratio              │ >= 3.0x                    │ < 2.0x                       │
├──────────────────────────────┼────────────────────────────┼──────────────────────────────┤
│ CAC Payback Period           │ <= 12 Months               │ > 18 Months                  │
├──────────────────────────────┼────────────────────────────┼──────────────────────────────┤
│ Gross Margin (Software/AI)   │ >= 75%                     │ < 60% (High Compute Costs)   │
├──────────────────────────────┼────────────────────────────┼──────────────────────────────┤
│ Net Revenue Retention (NRR)  │ >= 120%                    │ < 100%                       │
└──────────────────────────────┴────────────────────────────┴──────────────────────────────┘
```

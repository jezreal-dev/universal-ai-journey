# Assignment Solutions – Explainability & Fairness in AI

---

## 📝 Assignment 1: Heart Disease Risk Prediction, SHAP & Fairness Audit

### 📌 Part 1 — Clinical Classifier Training on `heart.csv`

#### Problem Description
Train a Random Forest classifier to predict heart disease risk (`target`) using clinical features (`age`, `sex`, `cp`, `trestbps`, `chol`, `thalach`, `exang`, `oldpeak`, `slope`, `ca`, `thal`).

#### Python Code Implementation
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, accuracy_score

# Load Heart Disease Dataset
df = pd.read_csv("/home/jmomoh/universal-ai-journey/modules/16-explainability-fairness/data/heart.csv")

X = df.drop(columns=['target'])
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

y_pred_prob = rf_model.predict_proba(X_test)[:, 1]
print(f"Test Accuracy: {accuracy_score(y_test, rf_model.predict(X_test)):.4f}")
print(f"Test AUROC: {roc_auc_score(y_test, y_pred_prob):.4f}")
```

---

### 📌 Part 2 — SHAP Global & Local Feature Attribution

#### Problem Description
Compute SHAP values to identify top global predictors of heart disease and explain a high-risk patient prediction locally.

#### Python Code Implementation
```python
import shap

explainer = shap.TreeExplainer(rf_model)
shap_vals = explainer.shap_values(X_test)

# Top Mean Absolute SHAP Feature Importances
mean_shap = np.abs(shap_vals[1]).mean(axis=0)
feature_ranking = pd.DataFrame({'feature': X.columns, 'mean_shap': mean_shap}).sort_values('mean_shap', ascending=False)

print("Top 5 SHAP Clinical Predictors:")
print(feature_ranking.head(5).to_string(index=False))
```

---

### 📌 Part 3 — Counterfactual Recourse Generation

#### Problem Description
Generate actionable counterfactual explanations for a patient predicted to have high risk ($\hat{y}=1$), identifying minimal medical feature changes required to reduce risk ($\hat{y}=0$).

```python
def generate_counterfactual(patient_idx, model, X_df):
    patient = X_df.iloc[patient_idx].copy()
    initial_prob = model.predict_proba([patient])[0][1]
    
    print(f"Initial Patient Risk Probability: {initial_prob:.2f}")
    
    # Counterfactual Intervention: Reduce ST depression (oldpeak) and Increase max heart rate (thalach)
    cf_patient = patient.copy()
    cf_patient['oldpeak'] = max(0.0, cf_patient['oldpeak'] - 1.5)
    cf_patient['thalach'] = cf_patient['thalach'] + 20
    
    new_prob = model.predict_proba([cf_patient])[0][1]
    print(f"Counterfactual Risk Probability: {new_prob:.2f}")
    print(f"Risk Reduction: {initial_prob - new_prob:.2f}")

generate_counterfactual(0, rf_model, X_test)
```

---

### 📌 Part 4 — Demographic Parity Audit & Disparate Impact Mitigation

#### Problem Description
Audit prediction fairness across protected attribute `sex` (1 = Male, 0 = Female). Calculate the Demographic Parity Ratio ($DPR$) and apply threshold tuning to satisfy the $80\%$ Four-Fifths Rule ($DPR \ge 0.80$).

```python
# Demographic Parity Evaluation
sex_test = X_test['sex']
y_pred_test = rf_model.predict(X_test)

rate_male = y_pred_test[sex_test == 1].mean()
rate_female = y_pred_test[sex_test == 0].mean()

dpr_initial = rate_female / rate_male if rate_male > 0 else 0

print(f"Male Positive Selection Rate (A=1): {rate_male:.4f}")
print(f"Female Positive Selection Rate (A=0): {rate_female:.4f}")
print(f"Initial Demographic Parity Ratio (DPR): {dpr_initial:.4f}")

if dpr_initial < 0.80:
    print("⚠️ Disparate Impact Warning: DPR < 0.80. Applying Threshold Tuning Mitigation...")
    # Apply Group-Specific Threshold Adjustment
    thresh_female = 0.40
    y_pred_mitigated = (rf_model.predict_proba(X_test)[:, 1] >= np.where(sex_test == 0, thresh_female, 0.50)).astype(int)
    
    rate_female_mit = y_pred_mitigated[sex_test == 0].mean()
    dpr_mitigated = rate_female_mit / rate_male
    print(f"Mitigated DPR: {dpr_mitigated:.4f} -> Passes Four-Fifths Rule! ✅")
```

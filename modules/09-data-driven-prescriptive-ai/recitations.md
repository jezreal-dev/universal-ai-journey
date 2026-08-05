# Module 9 Recitations: Data-Driven Prescriptive AI

---

## 💻 Recitation 1: From Predictions to Prescriptions Through Code

**Instructor**: Prof. Yu Ma (Assistant Professor, University of Wisconsin)  
**Lectures Covered**: Lecture 1 (From Predictions to Prescriptions)

---

### 🎯 Recitation Overview & Objectives
This recitation provides a hands-on implementation of the **Regress-and-Compare** (Predict-then-Optimize) prescriptive pipeline using Python (`scikit-learn` and `pandas`). Using empirical IBM retail sales data under two distinct marketing promotion schemes, we demonstrate how predictive machine learning models estimate counterfactual outcomes to guide optimal promotion assignment for each store location.

#### Key Learning Objectives:
1. **Data Preprocessing & Encoding**: Categorical feature encoding (`LabelEncoder`) and splitting observational datasets by treatment assignment.
2. **Predictive Model Fitting**: Training separate linear regression models for each promotion scheme ($T=1$ vs. $T=2$).
3. **Counterfactual Estimation**: Predicting sales under both candidate promotions for unseen test stores.
4. **Prescriptive Policy Execution**: Selecting the promotion that maximizes expected sales revenue ($\hat{t}_i = \arg\max_{t} \hat{y}_{i, t}$).
5. **Prescriptive Benefit Evaluation**: Quantifying model-driven sales lift against the theoretical **Oracle Prescription** and real-world historical baseline decisions.

---

### 📊 Dataset Overview
* **Source**: IBM Watson Analytics Campaign Effectiveness Dataset (Modified).
* **Train Set**: `promotion_train.csv` (384 observations: 252 for Promotion 1, 132 for Promotion 2).
* **Test Set**: `promotion_test.csv` (41 store-week observations with ground-truth counterfactuals `Sales_Prom1` and `Sales_Prom2`).
* **Features**:
  * `MarketSize`: Categorical (`Small`, `Medium`, `Large`).
  * `AgeOfStore`: Continuous (years).
  * `Week`: Continuous (promotion week 1-4).
* **Target / Outcome**: `SalesInThousands` (Weekly sales in $1,000s).

---

### 🐍 Code Implementation & Step-by-Step Walkthrough

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# ---------------------------------------------------------
# Step 1: Load Observational Datasets
# ---------------------------------------------------------
promotion_train = pd.read_csv("promotion_train.csv")
promotion_test = pd.read_csv("promotion_test.csv")

# ---------------------------------------------------------
# Step 2: Categorical Feature Encoding
# ---------------------------------------------------------
label_encoder = LabelEncoder()
promotion_train["MarketSize"] = label_encoder.fit_transform(
    promotion_train["MarketSize"]
)
promotion_test["MarketSize"] = label_encoder.transform(
    promotion_test["MarketSize"]
)

# ---------------------------------------------------------
# Step 3: Split Observational Data by Treatment (Promotion 1 vs 2)
# ---------------------------------------------------------
promotion1 = promotion_train[promotion_train["Promotion"] == 1]
promotion2 = promotion_train[promotion_train["Promotion"] == 2]

# ---------------------------------------------------------
# Step 4: Fit Separate Regression Models for Each Treatment
# ---------------------------------------------------------
features = ["MarketSize", "AgeOfStore", "Week"]
lm_prom1 = LinearRegression().fit(promotion1[features], promotion1["SalesInThousands"])
lm_prom2 = LinearRegression().fit(promotion2[features], promotion2["SalesInThousands"])

# Model Summaries
print("Promotion 1 Model Coefficients:", lm_prom1.coef_)
print("Promotion 1 Model Intercept:", lm_prom1.intercept_)
print("Promotion 2 Model Coefficients:", lm_prom2.coef_)
print("Promotion 2 Model Intercept:", lm_prom2.intercept_)

# ---------------------------------------------------------
# Step 5: Compute Oracle Benchmark (Known Counterfactuals)
# ---------------------------------------------------------
promotion_test["oracle_sales"] = promotion_test[
    ["Sales_Prom1", "Sales_Prom2"]
].max(axis=1)
promotion_test["oracle_benefit"] = (
    promotion_test["oracle_sales"] - promotion_test["SalesInThousands"]
)
print("Average Oracle Benefit ($1k):", promotion_test["oracle_benefit"].mean())

# ---------------------------------------------------------
# Step 6: Predict Counterfactuals & Execute Prescriptive Policy
# ---------------------------------------------------------
promotion_test["pred_prom1"] = lm_prom1.predict(promotion_test[features])
promotion_test["pred_prom2"] = lm_prom2.predict(promotion_test[features])

# Prescribe promotion with higher predicted sales
promotion_test["prescribe"] = np.where(
    promotion_test["pred_prom1"] > promotion_test["pred_prom2"], 1, 2
)

# Compute Model Prescriptive Benefit
promotion_test["benefit"] = np.where(
    promotion_test["prescribe"] == 1,
    promotion_test["Sales_Prom1"] - promotion_test["SalesInThousands"],
    promotion_test["Sales_Prom2"] - promotion_test["SalesInThousands"],
)

print(
    "Average Model Prescriptive Benefit ($1k):",
    promotion_test["benefit"].mean(),
)
```

---

### 📈 Empirical Results & Model Coefficients

#### Fitted Linear Model Coefficients:

| Model | MarketSize Coef | AgeOfStore Coef | Week Coef | Intercept ($\beta_0$) | Regression Equation |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Promotion 1 Model** | $-14.4217$ | $+0.1323$ | $+0.0840$ | $66.4911$ | $\hat{y}_1 = 66.49 - 14.42(\text{MarketSize}) + 0.13(\text{Age}) + 0.08(\text{Week})$ |
| **Promotion 2 Model** | $-12.2543$ | $+0.2148$ | $+0.5522$ | $53.6960$ | $\hat{y}_2 = 53.70 - 12.25(\text{MarketSize}) + 0.21(\text{Age}) + 0.55(\text{Week})$ |

#### Prescription Benefit Summary Table:

| Metric | Formula / Source | Average Sales Lift per Store-Week ($1,000s) | Annualized Store Impact ($) |
| :--- | :--- | :---: | :---: |
| **Historical Baseline** | Actual assigned sales $Y_{\text{observed}}$ | `$0.0000$` | `$0.00` |
| **Model Prescription** | $\hat{y}_{\hat{t}} - Y_{\text{observed}}$ | **`+$0.1734$`** | **`+$173.41`** / week |
| **Oracle Benchmark** | $\max(Y_1, Y_2) - Y_{\text{observed}}$ | **`+$2.4824$`** | **`+$2,482.44`** / week |

---

### 💡 Key Takeaways & Pedagogical Insights
1. **Model Prescriptions Over Random/Historical Assignment**:
   * Prescribing promotions using even simple linear regression models achieves a positive sales lift of **+$173.41 per store-week** over historical real-life assignments.

2. **The Oracle Gap & Need for Advanced Methods**:
   * The **Oracle Benefit** of **+$2,482.44** represents the maximum theoretical sales lift achievable with perfect foresight.
   * The gap between model-based benefit ($+\$173.41$) and oracle benefit ($+\$2,482.44$) demonstrates the limitations of simple linear regression models in capturing non-linear interactions and treatment assignment bias.

3. **Observational Treatment Assignment Bias**:
   * Historical data reflects strong assignment bias (Promotion 1 assigned 252 times vs Promotion 2 assigned 132 times).
   * *Qualitative Bias Explanation*: Promotion 1 may have been favored historically because it was simpler to deploy in stores (e.g. basic paper coupons), whereas Promotion 2 required complex store labor or operational setup.
   * Regress-and-Compare models trained on biased observational data carry over these implicit operational biases unless adjusted using Doubly Resilient estimation or propensity scoring.

4. **Model Misspecification vs. Prescriptive Performance**:
   * Fitting simple linear regression models assumes linear feature effects, which may fail to capture complex store-level interactions.
   * Swapping linear regression for tree-based models (CART, Random Forest) or Prescriptive Neural Networks (PNNs) improves counterfactual estimation accuracy and bridges the gap to the Oracle benchmark.

---

### 📝 Official Recitation 1 Summary

In this recitation, we learned how predictive models can be used not only to forecast outcomes but also to guide prescriptions—in this case, choosing the best promotion to maximize sales using IBM retail data. Learners practiced building linear regression models for two promotion types, comparing predicted sales, and evaluating the benefit of prescriptive modeling against both actual outcomes and an oracle benchmark.

#### Key Takeaways:
* **Data Preparation**: Prepared observational data by encoding categorical features (`MarketSize`) and splitting data by promotion type ($T=1$ vs. $T=2$).
* **Predictive Modeling**: Fit separate linear regression models to predict sales under promotion 1 and promotion 2.
* **Oracle Benchmark**: Defined the oracle prescription as the promotion that yields higher sales if both counterfactual outcomes were known perfectly.
* **Prescriptive Approximation**: Approximated the oracle by comparing predicted sales across candidate promotions and prescribing the option with higher expected revenue.
* **Benefit Evaluation**: Evaluated prescriptive benefit by measuring sales improvement relative to historical real-world store assignments.
* **Limitations**: Identified key limitations—prediction accuracy depends on model choice (linear vs non-linear), and inherent treatment assignment biases in historical data can affect future prescriptions.




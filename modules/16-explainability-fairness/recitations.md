# Recitation Notes – Explainability & Fairness in AI

---

## 🔬 Recitation 1: Explainable AI Across Modalities in Practice

### 1. Tabular Feature Attribution with SHAP (`TreeExplainer`)

SHAP computes exact Shapley attributions for tree ensembles (XGBoost / Random Forest), outputting global feature importances and local summary plots.

```python
import numpy as np
import pandas as pd
import shap
from sklearn.ensemble import RandomForestClassifier

# Load Heart Disease Dataset
df = pd.read_csv("/home/jmomoh/universal-ai-journey/modules/16-explainability-fairness/data/heart.csv")

X = df.drop(columns=['target'])
y = df['target']

# Train Model
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X, y)

# Compute SHAP Values via TreeExplainer
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

print("SHAP Matrix Shape (Class 1):", shap_values[1].shape) # (N_samples, N_features)
```

---

### 2. Local Text Explanation with LIME

LIME perturbs input text tokens, fitting a local sparse linear model to identify words driving text classification decisions.

```python
from lime.lime_text import LimeTextExplainer

class_names = ['Negative', 'Positive']
explainer_text = LimeTextExplainer(class_names=class_names)

# Sample Clinical Note
clinical_text = "Patient displays severe chest pain, elevated ST segment, and shortness of breath."

# Dummy Text Predictor Function
def dummy_predict_proba(texts):
    results = []
    for t in texts:
        score = 0.8 if "chest pain" in t.lower() or "elevated" in t.lower() else 0.2
        results.append([1.0 - score, score])
    return np.array(results)

exp = explainer_text.explain_instance(clinical_text, dummy_predict_proba, num_features=4)
print("LIME Local Text Feature Weights:")
for word, weight in exp.as_list():
    print(f"  Word: '{word:<15}' | Weight Contribution: {weight:+.4f}")
```

---

### 3. Visual Explanation with Grad-CAM

Gradient-weighted Class Activation Mapping (Grad-CAM) calculates gradients of target output logits with respect to final CNN feature maps ($\mathbf{A}^k$), forming spatial visual attention heatmaps:

$$L_{\text{Grad-CAM}}^c = \text{ReLU}\left( \sum_k \alpha_k^c \mathbf{A}^k \right) \quad \text{where } \alpha_k^c = \frac{1}{Z} \sum_{i} \sum_{j} \frac{\partial y^c}{\partial A_{i,j}^k}$$

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                               Multi-Modal XAI Tool Selection                             │
├──────────────────────┬────────────────────────────┬──────────────────────────────────────┤
│ Modality             │ Recommended XAI Method     │ Primary Advantage                    │
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ Tabular              │ SHAP (TreeExplainer)       │ Game-theoretic global + local consistency│
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ Text                 │ LIME / Integrated Gradients│ Word-level token contribution scores │
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ Image                │ Grad-CAM                   │ Spatial feature map heatmaps         │
└──────────────────────┴────────────────────────────┴──────────────────────────────────────┘
```

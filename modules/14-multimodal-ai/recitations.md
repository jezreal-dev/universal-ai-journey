# Recitation Notes – Multimodal AI

---

## 🔬 Recitation 1: Multimodal Learning & HAIM Framework Implementation

### 1. HAIM Multimodal Data Loading & Feature Processing

The **HAIM (Holistic AI for Medicine)** pipeline ingests multi-modal patient data streams, converting diverse unstructured clinical inputs into standardized numerical embedding matrices.

```python
import numpy as np
import pandas as pd
import torch
import torch.nn as nn

# Simulate Multimodal Patient Data Stream Batch (Batch Size N=5)
np.random.seed(42)

# Modality 1: EHR Tabular (d_tab = 10)
x_tab = np.random.randn(5, 10)

# Modality 2: Chest X-Ray Image Features (d_img = 64)
x_img = np.random.randn(5, 64)

# Modality 3: ECG Time-Series Features (d_ecg = 32)
x_ecg = np.random.randn(5, 32)

# Modality 4: BioBERT Clinical Notes Text Embeddings (d_txt = 128)
x_txt = np.random.randn(5, 128)

print("Modality Feature Shapes:")
print(f"  Tabular: {x_tab.shape}")
print(f"  CXR Img: {x_img.shape}")
print(f"  ECG Sig: {x_ecg.shape}")
print(f"  Notes Tx: {x_txt.shape}")
```

---

### 2. Early Fusion Pipeline (Concatenation)

Early fusion concatenates feature vectors from all four patient modalities into a single wide feature vector $\mathbf{x}_{\text{early}} \in \mathbb{R}^{5 \times 234}$ before passing into a unified classifier.

```python
# Early Fusion Feature Concatenation
x_early = np.concatenate([x_tab, x_img, x_ecg, x_txt], axis=-1)
print("\nEarly Fusion Concatenated Matrix Shape:", x_early.shape) # (5, 234)

# Define PyTorch Early Fusion Classifier
class EarlyFusionClassifier(nn.Module):
    def __init__(self, input_dim=234, hidden_dim=64, num_classes=1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_dim, num_classes),
            nn.Sigmoid()
        )
        
    def forward(self, x):
        return self.net(x)

model_early = EarlyFusionClassifier(input_dim=234)
tensor_early = torch.tensor(x_early, dtype=torch.float32)
predictions_early = model_early(tensor_early)

print("Early Fusion Predictions:\n", predictions_early.detach().numpy().round(3))
```

---

### 3. Late Fusion Pipeline (Decision-Level Ensemble)

Late fusion trains independent unimodal classifiers for each data modality and averages their predicted probabilities at inference time.

```python
# Unimodal Model Predictions for Patient Cohort
pred_tab = np.array([0.70, 0.20, 0.80, 0.40, 0.90])
pred_img = np.array([0.80, 0.30, 0.70, 0.50, 0.95])
pred_ecg = np.array([0.65, 0.10, 0.85, 0.30, 0.88])
pred_txt = np.array([0.75, 0.25, 0.90, 0.45, 0.92])

# Late Fusion: Ensemble Probability Averaging
weights = [0.25, 0.25, 0.25, 0.25]
late_fusion_preds = (
    weights[0] * pred_tab + 
    weights[1] * pred_img + 
    weights[2] * pred_ecg + 
    weights[3] * pred_txt
)

print("\nLate Fusion Ensemble Predictions:\n", late_fusion_preds.round(3))
```

---

### 4. Early vs. Late Fusion Comparison Matrix

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                                Fusion Architecture Comparison                            │
├──────────────────────┬────────────────────────────┬──────────────────────────────────────┤
│ Property             │ Early Fusion (Concatenation)│ Late Fusion (Decision Ensemble)      │
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ Cross-Modal Interaction│ High (interact at layer 1) │ None (isolated unimodal models)      │
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ Missing Data Handling│ Vulnerable if 1 modal missing│ Resilient (reweight remaining models)│
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ Model Complexity     │ Single Unified Model       │ M Independent Unimodal Models        │
└──────────────────────┴────────────────────────────┴──────────────────────────────────────┘
```

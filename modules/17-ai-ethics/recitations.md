# Recitation Notes – AI and Ethics

---

## 🔬 Applied AI Ethics & Fairness Auditing Code Implementations

### 1. Demographic Parity & Disparate Impact Audit

```python
import numpy as np
import pandas as pd

def audit_demographic_parity(y_pred, group_attr):
    """
    Computes Positive Selection Rate per demographic group and Disparate Impact Ratio (DPR).
    """
    groups = np.unique(group_attr)
    rates = {}
    
    for g in groups:
        mask = (group_attr == g)
        rate = np.mean(y_pred[mask])
        rates[g] = rate
        print(f"Group {g} Positive Selection Rate: {rate:.4f}")
        
    majority_rate = max(rates.values())
    protected_rate = min(rates.values())
    
    dpr = protected_rate / majority_rate if majority_rate > 0 else 0
    print(f"Demographic Parity Ratio (DPR): {dpr:.4f}")
    print(f"Passes Four-Fifths (80%) Rule? {dpr >= 0.80}")
    return dpr, rates

# Sample Verification Run
y_pred_dummy = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 1])
group_dummy = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) # 1 = Unprotected, 0 = Protected

audit_demographic_parity(y_pred_dummy, group_dummy)
```

---

### 2. Equalized Odds Audit (TPR & FPR Disparities)

```python
from sklearn.metrics import confusion_matrix

def audit_equalized_odds(y_true, y_pred, group_attr):
    """
    Evaluates True Positive Rate (TPR) and False Positive Rate (FPR) parity across groups.
    """
    groups = np.unique(group_attr)
    metrics = {}
    
    for g in groups:
        mask = (group_attr == g)
        tn, fp, fn, tp = confusion_matrix(y_true[mask], y_pred[mask]).ravel()
        tpr = tp / (tp + fn) if (tp + fn) > 0 else 0
        fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
        metrics[g] = {'TPR': tpr, 'FPR': fpr}
        print(f"Group {g} -> TPR: {tpr:.4f} | FPR: {fpr:.4f}")
        
    tpr_diff = abs(metrics[groups[0]]['TPR'] - metrics[groups[1]]['TPR'])
    fpr_diff = abs(metrics[groups[0]]['FPR'] - metrics[groups[1]]['FPR'])
    
    print(f"TPR Difference: {tpr_diff:.4f}")
    print(f"FPR Difference: {fpr_diff:.4f}")
    return metrics
```

---

### 3. Verification of Kleinberg Impossibility Theorem Math

```python
def check_impossibility_theorem(base_rate_A, base_rate_B, target_fpr, target_fnr):
    """
    Verifies that equal FPR & FNR across groups with different base rates GUARANTEES unequal calibration (PPV).
    """
    tpr = 1.0 - target_fnr
    
    ppv_A = (tpr * base_rate_A) / (tpr * base_rate_A + target_fpr * (1.0 - base_rate_A))
    ppv_B = (tpr * base_rate_B) / (tpr * base_rate_B + target_fpr * (1.0 - base_rate_B))
    
    print(f"Group A Base Rate: {base_rate_A:.2f} -> PPV Calibration: {ppv_A:.4f}")
    print(f"Group B Base Rate: {base_rate_B:.2f} -> PPV Calibration: {ppv_B:.4f}")
    print(f"Calibration Difference (PPV_B - PPV_A): {ppv_B - ppv_A:+.4f}")
    return ppv_A, ppv_B

check_impossibility_theorem(0.30, 0.60, 0.20, 0.10)
```

---

### 4. Direct Preference Optimization (DPO) Loss Implementation

```python
import torch
import torch.nn.functional as F

def dpo_loss(policy_chosen_logps, policy_rejected_logps, ref_chosen_logps, ref_rejected_logps, beta=0.1):
    """
    Computes Direct Preference Optimization (DPO) loss for LLM alignment.
    """
    pi_logratios = policy_chosen_logps - policy_rejected_logps
    ref_logratios = ref_chosen_logps - ref_rejected_logps
    
    logits = pi_logratios - ref_logratios
    losses = -F.logsigmoid(beta * logits)
    return losses.mean()
```

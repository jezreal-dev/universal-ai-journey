# Module 9 Assignments: Data-Driven Prescriptive AI

---

## 📝 Assignment 1: Predictive-Prescriptive Optimization & Policy Trees

---

### 🏥 Part 1: Hospital ICU Bed Allocation (Predictive vs. $P^2$ Approach)

#### 📌 Problem Setup & Context
A regional healthcare network consists of three hospitals (Hospitals 1, 2, and 3) sharing a total pool of $K = 40$ ICU beds. The decision objective is to allocate beds $\vec{z} = (z_1, z_2, z_3)$ to maximize the total number of admitted patients across the network for a future day.

---

#### ❓ Question 1: Admissions Function
* **Question**: Because a hospital cannot admit more patients than its allocated bed capacity ($z$) or arriving patient demand ($y$), how should the number of ICU admissions be expressed?
* **Formulation**:

$$\text{Admissions}(z, y) = \min(z, y)$$

---

#### ❓ Question 2: Deterministic Mathematical Formulation
* **Question**: What is the correct mathematical optimization formulation without uncertainty for a 3-hospital network with 40 total beds?
* **Formulation**:

$$\max_{z_1, z_2, z_3} \sum_{j=1}^3 \min(z_j, \hat{y}_j)$$

$$\text{s.t. } z_1 + z_2 + z_3 \le 40$$

$$z_1, z_2, z_3 \ge 0$$

---

#### 🌳 CART Model Decision Tree Structure & Predictions
A CART model predicts hospital ICU patient demand using features: `Nearby event?` (1=Yes, 0=No), `Temperature ≥ 40?`, `Weekend?`, and `Hist. avg ≥ 10 admissions?`.

```
                        [Nearby Event?]
                           /       \
                    (Yes) /         \ (No)
                         /           \
            [Temp >= 40?]            [Weekend?]
               /    \                  /     \
         (Yes)/      \(No)       (Yes)/       \(No)
             /        \              /         \
         Leaf L1    Leaf L2      Leaf L5   [Hist Avg >= 10?]
        (21,27,24)  (9,11)      (13,13,28)    /         \
         Mean=24    Mean=10      Mean=18 (Yes)/           \(No)
                                             /             \
                                         Leaf L3         Leaf L4
                                         (5,6,7)        (9,13,17)
                                         Mean=6          Mean=13
```

---

#### ❓ Question 3: Leaf L4 Predicted Demand
* **Leaf L4 Training Values**: $\{9, 13, 17\}$
* **Calculation**:

$$\hat{y}_{L4} = \frac{9 + 13 + 17}{3} = \frac{39}{3} = \mathbf{13}$$

---

#### ❓ Question 4: Hospital 3 Predicted Demand
* **Hospital 3 Features**: Nearby=0, Weekend=0, Temp=40, Hist.avg=15
* **Tree Routing**: Nearby=0 $\to$ Weekend=0 $\to$ Hist.avg=15 $\ge 10 \implies$ **Leaf L3**
* **Calculation**:

$$\hat{y}_3 = \frac{5 + 6 + 7}{3} = \mathbf{6}$$

---

#### ❓ Question 5: Updated 5-Hospital Formulation Without Uncertainty
* **Hospital Predictions**: $\hat{y}_1 = 24, \hat{y}_2 = 10, \hat{y}_3 = 6, \hat{y}_4 = 18, \hat{y}_5 = 13$.
* **Formulation**:

$$\max_{z_1, z_2, z_3, z_4, z_5} \left[ \min(z_1, 24) + \min(z_2, 10) + \min(z_3, 6) + \min(z_4, 18) + \min(z_5, 13) \right]$$

$$\text{s.t. } \sum_{j=1}^5 z_j \le 40 \quad (\text{or } K), \quad z_j \ge 0, \forall j \in \{1, \dots, 5\}$$

---

#### ❓ Question 6: Expected Demand under $P^2$ Predictive-Prescriptive Approach
* **Concept**: Under $P^2$, demand for Hospital 1 is not reduced to a point prediction $\hat{y}_1 = 24$. Instead, Hospital 1 inherits the empirical probability distribution $P(y_1)$ of training observations in **Leaf L1** ($\{21, 27, 24\}$).
* **Expected Admissions Formula for Hospital 1**:

$$\mathbb{E}_{y_1 \sim \text{Leaf L1}} [\min(z_1, y_1)] = \frac{1}{3} \left( \min(z_1, 21) + \min(z_1, 27) + \min(z_1, 24) \right)$$

---

#### ❓ Question 7: $P^2$ Formulation Modification Rules
* **Question**: How do we modify the formulation from Question 5 to use the $P^2$ predictive-prescriptive approach?
* **Answer**: **Modify only the objective.**
* **Explanation**: The deterministic point prediction terms $\min(z_j, \hat{y}_j)$ in the objective function are replaced with their expected values $\mathbb{E}_{y_j \sim \text{Leaf}(j)} [\min(z_j, y_j)]$ over the empirical leaf distributions. Physical bed capacity constraints ($\sum z_j \le 40$) remain unchanged.

---

---

### 💊 Part 2: Cholesterol Treatment via Optimal Policy Trees (OPTs)

#### 📌 Problem Setup & Context
An Optimal Policy Tree is trained on an 800-patient cholesterol dataset to prescribe optimal treatments:
* **Treatment A**: No Treatment
* **Treatment B**: PCSK9 Inhibitors
* **Treatment C**: Statins

```
                    [Pre_Chol >= 220?]
                       /          \
                (Yes) /            \ (No)
                     /              \
        [Family History?]       [BP_Systolic >= 140?]
           /        \              /             \
     (Yes)/          \(No)   (Yes)/               \(No)
         /            \          /                 \
     Leaf L1        Leaf L2   Leaf L3           [BMI >= 30?]
  Prescribe C    Prescribe B Prescribe C          /         \
  (Statins)       (PCSK9)    (Statins)      (Yes)/           \(No)
                                                /             \
                                            Leaf L4         Leaf L5
                                          Prescribe B     Prescribe A
                                           (PCSK9)       (No Treatment)
```

---

#### ❓ Question 1: Patient Treatment Prescription
* **Patient Profile**: Age=45, Pre_Chol=200, BP_Systolic=135, BMI=32.
* **Routing Path**:
  1. `Pre_Chol ≥ 220?`: $200 < 220 \implies$ **No**
  2. `BP_Systolic ≥ 140?`: $135 < 140 \implies$ **No**
  3. `BMI ≥ 30?`: $32 \ge 30 \implies$ **Yes** $\to$ **Leaf L4**
* **Prescribed Treatment**: **PCSK9 Inhibitors (Treatment B)**.

---

#### 📊 Leaf Population Breakdown & Empirical Analysis

| Leaf | Total Patients ($N_k$) | Prescribed Treatment | Treatment A (No Tx) Avg Post-Chol | Treatment B (PCSK9) Avg Post-Chol | Treatment C (Statins) Avg Post-Chol | Prescribed Observed Post-Chol |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **L1** | 180 | **C (Statins)** | 225 ($n=15$) | 210 ($n=69$) | **205** ($n=96$) | **205** |
| **L2** | 120 | **B (PCSK9)** | 225 ($n=11$) | **207** ($n=70$) | 209 ($n=39$) | **207** |
| **L3** | 212 | **C (Statins)** | 222 ($n=29$) | 199 ($n=45$) | **196** ($n=138$) | **196** |
| **L4** | 160 | **B (PCSK9)** | 237 ($n=22$) | **217** ($n=104$) | 218 ($n=34$) | **217** |
| **L5** | 128 | **A (No Tx)** | **208** ($n=24$) | 219 ($n=56$) | 212 ($n=48$) | **208** |
| **Total** | **800** | — | — | — | — | — |

---

#### ❓ Question 2: Observed Post-Medication Cholesterol for Leaf L1
* **Answer**: **205**
* **Explanation**: Leaf L1 prescribes Treatment C (Statins). The average post-medication cholesterol for Leaf L1 patients given Treatment C is **205**.

---

#### ❓ Question 3: Overall Observed OPT Post-Medication Cholesterol
* **Formula**: Weighted average across all 5 leaves:

$$\text{OPT Avg Post-Chol} = \frac{\sum_{k=1}^5 N_k \cdot \text{Chol}_k}{\sum_{k=1}^5 N_k}$$

$$\text{Weighted Sum} = (180 \times 205) + (120 \times 207) + (212 \times 196) + (160 \times 217) + (128 \times 208)$$
$$\text{Weighted Sum} = 36,900 + 24,840 + 41,552 + 34,720 + 26,624 = 164,636$$

$$\text{OPT Avg Post-Chol} = \frac{164,636}{800} = \mathbf{205.795} \approx \mathbf{205.80}$$

---

#### ❓ Question 4: Performance Improvement Percentage Over Real-Life Prescriptions
* **Real-Life Baseline Average Cholesterol**: $209.66$
* **OPT Prescribed Average Cholesterol**: $205.795$
* **Absolute Reduction**: $209.66 - 205.795 = 3.865$
* **Percentage Improvement**:

$$\text{Improvement \%} = \frac{\text{Real-Life Avg} - \text{OPT Avg}}{\text{Real-Life Avg}} \times 100\% = \frac{3.865}{209.66} \times 100\% = \mathbf{1.84\%}$$

---

---

---

---

## 📝 Assignment 2: $OP^2T$ Model Routing & Prescriptive Neural Networks (PNNs)

---

### 🌀 Part 1: Optimal Predictive Policy Trees ($OP^2T$) — Hurricane & Recidivism

#### 📌 Problem Setup & Context
$OP^2T$ models serve as interpretable routing functions across candidate machine learning models:
* $h_{\text{lr}}$: Tabular Logistic Regression
* $h_{\text{boost}}$: Tabular Boosted Trees (XGBoost)
* $h_{\text{cnn}}$: Convolutional Neural Network (Satellite Imagery)
* $h_{\text{ns}}$: Physics-Based Fluid Dynamics Simulator

---

#### ❓ Question 1: Hurricane Dimitris Model Routing (Non-Rejection Tree)
* **Input Profile**: Wind Speed = 50 knots, Wind Pressure = 950 hPa, Distance to Land = 15 km.
* **Routing Path**:
  1. `Wind Speed > 20 kts?`: $50 > 20 \implies$ **Right Branch** (High Speed)
  2. `Wind Pressure > 900 hPa?`: $950 > 900 \implies$ **50/50 Ensemble Leaf**
* **Prescribed Action**: **a combination of two models** (50/50 ensemble of $h_{\text{cnn}}$ and $h_{\text{ns}}$).

---

#### ❓ Question 2: Hurricane Matthew Model Routing (Non-Rejection Tree)
* **Input Profile**: Wind Speed = 25 knots, Wind Pressure = 800 hPa, Distance to Land = 50 km.
* **Routing Path**:
  1. `Wind Speed > 20 kts?`: $25 > 20 \implies$ **Right Branch**
  2. `Wind Pressure > 900 hPa?`: $800 \le 900 \implies$ **Physics Simulator Leaf**
* **Prescribed Action**: **physics based simulator** ($h_{\text{ns}}$).

---

#### ❓ Question 3: Hurricane Matthew Model Routing (With Rejection Tree)
* **Input Profile**: Wind Speed = 25 knots, Wind Pressure = 800 hPa, Distance to Land = 50 km.
* **Routing Path**:
  1. `Wind Speed > 20 kts?`: $25 > 20 \implies$ **Right Branch**
  2. `Wind Pressure > 900 hPa?`: $800 \le 900 \implies$ **Third Split** (`Distance to Land`)
  3. `Distance to Land > 20 km?`: $50 > 20 \implies$ **Rejection Leaf**
* **Prescribed Action**: **reject making a prediction**.

---

#### ❓ Question 4: Decision Enabled by Rejection Learning
* **Question**: What decision is enabled by rejection learning that is not available in traditional predictive modeling?
* **Answer**: **Deciding whether to make a prediction at all**
* **Explanation**: Rejection learning introduces an explicit dummy rejection action ("I Don't Know" button), enabling the system to abstain from making predictions in high-noise or out-of-distribution feature spaces and defer decisions to human experts.

---

#### ❓ Question 5: Recidivism Prediction Fairness Concern
* **Question**: In an $OP^2T$ for recidivism prediction, one branch leads to rejecting predictions for individuals aged 48 or older. Which concern is most directly raised by this design choice?
* **Answer**: **Rejecting predictions based on age may result in unequal treatment across age groups**
* **Explanation**: Automatically excluding specific demographic cohorts (Age $\ge 48$) from prediction scoring introduces systemic algorithmic bias and violates legal/ethical fairness guarantees of equal process under the law.

---

---

### 🏷️ Part 2: Prescriptive Neural Networks (PNNs) & Adaptive Pricing

#### 📌 Problem Setup & Context
An online book retailer uses a PNN to set adaptive prices per customer to maximize total books sold (`units_purchased`).
* **Treatment Options**: $t_1 = \$9.99, t_2 = \$11.99, t_3 = \$13.99, t_4 = \$15.99$.

---

#### ❓ Question 1: Variable Designations
* **Treatment Variable**: `purchase_price` (Book price set by retailer).
* **Outcome Variable**: `units_purchased` (Number of books sold in transaction).

---

#### 📊 Empirical Counterfactual & Prescription Tables

##### Table 1: Counterfactuals ($\Gamma$)
| Transaction ($i$) | $t_1 (\$9.99)$ | $t_2 (\$11.99)$ | $t_3 (\$13.99)$ | $t_4 (\$15.99)$ |
| :---: | :---: | :---: | :---: | :---: |
| **$i=1$** | $0.62$ | $0.55$ | $0.68$ | $0.60$ |
| **$i=2$** | $0.41$ | $0.47$ | $0.39$ | $0.46$ |
| **$i=3$** | $0.58$ | $0.52$ | $0.57$ | $0.50$ |
| **$i=4$** | $0.49$ | $0.45$ | $0.51$ | $0.48$ |
| **$i=5$** | $0.53$ | $0.60$ | $0.56$ | $0.58$ |

##### Table 2: Prescriptions by OPT and PNN
| Transaction ($i$) | OPT Hard Assignment $\mathbf{1}\{\tau(x_i)=t\}$ | PNN Probabilities $\mathbb{P}[\tau(x_i)=t]$ | Prescribed Price |
| :---: | :---: | :---: | :---: |
| **$i=1$** | $[0, 1, 0, 0]$ | $[0.25, 0.40, 0.10, 0.25]$ | OPT: $\$11.99$ / PNN: $\$11.99$ |
| **$i=2$** | $[0, 0, 1, 0]$ | $[0.20, 0.15, 0.50, 0.15]$ | OPT: $\$13.99$ / PNN: $\$13.99$ |
| **$i=3$** | $[0, 0, 0, 1]$ | $[0.15, 0.50, 0.20, 0.15]$ | OPT: $\$15.99$ / PNN: $\$11.99$ |
| **$i=4$** | $[0, 1, 0, 0]$ | $[0.30, 0.35, 0.10, 0.25]$ | OPT: $\$11.99$ / PNN: $\$11.99$ |
| **$i=5$** | $[0, 1, 0, 0]$ | $[0.20, 0.45, 0.15, 0.20]$ | OPT: $\$11.99$ / PNN: $\$11.99$ |

---

#### ❓ Question 2: Transaction 5 Prescription Comparison
* **Answer**: **The OPT and PNN both prescribe pricing the book at $11.99.**
* **Explanation**: OPT indicator is $[0, 1, 0, 0] \implies t_2 = \$11.99$. PNN max probability is $0.45$ at $t_2 \implies \$11.99$.

---

#### ❓ Question 3: OPT Objective Function Value
* **Formula**:

$$\text{Objective}_{\text{OPT}} = \frac{1}{5} \sum_{i=1}^5 \gamma_{i, \tau(x_i)} = \frac{0.55 + 0.39 + 0.50 + 0.45 + 0.60}{5} = \frac{2.49}{5} = \mathbf{0.50} \quad (0.498)$$

---

#### ❓ Question 4: PNN Objective Function Value
* **Formula**:

$$\text{Objective}_{\text{PNN}} = \frac{1}{5} \sum_{i=1}^5 \sum_{t=1}^4 \gamma_{i, t} \cdot p_{i, t}$$

$$\text{Sum} = 0.593 + 0.4165 + 0.536 + 0.4755 + 0.576 = 2.597$$
$$\text{Objective}_{\text{PNN}} = \frac{2.597}{5} = \mathbf{0.519} \quad (0.5194)$$

---

---

### 📝 Official Assignment 2 Summary

In this assignment, you extended your understanding of Optimal Predictive Policy Trees ($OP^2T$) and Prescriptive Neural Networks (PNNs) through two case studies: hurricane prediction and adaptive pricing for an online retailer. These exercises showed how predictive-prescriptive models can choose between competing predictors, decide when to abstain from making predictions, and directly optimize treatment or pricing strategies.

#### Key Takeaways:
* **Hurricane Prediction with $OP^2T$**:
  * Applied $OP^2T$ to route between different predictive models (logistic regression, boosted trees, CNNs, and physics-based simulators).
  * Explored conditions under which the tree recommends a single model, a combination of models, or rejection (choosing not to predict).
  * Learned how rejection learning reduces errors by avoiding unreliable predictions.
  * Examined fairness implications, such as bias introduced when rejecting predictions for subgroups (e.g., older individuals in recidivism prediction).
* **Adaptive Pricing with PNNs**:
  * Modeled book pricing decisions using customer features (age, past purchases, loyalty membership).
  * Compared prescriptions from Optimal Policy Trees versus Prescriptive Neural Networks on sample transactions.
  * Evaluated objective function values for both models to assess effectiveness ($\text{OPT} = 0.50$, $\text{PNN} = 0.519$).
  * Saw how PNNs leverage counterfactuals and a specialized loss function to directly optimize prescriptions, outperforming rule-based OPTs in flexibility.


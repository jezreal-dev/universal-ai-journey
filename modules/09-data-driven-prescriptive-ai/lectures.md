# Module 9: Data-Driven Prescriptive AI — Lecture Notes

## 📖 Lecture 1: From Predictions to Prescriptions

---

### L1.1 Using Predictions for Decision-Making

#### 🎯 Overview: Moving Beyond Forecasting
In classical machine learning, the primary goal is **predictive modeling**—forecasting an outcome variable $\hat{y}$ given input features $X$. However, in real-world business environments, predictions alone are insufficient; managers must take explicit actions. 

**Prescriptive AI** bridges this gap by determining the optimal decision policy $z^*$ that maximizes business utility under operational constraints.

```
+-------------------------------------------------------------------------------+
|                           ANALYTICS PARADIGM SHIFT                            |
+-------------------------------------------------------------------------------+
|  PREDICTIVE ANALYTICS:  What will happen?    -->  Forecast demand y^_j        |
|  PRESCRIPTIVE ANALYTICS: What should we do?  -->  Determine order quantity z*_j|
+-------------------------------------------------------------------------------+
|  * Data-Driven Decisions: Learn optimal decision policies directly from data.  |
|  * Model-Driven Decisions: Formulate optimization models (Linear/Integer Prog).|
+-------------------------------------------------------------------------------+
```

---

#### 🏬 Real-World Case Study: Fortune 100 Multimedia Retailer

* **Operational Scale**:
  * 1 Billion entertainment units produced annually.
  * 1.5 Million active titles across CD, DVD, and Blu-ray formats.
  * Distributed across 50,000+ retail stores worldwide.
* **Core Decision Problem**:
  * On a weekly basis for each store, **which DVD titles to order and in what exact quantities ($z_j$)**?
* **Key Challenges & Dynamics**:
  1. **Physical Shelf Capacity ($K$)**: Strictly limited retail shelf space per store.
  2. **Vast Title Catalog**: Massive combinatorial selection of candidate titles.
  3. **High Demand Uncertainty**: New releases spike immediately—accounting for **up to 10% of total sales in Week 1**—followed by a steep exponential decline over 70 weeks.

---

#### 📊 Data Infrastructure & Feature Correlations

##### 1. Internal Enterprise Data (50 GB per store):
* Weekly aggregated transaction history (2010–present).
* Store geographic coordinates, neighborhood demographics, and median household income.
* Media format attributes (DVD vs. Blu-ray).

##### 2. Public & External Features:
* Metadata: Genre (Action, Comedy, Drama), MPAA rating, cast, plot summary, awards/Oscar nominations.
* Historical Ratings & Box Office: US box office gross prior to DVD release, IMDb ratings, Rotten Tomatoes scores.

##### 3. Empirical Feature Correlations with Week 1 Demand ($y_1$):
* **US Box Office Gross**: $r = 0.32$ (Strong global popularity indicator).
* **IMDb User Vote Count**: $r = 0.25$ (Engagement indicator).
* **IMDb User Rating (Score)**: $r = 0.002$ (**Virtually uninformative** for initial commercial demand!).
* **Google Trends**: Localized interest index by state/canton/region (e.g. *Skyfall* showed local regional interest spikes far exceeding original theatrical distribution). **Top predictor of local demand!**

---

#### 🌲 Predictive Baseline: Random Forest Demand Model

* **Model**: Random Forest Regressor predicting next-week demand $y_j$.
* **Top 2 Features**:
  1. Local Google Trends interest index for the movie title.
  2. Mean historical sales volume at the specific store location.
* **Predictive Accuracy**: Overall $R^2 = 0.67$ (Stable over 30+ weeks).
* **Baseline Comparison**: Outperforms the naive "demand equals last week's sales" baseline, which fails severely during initial release weeks due to sales spikes.

---

#### 🧮 Objective Function & Optimization Formulation

##### Sales Mechanics:
If store order quantity is $z_j$ and actual customer demand is $y_j$, the number of units sold is bounded by both supply and demand:
$$\text{Units Sold}_j = \min(y_j, z_j)$$

##### Prescriptive Mathematical Optimization Problem:
Under known/predicted demand $y_j$, the objective is to maximize total inventory sales subject to physical shelf space constraint $K$:

$$\max_{z_j} \sum_{j} \min(y_j, z_j)$$

$$\text{subject to} \quad \sum_{j} z_j \le K$$
$$z_j \in \mathbb{Z}_{\ge 0} \quad \forall j$$

* **Decision Variables ($z_j$)**: Non-negative integer order quantity for title $j$.
* **Capacity Constraint ($K$)**: Total items ordered cannot exceed store physical shelf limit $K$.

---

### L1.2 The Predictive-Prescriptive (P2) Approach

#### 💡 The Core Innovation: Repurposing ML for Prescription
The fundamental breakthrough of the **Predictive-Prescriptive ($P^2$) approach** is that **we do not use the point prediction $\hat{y}$** (the mean of the leaf) to make decisions. 

Instead, we use the tree structure of machine learning models (CART, Random Forest) to extract the **entire empirical probability distribution of demand** for each item from the historical training data residing in its terminal leaf node!

```
+-------------------------------------------------------------------------------+
|                       PREDICTIVE vs. PRESCRIPTIVE (P^2)                       |
+-------------------------------------------------------------------------------+
|  TRADITIONAL PREDICTIVE:  Leaf samples {3, 5, 7} --> Point Prediction y^ = 5  |
|  PREDICTIVE-PRESCRIPTIVE: Leaf samples {3, 5, 7} --> Distribution P(y) = 1/3  |
|  * Formulates Stochastic Optimization: E[min(y, z)] directly in Objective!    |
+-------------------------------------------------------------------------------+
```

---

#### 🌳 CART Leaf Partitioning Example

Consider training a CART decision tree on 14 historical titles using features:
* $g$: Local Google Searches in prior week.
* $t$: US Theater Box Office Sales ($ millions).
* $s$: Store sales in previous week.

The 14 titles are partitioned into 4 leaf nodes. For 4 new incoming titles ($D=4$), each title routes to a leaf:

| Title Index ($j$) | Features $(g, t, s)$ | Leaf Destination | Leaf Historical Demands $y^{(k)}$ | Point Prediction $\hat{y}_j$ |
| :---: | :---: | :---: | :--- | :---: |
| **Title 1** ($z_1$) | $(7, 0.8\text{M}, 70)$ | Leaf 1 | $\{0, 2, 4\}$ | $\frac{0+2+4}{3} = \mathbf{2.0}$ |
| **Title 2** ($z_2$) | $(8, 1.5\text{M}, 45)$ | Leaf 2 | $\{3, 5, 7\}$ | $\frac{3+5+7}{3} = \mathbf{5.0}$ |
| **Title 3** ($z_3$) | $(12, 1.2\text{M}, 50)$ | Leaf 3 | $\{4, 6, 6, 8\}$ | $\frac{4+6+6+8}{4} = \mathbf{6.0}$ |
| **Title 4** ($z_4$) | $(14, 2.0\text{M}, 85)$ | Leaf 4 | $\{2, 5, 5, 28\}$ | $\frac{2+5+5+28}{4} = \mathbf{10.0}$ |

---

#### ⚠️ Failure of Deterministic Point-Prediction Optimization

If we naively plug point predictions $\hat{y}_j$ into the deterministic optimization problem with store capacity $K=20$:

$$\max_{z} \sum_{j=1}^4 \min(\hat{y}_j, z_j) = \max_z \left[ \min(2, z_1) + \min(5, z_2) + \min(6, z_3) + \min(10, z_4) \right]$$

$$\text{s.t.} \quad z_1 + z_2 + z_3 + z_4 \le 20, \quad z_j \in \mathbb{Z}_{\ge 0}$$

* **Flaw**: Point predictions produce degenerate, unstable solutions like $(0, 0, 0, 20)$ or $(2, 0, 2, 16)$, which completely ignore demand uncertainty, stockout penalties, and tail risks (such as Title 4 occasionally selling 28 units)!

---

#### 📐 The Predictive-Prescriptive ($P^2$) Mathematical Formulation

Under $P^2$, expected sales $\mathbb{E}[\min(y_j, z_j)]$ are calculated explicitly over the empirical distribution in each leaf:

$$\mathbb{E}[\min(y_1, z_1)] = \frac{1}{3}\min(0, z_1) + \frac{1}{3}\min(2, z_1) + \frac{1}{3}\min(4, z_1)$$

$$\mathbb{E}[\min(y_2, z_2)] = \frac{1}{3}\min(3, z_2) + \frac{1}{3}\min(5, z_2) + \frac{1}{3}\min(7, z_2)$$

$$\mathbb{E}[\min(y_3, z_3)] = \frac{1}{4}\min(4, z_3) + \frac{1}{4}\min(6, z_3) + \frac{1}{4}\min(6, z_3) + \frac{1}{4}\min(8, z_3)$$

$$\mathbb{E}[\min(y_4, z_4)] = \frac{1}{4}\min(2, z_4) + \frac{1}{4}\min(5, z_4) + \frac{1}{4}\min(5, z_4) + \frac{1}{4}\min(28, z_4)$$

##### Global $P^2$ Optimization Problem:

$$\max_{z_1, z_2, z_3, z_4} \sum_{j=1}^4 \mathbb{E}_{y_j \sim \text{Leaf}_j} [\min(y_j, z_j)]$$

$$\text{subject to} \quad \sum_{j=1}^4 z_j \le K, \quad z_j \in \mathbb{Z}_{\ge 0}$$

---

#### 🌲 Generalization to Ensembles (Random Forest $P^2$)

For a Random Forest containing $B = 1,000$ CART trees:
1. Each title $j$ routes to a specific leaf node $L_b(j)$ in tree $b \in \{1, \dots, B\}$.
2. The expected sales objective averages empirical leaf distributions across all $B$ trees:

$$\mathbb{E}[\min(y_j, z_j)] = \frac{1}{B} \sum_{b=1}^{B} \left( \frac{1}{|L_b(j)|} \sum_{i \in L_b(j)} \min(y_i, z_j) \right)$$

3. Combining this across all titles yields a smooth, resilient stochastic objective function that accounts for both intra-leaf demand variability and inter-tree model uncertainty.

---

#### 🚀 Real-World Impact & Results
* **Deployment**: Rolled out across **500 European retail stores** for the Fortune 100 multimedia company.
* **Financial Impact**: **+12% improvement in overall profitability** on over $1 Billion revenue $\implies$ **+$120 Million net profit increase!**
* **Personalization**: Decisions $z_j^*$ are automatically tailored to individual store capacity, local neighborhood demographics, regional search trends, and national buying behavior.
* **Broad Application Fields**: Healthcare intervention selection, adaptive pricing, revenue management, supply chain inventory, and transportation routing.

---

### 📝 Official Lecture 1 Summary

In this lecture, we explored the bridge between prediction and prescription, learning how predictions can guide but not dictate decision-making. We examined how prescriptive models use predictions to directly optimize outcomes.

#### Key Takeaways:
* **Prediction is an Input, Not the Output**: In operational decision-making, predicting $\hat{y}$ is merely an intermediate feature; the final objective is determining the optimal action $z^*$.
* **Aligning Decisions with Objectives**: Prescriptive analytics directly formulates decision policies that maximize business utility under real-world constraints.
* **Accuracy vs. Decision Quality**: Predictive accuracy ($R^2$ or RMSE) alone does not guarantee high-quality decisions; accounting for demand distributions and tail risks via the $P^2$ approach yields significantly higher profitability.

---

## 📖 Lecture 2: Policy Trees

**Instructor**: Prof. Dimitris Bertsimas (Boeing Leaders for Global Operations Professor of Management & Professor of Operations Research, MIT)

### 🎯 Overview & Learning Objectives
Lecture 2 introduces **policy trees**—interpretable, rule-based decision-making models that map input features directly to optimal actions. Unlike predictive decision trees (which output a expected numerical value $\hat{y}$ or class label $\hat{C}$ at each leaf), policy trees assign an explicit **prescriptive action/treatment $a^*$** to each leaf node.

#### Learning Objectives:
* **Define Policy Trees**: Explain how policy trees map feature spaces directly to optimal decision actions.
* **Differentiate Paradigms**: Contrast policy trees (direct prescription) with predictive CART trees and $P^2$ indirect optimization.
* **Understand Prescriptive Mechanics**: Master counterfactual evaluation and interpretable treatment rules.

---

### L2.1 What are Policy Trees?

#### 💡 Direct Prescription vs. Indirect Optimization
In Lecture 1, we introduced the **Predictive-Prescriptive ($P^2$)** framework, which builds a predictive model first and then solves an optimization problem over predicted distributions. 

**Policy Trees** take a direct step further: they train decision trees that **directly output a prescribed action/treatment $a^*$** at each leaf, modifying Optimal Classification Trees (OCT) to optimize operational outcomes directly without an intermediate optimization solver.

```
+-------------------------------------------------------------------------------+
|                       DIRECT vs. INDIRECT PRESCRIPTION                        |
+-------------------------------------------------------------------------------+
|  PREDICTIVE-PRESCRIPTIVE (P^2): Data --> Predict Distribution P(y) --> Solver --> Action a* |
|  OPTIMAL POLICY TREES (OPT):    Data -----------------------------------------> Action a* |
|  * Each terminal leaf node directly prescribes a treatment/action a*          |
|  * Highly interpretable: Provides explicit conditional rules (IF/THEN)        |
+-------------------------------------------------------------------------------+
```

---

#### 🏥 Case Study: TAVR Valve Selection in Healthcare

* **Medical Condition**: **Aortic Stenosis** (narrowing of the aortic valve restricting blood flow; affects ~2% of individuals over 65 years).
* **Surgical Procedure**: Transcatheter Aortic Valve Replacement (**TAVR**)—a minimally invasive procedure inserting a prosthetic valve via catheter.
* **Treatment Options ($\mathcal{A}$)**:
  1. `SAPIEN 3` (Edwards Lifesciences).
  2. `Evolut PRO` (Medtronic).
* **Primary Adverse Complication**: **Permanent Pacemaker Implantation (PPI)**.
  * Affects **7% to 18%** of TAVR procedures.
  * Associated with increased long-term mortality and higher post-operative care costs.
* **Prescriptive Goal**: Minimize the probability of a patient requiring a pacemaker ($Y \in \{0, 1\}$).

---

#### 🔍 Observational Data & The Counterfactual Framework

In observational electronic medical records (EMR):
* Each patient $i$ has feature vector $X_i$ (demographics, echo scans), assigned treatment $W_i \in \{\text{SAPIEN 3}, \text{Evolut PRO}\}$, and observed binary outcome $Y_i$.

##### The Fundamental Problem of Causal Prescriptive Inference:
```
                                +-------------------+
                                |   Patient (X_i)   |
                                +---------+---------+
                                          |
                    +---------------------+---------------------+
                    |                                           |
           Assigned: SAPIEN 3                         Counterfactual: Evolut PRO
           Observed: No Pacemaker (Y=0)                Unobserved: ??? (Y^?)
           [FACTUAL OUTCOME]                           [COUNTERFACTUAL OUTCOME]
```

* **Factual Outcome**: The observed result for the treatment the patient actually received.
* **Counterfactual Outcome**: What *would* have happened to that exact patient if given the alternative treatment.

---

#### 🌳 Optimal Policy Trees (OPTs) in Action

Using EMR data from **Hartford HealthCare** (Connecticut's largest health system), an **Optimal Policy Tree (OPT)** was trained to minimize pacemaker implantation rates.

##### Key Predictive Features ($X$):
* Demographics & Health Status: Age, sex, weight, hypertension, diabetes.
* Echocardiogram Scans: Coronary artery dimensions, height, sinotubular junction, minor aortic annulus diameter, peak aortic valve gradient, left ventricular internal diastolic dimension.

##### Discovered Prescriptive Decision Rules:
The trained 6-leaf OPT prescribes `SAPIEN 3` under two distinct clinical conditions:
1. **Rule 1**: Conduction effect present AND Minor Aortic Annulus Diameter $< 22.45$ mm AND Peak Aortic Valve Gradient $< 66$ mm.
2. **Rule 2**: No conduction effect AND Left Ventricular Internal Diastolic Dimension $> 3.85$ cm AND Patient Weight $> 56.1$ kg.
* **Default Rule**: In all other 4 subgroup conditions, the OPT prescribes `Evolut PRO`.

---

#### 📏 Evaluating Policy Trees under Observational Data

To evaluate an OPT's policy performance without true counterfactual ground truth, two foundational assumptions are applied:

1. **Policy Execution Assumption**: All patients partitioned into leaf node $L_k$ receive that leaf's prescribed treatment $a^*$.
2. **Empirical Counterfactual Rate**: The unobserved counterfactual pacemaker rate for patients in leaf $L_k$ under treatment $a^*$ is estimated by the **average pacemaker rate of training patients in leaf $L_k$ who actually received treatment $a^*$**:

$$\hat{Y}_{\text{leaf } k}(a^*) = \frac{\sum_{i \in L_k : W_i = a^*} Y_i}{|\{i \in L_k : W_i = a^*\}|}$$

* **Expected Policy Risk**:
$$R(\text{OPT}) = \sum_{k=1}^K \frac{|L_k|}{N} \cdot \hat{Y}_{\text{leaf } k}(a_k^*)$$

---

### L2.2 Real-World Applications & Empirical Evaluation

#### 🔬 Detailed Leaf Evaluation Mechanics (Node 4 Walkthrough)
Consider **Node 4** (the leftmost terminal leaf of the TAVR Optimal Policy Tree):
* **Subgroup Size**: 62 training patients mapped to Node 4 based on clinical feature splits.
* **OPT Prescribed Action ($a^*$)**: `SAPIEN 3` valve.
* **Empirical Counterfactual Rate Calculation**:
  * Of the 62 patients in Node 4, **40 patients actually received `SAPIEN 3`** in historical EMR data.
  * Their observed average pacemaker rate was **2.5%**.
* **Inference Rule**: Any new incoming patient assigned to Node 4 who receives `SAPIEN 3` has an estimated pacemaker risk of **2.5%**.

---

#### 📊 TAVR Empirical Results: In-Sample & Out-of-Sample

| Evaluation Dataset | Status Quo Pacemaker Rate | OPT Prescribed Pacemaker Rate | Relative Reduction in Adverse Complications |
| :--- | :---: | :---: | :---: |
| **In-Sample (Training Data)** | 13.60% | **8.87%** | **-34.74%** reduction |
| **Out-of-Sample (Test Data)** | 14.51% | **11.39%** | **-21.50%** reduction |

##### Clinical Deployment:
* Implemented as a real-time **Interactive Prescriptive Mobile/Desktop Calculator** integrated into Hartford HealthCare hospital IT systems and cardiologists' mobile devices.

```
+-------------------------------------------------------------------------------+
|                      TAVR PACEMAKER RATE REDUCTION SUMMARY                    |
+-------------------------------------------------------------------------------+
|  STATUS QUO TEST RATE: 14.51%  ========>  OPT PRESCRIBED TEST RATE: 11.39%   |
|  * Achieves 21.5% out-of-sample reduction in permanent pacemaker implants!   |
+-------------------------------------------------------------------------------+
```

---

#### 🌐 Cross-Domain Applications of Optimal Policy Trees (OPT)

```
+-------------------------------------------------------------------------------+
|                        MULTI-DOMAIN OPT APPLICATIONS                          |
+-------------------------------------------------------------------------------+
| 1. HEALTHCARE (TAVR):       Minimize Pacemaker Rate  --> -21.5% Complications |
| 2. HEALTHCARE (DIABETES):   Minimize A1C Blood Sugar --> 0.11 A1C Drop (>2x Threshold)|
| 3. WORKFORCE DEVELOPMENT:   Maximize Post-Training Salary --> Outperforms Status Quo |
| 4. ASSET MANAGEMENT:        Maximize Fund Flow       --> +8% to +15% Revenue Lift    |
+-------------------------------------------------------------------------------+
```

##### 1. Diabetes Healthcare Management (A1C Level Reduction)
* **Problem**: Prescribe 1 of **13 distinct diabetes medication treatment combinations**.
* **Objective**: Minimize Hemoglobin A1C blood sugar levels.
* **Result**: OPT prescriptions achieved an estimated **0.11 reduction in A1C levels**—more than **2x greater** than the clinically meaningful threshold of `0.05`!

##### 2. Workforce Development & Job Training
* **Features**: Age, education level, ethnicity, marital status, prior salary.
* **Treatments**: Job Training ($1$) vs. Control ($0$).
* **Objective**: Maximize post-program salary.
* **Result**: Discovered transparent demographic policy rules detailing which candidate profiles maximize wage returns from job training.

##### 3. Asset Management & Marketing Channel Optimization
* **Problem**: Recommending optimal customer interaction channels for a financial services provider.
* **Action Space ($\mathcal{A}$)**: Phone Call, Email, In-Person Meeting, No Action.
* **Objective**: Maximize net customer fund flow ($).
* **Result**: OPT recommendations achieved a **+8% to +15% lift in total fund inflow** over historical marketing strategies.

---

#### 🏆 Summary: The Competitive Edge of Optimal Policy Trees
* **Domain Primacy**: For **tabular data**, OPT represents the state-of-the-art prescriptive algorithm.
* **The Prescriptive Trifecta**:
  1. **Computational Tractability**: Efficient mathematical optimization.
  2. **Full Interpretability**: Clear, conditional IF/THEN decision logic.
  3. **High Empirical Performance**: Consistent out-of-sample decision gains across healthcare, finance, and operations.

---

### 📝 Official Lecture 2 Summary

In this lecture, we explored how policy trees serve as a transparent and structured way to represent decision policies. We saw that unlike predictive trees, which output predictions, policy trees output actions designed to optimize an objective.

#### Key Takeaways:
* **Feature-to-Action Mappings**: Policy trees provide transparent, interpretable rules mapping input feature vectors $X$ directly to optimal prescriptive actions $a^*$.
* **Direct Prescriptive Encoding**: Unlike predictive trees outputting numerical predictions $\hat{y}$, policy trees directly encode actionable operational decisions.
* **Transparency & Clarity**: Combining high empirical performance with full human interpretability offers unmatched trust and clarity in clinical, financial, and operational decision-making.

---

## 📖 Lecture 3: Policy Trees for Predictive Machine Learning

**Instructor**: Matthew Peroni (PhD Candidate, MIT Operations Research Center)

### 🎯 Overview & Learning Objectives
While previous lectures examined using predictive models to drive operational prescriptions ($P^2$, OPT), Lecture 3 explores the reciprocal paradigm: **how prescriptive policy trees can enhance predictive machine learning**. 

We study how policy trees act as **interpretable routing functions** that adaptively select the best predictive model for specific regions of the feature space $X$.

#### Learning Objectives:
* Understand how prescriptive policy frameworks inform and optimize predictive model selection.
* Combine predictive performance scores with prescriptive optimization objectives.
* Address limitations in traditional model selection and black-box Mixture of Experts (MoE) routing.

---

### L3.1 The Importance of Model Selection & Mixture of Experts

#### ⚖️ The Modern Model Selection Dilemma
Data scientists today choose from a massive ecosystem of algorithms: Linear/Ridge/Lasso regression, Decision Trees, Gradient Boosted Trees (XGBoost, LightGBM), Random Forests, Neural Networks, and Large Language Models. 

Model selection traditionally navigates a **three-way trade-off**:
1. **Performance**: Predictive accuracy ($R^2$, RMSE, AUC).
2. **Efficiency**: Computational speed, latency, and memory footprint.
3. **Interpretability**: Human transparency and regulatory explainability.

```
                                  PERFORMANCE
                                     /\
                                    /  \
                                   /    \
                                  /      \
                                 /        \
                    INTERPRETABILITY ------ EFFICIENCY
```

---

#### ⚠️ Limitations of Traditional Model Selection

##### Standard Model Selection Pipeline:
```
  [Raw Data] ---> [Train/Test Split] ---> [K-Fold Cross-Validation] ---> [Select Single Winner] ---> [Deploy]
```

##### Critical Flaw:
* Traditional pipelines select a **single global model** that achieves the best *average* performance across the entire dataset.
* **The Local Strength Fallacy**: Model $A$ might perform exceptionally well on Subgroup 1 (e.g. young patients, low income), while Model $B$ far outperforms on Subgroup 2 (e.g. elderly patients, high income). Selecting a single global winner discards Model $B$'s superiority in Subgroup 2!

---

#### 🔀 Mixture of Experts (MoE) & The Routing Function

To overcome single-model limitations, the machine learning community developed **Mixture of Experts (MoE)** architectures:

```
                                   +-------------------+
                                   |   Input Sample X  |
                                   +---------+---------+
                                             |
                                   +---------v---------+
                                   |  Routing Function |
                                   |       R(X)        |
                                   +----+---------+----+
                                        |         |
                          +-------------+         +-------------+
                          |                                     |
                +---------v---------+                 +---------v---------+
                |  Expert Model A   |                 |  Expert Model B   |
                |   (e.g., Linear)  |                 |   (e.g., XGBoost) |
                +-------------------+                 +-------------------+
```

* **Routing Function ($R(X)$)**: Maps input feature vector $X$ to the single expert model (or weighted ensemble of experts) best suited for that specific sample.
* **Neural MoE Router Problem**: In modern neural architectures, $R(X)$ is trained as a black-box neural network. Practitioners cannot interpret **why** a specific model was routed or **how** feature threshold shifts alter model selection, eliminating explainability.

---

#### 💡 Prescriptive Policy Trees as Interpretable Routers
To solve the black-box routing limitation, we redefine model selection as a **prescriptive policy problem**:
* **Action Space ($\mathcal{A}$)**: Set of candidate predictive models $\{M_1, M_2, \dots, M_K\}$.
* **Policy Tree Router**: An **Optimal Policy Tree (OPT)** learns interpretable IF/THEN feature rules that prescribe the optimal predictive model $M^*$ for each region of the feature space!

---

### L3.2 Optimal Predictive Policy Trees ($OP^2T$)

#### 💡 The Core Paradigm: Prescribing Models Instead of Treatments
The **Optimal Predictive Policy Tree ($OP^2T$)** framework adapts policy trees to select predictive models dynamically:

* **Traditional Policy Tree**: Prescribes medical treatments (e.g. `SAPIEN 3` vs. `Evolut PRO`) based on patient features $X$.
* **$OP^2T$ Model Router**: Prescribes **predictive models** $h_m \in \mathcal{H} = \{h_1, h_2, \dots, h_M\}$ based on input sample features $X$ to minimize prediction loss.

```
+-------------------------------------------------------------------------------+
|                       TRADITIONAL OPT vs. OP^2T ROUTER                        |
+-------------------------------------------------------------------------------+
|  TRADITIONAL OPT:  Patient Features X  --> Prescribes Treatment a* in {T1, T2}|
|  OP^2T ROUTER:    Sample Features X   --> Prescribes Model h* in {h1, h2, h3} |
+-------------------------------------------------------------------------------+
```

---

#### 🔓 The Causal Breakthrough: Exact Loss Evaluation (No Counterfactual Estimation!)

In clinical causal inference, estimating counterfactual outcomes for unassigned treatments is a major challenge because missing data must be inferred.

**$OP^2T$ completely bypasses counterfactual estimation!**
* Because training and validation samples $(X_i, y_i)$ have ground-truth targets $y_i$, we can run every candidate model $h_m$ on sample $X_i$ and compute the **exact loss** $L(y_i, h_m(X_i))$ for all $m \in \{1, \dots, M\}$ without any missing data!
* **Regression Loss**: Squared Error $(y_i - h_m(X_i))^2$ or Absolute Error $|y_i - h_m(X_i)|$.
* **Classification Loss**: Cross-Entropy Loss or Zero-One Misclassification Loss $\mathbb{I}(\hat{y}_i \ne y_i)$.

---

#### 🧮 Numerical Example: Income Prediction Benchmark

Consider predicting Income $y$ ($k) based on Years of Experience $x_1$ across 4 samples:

| Sample $i$ | Experience $x_1$ | Target $y$ | Model $h_1(x)$ | Model $h_2(x)$ | Model $h_3(x)$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | 2 | 20 | **22** (SE: 4) | 15 (SE: 25) | 10 (SE: 100) |
| **2** | 4 | 30 | **34** (SE: 16) | 20 (SE: 100) | 15 (SE: 225) |
| **3** | 7 | 60 | 40 (SE: 400) | 50 (SE: 100) | **59** (SE: 1) |
| **4** | 10 | 90 | 50 (SE: 1600) | 70 (SE: 400) | **91** (SE: 1) |

##### 1. Best Single Global Model Baseline ($h_3$):
* Evaluating $h_3$ across all 4 samples yields total squared loss $= 100 + 225 + 1 + 1 = 327 \implies \mathbf{\text{MSE} = 81.75}$ (or $h_2$ with total loss $= 625 \implies \text{MSE} = 156.25$). Model $h_3$ is chosen globally.

##### 2. $OP^2T$ Policy Tree Routing ($x_1 \le 5$):
* **Left Leaf ($x_1 \le 5$)**: Prescribes **Model $h_1$** $\implies$ Squared Loss $= 4 + 16 = \mathbf{20}$.
* **Right Leaf ($x_1 > 5$)**: Prescribes **Model $h_3$** $\implies$ Squared Loss $= 1 + 1 = \mathbf{2}$.
* **Total $OP^2T$ Loss**: $20 + 2 = \mathbf{22} \implies \mathbf{\text{MSE} = 5.50}$.
* **Performance Gain**: $OP^2T$ reduces Mean Squared Error from **81.75 down to 5.50** (**-93.2% error reduction**)!

---

#### 🛡️ Validation Protocol & Overfitting Protection

```
  [Full Dataset]
        |
        +---> [Base Model Training Set (80%)] ---> Train Base Models {h1, h2, h3}
        |
        +---> [Validation Set (20%)] -----------> Train OP^2T Policy Router!
```

* **Validation Data Requirement**: $OP^2T$ **must be trained on a validation dataset completely separate** from the data used to train base models $h_1, \dots, h_M$.
* **Overfitting Hazard**: If $OP^2T$ were trained on base model training data, it would over-fit by routing to models that memorized specific training points. Training on held-out validation data ensures the router learns genuine out-of-sample generalization strengths.

---

### L3.3 Real-World Case Study & Rejection Learning

#### 🌀 Realistic Case Study: High-Stakes Hurricane Prediction
* **Prediction Task**: Binary classification—predicting whether an approaching hurricane will reach **Category 3 or greater** upon landfall.
* **Heterogeneous Model Zoo ($\mathcal{H}$)**:
  1. `Logistic Regression`: Simple, transparent baseline model.
  2. `Convolutional Neural Network (CNN)`: Processes 2D satellite cloud imagery.
  3. `Boosted Trees (XGBoost)`: Processes tabular meteorological data.
  4. `Physics-Based Simulator`: Numerical fluid dynamics differential equation solver.

##### $OP^2T$ Routing Discoveries:
* **Rule 1** (Low Wind Speed AND Short Distance to Land): Prescribes `Logistic Regression` $\implies$ Proves that simple, interpretable models can be routed without sacrificing accuracy under low-complexity conditions.
* **Rule 2** (Wind Speed $> 20$ knots AND Low Atmospheric Pressure): Prescribes `Physics-Based Simulator` $\implies$ Physics-based equations dominate during complex high-velocity dynamics.

---

#### 🛑 Rejection Learning: The "I Don't Know" Mechanism

In high-stakes domains (disaster management, oncology, autonomous flight), an incorrect prediction incurs catastrophic costs. **Rejection Learning** equips the system with an option to defer predictions ("I don't know" button) to human experts.

```
+-------------------------------------------------------------------------------+
|                        OP^2T REJECTION LEARNING MECHANISM                     |
+-------------------------------------------------------------------------------+
|  Candidate Actions A = {Model 1, Model 2, Model 3, DUMMY REJECTION MODEL}     |
|  * Set Rejection Loss L_reject (cost of human deferral / audit).              |
|  * IF Min(Loss(Models 1..3)) > L_reject --> Prescribe REJECTION!               |
+-------------------------------------------------------------------------------+
```

##### How $OP^2T$ Implements Rejection Learning:
1. Augment action space with a **Dummy Rejection Action** $M_{\text{reject}}$.
2. Assign a constant loss $L_{\text{reject}}$ representing the cost of human review or deferral.
3. If all candidate models $h_1, \dots, h_M$ exhibit high expected loss in a feature leaf exceeding $L_{\text{reject}}$, $OP^2T$ automatically prescribes **Rejection**.

##### Asymmetric Risk Tuning:
If false positives carry severe penalties (e.g. unnecessary mass evacuations), set a low $L_{\text{reject}}$ for positive instances. $OP^2T$ will defer to human decision-makers unless model predictions are extraordinarily confident.

---

#### 🔍 Interpretable Failure Mode Discovery

In the Hurricane $OP^2T$ with rejection:
* **Discovered Rejection Rule**: When **Wind Speed $> 20$ knots AND Low Pressure AND Distance to Land $\ge 100$ km**, the tree prescribes **Rejection**.
* **Operational Insight**: Exposes the exact feature subspace where **all available predictive models fail**!
* **Actionable Guidance**: Guides meteorologists to deploy specialized ocean buoys or gather targeted satellite observations in that specific offshore feature region.

---

#### 🌟 Key Architectural Advantages of $OP^2T$

```
+-------------------------------------------------------------------------------+
|                          THREE ADVANTAGES OF OP^2T                            |
+-------------------------------------------------------------------------------+
| 1. MODEL-AGNOSTIC:     Pairs ML, Deep Learning, LLMs & Physics Simulators!   |
| 2. ASYMMETRIC FEATURES: Router uses Tabular X_meta; Base Models use Images X_img!|
| 3. NON-INVASIVE:       Leaves pre-trained models intact while optimizing routing.|
+-------------------------------------------------------------------------------+
```

1. **Model-Agnostic Flexibility**: Operates directly across statistical models, deep neural networks, LLMs, and non-data-driven physics simulators.
2. **Asymmetric Feature Spaces (Structured Router for Unstructured Models)**:
   * The router can use structured tabular features ($X_{\text{meta}}$: wind speed, pressure, location) while base models process unstructured inputs ($X_{\text{img}}$: satellite images, text).
3. **Non-Invasive Complementarity**: Enhances existing production models without requiring retraining or architecture modification.

---

### L3.4 Real-World Case Study: Concrete Compressive Strength

#### 🏗️ Industrial Application & Objective
* **Goal**: Predict the **compressive strength** (maximum structural load/force before breakage) of industrial concrete mixtures based on raw ingredient proportions: Cement, Water, Blast Furnace Slag, Fly Ash, Superplasticizer, Coarse Aggregate, Fine Aggregate, and Age.
* **Domain Significance**: Critical structural safety metric in civil engineering (bridges, skyscrapers, dams).
* **Model Zoo ($\mathcal{H}$)**: `XGBoost`, `Random Forest`, `Multi-Layer Perceptron (MLP)`, `Linear Regression`, and Model Ensembles.
* **Loss Function**: Squared Error $(y_i - \hat{y}_i)^2$.

---

#### 🌳 $OP^2T$ Tree Discoveries: Non-Rejection vs. Rejection

```
+-------------------------------------------------------------------------------+
|                      CONCRETE STRENGTH OP^2T ROUTING RULES                    |
+-------------------------------------------------------------------------------+
|  NON-REJECTION OPT:  Cement < 357 kg/m^3  --> Prescribe XGBOOST             |
|                      Cement >= 357 kg/m^3 --> Prescribe RANDOM FOREST        |
|  * Discards Linear Regression & MLP (both underperform across all leaves).    |
+-------------------------------------------------------------------------------+
|  REJECTION OPT:      High Slag Density AND Low Water Density --> REJECT!      |
|  * Identifies dry, slag-heavy mixes as dangerous, error-prone regions.        |
+-------------------------------------------------------------------------------+
```

##### 1. Non-Rejection Policy Tree Insights:
* `XGBoost` and `Random Forest` dominate all other candidate models (`Linear Regression` and `MLP` are completely discarded).
* **Cement Threshold Split**:
  * **Rule 1** (Cement $< 357\text{ kg/m}^3$): Prescribes **`XGBoost`**.
  * **Rule 2** (Cement $\ge 357\text{ kg/m}^3$): Prescribes **`Random Forest`**.
* **Domain Takeaway**: Gradient boosting captures non-linear interactions better in lean/low-cement mixtures, whereas random forest bagging generalizes better on dense/high-cement mixtures.

##### 2. Rejection Policy Tree Insights:
* Adding the dummy rejection action causes the policy tree to refine its feature space partitioning.
* **Discovered Rejection Rule**: When **Blast Furnace Slag density is High AND Water density is Low**, $OP^2T$ prescribes **Rejection**.
* **Engineering Action**: Alerts civil engineers that low-water/high-slag concrete mixtures induce unpredictable non-linear chemical curing dynamics, guiding targeted lab testing for dry slag mixes.

---

#### 📊 Empirical Performance & Rejection Trade-Off

| Model / Framework | Rejection Threshold ($L_{\text{reject}}$) | Rejection Rate (%) | Predicted Subset MSE | Overall Generalization |
| :--- | :---: | :---: | :---: | :--- |
| **Best Single Model (Hindsight)** | No Rejection | 0.0% | Baseline | Single global winner (Random Forest / XGBoost). |
| **Non-Prescriptive MoE** | No Rejection | 0.0% | Higher | Non-interpretable mixture weighting. |
| **$OP^2T$ (Low Rejection)** | Strict Penalty | 5.2% | **-18.4%** MSE | Rejects extreme outliers. |
| **$OP^2T$ (Balanced Rejection)**| Medium Penalty | **17.0%** | **Massive MSE Drop** | **Optimal Trade-off**: Rejects top 17% tricky samples. |
| **$OP^2T$ (High Rejection)** | Lenient Penalty | 32.5% | Ultra-Low MSE | High precision on remaining 67.5% samples. |

##### Key Empirical Finding:
Taking a **prescriptive $OP^2T$ approach** significantly outperforms the best single model chosen in hindsight and non-prescriptive mixture of experts baselines. By rejecting just **17% of tricky/unstable samples**, $OP^2T$ achieves a massive reduction in prediction error on the remaining 83% deployed samples.

---

### L3.5 Recidivism Prediction & Algorithmic Bias Diagnostics

#### ⚖️ High-Stakes Criminal Justice Domain & Fairness Challenges
* **Task**: Recidivism prediction—determining whether a formerly convicted individual will be charged with a new crime within 3 years of release from prison.
* **Dataset**: National Institute of Justice (NIJ) empirical dataset containing demographic data, drug use history, arrest history, employment status, and 3-year recidivism target labels.
* **Ethical Hazard**: Using automated machine learning for criminal justice decisions (parole, bail, sentencing) risks perpetuating and amplifying systemic socio-economic and demographic biases.
* **The Blindness Fallacy**: Simply removing protected features (e.g. race or gender) from the feature set does **NOT** eliminate bias, as remaining correlated variables (ZIP code, employment history, prior arrests) act as proxies.

---

#### 🔍 $OP^2T$ as a Bias & Fairness Diagnostic Engine

Training an $OP^2T$ with a rejection option on the NIJ dataset revealed critical ethical diagnostics directly from the policy tree topology:

```
+-------------------------------------------------------------------------------+
|                       OP^2T ALGORITHMIC BIAS DIAGNOSTICS                      |
+-------------------------------------------------------------------------------+
| 1. AGE-BASED REJECTION:  Tree prescribes REJECT based on Age thresholds!      |
|    --> Exposes that ALL candidate models are unstable for specific age groups. |
| 2. ZIP-CODE ROUTING:    Tree selects Model A vs B based on ZIP Code!           |
|    --> Exposes geographic bias; global models penalize specific neighborhoods.|
| 3. INTERPRETABLE ROUTE: Tree identifies sub-populations where Logistic         |
|    Regression equals Black-Box accuracy --> Enables 100% Explainability!      |
+-------------------------------------------------------------------------------+
```

##### 1. Age-Based Rejection Routing:
* The $OP^2T$ prescribed **Rejection** based on **Age** thresholds.
* **Diagnostic Insight**: Indicates that *all* candidate predictive models exhibit high error and instability for specific age cohorts. Relying on predictions for these demographic groups would lead to unfair, biased judicial treatment.

##### 2. Geographic / ZIP-Code Partitioning:
* The $OP^2T$ selected different base models based on **ZIP Code**.
* **Diagnostic Insight**: Reveals that predictive models perform unequally across geographic neighborhoods. Selecting a single global model imposes hidden performance penalties and systematic bias on residents of specific ZIP codes.

##### 3. Prescribing Interpretable Models Without Accuracy Loss:
* Black-box models (XGBoost, Deep Neural Nets) obscure how predictions are generated.
* **Operational Fix**: $OP^2T$ identifies specific feature sub-populations where simple, fully explainable models (e.g. `Logistic Regression`) perform **equally as well as black-box models**, allowing practitioners to safely deploy transparent models without sacrificing predictive accuracy.

---

#### 🏁 Summary of Lecture 3: Prescriptive Methods for Predictive ML

* **Reciprocal Enhancement**: Prescriptive policy trees ($OP^2T$) enhance predictive modeling by serving as interpretable routing functions.
* **Non-Invasive Deployment**: $OP^2T$ operates on pre-trained, frozen production models without requiring retraining, making it an immediate, practical tool for model selection, rejection learning, and fairness auditing.
* **Research Attribution**: Based on research by Matthew Peroni and Prof. Dimitris Bertsimas (MIT Operations Research Center).

---

### 📝 Official Lecture 3 Summary

In this lecture, we examined how predictive ML models can be transformed into prescriptive decision tools via policy trees. We explored strategies for mapping predictions to optimal actions and the considerations needed to maintain decision quality.

#### Key Takeaways:
* **Adapting Predictions for Prescriptions**: Predictive models can guide decision-making, but must be adapted using prescriptive policy trees ($OP^2T$) to optimize operational objectives.
* **Incorporating Predictive Scores**: Policy trees incorporate exact predictive scores and losses across candidate models to determine optimal routing rules.
* **Balancing Accuracy & Decision Objectives**: Integrating predictive ML into prescriptive decision-making requires balancing raw predictive accuracy with decision goals, rejection options, and fairness constraints.

---

## 📖 Lecture 4: Prescriptive Neural Networks (PNNs)

**Instructors**: Lisa Everest (L4.1) & Vassilina Stoumpou (L4.2) (PhD Candidates, MIT Operations Research Center)

### 🎯 Overview & Learning Objectives
Lecture 4 introduces **Prescriptive Neural Networks (PNNs)**—a deep learning framework designed to handle unstructured multi-modal data (images, text, video, sensors) while directly optimizing prescriptive decision policies. We examine PNN architecture, end-to-end loss formulations, and how to * **Recover Interpretability**: Mirror PNN decision boundaries using Mirrored Optimal Classification Trees (Mirrored OCTs).

---

### L4.1 The Optimal Prescription Problem & Counterfactual Estimation

#### 🎯 The Optimal Prescription Problem Formulation
The **optimal prescription problem** asks: *Given observational sample features $X_i$, what treatment $t^* \in \mathcal{T}$ should be prescribed to minimize (or maximize) expected outcome $Y_i$?*

```
+-------------------------------------------------------------------------------+
|                       FOUR CATEGORIES OF TREATMENT SPACES                     |
+-------------------------------------------------------------------------------+
| 1. SINGLE DISCRETE / BINARY: T in {0, 1}           --> Drug vs. Control       |
| 2. MULTIPLE DISCRETE:        T in {A, B, C, ...}  --> 1 of K Medication Types|
| 3. SINGLE CONTINUOUS:        T in [a, b]          --> Continuous Dosage Range |
| 4. MULTIPLE CONTINUOUS:      T_vec in R^k         --> Combinatorial Dosages   |
|    (e.g., Joint Metformin + Insulin + Oral Agent continuous dosage vectors)   |
+-------------------------------------------------------------------------------+
```

---

#### 🌟 Why Prescriptive Neural Networks (PNNs)?

| Historical Approach | Multimodal Ingestion | Non-Linear Capacity | Treatment Scalability | Differentiable End-to-End |
| :--- | :---: | :---: | :---: | :---: |
| **Regress-and-Compare** | ❌ No | Moderate | Poor (Fails on Continuous) | ❌ No |
| **Causal Forests** | ❌ No | Tree-based | Poor (Scales poorly with $\vec{T}$) | ❌ No |
| **Optimal Policy Trees (OPT)** | ❌ No (Tabular only) | Axis-aligned splits | Moderate | ❌ No |
| **Prescriptive Neural Networks (PNN)** |  **Yes (Text/Images/Tabular)** |  **Deep Expressive Power** |  **Integrated (Binary $\to$ Mult. Cont.)** |  **Yes** |

---

#### 🛠️ The 4-Step PNN Pipeline Architecture

```
  +-----------------------+      +------------------------------+
  |  Step 1: Embedding    | ---> |  Step 2: Counterfactual      |
  |  Extraction           |      |  Estimation (Matrix Gamma)   |
  +-----------------------+      +--------------+---------------+
                                                |
  +-----------------------+      +--------------v---------------+
  |  Step 4: Mirrored     | <--- |  Step 3: Train PNN Policy    |
  |  OCT (Interpretability)|      |  Neural Network              |
  +-----------------------+      +------------------------------+
```

---

#### 📦 Step 1: Multimodal Embedding Extraction
PNNs convert heterogeneous data modalities into a single unified continuous embedding vector $\vec{E}_i$:

1. **Tabular Features**: Processed via standard normalization $\vec{x}_{\text{tab}}$.
2. **Unstructured Text (Notes)**: Ingested via pre-trained Transformer Encoders (BERT, Clinical-Longformer) $\to \vec{e}_{\text{text}}$.
3. **Unstructured Images (Scans)**: Ingested via pre-trained Vision Encoders (DenseNet, ResNet) $\to \vec{e}_{\text{img}}$.
4. **Concatenation**:

$$\vec{E}_i = \text{Concat}(\vec{x}_{\text{tab}}, \vec{e}_{\text{text}}, \vec{e}_{\text{img}})$$

---

#### 🔮 Step 2: Counterfactual Estimation & Rewards Matrix ($\Gamma$)

##### The Counterfactual Table:
In observational historical records, we only observe factual cell outcomes (gray), while unobserved counterfactual cell outcomes (red) must be inferred:

| Patient ($i$) | Assigned Treatment $W_i$ | Observed Outcome $Y_i$ | Treatment A (Factual) | Treatment B (Counterfactual) | Treatment C (Counterfactual) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Patient 1** | **Treatment A** | `0.82` | **0.82** (Observed) | $\hat{\gamma}_{1, B}$ (Inferred) | $\hat{\gamma}_{1, C}$ (Inferred) |
| **Patient 2** | **Treatment B** | `0.45` | $\hat{\gamma}_{2, A}$ (Inferred) | **0.45** (Observed) | $\hat{\gamma}_{2, C}$ (Inferred) |

##### Estimation Methods:
1. **Direct Method**: Trains independent regression models $\hat{m}_t(X)$ for each treatment. 
   * *Flaw*: Suffers from **treatment assignment bias** if certain treatments are heavily imbalanced in historical data.
2. **Doubly Resilient Method**: Combines a classification model for **propensity scores** $e_t(X) = P(W=t \mid X)$ with regression models, reweighting outcomes by inverse propensity scores to eliminate treatment assignment bias.

##### Resulting Rewards Matrix ($\Gamma$):
Produces an $N \times |\mathcal{T}|$ matrix $\Gamma$, where entry $\gamma_{i, t}$ represents the estimated counterfactual outcome for patient $i$ under treatment $t$.

---

### L4.2 PNN Loss Function, Mirrored OCTs & Experimental Benchmarks

#### 🧮 Step 3: PNN Architecture & Differentiable Prescriptive Loss

##### Architecture & Softmax Layer:
Structurally, a PNN is a deep Feedforward Neural Network taking unified embeddings $\vec{E}_i$ as input, with one or more hidden layers and an output layer of $N_t$ neurons (one for each distinct treatment $t \in \mathcal{T}$).

A **Softmax activation function** maps output logits to continuous treatment assignment probabilities $p_{i, t} \in [0, 1]$:

$$p_{i, t}(\theta) = \frac{\exp(z_{i, t})}{\sum_{k=1}^{N_t} \exp(z_{i, k})}$$

```
+-------------------------------------------------------------------------------+
|                       PNN DIFFERENTIABLE PRESCRIPTIVE LOSS                    |
+-------------------------------------------------------------------------------+
|  HARD INDICATOR LOSS (OPT):   Loss = Sum_i Sum_t gamma_{i,t} * I(t^ = t)      |
|  * Non-differentiable! Cannot compute gradients for backpropagation.         |
|  SMOOTH PNN LOSS (SOFTMAX):   L_PNN(theta) = 1/N Sum_i Sum_t gamma_{i,t} * p_{i,t}|
|  * Fully Differentiable! Backpropagates counterfactual rewards through network!|
+-------------------------------------------------------------------------------+
```

##### Mathematical Loss Formulation:
For a minimization objective (e.g. minimizing mortality or blood sugar), the PNN directly minimizes expected counterfactual cost:

$$\mathcal{L}_{\text{PNN}}(\theta) = \frac{1}{N} \sum_{i=1}^N \sum_{t=1}^{N_t} \gamma_{i, t} \cdot p_{i, t}(\theta)$$

* **Gradient Dynamics**: Backpropagation computes $\frac{\partial \mathcal{L}}{\partial \theta}$, driving probabilities $p_{i, t} \to 1$ for treatments with small counterfactual costs $\gamma_{i, t}$, and $p_{i, t} \to 0$ for bad treatments.
* **Final Prescription**: $\hat{t}_i^* = \arg\max_t p_{i, t}$.

---

#### 🪞 Step 4: Recovering Interpretability via Mirrored OCTs

```
  [Unstructured Data] ---> [PNN Deep Model] ---> [Prescriptions t^*] ---> [Train Mirrored OCT] ---> [Transparent Rules]
```

* **The Mirrored OCT Framework**:
  * Train an **Optimal Classification Tree (OCT)** using the **PNN's prescribed treatments $\hat{t}_i^*$ as target labels**.
  * The OCT "mirrors" the complex PNN decision boundary into transparent IF/THEN rules.
  * **Empirical Guarantee**: Mirrored OCTs preserve almost 100% of the PNN's performance gains without sacrificing human interpretability.

---

#### 🧪 Experimental Results Across 6 Real-World Datasets

##### Evaluation Protocol:
* Evaluated on a strict **50/50 Train/Test split**.
* Performance measured as **Relative Percentage Improvement** over status-quo real-life clinical/business decisions.

| Dataset Name | Domain | Modality | Treatment Space | Outcome Goal | PNN / Mirrored OCT Performance Gain | Key Finding |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **TAVR Valve Replacement** | Healthcare | Multimodal (Tabular + CTA Notes) | Discrete (SAPIEN 3 vs Evolut) | Min Pacemaker | **Statistically Significant Improvement** | Multimodal PNN far outperforms tabular-only PNN! |
| **Severe Liver Injury** | Healthcare | Multimodal (Tabular + CT Notes) | Binary (Surgery vs Observation) | Min Mortality | **Consistent Mortality Reduction** | Demonstrates text notes boost decision quality. |
| **Type 2 Diabetes** | Healthcare | Structured (60k patients) | Multiple Continuous (Metformin+Insulin+Oral) | Min HbA1C | **Outperforms Baselines** | Handles high-dimensional continuous dosage vectors. |
| **Strawberry Pricing** | Retail | Structured (100k transactions) | Single Continuous Price ($) | Max Revenue | **Statistically Significant Revenue Lift** | Mirrored OCT preserves PNN revenue gains. |
| **Spleen Injury** | Healthcare | Structured | 3 Discrete Options | Min Mortality | **>10% Mortality Reduction** | Outperforms standard decision trees. |
| **REBOA Trauma** | Healthcare | Structured (10k patients) | Binary (REBOA Surgery vs Control) | Min Mortality | **Superior Survival Rates** | Regress-and-Compare fails; PNN dominates. |

---

#### 🏆 Summary of PNN Framework
1. **Multimodal Ingestion**: PNNs are the first prescriptive AI framework capable of processing text, images, and tabular data simultaneously via embedding concatenation.
2. **Flexible Treatment Handling**: Directly handles binary, multiple discrete, single continuous, and multiple continuous treatment spaces.
3. **End-to-End Differentiable Optimization**: Directly minimizes expected counterfactual outcomes $\sum \gamma_{i, t} p_{i, t}$.
4. **Mirrored OCTs**: Solves the black-box dilemma by extracting transparent decision rules without sacrificing performance.

---

### 📝 Official Lecture 4 Summary

In this lecture, we explored how prescriptive neural networks directly learn decision policies that maximize outcomes. We covered their architecture, the integration of optimization into training, and the benefits of handling high-dimensional and nonlinear decision spaces.

#### Key Takeaways:
* **Merging Deep Learning & Prescriptive AI**: PNNs combine the representational power of deep learning (processing text, images, and tabular data) with direct prescriptive decision goals.
* **Direct Policy Optimization**: They directly learn optimal actions via a smooth, differentiable loss function without requiring a separate prediction step.
* **High-Dimensional & Continuous Scalability**: PNNs are uniquely suited for complex, non-linear, high-dimensional, and continuous treatment decision problems.
* **Interpretability via Mirrored OCTs**: Mirrored Optimal Classification Trees are trained on PNNs' learned prescriptions to provide transparent decision rules with minimal reduction in performance.











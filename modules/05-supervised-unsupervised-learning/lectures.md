# Supervised and Unsupervised Learning – Lectures

📅 Completed — June 2026  
🎓 MIT Open Learning via 3MTT  

---

## Section Progress
- [x] Lecture 1: Linear Regression & the Statistical Sommelier  
- [x] Lecture 2: Logistic Regression & The Framingham Heart Study  
- [x] Lecture 3: Tree-Based Methods & The Supreme Court  
- [x] Lecture 4: Classification Performance Metrics & Healthcare Quality  
- [x] Lecture 5: Foundations of Clustering  
- [x] Lecture 6: Interpretable Clustering  

---

## Lecture 1: Linear Regression & the Statistical Sommelier

### Overview
This lecture introduces **linear regression**, a fundamental tool in supervised learning. The lecture showcases how a simple quantitative model can disrupt a domain dominated by subjective, expert judgment. It uses the case of **Orley Ashenfelter**, a Princeton economist who challenged the authority of world-famous wine critics (like Robert Parker) by predicting Bordeaux wine quality and auction prices using weather data and aging variables, without tasting a single drop.

### Learning Objectives
- Predict a continuous outcome variable (dependent variable) using one or more independent variables.
- Calculate and interpret linear regression coefficients.
- Evaluate model performance using Sum of Squared Errors (SSE), Total Sum of Squares (SST), and $R^2$.
- Contrast quantitative model-based predictions with subjective expert opinions.

### Key Concepts

#### Mathematical Model
The multiple linear regression model assumes a linear relationship between the dependent variable $y_i$ and $k$ independent variables $x_{ij}$:
\[y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \dots + \beta_k x_{ik} + \epsilon_i\]
Where:
- $\beta_0$: Intercept (value of $y$ when all independent variables are zero).
- $\beta_j$: Regression coefficient representing the change in $y$ for a one-unit change in $x_j$, holding other variables constant.
- $\epsilon_i$: Idiosyncratic error/noise for observation $i$.

#### Ordinary Least Squares (OLS)
The coefficients ($\beta_j$) are estimated by minimizing the **Sum of Squared Errors (SSE)**:
\[\text{SSE} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2\]
Where $\hat{y}_i$ is the predicted value.

#### R-squared ($R^2$) Metric
$R^2$ measures the proportion of variance in the dependent variable explained by the model, relative to a baseline model (which predicts the training mean $\bar{y}$ for all observations):
- **Total Sum of Squares (SST):** The squared differences from the baseline mean:
  \[\text{SST} = \sum_{i=1}^{n} (y_i - \bar{y})^2\]
- **R-squared Formula:**
  \[R^2 = 1 - \frac{\text{SSE}}{\text{SST}}\]
- **Interpretation:** $R^2 = 0$ means the model performs no better than the baseline mean; $R^2 = 1$ indicates a perfect fit.

#### The Bordeaux Wine Case
- **Dependent Variable (y):** $\log(\text{Price})$ in auctions (approximates quality).
- **Independent Variables (x):**
  - **Age** of the wine (older wines are generally scarcer and more expensive).
  - **Average growing season temperature** (higher temperatures improve grape ripeness).
  - **Harvest rain** (rain during harvest swells grapes, diluting flavor).
  - **Winter rain** (replenishes soil moisture before the growing season).
- **Outcome:** The model correctly identified that the 1989 vintage would be the "wine of the century" and 1990 would be even better, outperforming critic Robert Parker who originally called 1986 exceptional and 1989 mediocre.

---

## Lecture 2: Logistic Regression & The Framingham Heart Study

### Overview
This lecture introduces **logistic regression** for binary outcomes through the lens of **The Framingham Heart Study**, one of the most influential medical studies of the 20th century. Launched in 1948 in Framingham, Massachusetts, it followed over 5,000 residents to systematically track risk factors for Cardiovascular Disease (CVD). This study debunked major historical medical misconceptions—such as untreated high blood pressure being a healthy physiological mechanism, which contributed to President Franklin D. Roosevelt's death in 1945.

### Learning Objectives
- Apply logistic regression to model and predict binary class outcomes (0 or 1).
- Compute and interpret odds and the logistic (sigmoid) transformation.
- Understand significance levels of regression coefficients using standard errors and p-value markers.
- Grasp the necessity of external model validation across diverse cohorts.

### Key Concepts

#### The Logistic Model & Sigmoid Function
Linear regression is unsuitable for binary outcomes because it can predict probabilities outside the $[0, 1]$ range. Logistic regression models the probability $P(y = 1)$ using the **logistic (sigmoid) function**:
\[P(y = 1) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \dots + \beta_k x_k)}}\]

#### Odds and Log-Odds (Logit)
- **Odds:** The ratio of the probability of occurrence to the probability of non-occurrence:
  \[\text{Odds} = \frac{P}{1 - P} = e^{\beta_0 + \beta_1 x_1 + \dots + \beta_k x_k}\]
- **Logit (Log-Odds):** Taking the natural logarithm of the odds yields a linear equation:
  \[\log\left(\frac{P}{1 - P}\right) = \beta_0 + \beta_1 x_1 + \dots + \beta_k x_k\]
- **Interpretation:** A one-unit increase in $x_j$ increases the log-odds by $\beta_j$, which multiplies the odds by $e^{\beta_j}$.

#### Differentiating Risk Factors
- **Demographics:** Age, Sex, Education.
- **Behaviors:** Smoking status, number of cigarettes per day.
- **Medical History:** Blood pressure medication (BPmeds), prevalent stroke, prevalent hypertension, diabetes.
- **Physical/Clinical Exams:** Total cholesterol, systolic blood pressure (sysBP), diastolic blood pressure (diaBP), BMI, heart rate, and blood glucose level.

#### Model Refinement & Significance
- **Multicollinearity:** Correlated predictors (e.g., diabetes and glucose, or sysBP and diaBP) can create high standard errors and counterintuitive coefficient signs.
- **Pruning:** Removing insignificant variables (using significance stars where `***` $p < 0.001$, `**` $p < 0.01$, `*` $p < 0.05$, `.` $p < 0.1$) refines the model to have positive, statistically significant coefficients that align with medical consensus.
- **Modifiable Risk Factors:** Identifies actionable areas for patient intervention, such as smoking cessation or using statins/diuretics to lower cholesterol and blood pressure.

#### Validation and Generalizability
- **Internal Validation:** Splitting data into train/test sets.
- **External Validation:** Testing the Framingham model on other cohorts (e.g., ARIC for Black individuals, Honolulu Heart Program for Japanese-Americans). The model systematically overpredicted CHD risk for Japanese-Americans by a factor of 2, demonstrating that risk models must be calibrated to specific populations.

---

## Lecture 3: Tree-Based Methods & The Supreme Court

### Overview
This lecture introduces **Classification and Regression Trees (CART)**, a popular non-parametric machine learning method. CART offers exceptional interpretability by mimicking human decision pathways. To demonstrate its power, the lecture presents a head-to-head competition where a simple CART model predicted Supreme Court decisions, outperforming a panel of legal scholars who had deep qualitative expertise.

### Learning Objectives
- Understand the recursive partitioning process of CART.
- Interpret decision tree nodes, splits, and terminal leaves.
- Prevent overfitting using bucket constraints (minbucket) and complexity parameters (cp).
- Grasp how Random Forests improve predictive performance through ensembling.

### Key Concepts

#### Classification and Regression Trees (CART)
- **Structure:** A decision tree starts with a single root node and splits data recursively into child nodes based on binary thresholds (e.g., $x_j < v$).
- **Splitting Criteria:** Splits are selected to maximize **node purity**:
  - For classification: Minimizing **Gini Impurity** or **Entropy**.
  - For regression: Minimizing the **Residual Sum of Squares (RSS)**.
- **Terminal Leaves:** Nodes at the bottom of the tree that contain final class or numerical predictions.

#### Overfitting and Regularization
- If unrestricted, a tree can grow until every observation occupies its own leaf node, creating a model that does not generalize.
- **Minbucket (Minimum Bucket Size):** Restricts splits so that each child node must contain at least a specified minimum number of observations.
- **Complexity Parameter (cp):** Penalizes larger trees. Similar to adjusted $R^2$, a split is only made if it improves the model's objective function by more than $cp$.

#### Ensemble Methods: Random Forests
- **Bagging (Bootstrap Aggregating):** Training multiple decision trees on different random samples (bootstrapped) of the dataset.
- **Feature Randomness:** At each node split in a tree, only a random subset of predictors is considered, reducing correlation among the trees.
- **Prediction:** Final prediction is made by taking a majority vote (for classification) or an average (for regression) across all trees, yielding higher accuracy at the cost of direct interpretability.

---

## Lecture 4: Classification Performance Metrics & Healthcare Quality

### Overview
Using a case study of predicting quality in healthcare through insurance claims data, this lecture explores the trade-offs of classification models. Because probabilities are continuous, predicting classes requires establishing a **probability threshold ($t$)**. Selecting this threshold directly shifts the balance of model errors, which is critical in healthcare where diagnosing a sick patient as healthy (false negative) can be fatal, while diagnosing a healthy patient as sick (false positive) causes unnecessary anxiety and costs.

### Learning Objectives
- Build and interpret a **Confusion Matrix**.
- Calculate and explain classification accuracy, sensitivity, specificity, and false positive rate.
- Evaluate model performance using ROC curves and the Area Under the Curve (AUC) metric.
- Understand the business and medical trade-offs of shifting the threshold $t$.

### Key Concepts

#### Thresholding
A logistic regression model outputs a continuous probability $P(y = 1)$. A threshold $t \in [0, 1]$ transforms this into a binary class prediction:
- Predict class 1 if $P(y = 1) \geq t$
- Predict class 0 if $P(y = 1) < t$

#### Confusion Matrix
A tabular layout showing actual vs. predicted classes:

| | Predicted $0$ (Good Care) | Predicted $1$ (Poor Care) |
|---|---|---|
| **Actual $0$ (Good Care)** | **True Negative (TN)** | **False Positive (FP)** |
| **Actual $1$ (Poor Care)** | **False Negative (FN)** | **True Positive (TP)** |

#### Performance Metrics
- **Accuracy:** Proportion of correct predictions:
  \[\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{Total}}\]
- **Sensitivity (Recall or True Positive Rate):** Proportion of actual positives correctly identified:
  \[\text{Sensitivity} = \frac{\text{TP}}{\text{TP} + \text{FN}}\]
- **Specificity (True Negative Rate):** Proportion of actual negatives correctly identified:
  \[\text{Specificity} = \frac{\text{TN}}{\text{TN} + \text{FP}}\]
- **False Positive Rate (FPR):** Proportion of actual negatives incorrectly predicted as positive:
  \[\text{FPR} = 1 - \text{Specificity} = \frac{\text{FP}}{\text{TN} + \text{FP}}\]

#### Threshold Trade-offs
- **High Threshold ($t \to 1$):** Conservative predictions. High specificity, low sensitivity (detects only the most certain cases, missing many positives).
- **Low Threshold ($t \to 0$):** Aggressive predictions. High sensitivity, low specificity (detects almost all positives, but with many false alarms).

#### ROC Curve and AUC
- **Receiver Operating Characteristic (ROC) Curve:** Plots **Sensitivity** on the y-axis against **$1 - \text{Specificity}$** (FPR) on the x-axis for all possible thresholds $t$.
- **Area Under the Curve (AUC):** Summarizes the ROC curve into a single value representing the probability that the model will rank a randomly chosen positive observation higher than a randomly chosen negative one:
  - $\text{AUC} = 0.5$: Equal to random guessing.
  - $\text{AUC} = 1.0$: Perfect classifier.

---

## Lecture 5: Foundations of Clustering

### Overview
This lecture introduces **unsupervised learning**, specifically **clustering**, a technique for grouping data points without prior labels. Clustering uncovers hidden structures based on similarity, which is highly useful in market segmentation, identifying clinical subgroups, and analyzing user profiles. The lecture covers two primary algorithms: **K-means** and **hierarchical clustering**, emphasizing the necessity of data normalization.

### Learning Objectives
- Formulate and calculate distances between observations.
- Contrast K-means (flat, centroid-based) and hierarchical (nested, linkage-based) clustering.
- Understand the mathematical impact of feature scaling.
- Determine the optimal number of clusters using scree plots and dendrograms.

### Key Concepts

#### Distance Metric (Euclidean Distance)
Clustering relies on distance to quantify similarity. The distance between two observations $i$ and $j$ in $p$-dimensional space is:
\[d(i, j) = \sqrt{(x_{i1} - x_{j1})^2 + (x_{i2} - x_{j2})^2 + \dots + (x_{ip} - x_{jp})^2}\]

#### Data Normalization (Feature Scaling)
If one variable is measured in thousands (e.g., account balance in miles) and another in single digits (e.g., number of transactions), the variable with the larger scale will dominate distance calculations. Normalization ensures each feature contributes equally:
\[z_{ip} = \frac{x_{ip} - \mu_p}{\sigma_p}\]
Where $\mu_p$ is the mean and $\sigma_p$ is the standard deviation of feature $p$.

#### K-means Clustering
- **Algorithm:**
  1. Specify the number of clusters $K$.
  2. Randomly initialize $K$ cluster centroids.
  3. Assign each observation to the nearest centroid.
  4. Recalculate centroids as the mean of all assigned observations.
  5. Repeat steps 3 and 4 until assignments no longer change.
- **Properties:** Flat, fast, scalable; but requires specifying $K$ up front and can converge to local minima depending on initialization.

#### Hierarchical Clustering (Agglomerative)
- **Algorithm:**
  1. Start with each observation in its own cluster (n clusters).
  2. Combine the two clusters that have the smallest dissimilarity.
  3. Recompute dissimilarities between the new cluster and all other clusters.
  4. Repeat steps 2 and 3 until all points are merged into a single cluster.
- **dissimilarity Linkages:**
  - **Single linkage:** Distance between the closest points in two clusters.
  - **Complete linkage:** Distance between the furthest points.
  - **Average linkage:** Mean distance between all pairs.
  - **Ward's method:** Minimizes the increase in total within-cluster variance.
- **Dendrogram:** A tree-like diagram showing the order and distance at which clusters were merged. The vertical height represents the distance at which splits occur. The amount of "wiggle room" (vertical distance without splits) indicates cluster resilience.

#### Selecting the Number of Clusters
- **Scree Plot (Elbow Method):** Plots the Within-Cluster Sum of Squares (WCSS) against the number of clusters $K$. The optimal $K$ is located at the "elbow" where WCSS drop decelerates.
  \[\text{WCSS} = \sum_{k=1}^{K} \sum_{i \in C_k} d(x_i, \mu_k)^2\]

---

## Lecture 6: Interpretable Clustering

### Overview
While clustering is a powerful way to segment data, the resulting clusters can be difficult to explain because they are defined in high-dimensional space. This lecture introduces **interpretable clustering**, a methodology that combines unsupervised clustering with supervised classification trees. By training a decision tree (like CART or Optimal Classification Trees) to predict cluster assignments using the original features, we can generate transparent, rule-based profiles that are easily understood by decision-makers.

### Learning Objectives
- Identify the limitations of "black-box" clustering centroids.
- Combine unsupervised clustering with supervised decision trees.
- Formulate simple, rule-based customer or operational segments.
- Interpret and apply the Bluebikes ridership case study.

### Key Concepts

#### The Methodology of Interpretable Clustering
1.  **Cluster the Data:** Run K-means or hierarchical clustering on the normalized dataset to assign each observation $i$ a cluster label $C_i \in \{0, 1, \dots, K-1\}$.
2.  **Define Target:** Treat the cluster labels $C_i$ as the dependent variable (target).
3.  **Train a Decision Tree:** Train a decision tree (such as CART) using the original, un-normalized features to predict the target $C_i$.
4.  **Extract Rules:** Read the decision tree splits to describe each cluster using clear logic (e.g., "If high blood pressure = Yes and diabetes = Yes, then Cluster 1").
5.  **Evaluate Fit:** Measure the tree's classification accuracy. High accuracy indicates that the decision tree splits successfully capture the geometric boundaries of the clusters.

#### Bluebikes Ridership Case Study
- **Goal:** Segment users of the Boston bike-share program (Bluebikes) to optimize station placement and marketing.
- **Variables:** Ride duration, weekday vs. weekend, user age, subscriber status, and route type.
- **Unsupervised Result:** K-means creates distinct user groups.
- **Interpretable Tree Result:** Generates clear, rule-based profiles:
  - **Profile A (Commuters):** Short rides, weekdays, subscribers.
  - **Profile B (Leisure Riders):** Longer rides, weekends, non-subscribers.
  - **Profile C (Long-Distance Commuters):** High-duration rides, weekdays, older age.
- **Impact:** Allows managers to make targeted operational decisions (e.g., restocking bikes at commuter hubs during rush hours) rather than relying on abstract multi-dimensional centroids.

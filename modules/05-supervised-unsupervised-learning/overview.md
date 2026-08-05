# Supervised and Unsupervised Learning – Overview

📅 Completed — June 2026  
🎓 MIT Open Learning via 3MTT  

---

## Section Progress
- [x] Module Overview  
- [x] Learning Goals  
- [x] Lecture & Recitation Roadmap  

---

## Module Overview

**Instructors:**  
- **Dimitris Bertsimas**, Boeing Leaders for Global Operations Professor of Management and Professor of Operations Research at MIT.
- **Vassilina Stoumpou**, PhD Candidate at MIT's Operations Research Center.
- **Yu Ma**, Assistant Professor at the University of Wisconsin.

This module explores the dual core pillars of machine learning: **supervised learning** (where models learn from labeled historical outcomes to make predictive judgments) and **unsupervised learning** (where algorithms group unlabeled observations purely based on internal patterns and similarity). Through real-world case studies in viticulture, cardiology, the legal system, healthcare administration, and medical records, this module bridges the gap between machine-generated predictions and human understanding.

---

## Learning Goals

By the end of this module, learners will be able to:

### In Supervised Learning:
- **Understand and apply multiple modeling paradigms**, including linear regression, logistic regression, and classification and regression trees (CART).
- **Interpret model parameters** such as OLS regression coefficients, odds ratios, and decision tree splits.
- **Evaluate model performance** using metrics like $R^2$, sum of squared errors (SSE), classification accuracy, area under the ROC curve (AUC), sensitivity, and specificity.
- **Identify and address multicollinearity** when predictors share strong correlations.
- **Perform model validation** (internal cross-validation and external cohort generalizability testing) to evaluate model resilience.

### In Unsupervised Learning:
- **Define and apply clustering methods** including K-means and hierarchical clustering to segment unlabeled observations.
- **Normalize and scale features** to ensure features contribute equally to distance calculations.
- **Select optimal cluster numbers** using tools like dendrogram wiggles and scree plots (elbow method).
- **Make clusters interpretable and actionable** by training decision trees on cluster assignments.

---

## Lecture & Recitation Roadmap

| Type | # | Title | Core Concepts |
|---|---|---|---|
| **Lecture** | 1 | Linear Regression & the Statistical Sommelier | Predicting wine quality, OLS, residuals, SSE, SST, and $R^2$ |
| **Lecture** | 2 | Logistic Regression & The Framingham Heart Study | Predicting 10-year coronary heart disease, logistic curves, odds, significance stars |
| **Lecture** | 3 | Tree-Based Methods & The Supreme Court | CART models, leaf nodes, minbucket, complexity parameter, random forests |
| **Lecture** | 4 | Classification Performance Metrics & Healthcare Quality | Confusion matrices, accuracy, sensitivity, specificity, AUC, ROC curves, probability thresholds |
| **Lecture** | 5 | Foundations of Clustering | K-means, hierarchical clustering, Euclidean distance, normalization, scree plots |
| **Lecture** | 6 | Interpretable Clustering | Integrating K-means with Optimal Classification Trees (OCT) for rule-based profiles |
| **Recitation** | 1 | Regression in Action: Wine & Cardiology | Step-by-step linear and logistic regression modeling |
| **Recitation** | 2 | Tree Methods: Supreme Court Decisions | Training CART trees and evaluating decision boundaries |
| **Recitation** | 3 | Holistic Supervised Pipeline: Boston Airbnb | Clean data, feature engineering, regression, classification, ensembling |
| **Recitation** | 4 | Unsupervised Segmentation: Heart Failure | K-means, hierarchical clustering, dendrograms, cluster profiling |

---

## My Reflections

This module feels like the most hands-on and mathematically rewarding section yet. It bridges simple statistics to predictive analytics, using data to challenge or augment human expertise in fields where subjective opinion has historically reigned supreme (like wine critique or legal predictions).

I am fascinated by how **logistic regression** has literally reshaped modern medicine. Learning that President Franklin D. Roosevelt's fatal blood pressure of 300/190 went untreated because doctors at the time believed hypertension was a necessary physiological mechanism to "push blood through the arteries" underscores how far we've come. The Framingham Heart Study proved that data-driven analytics can identify risk factors (smoking, high blood pressure, cholesterol) and prompt clinical interventions (like statins and diuretics) that save millions of lives.

The transition to **unsupervised learning** is also eye-opening. Clustering allows us to discover natural divisions in data when there are no labels. Using decision trees on top of cluster centroids to create "interpretable clustering" is a brilliant bridge between complex math and executive decision-making. 

**Key takeaway:** ML models are only as good as our understanding of them. Combining predictive strength with interpretability—whether through simplified regressions, decision trees, or cluster profiling—is key to building trustworthy systems in high-stakes fields like healthcare.

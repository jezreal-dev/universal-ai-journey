# Supervised and Unsupervised Learning – Recitations

📅 Completed — June 2026  
🎓 MIT Open Learning via 3MTT  

---

## Section Progress
- [x] Recitation 1: Regression in Action (Wine & Cardiology)  
- [x] Recitation 2: Tree Methods (Supreme Court Decisions)  
- [x] Recitation 3: Holistic Supervised Pipeline (Boston Airbnb)  
- [x] Recitation 4: Unsupervised Segmentation (Heart Failure Clinical Records)  

---

## Recitation 1: Regression in Action (Wine & Cardiology)

### Overview
This recitation demonstrates the practical implementation of linear and logistic regression in Python using `pandas`, `statsmodels`, and `scikit-learn`. Using the Bordeaux wine dataset and the Framingham heart study dataset, we build, evaluate, and interpret predictive models.

### Key Workflows

#### 1. Multiple Linear Regression (Bordeaux Wine)
- **Data Load:** Loaded `wine.csv` (training data) and `wineTest.csv` (out-of-sample testing data).
- **Model Fitting:** Regressed $\log(\text{Price})$ against `AGST` (Average Growing Season Temperature), `HarvestRain`, `WinterRain`, and `Age` using ordinary least squares (OLS):
  ```python
  import pandas as pd
  import statsmodels.api as sm
  
  train = pd.read_csv("wine.csv")
  X = train[["AGST", "HarvestRain", "WinterRain", "Age"]]
  X = sm.add_constant(X)
  y = train["LogPrice"]
  
  model = sm.OLS(y, X).fit()
  print(model.summary())
  ```
- **Evaluation:** Evaluated training $R^2$ (typically around $0.8286$) and computed out-of-sample $R^2$ on test data:
  ```python
  test = pd.read_csv("wineTest.csv")
  X_test = sm.add_constant(test[["AGST", "HarvestRain", "WinterRain", "Age"]])
  preds = model.predict(X_test)
  
  SST = ((test["LogPrice"] - train["LogPrice"].mean()) ** 2).sum()
  SSE = ((test["LogPrice"] - preds) ** 2).sum()
  test_R2 = 1 - (SSE / SST)
  ```

#### 2. Logistic Regression (Framingham CHD Risk)
- **Model Fitting:** Fit a logistic regression model to predict the 10-year risk of CHD using training patient profiles.
- **Variable Selection:** Pruned insignificant variables (such as education and diastolic blood pressure) to build a resilient, parsimonious model where all remaining coefficients are positive and statistically significant (e.g., age, male, cigarettes per day, totChol, sysBP, glucose).
- **Out-of-Sample AUC:** Evaluated predictions on the test set, computing the Area Under the ROC Curve (AUC) to assess how well the model distinguishes between high-risk and low-risk patients (achieving an AUC of approximately $0.74$).

---

## Recitation 2: Tree Methods (Supreme Court Decisions)

### Overview
This recitation focuses on tree-based modeling (CART and Random Forests) in Python. Using Supreme Court voting data (`Stevens.csv`), we predict whether Justice John Paul Stevens will vote to reverse or affirm a lower court's decision. We walk through data splitting, training decision trees, optimizing parameters, and comparing performance against random forest ensembles.

### Key Workflows

#### 1. Classification Trees (CART)
- **Parameters:** Explored parameters that control tree depth and splitting behavior:
  - `minbucket`: The minimum number of observations required in a leaf node.
  - `cp` (Complexity Parameter): Minimum improvement required for a node to split.
- **Tree Visualization:** Built classification trees using `scikit-learn`'s `DecisionTreeClassifier` and visualized split conditions (such as the source court or the issue area):
  ```python
  from sklearn.tree import DecisionTreeClassifier, plot_tree
  import matplotlib.pyplot as plt
  
  # Predicts Reverse (1) vs. Affirm (0)
  clf = DecisionTreeClassifier(min_samples_leaf=5, random_state=42)
  clf.fit(X_train, y_train)
  
  plt.figure(figsize=(12, 8))
  plot_tree(clf, feature_names=X_train.columns, class_names=["Affirm", "Reverse"], filled=True)
  ```
- **Evaluation:** Evaluated accuracy and AUC on test data. Discussed how changing `minbucket` from 5 to 50 prevents overfitting by creating a simpler, more interpretable tree.

#### 2. Random Forests
- **Training:** Trained a Random Forest classifier consisting of 500 trees:
  ```python
  from sklearn.ensemble import RandomForestClassifier
  
  rf = RandomForestClassifier(n_estimators=500, min_samples_leaf=5, random_state=42)
  rf.fit(X_train, y_train)
  ```
- **Trade-off:** Observed that the Random Forest increased test accuracy (often by 3-5% over a single tree), but sacrificed the direct, visual interpretability of the decision splits.

---

## Recitation 3: Holistic Supervised Pipeline (Boston Airbnb)

### Overview
This recitation walks through an end-to-end data science pipeline using Boston Airbnb listings data (`listings_with_amenities.csv`). We cover data preparation, feature engineering, regression modeling for price prediction, and classification modeling to predict high-value properties.

### Key Workflows

#### 1. Data Cleaning and Preprocessing
- **Missing Data:** Imputed missing values in features like `review_scores_rating`.
- **Feature Engineering:** Extracted numeric columns and engineered features from text descriptions (e.g., parsing amenities to count facilities like Wifi or Air Conditioning).
- **Categorical Encoding:** One-hot encoded categorical variables (such as neighborhood and property type).

#### 2. Price Prediction (Regression)
- **Model Fitting:** Built linear regression and CART regression trees to predict the continuous listing price.
- **Evaluation:** Calculated Root Mean Squared Error (RMSE) and $R^2$ on test data.
- **Centering/Scaling:** Standardized numeric features to make linear coefficients comparable in magnitude.

#### 3. Predicting High-Value Listings (Classification)
- **Target Definition:** Converted the listing price into a binary outcome:
  - `1` if price > \$150 (High Value)
  - `0` otherwise
- **Modeling:** Trained logistic regression, classification trees, and Random Forests on the binary target.
- **Thresholding:** Evaluated different probability thresholds ($t$) using confusion matrices. Plotting the ROC curve demonstrated the trade-off: lowering $t$ raised sensitivity (detecting more expensive listings) but lowered specificity (more false positives).

---

## Recitation 4: Unsupervised Segmentation (Heart Failure Clinical Records)

### Overview
This recitation covers the unsupervised learning workflow using heart failure patient data (`heart_failure.csv`). We apply hierarchical and K-means clustering to segment patients into clinical profiles, use WCSS and dendrograms to select cluster counts, and train a decision tree on the cluster labels to make the groupings interpretable.

### Key Workflows

#### 1. Normalization and Distance
- **Scaling:** Scaled clinical features (age, creatinine phosphokinase, ejection fraction, platelets, serum sodium, serum creatinine) to have a mean of 0 and standard deviation of 1. This prevents variables with large ranges (e.g., platelets in the hundreds of thousands) from dominating distance calculations:
  ```python
  from sklearn.preprocessing import StandardScaler
  
  scaler = StandardScaler()
  scaled_features = scaler.fit_transform(df[numeric_cols])
  ```

#### 2. Hierarchical Clustering
- **Linkages:** Applied agglomerative clustering using different linkage criteria (Ward's, Average, Complete, and Single).
- **Dendrogram:** Visualized the merge hierarchy using SciPy's dendrogram functions:
  ```python
  from scipy.cluster.hierarchy import linkage, dendrogram
  
  mergings = linkage(scaled_features, method="ward")
  dendrogram(mergings, labels=df.index, leaf_rotation=90)
  ```
- **Wiggle Room:** Analyzed the vertical heights of the dendrogram to identify stable thresholds (where cluster counts remain unchanged over a wide range of distances).

#### 3. K-means Clustering & The Elbow Method
- **Scree Plot:** Plotted the Within-Cluster Sum of Squares (WCSS) for $K \in [1, 10]$ to find the "elbow" point:
  ```python
  from sklearn.cluster import KMeans
  
  wcss = []
  for k in range(1, 11):
      kmeans = KMeans(n_clusters=k, random_state=42)
      kmeans.fit(scaled_features)
      wcss.append(kmeans.inertia_)
  ```
- **Fitting:** Selected $K=4$ and fit the final K-means model to retrieve cluster labels.

#### 4. Interpretable Clustering
- **Decision Tree Integration:** Trained a CART classifier to predict the cluster labels using the original, un-scaled clinical features:
  ```python
  from sklearn.tree import DecisionTreeClassifier
  
  clf = DecisionTreeClassifier(max_depth=3, random_state=42)
  clf.fit(df[numeric_cols], kmeans.labels_)
  ```
- **Rules Extraction:** The decision tree splits revealed clear clinical profiles, explaining how patients were assigned to groups based on easily understood thresholds (e.g., "Creatinine > 1.5 mg/dL and Ejection Fraction < 30%").

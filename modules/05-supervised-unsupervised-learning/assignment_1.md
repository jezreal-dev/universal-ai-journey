# Supervised and Unsupervised Learning – Assignments

📅 Completed — June 2026  
🎓 MIT Open Learning via 3MTT  

---

## Section Progress
- [x] Part 1: Predicting Life Expectancy in the United States  
- [x] Part 2: Exploring Climate Change  

---

## Part 1: Predicting Life Expectancy in the United States

### Overview
In this assignment, we examine the `statedata.csv` dataset, which contains metrics on all 50 U.S. states from the 1970s. The goal is to build a multiple linear regression model to predict the average **Life Expectancy (`Life.Exp`)** in each state using predictors like population, income, illiteracy, murder rate, high school graduation rate, frost days, and area.

---

### Questions and Solutions

#### Question 1: Scatter Plot Swapping
If the arguments to `plt.scatter()` were accidentally swapped, what would be the most noticeable effect on the plot?
- ✅ **The outline of the U.S. would appear rotated across the diagonal**
- The axes labels would automatically correct themselves
- Alaska and Hawaii would disappear
- The plot would become empty
> **Explanation:** Plotting longitude ($x$) vs. latitude ($y$) generates a scatter plot representing the physical geography (outline) of the United States. Swapping the axes swaps the horizontal and vertical coordinates, rotating the map across the $y = x$ diagonal line.

#### Question 2: Murder Rate by Region
Which region has the highest median murder rate?
- West
- ✅ **South**
- North Central
- Northeast
> **Explanation:** Subsetting the dataset and grouping by `state.region` yields the following median murder rates:
> - South: **10.85**
> - North Central: **6.90**
> - West: **6.10**
> - Northeast: **3.25**

#### Question 3: Boxplot Limitations
Which limitation of the boxplot makes the subsetting step especially important?
- Boxplots hide the median
- Boxplots only work for large datasets
- ✅ **Boxplots do not identify individual observations by name**
- Boxplots cannot display numerical values
> **Explanation:** While boxplots are excellent for displaying quartiles, medians, and outliers, they only show summary distributions and anonymous points, making it impossible to identify which specific state corresponds to a given outlier without subsetting the data.

#### Question 4: Regression Coefficients
What is the coefficient value for Murder in the linear regression model predicting life expectancy?
- ✅ **`-0.3011`**
> **Explanation:** Fitting a multiple linear regression model using all independent variables (`Population`, `Income`, `Illiteracy`, `Murder`, `HS.Grad`, `Frost`, `Area`) yields an OLS coefficient for `Murder` of **`-0.301123`**.

#### Question 5: Coefficient Interpretation
In the fitted model, what is the correct interpretation of the coefficient for Murder?
- Murder rate has no effect once other variables are included
- ✅ **For a one-unit increase in murder rate, predicted life expectancy changes by the coefficient**
- For a one-unit increase in murder rate, income changes by the coefficient
- For a one-unit increase in life expectancy, murder rate decreases by the coefficient
> **Explanation:** In multiple linear regression, each coefficient represents the expected change in the dependent variable (`Life.Exp`) for a one-unit increase in that independent variable, holding all other variables constant.

#### Question 6: Scatter Plot Relationship
Which visual feature of the scatter plot most strongly supports the observed relationship between income and life expectancy?
- Points form a vertical band
- ✅ **Points tend to slope upward from left to right**
- Points form a horizontal band
- Points are tightly clustered at a single income value
> **Explanation:** A positive relationship between two continuous variables is visually represented by points sloping upwards from left to right (as $x$ increases, $y$ increases).

#### Question 7: Multicollinearity Causes
Which situation would most directly lead to multicollinearity in the life expectancy regression model?
- Including a predictor with a very small coefficient
- ✅ **Including predictors that are strongly correlated with each other**
- Including both numeric and categorical predictors
- Including a predictor that has no variation across states
> **Explanation:** Multicollinearity occurs when two or more independent variables are highly linearly correlated, making it difficult for the regression model to estimate their individual effects independently.

#### Question 8: Simplified Models
Which of the following best explains why the final model uses fewer predictors than the original model?
- The remaining variables were chosen randomly
- The removed variables had missing data
- ✅ **A simpler model can explain the data well without unnecessary or redundant variables**
- Fewer predictors always guarantee better prediction accuracy
> **Explanation:** In model building, we aim for parsimony. Removing statistically insignificant variables simplifies the model, makes coefficients easier to interpret, and reduces multicollinearity, without significantly reducing the model's explanatory power.

#### Question 9: R-squared Score Changes
Removing insignificant variables changes the R^2 Score value of the model. By looking at the summary output for both the initial model (all independent variables) and the simplified model (only 4 independent variables) and using what you learned in class, which of the following correctly explains the change in the R^2 Score value?
- We expect the "R^2 Score" of the simplified model to be about the same as the initial model (we have no way of knowing if it will be slightly worse or slightly better than the R^2 Score of the initial model).
- We expect the "R^2 Score" value of the simplified model to be slightly better than that of the initial model. It can't be worse than the "R^2 Score" value of the initial model.
- ✅ **We expect the "R^2 Score" value of the simplified model to be slightly worse than that of the initial model. It can't be better than the "R^2 Score" value of the initial model.**
> **Explanation:** Standard $R^2$ will mathematically always decrease (or remain equal) when variables are removed from a regression model. It can never increase because the full model contains a superset of the predictors and can at least fit the data as well as the simplified version. Here, R-squared changed from **0.7362** (full) to **0.7360** (simplified), representing a negligible decrease.

#### Question 10: Washington Predictions
Why might Washington have the highest predicted life expectancy even if another state has a higher observed value?
- ✅ **Because predictions depend on the selected predictors and their coefficients, not directly on observed outcomes**
- Because the model ignores life expectancy
- Because the dataset was standardized
- Because predictions are random
> **Explanation:** The regression model makes predictions based on the weighted sum of a state's independent variables (`Population`, `Murder`, `HS.Grad`, `Frost`), not on its actual observed life expectancy. If a state has a favorable combination of these predictors, it will receive a high predicted value.

#### Question 11: Actual Life Expectancy
Which description best matches the type of quantity being identified when we ask for the state with the lowest actual life expectancy?
- A value adjusted for multicollinearity
- A value derived from regression coefficients
- A value estimated by a regression model
- ✅ **A value directly observed in the dataset**
> **Explanation:** Actual life expectancy refers to the raw, observed value in the data, which for the lowest state is **South Carolina** (**67.96** years).

#### Question 12: High Predictions
Why can a state have the highest predicted life expectancy even if it is not highest on every individual predictor?
- ✅ **Because predictions are based on a weighted combination of all predictors**
- Because predictions are random
- Because life expectancy is standardized
- Because predictors are ignored by the model
> **Explanation:** A state does not need to be the best in every individual category. The model aggregates the weighted contributions of all variables, so high performance in major categories (like high graduation rates and low murder rates) can offset mediocre values elsewhere.

#### Question 13: Finding Maximums
What operation correctly identifies the state with the highest observed life expectancy?
- Sorting predictors by coefficient size
- ✅ **Finding the maximum value in the observed life expectancy data**
- Examining t-statistics
- Finding the maximum predicted value
> **Explanation:** Observed life expectancy is the dependent variable. Finding the state with the maximum value in that column (which is **Hawaii** at **73.6** years) directly identifies it.

#### Question 14: Smallest Absolute Error
Which quantity must be examined to determine where the model makes the smallest absolute prediction error?
- The p-values from the model summary
- ✅ **The absolute values of the residuals**
- The predicted life expectancy values
- The regression coefficients
> **Explanation:** Prediction error (residual) is the difference between observed and predicted values ($y_i - \hat{y}_i$). The smallest absolute prediction error is found by taking the minimum of the absolute residuals (which is **Indiana** with an absolute error of **0.0216**).

#### Question 15: Least Accurate Prediction
Which quantity should be examined to identify the least accurate prediction made by the model?
- The minimum p-value
- ✅ **The maximum absolute residual**
- The largest coefficient
- The smallest predicted value
> **Explanation:** The least accurate prediction corresponds to the point furthest from the regression line, which represents the maximum absolute residual (which is **Hawaii** with an absolute error of **1.5068**).

---

## Part 2: Exploring Climate Change

### Overview
In this assignment, we use `climate_change.csv` containing monthly atmospheric concentrations and global temperature anomalies from May 1983 to December 2008. We split the data into a training set (up to and including 2006) and a testing set (post-2006) to analyze climate trends, model multicollinearity, and test out-of-sample predictive power.

---

### Questions and Solutions

#### Question 1: R-squared Source Data
Is the reported R^2 computed using the training data or the testing data? (answer with one word: training or testing)
- ✅ **`training`**
> **Explanation:** The standard R-squared value reported in a model's summary output is calculated based on the data used to fit (train) the model.

#### Question 2: Statistical Significance
Which of the following variables has a statistically significant coefficient (p-value < 0.05) in the full regression model?
- N2O
- CH4
- ✅ **MEI**
> **Explanation:** Running OLS on the training set with all predictors (`MEI`, `CO2`, `CH4`, `N2O`, `CFC-11`, `CFC-12`, `TSI`, `Aerosols`) shows that `MEI` has a p-value of **0.000** (statistically significant), while `N2O` has a p-value of **0.055** and `CH4` has a p-value of **0.810** (both insignificant).

#### Question 3: Unexpected Coefficient Signs
In a multiple linear regression model, why can a variable’s coefficient have an unexpected sign even if the variable is strongly related to the response when examined on its own?
- Because regression coefficients always represent causal effects
- Because the response variable is standardized
- ✅ **Because the variable shares strong correlations with other predictors in the model**
- Because linear regression forces coefficients to alternate signs
> **Explanation:** This is a classic symptom of multicollinearity. When predictors are highly correlated (e.g., greenhouse gases rising together over time), the model cannot easily separate their individual contributions, leading to high variance in coefficient estimates and signs that run opposite to physical reality.

#### Question 4: Correlated Predictors
Which of the following variables have an absolute correlation above 0.7 with CFC.12? (Select all that apply.)
- ✅ **CO2** (0.8527)
- ✅ **N2O** (0.8679)
- ✅ **CH4** (0.9636)
- MEI (0.0083)
- Aerosols (-0.2251)
- TSI (0.2553)
> **Explanation:** The correlation matrix of the training data shows that carbon dioxide, nitrous oxide, and methane all share strong linear correlations ($> 0.7$) with CFC-12 due to common anthropogenic increases. (Note: CFC-11 also has a correlation of 0.8690, but it was not listed in the options).

#### Question 5: Negative Coefficients in Reduced Model
How many independent variables in the reduced model have negative coefficients?
- ✅ **`1`**
> **Explanation:** The reduced model includes four independent variables (`MEI`, `N2O`, `TSI`, `Aerosols`). The OLS training coefficients are:
> - `MEI`: **+0.0642** (positive)
> - `N2O`: **+0.0253** (positive)
> - `TSI`: **+0.0795** (positive)
> - `Aerosols`: **-1.7017** (negative)
>
> Thus, exactly **1** independent variable (Aerosols) has a negative coefficient. (The constant/intercept is -116.2269, but it is not an independent variable).

#### Question 6: R-squared Change Evaluation
Is the change in R^2 between the full and reduced models greater than 0.05?
- No
- ✅ **Yes**
> **Explanation:** Evaluating the change on the out-of-sample **testing data** (which represents the standard model comparison step on holdout data in this assignment):
> - Full Model Test $R^2$: **0.6274**
> - Reduced Model Test $R^2$: **0.4968**
> - **Difference:** $0.6274 - 0.4968 = \mathbf{0.1306}$ (which is greater than 0.05).
> 
> *(Note: On the training set, the R-squared values are 0.7509 for the full model and 0.7261 for the reduced model, representing a difference of 0.0248, which is less than 0.05. However, on the test set, the difference is 0.1306, which is greater than 0.05.)*

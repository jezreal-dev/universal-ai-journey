# Supervised and Unsupervised Learning – Assignment 2

📅 Completed — June 2026  
🎓 MIT Open Learning via 3MTT  

---

## Section Progress
- [x] Part 1: Predicting Loan Repayments using Logistic Regression  
- [x] Part 2: Predicting Stock Returns with Tree-Based Methods  

---

## Part 1: Predicting Loan Repayments

### Overview
In this assignment, we examine the `loans_imputed.csv` dataset, which contains 9,578 3-year loans from LendingClub.com. The goal is to build logistic regression models to predict whether a borrower will fail to fully repay their loan (`not.fully.paid = 1`) based on their credit policy, loan purpose, interest rate, installment size, annual income, debt-to-income ratio, FICO score, credit history length, revolving balance, credit inquiries, and derogatory records.

---

### Questions and Solutions

#### Question 1: Fraction of Unpaid Loans
What fraction of loans have `not.fully.paid = 1` according to the dataset summary? (round to 4 decimal places)
- ✅ **`0.1601`** (exact: `0.160054`)
> **Explanation:** The mean of the binary variable `not.fully.paid` is `0.160054`, which indicates that approximately 16.01% of the 9,578 loans were not fully repaid.

#### Question 2: Significant Credit-History Variables
Which credit-history variables are significant in the full logistic regression model? (Select all that apply.)
- ✅ **`fico`** (p-value < 0.001)
- ✅ **`revol.bal`** (p-value = 0.001)
- ✅ **`pub.rec`** (p-value = 0.001)
- `days.with.cr.line` (p-value = 0.900)
> **Explanation:** Looking at the OLS Logit regression summary, the p-values for `fico` (z = -5.414, p = 0.000), `revol.bal` (z = 3.399, p = 0.001), and `pub.rec` (z = 3.207, p = 0.001) are all well below the standard 0.05 significance level. `days.with.cr.line` has a p-value of 0.900, meaning it is not statistically significant.

#### Question 3: Log-Odds of Non-Payment Comparison
Consider two loan applications, which are identical other than the fact that the borrower in Application A has FICO credit score 700 while the borrower in Application B has FICO credit score 710. Is the log-odds of non-payment higher for A or B?
- ✅ **`A`**
- `B`
> **Explanation:** The coefficient for the `fico` score in our logistic regression model is **$-0.0092$**. Since this coefficient is negative, an increase in FICO score decreases the log-odds of a borrower defaulting. Consequently, Application A (FICO 700) has a higher predicted risk (higher log-odds of non-payment) than Application B (FICO 710).

#### Question 4: FICO Score Odds Ratio
Consider two loan applications, which are identical other than the fact that the borrower in Application A has FICO credit score 300 while the borrower in Application B has FICO credit score 320. Now, let $O(A)$ be the odds of loan A not being paid back in full, and define $O(B)$ similarly for loan B. What is the value of $O(A)/O(B)$?
- ✅ **`1.2019`** (or `1.20`)
> **Explanation:** The change in FICO score is $-20$ units. The odds ratio is given by:
> $$\frac{O(A)}{O(B)} = e^{\beta_{\text{fico}} \times (300 - 320)} = e^{-0.00919648 \times (-20)} = e^{0.18393} \approx 1.2019$$
> This means that a borrower with a FICO score of 300 has 1.20 times the odds of defaulting compared to an otherwise identical borrower with a FICO score of 320.

#### Question 5: Misclassified Test Observations
How many test observations were misclassified in the logistic regression model? (using a threshold of 0.5)
- ✅ **`470`**
> **Explanation:** The confusion matrix on the test set is:
> * True Negatives: `2394` | False Positives: `20`
> * False Negatives: `450` | True Positives: `10`
> 
> The total number of misclassified test observations is the sum of false positives and false negatives: $20 + 450 = 470$.

#### Question 6: Majority Class Proportion
What proportion of the test set belongs to the majority class? (Round to 4 decimal places)
- ✅ **`0.8399`** (exact: `0.839944`)
> **Explanation:** The test set contains 2,874 observations, of which 2,414 are fully paid (`not.fully.paid = 0`) and 460 are unpaid (`not.fully.paid = 1`). The majority class proportion is:
> $$\text{Proportion} = \frac{2414}{2874} \approx 0.8399$$

#### Question 7: Ranking Probability (AUC)
What percentage of the time does the model rank unpaid loans above paid loans in the test set? (Round to 1 decimal place)
- ✅ **`67.9%`** (exact: `0.6787` or `67.87%`)
> **Explanation:** The probability of ranking an unpaid loan above a paid loan is exactly represented by the Area Under the ROC Curve (AUC), which is **0.6787** (or 67.9% when rounded to one decimal place).

#### Question 8: Significance of Interest Rate
The variable `int.rate` is highly significant in the bivariate model, but it is not significant at the 0.05 level in the model trained with all the independent variables. What is the most likely explanation for this difference?
- ✅ **`int.rate is correlated with other risk-related variables, and therefore does not incrementally improve the model when those other variables are included.`**
- These models are trained on a different set of observations, so the coefficients are not comparable.
- This effect is likely due to the training/testing set split we used. In other splits, we could see the opposite effect.
> **Explanation:** Interest rate is strongly negatively correlated with FICO credit score (correlation coefficient of **$-0.718$**). Because FICO and other risk metrics are already present in the full model, `int.rate` becomes redundant and does not explain significant additional variance.

#### Question 9: Bivariate Predicted Probability Threshold
Is the maximum predicted probability of a loan not being paid in full from the bivariate model greater than 0.5?
- ✅ **`No`**
- `Yes`
> **Explanation:** The maximum predicted probability of non-payment output by the bivariate model is **`0.4433`**, which occurs for the maximum interest rate in the test set. Since this is less than 0.5, no loans would be predicted as unpaid at a 0.5 threshold.

#### Question 10: AUC Improvement
How much does adding the additional predictors in the full model improve test set AUC? (Round to 3 decimal places)
- ✅ **`0.062`** (exact: `0.0619`)
> **Explanation:** 
> * Full Model Test AUC: **0.6787**
> * Bivariate Model Test AUC: **0.6169**
> * **Improvement:** $0.6787 - 0.6169 = 0.0618 \approx 0.062$.

---

## Part 2: Predicting Stock Returns with Tree-Based Methods

### Overview
In this assignment, we examine the `StocksCluster.csv` dataset, which contains monthly returns of NASDAQ stocks from 2000 to 2009. The objective is to build and evaluate models to predict whether a stock will have a positive return in December (`PositiveDec = 1`) using the returns from January through November as predictors.

---

### Questions and Solutions

#### Question 1: Subset Size
Suppose the StocksCluster.csv dataset is split evenly into two subsets by rows. How many observations would each subset contain?
- ✅ **`5790`**
> **Explanation:** The total number of rows in the dataset is 11,580. Dividing this by 2 gives exactly 5,790 observations per subset.

#### Question 2: Baseline Probability
Using the dataset, what proportion of observations have December returns greater than 0? (Round to 3 decimal places)
- ✅ **`0.546`** (exact: `0.546114`)
> **Explanation:** The mean of the binary dependent variable `PositiveDec` across the entire dataset is `0.5461`, meaning 54.6% of observations represent positive returns in December.

#### Question 3: Pairwise Correlations
Is the maximum pairwise correlation between monthly returns greater than 0.2?
- ✅ **`No`**
- `Yes`
> **Explanation:** Computing the correlation matrix for the monthly return variables (January through November) reveals that the maximum correlation between any two months is **0.1917** (which is less than 0.2).

#### Question 4: Largest Mean Monthly Return
Which month (from January through November) has the largest mean return across all observations in the dataset?
- ✅ **`April`** (mean return of `0.0263`)
> **Explanation:** Comparing monthly mean returns across the dataset shows that April has the highest average return of **0.0263**, followed by May (**0.0247**).

#### Question 5: May vs. September Return Difference
What is the numerical difference between the mean return in May and the mean return in September? (Round to 3 decimal places)
- ✅ **`0.039`** (exact: `0.039457`)
> **Explanation:** The average return in May is $+0.024737$ and in September is $-0.014721$. The difference is:
> $$\text{Difference} = 0.024737 - (-0.014721) = 0.039458 \approx 0.039$$

#### Question 6: Training Set Accuracy
Is the reported training accuracy of the Logistic Regression Model greater than 0.55?
- ✅ **`Yes`**
- `No`
> **Explanation:** Fitting a multiple logistic regression model on the training set (random state 144) yields a training accuracy of **`0.568`** (56.8%), which is greater than 0.55.

#### Question 7: Test Set vs. Training Set Accuracy
Is the test-set accuracy higher or lower than the training-set accuracy?
- ✅ **`Higher`**
- `Lower`
> **Explanation:** 
> * Training Set Accuracy: **0.5680** (56.8%)
> * Test Set Accuracy: **0.5841** (58.4%)
> 
> The test-set accuracy is higher than the training-set accuracy for this specific train/test split.

#### Question 8: Test Set Majority Class Proportion
What proportion of test observations actually have PositiveDec = 1? (Round to 3 decimal places)
- ✅ **`0.550`** (exact: `0.550086`)
> **Explanation:** The test set baseline rate (representing the proportion of positive returns in December) is **0.550**, which is also the accuracy of a simple baseline model predicting always PositiveDec = 1 on the test set.

#### Question 9: CART Ranking Performance
Does the CART model achieve better ranking performance than random ordering in the test set?
- ✅ **`Yes`**
- `No`
> **Explanation:** The test set AUC for the CART decision tree is **0.5194**. While this is quite low, it is still greater than 0.5 (which is the expected AUC of a completely random ordering).

#### Question 10: First Split Condition Type
Using the CART tree visualization, is the first split based on a numeric threshold or a categorical condition?
- ✅ **`numeric threshold`**
> **Explanation:** Scikit-learn's `DecisionTreeClassifier` only supports numerical splits. Furthermore, all predictor features in the dataset (monthly returns) are continuous numerical variables, so the splits are numeric inequalities (e.g., `ReturnOct <= 0.015`).

#### Question 11: Random Forest Improvement
How much does the Random Forest model improve the test set AUC, as compared to the CART model? (Round to 3 decimal places)
- ✅ **`0.099`** (exact: `0.099136`)
> **Explanation:** 
> * Random Forest Test AUC: **0.6185**
> * CART Test AUC: **0.5194**
> * **Improvement:** $0.6185 - 0.5194 = 0.0991 \approx 0.099$.

#### Question 12: Boosting vs. CART AUC Comparison
Is the Boosting model’s test-set AUC higher or lower than the CART model’s test AUC?
- ✅ **`Higher`**
- `Lower`
> **Explanation:** The Gradient Boosting model's test set AUC is **`0.5836`**, which is higher than the CART model's test set AUC of **`0.5194`**.

import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score

def main():
    print("=== PART 1: PREDICTING LOAN REPAYMENT ===")
    
    # Try multiple paths for cross-platform robustness
    paths = [
        "loans_imputed.csv",
        "Assignment_2/asset-v1_UAI_SOURCE+UAI.1+2T2025+type@asset+block@loans_imputed.csv",
        r"C:\Users\USER\Desktop\MIT assignment\Module_4_Assignment\Assignment_2\asset-v1_UAI_SOURCE+UAI.1+2T2025+type@asset+block@loans_imputed.csv",
        "/home/jmomoh/universal-ai-journey/resources/loans_imputed.csv"
    ]
    
    loans = None
    for path in paths:
        try:
            loans = pd.read_csv(path)
            print(f"Loaded loans data from: {path}")
            break
        except FileNotFoundError:
            continue
            
    if loans is None:
        raise FileNotFoundError("Could not find loans_imputed.csv in any of the search paths.")
        
    # Q1: Fraction of loans not fully paid
    frac_unpaid = loans["not.fully.paid"].mean()
    print(f"Q1: Fraction of loans with not.fully.paid = 1: {frac_unpaid:.6f} (rounded 4 dec: {frac_unpaid:.4f})")

    # Split dataset
    train, test = train_test_split(loans, test_size=0.3, stratify=loans["not.fully.paid"], random_state=144)

    X_train = train.drop(columns=["not.fully.paid"])
    y_train = train["not.fully.paid"]
    X_train_encoded = pd.get_dummies(X_train, columns=['purpose'], drop_first=True, dtype=int)

    # Fit full model
    model_full = sm.Logit(y_train, sm.add_constant(X_train_encoded)).fit()
    print("\nFull Logistic Regression Model Summary:")
    print(model_full.summary())

    # Get exact FICO coefficient
    fico_coef = model_full.params["fico"]
    print(f"\nExact FICO coefficient: {fico_coef:.8f}")

    # Q4: Odds ratio O(A)/O(B) for FICO 300 vs 320
    odds_ratio = np.exp(fico_coef * -20)
    print(f"Q4: Odds ratio O(A)/O(B) for FICO 300 vs 320: {odds_ratio:.6f}")

    # Predictions on test set
    X_test = test.drop(columns=["not.fully.paid"])
    y_test = test["not.fully.paid"]
    X_test_encoded = pd.get_dummies(X_test, columns=['purpose'], drop_first=True, dtype=int)
    test["predicted.risk"] = model_full.predict(sm.add_constant(X_test_encoded))

    # Q5: Misclassified test observations at 0.5 threshold
    conf = confusion_matrix(y_test, test["predicted.risk"] > 0.5)
    misclassified = conf[0, 1] + conf[1, 0]
    print(f"\nQ5: Confusion matrix on test set:\n{conf}")
    print(f"Q5: Misclassified observations: {misclassified}")

    # Q6: Majority class proportion in test set
    majority_prop = (y_test == 0).mean()
    print(f"Q6: Majority class proportion in test: {majority_prop:.6f} (rounded 4 dec: {majority_prop:.4f})")

    # Q7: Test set AUC
    full_auc = roc_auc_score(y_test, test["predicted.risk"])
    print(f"Q7: Test set AUC: {full_auc:.6f}")

    # Q8/Q9: Bivariate model
    mod_biv = sm.Logit(y_train, sm.add_constant(train[["int.rate"]])).fit()
    print("\nBivariate Logistic Regression Model Summary:")
    print(mod_biv.summary())

    pred_biv = mod_biv.predict(sm.add_constant(test[["int.rate"]]))
    max_pred_biv = np.max(pred_biv)
    print(f"Q9: Maximum predicted probability in bivariate model: {max_pred_biv:.6f}")

    # Q10: AUC Improvement
    biv_auc = roc_auc_score(y_test, pred_biv)
    auc_diff = full_auc - biv_auc
    print(f"Bivariate model AUC: {biv_auc:.6f}")
    print(f"Q10: AUC Improvement: {auc_diff:.6f} (rounded 3 dec: {auc_diff:.3f})")


    print("\n=== PART 2: PREDICTING STOCK RETURNS ===")
    
    stock_paths = [
        "StocksCluster.csv",
        "Assignment_2/asset-v1_UAI_SOURCE+UAI.1+2T2025+type@asset+block@StocksCluster.csv",
        r"C:\Users\USER\Desktop\MIT assignment\Module_4_Assignment\Assignment_2\asset-v1_UAI_SOURCE+UAI.1+2T2025+type@asset+block@StocksCluster.csv",
        "/home/jmomoh/universal-ai-journey/resources/StocksCluster.csv"
    ]
    
    stocks = None
    for path in stock_paths:
        try:
            stocks = pd.read_csv(path)
            print(f"Loaded stocks data from: {path}")
            break
        except FileNotFoundError:
            continue
            
    if stocks is None:
        raise FileNotFoundError("Could not find StocksCluster.csv in any of the search paths.")

    # Q1: Half observations
    half_obs = len(stocks) / 2
    print(f"Q1: Number of observations in half subset: {half_obs}")

    # Q2: Proportion of positive Dec returns
    prop_pos_dec = stocks["PositiveDec"].mean()
    print(f"Q2: Proportion with positive Dec returns: {prop_pos_dec:.6f} (rounded 3 dec: {prop_pos_dec:.3f})")

    # Q3: Max pairwise correlation
    corr_matrix = stocks.corr()
    max_corr = corr_matrix[corr_matrix != 1].max().max()
    print(f"Q3: Maximum pairwise correlation between monthly returns: {max_corr:.6f}")

    # Q4: Month with largest mean return
    mean_returns = stocks.mean()
    print("\nMonthly Mean Returns:")
    print(mean_returns)

    # Q5: Difference between May and September mean returns
    diff_may_sep = mean_returns["ReturnMay"] - mean_returns["ReturnSep"]
    print(f"Q5: May return - Sept return: {diff_may_sep:.6f} (rounded 3 dec: {diff_may_sep:.3f})")

    # Split dataset
    X_stock = stocks.drop(columns=["PositiveDec"])
    y_stock = stocks["PositiveDec"]
    X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X_stock, y_stock, test_size=0.3, random_state=144)

    # Logistic Regression
    logit_stocks = sm.Logit(y_train_s, sm.add_constant(X_train_s)).fit()
    train_pred_s = logit_stocks.predict(sm.add_constant(X_train_s)) > 0.5
    train_acc_s = accuracy_score(y_train_s, train_pred_s)
    test_pred_s = logit_stocks.predict(sm.add_constant(X_test_s)) > 0.5
    test_acc_s = accuracy_score(y_test_s, test_pred_s)
    print(f"\nQ6: Training set accuracy: {train_acc_s:.6f}")
    print(f"Q7: Test set accuracy: {test_acc_s:.6f}")

    # Q8: Proportion of test observations with PositiveDec = 1
    prop_test_pos = y_test_s.mean()
    print(f"Q8: Proportion of test set with PositiveDec = 1: {prop_test_pos:.6f} (rounded 3 dec: {prop_test_pos:.3f})")

    # CART Model
    cart = DecisionTreeClassifier(random_state=144)
    cart.fit(X_train_s, y_train_s)
    cart_pred = cart.predict_proba(X_test_s)[:, 1]
    cart_auc = roc_auc_score(y_test_s, cart_pred)
    print(f"\nQ9: CART Test AUC: {cart_auc:.6f}")

    # Random Forest Model
    rf = RandomForestClassifier(n_estimators=1000, min_samples_leaf=10, random_state=144)
    rf.fit(X_train_s, y_train_s)
    rf_pred = rf.predict_proba(X_test_s)[:, 1]
    rf_auc = roc_auc_score(y_test_s, rf_pred)
    print(f"Random Forest Test AUC: {rf_auc:.6f}")
    print(f"Q11: RF AUC - CART AUC: {rf_auc - cart_auc:.6f} (rounded 3 dec: {rf_auc - cart_auc:.3f})")

    # Gradient Boosting Model
    gbm = GradientBoostingClassifier(n_estimators=1000, learning_rate=0.001, max_depth=10, random_state=144)
    gbm.fit(X_train_s, y_train_s)
    gbm_pred = gbm.predict_proba(X_test_s)[:, 1]
    gbm_auc = roc_auc_score(y_test_s, gbm_pred)
    print(f"Q12: Boosting Test AUC: {gbm_auc:.6f} (compared to CART AUC {cart_auc:.6f})")

if __name__ == "__main__":
    main()

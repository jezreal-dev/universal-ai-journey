"""
MIT Universal AI Journey
Module 5: Supervised and Unsupervised Learning
Regression Analysis for U.S. Life Expectancy & Global Climate Change

This script builds multiple linear regression models on:
1. U.S. States dataset (predicting Life Expectancy)
2. Global Climate Change dataset (predicting global temperature anomalies)
It prints statistical summaries and answers specific assignment questions.
"""

import os
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Define possible search paths for datasets
ASSIGNMENT_DIR = r"C:\Users\USER\Desktop\MIT assignment\Module_4_Assignment"
WSL_FALLBACK_DIR = "/mnt/c/Users/USER/Desktop/MIT assignment/Module_4_Assignment"

def find_file(filename):
    """Locates the dataset dynamically across Windows and WSL paths."""
    paths = [
        os.path.join(ASSIGNMENT_DIR, filename),
        os.path.join(WSL_FALLBACK_DIR, filename),
        filename  # local directory fallback
    ]
    for path in paths:
        if os.path.exists(path):
            return path
    raise FileNotFoundError(f"Could not locate {filename} in any standard path.")

def run_us_states_analysis():
    print("\n" + "="*50)
    print("PART 1: U.S. STATES LIFE EXPECTANCY ANALYSIS")
    print("="*50)
    
    # 1. Load Data
    csv_file = "asset-v1_UAI_SOURCE+UAI.1+2T2025+type@asset+block@statedata.csv"
    try:
        path = find_file(csv_file)
        print(f"Loading state dataset from: {path}")
        df = pd.read_csv(path)
    except FileNotFoundError as e:
        print(e)
        return

    # 2. Q2: Median murder rate by region
    print("\n[Q2] Median Murder Rate by Region:")
    region_medians = df.groupby("state.region")["Murder"].median()
    print(region_medians)
    print(f"Highest Median Murder Rate Region: {region_medians.idxmax()} ({region_medians.max()})")

    # 3. Fit Full Regression Model
    # DV: Life.Exp
    # IVs: Population, Income, Illiteracy, Murder, HS.Grad, Frost, Area
    X_vars = ["Population", "Income", "Illiteracy", "Murder", "HS.Grad", "Frost", "Area"]
    X = df[X_vars]
    y = df["Life.Exp"]
    
    X_const = sm.add_constant(X)
    model_full = sm.OLS(y, X_const).fit()
    print("\nFull Model Summary (State Data):")
    print(model_full.summary())
    print(f"[Q4] Murder Coefficient in Full Model: {model_full.params['Murder']:.4f}")

    # 4. Fit Simplified Model (Population, Murder, HS.Grad, Frost)
    X_simp_vars = ["Population", "Murder", "HS.Grad", "Frost"]
    X_simp = df[X_simp_vars]
    X_simp_const = sm.add_constant(X_simp)
    model_simp = sm.OLS(y, X_simp_const).fit()
    
    print("\nSimplified Model Summary (State Data):")
    print(model_simp.summary())
    print(f"Full Model R2: {model_full.rsquared:.4f}")
    print(f"Simplified Model R2: {model_simp.rsquared:.4f}")
    print(f"[Q9] R2 Change (Simplified - Full): {model_simp.rsquared - model_full.rsquared:.6f}")

    # 5. Predictions and residual diagnostics on simplified model
    df["predicted"] = model_simp.predict(X_simp_const)
    df["residual"] = df["Life.Exp"] - df["predicted"]
    df["abs_residual"] = df["residual"].abs()

    # Washington state check
    wash_row = df[df["state.name"] == "Washington"].iloc[0]
    print("\nWashington State Predictions:")
    print(f"  Observed Life Expectancy: {wash_row['Life.Exp']:.2f}")
    print(f"  Predicted Life Expectancy: {wash_row['predicted']:.4f}")
    print(f"  Residual (Observed - Predicted): {wash_row['residual']:.4f}")

    # Outlier / Error check
    min_actual = df.loc[df["Life.Exp"].idxmin()]
    max_actual = df.loc[df["Life.Exp"].idxmax()]
    min_err = df.loc[df["abs_residual"].idxmin()]
    max_err = df.loc[df["abs_residual"].idxmax()]

    print(f"\n[Q11] Lowest Actual Life Expectancy: {min_actual['state.name']} ({min_actual['Life.Exp']} years)")
    print(f"[Q13] Highest Observed Life Expectancy: {max_actual['state.name']} ({max_actual['Life.Exp']} years)")
    print(f"[Q14] Smallest Absolute Prediction Error: {min_err['state.name']} (Error: {min_err['abs_residual']:.4f})")
    print(f"[Q15] Least Accurate Prediction (Largest Absolute Error): {max_err['state.name']} (Error: {max_err['abs_residual']:.4f})")


def run_climate_analysis():
    print("\n" + "="*50)
    print("PART 2: GLOBAL CLIMATE CHANGE ANALYSIS")
    print("="*50)
    
    # 1. Load Data
    csv_file = "asset-v1_UAI_SOURCE+UAI.1+2T2025+type@asset+block@climate_change.csv"
    try:
        path = find_file(csv_file)
        print(f"Loading climate dataset from: {path}")
        df = pd.read_csv(path)
    except FileNotFoundError as e:
        print(e)
        return

    # 2. Split Train/Test sets
    # Train is observations up to and including 2006 (Year <= 2006)
    # Test is remaining observations (Year > 2006)
    train = df[df["Year"] <= 2006]
    test = df[df["Year"] > 2006]
    print(f"Training observations: {len(train)}")
    print(f"Testing observations: {len(test)}")

    # 3. Q4: Correlations with CFC-12 in training data
    corr_vars = ["CO2", "N2O", "CH4", "CFC-11", "CFC-12", "Aerosols", "TSI", "MEI"]
    corr_matrix = train[corr_vars].corr()
    print("\n[Q4] Correlation of training variables with CFC-12:")
    print(corr_matrix["CFC-12"])
    high_corr = corr_matrix.index[(corr_matrix["CFC-12"].abs() > 0.7) & (corr_matrix.index != "CFC-12")].tolist()
    print(f"Variables with absolute correlation > 0.7 with CFC-12: {high_corr}")

    # 4. Fit Full Regression Model on Training Set
    # DV: Temp
    # IVs: MEI, CO2, CH4, N2O, CFC-11, CFC-12, TSI, Aerosols
    X_vars = ["MEI", "CO2", "CH4", "N2O", "CFC-11", "CFC-12", "TSI", "Aerosols"]
    X_train = train[X_vars]
    y_train = train["Temp"]
    
    X_train_const = sm.add_constant(X_train)
    model_full = sm.OLS(y_train, X_train_const).fit()
    print("\nClimate Full Model Summary (Training Data):")
    print(model_full.summary())
    
    # 5. Fit Reduced Regression Model on Training Set
    # DV: Temp
    # IVs: MEI, N2O, TSI, Aerosols
    X_red_vars = ["MEI", "N2O", "TSI", "Aerosols"]
    X_train_red = train[X_red_vars]
    
    X_train_red_const = sm.add_constant(X_train_red)
    model_red = sm.OLS(y_train, X_train_red_const).fit()
    print("\nClimate Reduced Model Summary (Training Data):")
    print(model_red.summary())

    # Count negative coefficients in reduced model (excluding intercept)
    neg_coefs = [var for var in X_red_vars if model_red.params[var] < 0]
    print(f"\n[Q5] Variables in reduced model with negative coefficients: {neg_coefs} (Count: {len(neg_coefs)})")

    # 6. Out-of-sample Testing Diagnostics
    X_test_full = sm.add_constant(test[X_vars])
    X_test_red = sm.add_constant(test[X_red_vars])
    y_test = test["Temp"]
    
    preds_full = model_full.predict(X_test_full)
    preds_red = model_red.predict(X_test_red)
    
    # Compute test set R2 using the training mean as baseline
    train_mean = y_train.mean()
    SST = ((y_test - train_mean) ** 2).sum()
    
    SSE_full = ((y_test - preds_full) ** 2).sum()
    r2_test_full = 1 - (SSE_full / SST)
    
    SSE_red = ((y_test - preds_red) ** 2).sum()
    r2_test_red = 1 - (SSE_red / SST)
    
    diff = abs(r2_test_full - r2_test_red)
    print("\nTest Set Performance (Out-of-Sample):")
    print(f"  Full Model Test R2: {r2_test_full:.5f}")
    print(f"  Reduced Model Test R2: {r2_test_red:.5f}")
    print(f"  [Q6] Difference in Test R2: {diff:.5f}")
    print(f"  Is change > 0.05? {diff > 0.05}")


if __name__ == "__main__":
    run_us_states_analysis()
    run_climate_analysis()

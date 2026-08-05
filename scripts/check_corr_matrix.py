import os
import sys
import pandas as pd
import numpy as np

# Standard paths for the BRFSS dataset
WINDOWS_PATH = r"C:\Users\USER\Desktop\MIT assignment\Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System.csv"
WSL_PATH = "/mnt/c/Users/USER/Desktop/MIT assignment/Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System.csv"

def get_csv_path():
    """Determines the CSV path from arguments or searches default locations."""
    if len(sys.argv) > 1:
        arg_path = sys.argv[1]
        if os.path.exists(arg_path):
            return arg_path
        else:
            print(f"Warning: Specified path '{arg_path}' does not exist. Falling back to default search.")

    for path in [WINDOWS_PATH, WSL_PATH]:
        if os.path.exists(path):
            return path
            
    # Try local folder search
    local_name = "Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System.csv"
    if os.path.exists(local_name):
        return local_name
        
    raise FileNotFoundError(
        "Could not locate the BRFSS CSV file. Please make sure the file exists at:\n"
        f" - Windows: {WINDOWS_PATH}\n"
        f" - WSL: {WSL_PATH}\n"
        "Or pass the path as a command line argument: python check_corr_matrix.py <path_to_csv>"
    )

def main():
    try:
        csv_path = get_csv_path()
        print(f"Loading BRFSS dataset from: {csv_path}")
        brfss = pd.read_csv(csv_path)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Pivot table to group by year, location, and income, aligning questions as columns
    print("Pivoting data to align physical activity and nutrition indicators...")
    pivoted_df = brfss.pivot_table(
        index=["YearEnd", "LocationAbbr", "Income"], 
        columns='Question', 
        values='Data_Value', 
        aggfunc="mean"
    ).reset_index()

    # Mapping of long, descriptive survey questions to short, clean variable names
    rename_map = {
        'Percent of adults aged 18 years and older who have an overweight classification': 'Overweight',
        'Percent of adults aged 18 years and older who have obesity': 'Obesity',
        'Percent of adults who achieve at least 150 minutes a week of moderate-intensity aerobic physical activity or 75 minutes a week of vigorous-intensity aerobic activity (or an equivalent combination)': 'Meets Basic Activity',
        'Percent of adults who achieve at least 150 minutes a week of moderate-intensity aerobic physical activity or 75 minutes a week of vigorous-intensity aerobic physical activity and engage in muscle-strengthening activities on 2 or more days a week': 'Meets Full Guidelines',
        'Percent of adults who achieve at least 300 minutes a week of moderate-intensity aerobic physical activity or 150 minutes a week of vigorous-intensity aerobic activity (or an equivalent combination)': 'High Activity Level',
        'Percent of adults who engage in muscle-strengthening activities on 2 or more days a week': 'Strength Training',
        'Percent of adults who engage in no leisure-time physical activity': 'Inactive',
        'Percent of adults who report consuming fruit less than one time daily': 'Low Fruit Intake',
        'Percent of adults who report consuming vegetables less than one time daily': 'Low Vegetable Intake'
    }

    pivoted_df = pivoted_df.rename(columns=rename_map)

    # Calculate pairwise correlation of numeric features
    print("\nPairwise Correlation Matrix of Key Behavioral Indicators:")
    corr_matrix = pivoted_df.select_dtypes(include='number').corr()
    
    # Format and print correlation matrix
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    print(corr_matrix.round(4))

if __name__ == "__main__":
    main()

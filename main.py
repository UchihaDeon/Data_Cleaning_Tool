"""
Demo Script for Data Cleaning & Preprocessing Tool
Author: Deon
"""
import numpy as np
import pandas as pd
from scipy.stats import zscore

from cleaner import (
    handle_missing_values,
    remove_duplicates,
    detect_outliers_zscore,
    detect_outliers_iqr
)

# Sample dataset
df = pd.read_csv("sample_data.csv")

print("🔹 Original Data:")
print(df)

# Step 1: Handle missing values
df_cleaned = handle_missing_values(df, strategy='mean')
print("\n🔹 After Handling Missing Values (mean):")
print(df_cleaned)

# Step 2: Remove duplicates
df_cleaned = remove_duplicates(df_cleaned)
print("\n🔹 After Removing Duplicates:")
print(df_cleaned)

# Step 3: Remove outliers using Z-score
def detect_outliers_zscore(df, threshold=3):
    numeric_df = df.select_dtypes(include=[np.number])
    if numeric_df.std().min() == 0:
        print("⚠️ Warning: Z-score may be unreliable due to low variance.")
        return df
    z_scores = np.abs(zscore(numeric_df))
    return df[(z_scores < threshold).all(axis=1)]

# Step 4: Remove outliers using IQR
df_iqr = detect_outliers_iqr(df_cleaned)
print("\n🔹 After Removing Outliers (IQR):")
print(df_iqr)
"""
Data Cleaning & Preprocessing Tool
Author: Deon

This module provides functions to clean and preprocess datasets by handling missing values,
removing duplicates, and detecting outliers using Z-score and IQR methods.
"""

import pandas as pd
import numpy as np
from scipy.stats import zscore

def handle_missing_values(df, strategy='mean'):
    """
    Handles missing values in the DataFrame.
    strategy: 'drop', 'mean', 'median', or 'mode'
    """
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'mean':
        return df.fillna(df.mean(numeric_only=True))
    elif strategy == 'median':
        return df.fillna(df.median(numeric_only=True))
    elif strategy == 'mode':
        return df.fillna(df.mode().iloc[0])
    else:
        raise ValueError("Invalid strategy. Choose from 'drop', 'mean', 'median', 'mode'.")

def remove_duplicates(df):
    """
    Removes duplicate rows from the DataFrame.
    """
    return df.drop_duplicates()

def detect_outliers_zscore(df, threshold=3):
    """
    Detects and removes outliers using Z-score method.
    threshold: Z-score threshold (default = 3)
    """
    numeric_df = df.select_dtypes(include=[np.number])
    z_scores = np.abs(zscore(numeric_df))
    return df[(z_scores < threshold).all(axis=1)]

def detect_outliers_iqr(df):
    """
    Detects and removes outliers using IQR method.
    """
    numeric_df = df.select_dtypes(include=[np.number])
    Q1 = numeric_df.quantile(0.25)
    Q3 = numeric_df.quantile(0.75)
    IQR = Q3 - Q1
    mask = ~((numeric_df < (Q1 - 1.5 * IQR)) | (numeric_df > (Q3 + 1.5 * IQR))).any(axis=1)
    return df[mask]
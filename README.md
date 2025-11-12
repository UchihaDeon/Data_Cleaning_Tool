# Data Cleaning & Preprocessing Tool

A modular Python tool for automating essential data cleaning tasks — designed for analysts and data scientists working with real-world datasets.

## 🔍 Overview

Real-world data often contains missing values, duplicates, and outliers that can distort analysis and model performance. This tool streamlines the preprocessing workflow using robust statistical techniques and efficient Pandas operations.

## ⚙️ Features

- **Missing Value Handling**  
  Drop or impute missing values using mean, median, or mode strategies.

- **Duplicate Removal**  
  Automatically detects and removes duplicate rows.

- **Outlier Detection**  
  Supports Z-score and IQR-based outlier removal for numeric columns.

## 📦 Libraries Used

- `pandas` — data manipulation  
- `numpy` — numerical operations  
- `scipy` — Z-score calculation

## 🚀 Installation

```bash
pip install pandas numpy scipy

🧪 Usage Example
from cleaner import (
    handle_missing_values,
    remove_duplicates,
    detect_outliers_zscore,
    detect_outliers_iqr
)

# Load your dataset
import pandas as pd
df = pd.read_csv("your_data.csv")

# Clean your data
df = handle_missing_values(df, strategy='mean')
df = remove_duplicates(df)
df = detect_outliers_iqr(df)


📁 Sample Output
🔹 Original Data:
     Age   Salary
0   25.0  50000.0
1   30.0      NaN
...

🔹 After Handling Missing Values (mean):
     Age   Salary
0   25.0  50000.0
1   30.0  50000.0
...

🔹 After Removing Outliers (IQR):
    Age   Salary
0  25.0  50000.0
1  30.0  50000.0
...


📄 License
This project is licensed under the MIT License. Feel free to use and modify it for personal or professional use.
Author: Deon
BCA Undergraduate | Data Science Intern
GitHub: Deon Jose
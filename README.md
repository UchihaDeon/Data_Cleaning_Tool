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
- **Modular design with reusable functions in cleaner.py**
- **Sample dataset included for testing**
- **Command-line and GUI interfaces available**


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
```
## 🖥️ Streamlit GUI
This project includes a user-friendly Streamlit interface that allows users to interact with the tool without writing code.
🔹 GUI Features
- CSV Upload: Upload any tabular dataset
- Missing Value Handling: Choose from drop, mean, median, or mode
- Duplicate Removal: Optional checkbox to remove repeated rows
- Outlier Detection: Select between Z-score, IQR, or skip
- Live Data Preview: View the dataset after each cleaning step
- Row Count Logs: See how many rows were affected
- Download Cleaned Data: Export the final dataset as a CSV file
```bash
▶️ Run the GUI
streamlit run app.py



▶️ Run the CLI Demo
python main.py


```
**📊 Sample Dataset**

A sample dataset (sample_data.csv) is included to demonstrate the tool’s capabilities. It contains:
- Missing values
- Duplicate rows
- Outliers (e.g., age = 120)
This dataset allows users to test all core features of the tool.

**📥 Download Option**

After cleaning, users can download the processed dataset directly from the Streamlit interface using the Download Cleaned Data button.


## 📄 License

This project is licensed under the MIT License. Feel free to use and modify it for personal or professional use.
Author: Deon
BCA Undergraduate | Data Science Intern
GitHub: Deon Jose
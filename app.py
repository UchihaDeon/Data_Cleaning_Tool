import streamlit as st
import pandas as pd
import io
from cleaner import (
    handle_missing_values,
    remove_duplicates,
    detect_outliers_zscore,
    detect_outliers_iqr
)

st.title("🧼 Data Cleaning & Preprocessing Tool")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("🔹 Original Data")
    st.dataframe(df)

    strategy = st.selectbox("Missing Value Strategy", ["drop", "mean", "median", "mode"])
    df = handle_missing_values(df, strategy)
    st.subheader("🔹 After Handling Missing Values")
    st.dataframe(df)

    if st.checkbox("Remove Duplicates"):
        st.write(f"Rows before duplicate removal: {len(df)}")
        df = remove_duplicates(df)
        st.write(f"Rows after duplicate removal: {len(df)}")
        st.subheader("🔹 After Removing Duplicates")
        st.dataframe(df)

    outlier_method = st.radio("Outlier Detection Method", ["None", "Z-score", "IQR"])
    if outlier_method == "Z-score":
        df = detect_outliers_zscore(df)
        st.subheader("🔹 After Removing Outliers (Z-score)")
        st.dataframe(df)
    elif outlier_method == "IQR":
        df = detect_outliers_iqr(df)
        st.subheader("🔹 After Removing Outliers (IQR)")
        st.dataframe(df)

    st.success("✅ Cleaning Complete!")



    # Convert cleaned DataFrame to CSV
    csv = df.to_csv(index=False)
    b = io.BytesIO()
    b.write(csv.encode())
    b.seek(0)

    # Streamlit download button
    st.download_button(
        label="📥 Download Cleaned Data as CSV",
        data=b,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )
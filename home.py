import streamlit as st

st.set_page_config(
    page_title="StockVision",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📈 StockVision")
st.subheader("AI-Powered Stock Market Anomaly Detection")

st.markdown(
    """
Welcome to **StockVision**, an interactive platform for detecting abnormal stock market behavior using statistical methods and machine learning.

### Features

- 📊 Asset Explorer
- 📈 Technical Indicators
- 🤖 Anomaly Detection
- 📌 Model Comparison
- 🔍 Root Cause Analysis
- 📄 Report Generator

👈 Select a page from the sidebar to get started.
"""
)
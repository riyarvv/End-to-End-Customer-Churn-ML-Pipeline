import streamlit as st

def about_page():

    st.title("About the Model")

    st.markdown("""
    ## Model

    Logistic Regression

    ## Dataset

    IBM Telco Customer Churn

    ## Features

    • Customer demographics

    • Services

    • Billing

    • Contract

    • Usage

    ## Performance

    Accuracy: 79%

    ROC-AUC: 0.83
    """)
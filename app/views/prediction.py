from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

import joblib

model = joblib.load(
    BASE_DIR /
    "models" /
    "logistic_regression.pkl"
)

import streamlit as st
import pandas as pd

from src.feature_engineering import engineer_features

def prediction_page():
    st.header("Customer Information")

    col1, col2 = st.columns(2)

    with col1:
        gender=st.selectbox(
            "Gender",
            ["Male","Female"]
        )

        partner=st.selectbox(
            "Partner",
            ["Yes","No"]
        )

    with col2:

        senior = st.selectbox(
            "Senior Citizen",
            [0,1]
        )

        dependents = st.selectbox(
            "Dependents",
            ["Yes","No"]
        )

    st.header("Account Information")

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=100,
        value=12
    )

    monthly = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0,
    step=1.0,
    format="%.2f"
    )

    total = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=2200.0,
    step=1.0,
    format="%.2f"
    )

    st.header("Services")

    col1, col2 = st.columns(2)

    with col1:
        internet_service=st.selectbox(
            "Internet Service",
            ["Fiber optic","DSL","No"]
        )

        online_security=st.selectbox(
            "Online Security",
            ["Yes","No","No internet service"]
        )

        online_backup=st.selectbox(
            "Online Backup",
            ["Yes","No","No internet service"]
        )

        device_protection=st.selectbox(
            "Device Protection",
            ["Yes","No","No internet service"]
        )

        tech_support=st.selectbox(
            "Tech Support",
            ["Yes","No","No internet service"]
        )


    with col2:

        streaming_tv=st.selectbox(
            "Streaming TV",
            ["Yes","No","No internet service"]
        )

        streaming_movies=st.selectbox(
            "Streaming Movies",
            ["Yes","No","No internet service"]
        )

        phone_service=st.selectbox(
            "Phone Service",
            ["Yes","No"]
        )

        multiple_lines=st.selectbox(
            "Multiple Lines",
            ["Yes","No","No phone service"]
        )


    st.header("Billing")

    contract=st.selectbox(
        "Contract",
        ["Month-to-month","One year","Two year"]
    )

    paperless_billing=st.selectbox(
        "Paperless Billing",
        ["Yes","No"]
    )

    payment_method=st.selectbox(
        "Payment Method",
        ["Electronic check","Mailed check","Bank transfer (automatic)","Credit card (automatic)"]
    )

    input_df = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [senior],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "PhoneService": [phone_service],
        "MultipleLines": [multiple_lines],
        "InternetService": [internet_service],
        "OnlineSecurity": [online_security],
        "OnlineBackup": [online_backup],
        "DeviceProtection": [device_protection],
        "TechSupport": [tech_support],
        "StreamingTV": [streaming_tv],
        "StreamingMovies": [streaming_movies],
        "Contract": [contract],
        "PaperlessBilling": [paperless_billing],
        "PaymentMethod": [payment_method],
        "MonthlyCharges": [monthly],
        "TotalCharges": [total]
    })

    input_df = engineer_features(input_df)

    if st.button("Predict Churn"):

        prediction = model.predict(input_df)[0]

        probability = model.predict_proba(input_df)[0]

        st.subheader("Prediction")

        if prediction == "Yes":
            st.error("⚠️ Customer is likely to churn.")
        else:
            st.success("✅ Customer is likely to stay.")

        churn_probability = probability[1] * 100

        st.metric(
            "Churn Probability",
            f"{churn_probability:.2f}%"
        )

        st.progress(churn_probability / 100)

        from utils.ui_helpers import show_risk_level

        show_risk_level(churn_probability)

        if prediction == "Yes":

            st.warning("""
    Suggested Actions

    • Offer long-term contract discounts

    • Contact customer support team

    • Offer loyalty benefits
    """)

        else:

            st.info("""
    Customer appears loyal.

    Continue providing good service.
    """)
        with st.expander("Customer Summary"):
            st.dataframe(input_df)

        result = pd.DataFrame({
            "Prediction":[prediction],
            "Probability":[churn_probability]
        })

        csv = result.to_csv(index=False)

        st.download_button(
            label="📥 Download Prediction",
            data=csv,
            file_name="prediction.csv",
            mime="text/csv"
        )
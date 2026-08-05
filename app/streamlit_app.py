import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

import streamlit as st
import pandas as pd
import joblib

from src.feature_engineering import (
    create_new_customer_feature,
    create_tenure_group,
    create_monthlyCharge_classifier
)

st.set_page_config(
  page_title="Customer Churn Predictor",
  page_icon="📊",
  layout="wide"
)

st.title("📊 Customer Churn Prediction")

st.markdown("""
Predict whether a telecom customer is likely to churn using a Machine Learning model.
""")

st.sidebar.title("About")

st.sidebar.write("""
Model:
Logistic Regression

Dataset:
IBM Telco Customer Churn

Built by:
Riya
""")

st.sidebar.title("📊 Customer Churn Predictor")

page = st.sidebar.radio(
    "Navigation",
    [
        "Prediction",
        "About Model",
        "Business Insights"
    ]
)

if page == "Prediction":

    # Put ALL your existing prediction code here
    model_path = BASE_DIR / "models" / "logistic_regression.pkl"

model = joblib.load(model_path)

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
    value=70.0
)

total = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=2200.0
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

input_df = create_new_customer_feature(input_df)

input_df = create_tenure_group(input_df)

input_df = create_monthlyCharge_classifier(input_df)


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

    if churn_probability < 30:
      st.success("🟢 Low Risk")

    elif churn_probability < 70:
      st.warning("🟡 Medium Risk")

    else:
      st.error("🔴 High Risk")

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

elif page == "About Model":

    st.title("About the Model")

    st.write("""
    Model Used:
    Logistic Regression

    Dataset:
    IBM Telco Customer Churn

    Accuracy:
    81%

    ROC-AUC:
    0.84
    """)

elif page == "Business Insights":

    st.title("Business Insights")

    st.write("""
    Key findings:

    • Month-to-month contracts have higher churn.

    • Electronic check customers churn more.

    • Long-tenure customers rarely churn.

    • Two-year contracts significantly reduce churn.
    """)

st.sidebar.markdown("## Model Performance")

st.sidebar.metric(
    "Accuracy",
    "79.25%"
)

st.sidebar.metric(
    "ROC-AUC",
    "0.83"
)


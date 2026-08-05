import streamlit as st
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from pages.prediction import prediction_page
from pages.about import about_page
from pages.business_insights import business_insights_page

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide"
)

st.sidebar.title("📊 Customer Churn Predictor")

st.sidebar.metric(
    "Accuracy",
    "79.25%"
)

st.sidebar.metric(
    "ROC-AUC",
    "0.83"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Prediction",
        "About Model",
        "Business Insights"
    ]
)

if page=="Prediction":
    prediction_page()

elif page=="About Model":
    about_page()

elif page=="Business Insights":
    business_insights_page()
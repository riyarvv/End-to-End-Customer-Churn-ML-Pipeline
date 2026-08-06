import streamlit as st
import sys
from pathlib import Path

# ---------------------------------------------------
# Project Path
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# ---------------------------------------------------
# Import Pages
# ---------------------------------------------------

from views.prediction import prediction_page
from views.about import about_page
from views.business_insights import business_insights_page

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.title("📊 Customer Churn Predictor")

st.sidebar.success("✅ Model Loaded")

st.sidebar.metric(
    "Accuracy",
    "79.25%"
)

st.sidebar.metric(
    "ROC-AUC",
    "0.83"
)

st.sidebar.metric(
    "Algorithm",
    "Logistic Regression"
)

st.sidebar.metric(
    "Features",
    "22"
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "Prediction",
        "About Model",
        "Business Insights"
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "Built using\n\n"
    "- Python\n"
    "- Scikit-Learn\n"
    "- Streamlit\n"
    "- Pandas"
)

# ---------------------------------------------------
# Routing
# ---------------------------------------------------

if page == "Prediction":
    prediction_page()

elif page == "About Model":
    about_page()

elif page == "Business Insights":
    business_insights_page()
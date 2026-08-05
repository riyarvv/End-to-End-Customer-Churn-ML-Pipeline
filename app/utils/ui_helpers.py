import streamlit as st

def show_risk_level(probability):

    if probability < 30:

        st.success("🟢 Low Risk")

    elif probability < 70:

        st.warning("🟡 Medium Risk")

    else:

        st.error("🔴 High Risk")
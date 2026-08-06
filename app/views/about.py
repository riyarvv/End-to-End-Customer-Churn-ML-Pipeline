import streamlit as st


def about_page():

    st.title("🤖 About the Model")

    st.markdown("---")

    st.subheader("Dataset")

    st.write("""
IBM Telco Customer Churn Dataset

• 7,043 telecom customers

• Binary Classification

• Predict whether a customer will churn.
""")

    st.subheader("Machine Learning Algorithm")

    st.success("Logistic Regression")

    st.write("""
Why Logistic Regression?

• Fast

• Interpretable

• Excellent baseline model

• Produces probabilities instead of only Yes/No predictions.
""")

    st.subheader("Model Performance")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Accuracy", "79.25%")

    with col2:
        st.metric("ROC-AUC", "0.83")

    st.markdown("---")

    st.info("""
This model can help businesses identify customers who are likely to leave so they can take preventive action.
""")
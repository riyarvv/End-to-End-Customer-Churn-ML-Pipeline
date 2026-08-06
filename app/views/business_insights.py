import streamlit as st


def business_insights_page():

    st.title("📈 Business Insights")

    st.markdown("---")

    with st.expander("📉 Contract Type"):

        st.write("""
Customers with **Month-to-month contracts** churn much more frequently.

Recommendation:
Offer discounts for yearly plans.
""")

    with st.expander("💳 Payment Method"):

        st.write("""
Customers paying through **Electronic Check** have the highest churn rate.

Recommendation:
Encourage AutoPay or Credit Card payments.
""")

    with st.expander("📡 Internet Service"):

        st.write("""
Fiber Optic users show higher churn than DSL customers.

Recommendation:
Investigate customer satisfaction among Fiber users.
""")

    with st.expander("📅 Customer Tenure"):

        st.write("""
Customers with low tenure are significantly more likely to churn.

Recommendation:
Improve onboarding and first-year customer engagement.
""")

    with st.expander("💰 Monthly Charges"):

        st.write("""
Higher monthly charges are associated with higher churn.

Recommendation:
Provide loyalty discounts or bundled service plans.
""")
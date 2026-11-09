import streamlit as st
from src.predict import predict_churn

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Customer Churn Prediction")
st.write("Enter customer details to estimate the likelihood of churn.")

st.subheader("Customer Information")

gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Has Partner?", ["Yes", "No"])
dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
phone = st.selectbox("Phone Service", ["Yes", "No"])
internet = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)
contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)
payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)
monthly = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)
total = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=840.0
)

if st.button("Predict Churn"):
    customer = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "InternetService": internet,
        "Contract": contract,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    try:
        result = predict_churn(customer)

        st.metric(
            "Churn Probability",
            f"{result['probability']:.1%}"
        )

        if result["prediction"] == 1:
            st.error("⚠️ Customer is likely to churn.")
        else:
            st.success("✅ Customer is likely to stay.")

        st.caption(
            "This is a model estimate, not a certainty."
        )

    except FileNotFoundError as error:
        st.error(str(error))
    except Exception as error:
        st.error(f"Prediction failed: {error}")

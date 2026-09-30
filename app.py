import streamlit as st
import pandas as pd
import joblib


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Mobile Financial Fraud Detection",
    page_icon="📱",
    layout="wide"
)


# --------------------------------------------------
# Load Trained Model
# --------------------------------------------------
@st.cache_resource
def load_model():
    return joblib.load("best_model.pkl")


model = load_model()


# --------------------------------------------------
# App Title
# --------------------------------------------------
st.title("📱💸 Fraud Detection in Mobile Financial Transactions")
st.write(
    "Enter the transaction details below to predict whether "
    "the transaction is fraudulent or legitimate."
)
st.divider()


# --------------------------------------------------
# Input Section
# --------------------------------------------------
st.subheader("Transaction Details")

col1, col2 = st.columns(2)

with col1:
    step = st.number_input(
        "Transaction Step",
        min_value=1,
        value=1,
        step=1
    )

    transaction_type = st.selectbox(
        "Transaction Type",
        ["TRANSFER", "CASH_OUT", "PAYMENT", "CASH_IN", "DEBIT"]
    )

    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )

    old_balance_org = st.number_input(
        "Old Balance (Origin)",
        min_value=0.0,
        value=5000.0,
        step=100.0
    )

with col2:
    new_balance_org = st.number_input(
        "New Balance (Origin)",
        min_value=0.0,
        value=4000.0,
        step=100.0
    )

    old_balance_dest = st.number_input(
        "Old Balance (Destination)",
        min_value=0.0,
        value=0.0,
        step=100.0
    )

    new_balance_dest = st.number_input(
        "New Balance (Destination)",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )

st.divider()


# --------------------------------------------------
# Feature Engineering
# --------------------------------------------------
is_all_funds_withdrawn = int(old_balance_org == amount)
is_dest_empty_before = int(old_balance_dest == 0)
amount_to_balance_ratio = amount / (old_balance_org + 1)


# --------------------------------------------------
# Create Input DataFrame
# --------------------------------------------------
input_data = pd.DataFrame({
    "step": [step],
    "type": [transaction_type],
    "amount": [amount],
    "oldbalanceOrg": [old_balance_org],
    "newbalanceOrig": [new_balance_org],
    "oldbalanceDest": [old_balance_dest],
    "newbalanceDest": [new_balance_dest],
    "is_all_funds_withdrawn": [is_all_funds_withdrawn],
    "is_dest_empty_before": [is_dest_empty_before],
    "amount_to_balance_ratio": [amount_to_balance_ratio]
})


# --------------------------------------------------
# Prediction Button & Output
# --------------------------------------------------
if st.button("🔍 Detect Fraud", use_container_width=True):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]
    classes = model.classes_

    class_probabilities = dict(zip(classes, probability))
    legitimate_probability = class_probabilities.get(0, 0) * 100
    fraud_probability = class_probabilities.get(1, 0) * 100

    st.divider()
    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ FRAUDULENT TRANSACTION DETECTED")
        st.metric("Fraud Probability", f"{fraud_probability:.2f}%")
        st.warning("This transaction has characteristics associated with fraudulent activity.")
    else:
        st.success("✅ LEGITIMATE TRANSACTION")
        st.metric("Legitimate Probability", f"{legitimate_probability:.2f}%")

    st.subheader("Prediction Probability")
    prob_col1, prob_col2 = st.columns(2)
    with prob_col1:
        st.metric("Legitimate Probability", f"{legitimate_probability:.2f}%")
    with prob_col2:
        st.metric("Fraud Probability", f"{fraud_probability:.2f}%")

    # --------------------------------------------------
    # Transaction Summary (Inside button click so it displays with results)
    # --------------------------------------------------
    st.divider()
    st.subheader("Transaction Summary")

    summary_col1, summary_col2 = st.columns(2)

    with summary_col1:
        st.write(f"**Transaction Type:** {transaction_type}")
        st.write(f"**Transaction Amount:** ₹{amount:,.2f}")
        st.write(f"**Origin Balance Before:** ₹{old_balance_org:,.2f}")
        st.write(f"**Origin Balance After:** ₹{new_balance_org:,.2f}")

    with summary_col2:
        st.write(f"**Destination Balance Before:** ₹{old_balance_dest:,.2f}")
        st.write(f"**Destination Balance After:** ₹{new_balance_dest:,.2f}")
        st.write(f"**Amount / Balance Ratio:** {amount_to_balance_ratio:.2f}")
        st.write(f"**All Funds Withdrawn:** {'Yes' if is_all_funds_withdrawn else 'No'}")
        st.write(f"**Destination Empty Before:** {'Yes' if is_dest_empty_before else 'No'}")
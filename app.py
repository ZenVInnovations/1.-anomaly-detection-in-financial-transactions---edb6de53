
import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest

# --- Anomaly detection function ---
def detect_anomalies(data):
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(data)
    data['anomaly'] = model.predict(data)
    return data

# --- Sample dummy data ---
def load_sample_data():
    return pd.DataFrame({
        'amount': [100, 5000, 90000, 300, 100000],
        'transaction_type': [0, 1, 0, 1, 0],
        'account_age': [2.0, 5.0, 0.3, 4.5, 0.1]
    })

# --- Streamlit App UI ---
st.title("Anomaly Detection in Financial Transactions")

st.write("This app uses Machine Learning to detect unusual financial transactions.")

if st.button("Run Anomaly Detection on Sample Data"):
    df = load_sample_data()
    st.write("Sample Input Data:")
    st.dataframe(df)

    result = detect_anomalies(df)

    st.write("Anomaly Detection Result:")
    st.dataframe(result)

    st.markdown("**Note:** `-1` = Anomaly, `1` = Normal")
else:
    st.info("Click the button to analyze dummy financial data.")

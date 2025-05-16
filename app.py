import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Financial Transactions Anomaly Detection")

# Load data
df = pd.read_csv('labeled_transactions.csv')

# Show data overview
st.subheader("Transaction Data Preview")
st.dataframe(df.head())

# Show anomaly counts
st.subheader("Anomaly Summary")
counts = df['AnomalyLabel'].value_counts()
st.write(counts)

# Plot anomaly counts
fig, ax = plt.subplots()
counts.plot(kind='bar', ax=ax)
ax.set_xticklabels(['Normal', 'Anomalous'], rotation=0)
st.pyplot(fig)

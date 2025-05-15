import pandas as pd
from sklearn.ensemble import IsolationForest

# Step 1: Load the data
df = pd.read_csv('transactions.csv')

# Step 2: Handle missing values
df.dropna(inplace=True)

# Step 3: Convert 'Time' column to datetime format
df['Time'] = pd.to_datetime(df['Time'])

# Step 4: Encode categorical columns using one-hot encoding
df_encoded = pd.get_dummies(df, columns=['Type', 'Location', 'MerchantCategory'])

# Step 5: Select features for model training (drop identifiers and datetime)
X = df_encoded.drop(columns=['TransactionID', 'Time'])

# Step 6: Train Isolation Forest model
model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
df_encoded['anomaly'] = model.fit_predict(X)

# Step 7: Convert model output to readable labels
df_encoded['anomaly'] = df_encoded['anomaly'].map({1: 'Normal', -1: 'Anomalous'})

# Step 8: Attach anomaly labels to original dataframe
df_result = df.copy()
df_result['AnomalyLabel'] = df_encoded['anomaly']

# Step 9: Save result to new CSV
df_result.to_csv('labeled_transactions.csv', index=False)

print("Preprocessing and anomaly detection completed.")
print("Results saved to 'labeled_transactions.csv'")
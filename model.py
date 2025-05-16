from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    """
    Detect anomalies in financial transactions.
    Adds a new column 'anomaly' to the dataset.
    """
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(data)
    data['anomaly'] = model.predict(data)
    return data

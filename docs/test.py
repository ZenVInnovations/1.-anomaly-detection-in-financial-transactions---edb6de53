import pandas as pd
from model import detect_anomalies

# Sample test data
test_data = pd.DataFrame({
    'amount': [100, 5000, 90000],
    'transaction_type': [0, 1, 0],
    'account_age': [2.0, 5.0, 0.3]
})

# Detect anomalies
result = detect_anomalies(test_data)

# Show result
print(result)

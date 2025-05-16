
import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess(file_path):
    df = pd.read_csv(file_path)
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[['amount', 'time']])
    return df, scaled, scaler

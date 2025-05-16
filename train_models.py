
import numpy as np
from sklearn.ensemble import IsolationForest
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from utils import load_and_preprocess

df, scaled_data, _ = load_and_preprocess('data/sample_transactions.csv')

iso_model = IsolationForest(n_estimators=100, contamination=0.01)
df['anomaly_iforest'] = iso_model.fit_predict(scaled_data)

autoencoder = Sequential([
    Dense(8, activation='relu', input_shape=(scaled_data.shape[1],)),
    Dense(4, activation='relu'),
    Dense(8, activation='relu'),
    Dense(scaled_data.shape[1], activation='linear')
])

autoencoder.compile(optimizer='adam', loss='mse')
autoencoder.fit(scaled_data, scaled_data, epochs=20, batch_size=32, verbose=1)
autoencoder.save('models/autoencoder_model.h5')

recon = autoencoder.predict(scaled_data)
mse = np.mean(np.power(scaled_data - recon, 2), axis=1)
df['reconstruction_error'] = mse
df['anomaly_autoencoder'] = (mse > np.percentile(mse, 95)).astype(int)

df.to_csv('data/processed_with_anomalies.csv', index=False)
print("Training complete and saved to CSV.")

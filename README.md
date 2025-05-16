# 💸 Anomaly Detection in Financial Transactions

This project applies AI-driven anomaly detection techniques to identify unusual patterns in financial transaction data. It uses machine learning models such as Isolation Forest to flag potential fraudulent activities or errors, ensuring data integrity and security.

---

## 🚀 Project Overview

- 📊 **Goal**: Detect anomalies or suspicious behavior in financial datasets.
- 🤖 **ML Models Used**: Isolation Forest (can be extended to Autoencoders).
- 🎯 **Use Case**: Useful for banks, financial institutions, and auditors.

---

## 🧰 Tech Stack

| Category       | Tools / Libraries                             |
|----------------|-----------------------------------------------|
| Programming    | Python 3.x                                    |
| Libraries      | Pandas, NumPy, Scikit-learn, Streamlit        |
| Visualization  | Streamlit                                     |
| Deployment     | Streamlit Cloud                               |

---

## 📁 Folder Structure
```
anomaly-detection-financial-transactions/
│
├── app.py # Main Streamlit application
├── transactions.csv # Sample financial transaction dataset
├── requirements.txt # Python dependencies
├── test_model.py # Test script to validate anomaly detection
├── drawio-flowchart.png # Flowchart of project pipeline
├── README.md # Project documentation
```
---

## ⚙️ How It Works

1. 📥 **Load transaction data** (CSV format).
2. 🧹 **Preprocess data**: handle missing values, select features.
3. 🌲 **Apply Isolation Forest** to detect anomalies.
4. 🔍 **Label transactions** as normal or anomalous.
5. 📊 **Visualize results** in a Streamlit app.

🛠️ Installation & Usage
🔧 Setup Instructions (Locally)
 1. Clone this repository
    git clone https://github.com/Anushaa244/1.-anomaly-detection-in-financial-transactions---edb6de53
    cd anomaly-detection-financial-transactions
2.Install required libraries
   pip install -r requirements.txt
3. Run Streamlit app
   streamlit run app.py

---

☁️ Deploy on Streamlit Cloud
1.Push this repository to GitHub.

2.Go to: https://streamlit.io/cloud

3.Sign in → Deploy a new app → Connect your GitHub repo.

4.Select app.py as the entry point.

5.Done! we receive a live URL.
https://1-anomaly-detection-in-financial-transactions---edb6de53-cqmao.streamlit.app/

📌 Future Improvements
 * Add deep learning model: Autoencoder

 * Include time-based anomaly tracking

 * Improve UI with more charts & filters

 * Add database support (e.g., MongoDB, PostgreSQL)

## Contributors

- Anusha SA  





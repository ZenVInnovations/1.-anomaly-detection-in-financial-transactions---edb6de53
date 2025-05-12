# 💳 Anomaly Detection in Financial Transactions

This project implements an AI-based system to detect anomalous or fraudulent transactions in financial data using **Isolation Forest** and **Autoencoders**. It includes a full ML pipeline: preprocessing, training, evaluation, visualization, and deployment via **Streamlit Cloud**.

---

## 📌 Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Flowchart](#flowchart)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Folder Structure](#folder-structure)
- [Contributors](#contributors)

---

## ✅ Overview

The goal of this project is to build a robust anomaly detection system for financial transactions, capable of:
- Detecting fraud or data errors in transaction records.
- Using both classical (Isolation Forest) and deep learning (Autoencoder) models.
- Visualizing results in a user-friendly dashboard.

---

## 🧰 Tech Stack

| Technology        | Purpose                         |
|-------------------|----------------------------------|
| Python            | Programming Language             |
| Pandas, Numpy     | Data Manipulation                |
| Scikit-learn      | Machine Learning (Isolation Forest) |
| TensorFlow/Keras  | Deep Learning (Autoencoder)      |
| Matplotlib, Seaborn | Visualization                  |
| Streamlit         | App UI and Deployment            |

---

## 🧠 Architecture
Data (CSV/API)
↓
Preprocessing (scaling, filtering)
↓
Model Training (IF / Autoencoder)
↓
Anomaly Detection
↓
Visualization & Report (Streamlit UI)
↓
Deployment (Streamlit Cloud)


---

## 🗺️ Flowchart

![Flowchart](flowchart.png)

---

## 🌐 Demo

▶️ Live App: [https://your-streamlit-app-link](https://your-streamlit-app-link)  
📂 GitHub Repo: [https://github.com/your-username/anomaly-detection](https://github.com/your-username/anomaly-detection)

---

## 🛠️ Installation

```bash
git clone https://github.com/your-username/anomaly-detection
cd anomaly-detection-financial-transactions
pip install -r requirements.txt
---

### 🚀Usage
streamlit run app/app.py

# 🛡️**Fraud Detection in Mobile Financial Transactions**
---

## 🚀**Project Overview**
---
This project focuses on detecting fraudulent mobile financial transactions using machine learning. The main goal is to develop a robust machine learning model that can accurately identify whether a transaction is legitimate or fraudulent in real time.

The project follows a complete Data Science workflow:
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Model Training & Evaluation
- Saving the Best Model
- Deployment using Streamlit
---
## 🌐**Live app**
---
👉https://detectfraud3.streamlit.app/

---
## 📂**Project Structure**
---
```text
fraud_detection_analysis/
│
├── Data/
│   ├── Fraud_Analysis_Dataset.csv
│   ├── Fraud_Analysis_Cleaned_Dataset.csv
│ 
├── notebook/
│   ├── basic_data_preprocessing.ipynb
│   ├── EDA.ipynb
│
├── src/
│   ├── model_building.ipynb
|      
├── .venv/
├──  best_model.pkl
├── app.py
├── requirement.txt
└── 
```
---
## ⚙️**Tech Stack**
---
- 🐍 Python : Programming Language
- 🐼 Pandas, 🔢NumPy : Data Manipulation & Analysis
- 📊 Matplotlib, 📈Seaborn : Data Visualization
- 🤖 Scikit-learn, 🌳XGBoost : Machine Learning
- 📦 Joblib : Model Saving & Loading
- 🚀 Streamlit : Deployment
---
## 🧠**Machine Learning Workflow**
---
### 1. 📥Data Collection
  - Fraud_Analysis_Dataset.csv
### 2. 🧹Data Cleaning & Preprocessing
  - Check Shape and size of the data 
  - Detect duplicate rows and remove them
  - Check null values
  - Saved cleaned data
### 3. 📊 Exploratory Data Analysis (EDA)
  - Analyzed the distribution of fraudulent and legitimate transactions.
  - Studied different transaction types.
  - Analyzed transaction amounts and other important numerical features.
  - Identified patterns and relationships in the dataset.
### 4. ⚙️Model Training & Evaluation
  - Preprocessing (Feature Scaling, Feature Engineering, Encoding categorical variables) using Pipeline.
  - Train multiple models.
  - Compared model performance using different evaluation metrics.
  - Best model selected and saved (best_model.pkl) using joblib
### 5. 🚀Deployment
  - Streamlit app for real-time prediction
---
## ▶️**How to Run Locally**
---
### 1. 📥Clone the repository
  - git clone <your-repo-link>
  - cd fraud_detection_analysis
### 2. 🐍Create virtual environment
  - python -m venv venv
### 3. ▶️ Activate the Virtual Environment
  #### Windows
  - venv\Scripts\activate   
### 3. 📦Install dependencies
  - pip install -r requirements.txt
### 4. 🚀Run the app
  - streamlit run app.py
---
## 📌**Features**
---
- 👤User-friendly UI
- ⚡Real-time fraud detection
- 📝Supports multiple transaction input features
- 🔄 Scalable preprocessing and ML pipeline
- 📊 Displays prediction results and probability
---
## ⚠️**Note**
---
- Please make sure all required dependencies are installed before running the project locally.
- Please update the data path accordingly if running locally.
---
## 📈**Future Improvements**
---
- 📱 Develop a mobile-friendly version of the application
- 🔄 Add real-time transaction monitoring
- 📊 Add more interactive analytics and dashboards
- 🧠 Experiment with more advanced machine learning and deep learning models
- 🚨 Add an alert system for high-risk transactions
- ☁️ Deploy the model using a scalable cloud platform
- 🔐 Improve security and data privacy


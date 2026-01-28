# 🏦 Loan Prediction Web Application

🔗 **Live Demo:** https://loan-prediction-t391.onrender.com  

---

# 🏦 Loan Prediction Web Application

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![Deployment](https://img.shields.io/badge/Live-Demo-brightgreen)

---

## 📌 Project Overview

Predicting whether a loan should be approved is a critical task for financial institutions.  
This application uses **Machine Learning** to automate the loan approval process by analyzing applicant data and providing a **Yes / No** recommendation.
Manual loan approval processes are time-consuming, inconsistent, and prone to human error. Financial institutions need an automated, reliable system to assess applicant risk and determine loan eligibility quickly and accurately.

The system helps:
- Reduce manual decision errors
- Speed up credit risk assessment
- Improve consistency in loan approvals

---

## 🎯 Key Objectives
- Identify high-risk loan applicants  
- Minimize financial loss due to defaults  
- Provide a user-friendly interface for credit officers  

---

## 🏗️ System Architecture

The application follows a complete **end-to-end ML pipeline**:

1. **Data Collection**  
   - Historical loan data (CSV / Database)

2. **Data Preprocessing**  
   - Handling missing values  
   - Encoding categorical variables  
   - Feature scaling

3. **Model Training**  
   - Logistic Regression  
   - Decision Tree  
   - Random Forest  

4. **Deployment**  
   - Flask-based web application  
   - Gunicorn server  
   - Deployed on Render

---

## 🚀 Features

- **Real-time Prediction**  
  Enter applicant details and instantly receive a loan approval decision.

- **Data Visualization**  
  Visual insights into loan approval trends and applicant patterns.

- **Model Interpretation**  
  Understand key factors influencing decisions such as:
  - Credit History  
  - Applicant Income  
  - Loan Amount  

---

## 🛠️ Tech Stack

**Language**
- Python

**Libraries**
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Seaborn  

**Web Framework**
- Flask  

**Development Environment**
- Jupyter Notebook  
- Visual Studio Code  

**Deployment**
- Render  
- Gunicorn  

---

## 📂 How to Run Locally

```bash
git clone https://github.com/your-username/loan_prediction.git
cd loan_prediction
pip install -r requirements.txt
python app.py

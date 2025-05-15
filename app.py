import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model and the scaler
try:
    model = joblib.load('churn_model.joblib')
    scaler = joblib.load('scaler.joblib')
except FileNotFoundError:
    st.error("Error: Make sure 'churn_model.joblib' and 'scaler.joblib' are in the same directory as this app.")
    st.stop()

st.title("Telco Customer Churn Prediction")
st.write("Enter customer features to predict churn.")

# Get the feature names that the model was trained on (excluding 'Churn')
feature_names = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
                 'PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup',
                 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
                 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges',
                 'InternetService_Fiber optic', 'InternetService_No',
                 'Contract_One year', 'Contract_Two year',
                 'PaymentMethod_Credit card (automatic)',
                 'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check']

# Create input fields based on the feature names
user_inputs = {}
for feature in feature_names:
    if feature == 'gender':
        user_inputs[feature] = st.selectbox(f"Select {feature}", ["Female", "Male"])
        user_inputs[feature] = 1 if user_inputs[feature] == "Female" else 0 # Assuming Female is 1, Male is 0
    elif feature in ['Partner', 'Dependents', 'PhoneService', 'MultipleLines',
                   'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                   'StreamingTV', 'StreamingMovies', 'PaperlessBilling',
                   'InternetService_Fiber optic', 'InternetService_No',
                   'Contract_One year', 'Contract_Two year',
                   'PaymentMethod_Credit card (automatic)',
                   'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check']:
        user_inputs[feature] = st.selectbox(f"Select {feature}", ["No", "Yes"])
        user_inputs[feature] = 1 if user_inputs[feature] == "Yes" else 0
    elif feature in ['SeniorCitizen']:
        user_inputs[feature] = st.selectbox(
            f"Is the customer a Senior Citizen?", ["No", "Yes"]
        )
        user_inputs[feature] = 1 if user_inputs[feature] == "Yes" else 0
    elif feature in ['tenure']:
        user_inputs[feature] = st.number_input(f"Enter customer tenure (months)", min_value=0)
    elif feature in ['MonthlyCharges']:
        user_inputs[feature] = st.number_input(f"Enter monthly charges", min_value=0.0)
    elif feature in ['TotalCharges']:
        user_inputs[feature] = st.number_input(f"Enter total charges", min_value=0.0)

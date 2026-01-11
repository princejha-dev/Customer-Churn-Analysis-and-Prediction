import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Customer Churn Prediction", layout="wide")

st.title("🔮 Customer Churn Prediction")
st.write("Enter customer details to predict whether they will churn or not.")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior_citizen = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

with col2:
    online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])

col3, col4 = st.columns(2)

with col3:
    payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 500.0, 65.0)

with col4:
    total_charges = st.number_input("Total Charges ($)", 0.0, 10000.0, 800.0)

# Create prediction button
if st.button("Predict Churn", key="predict_button"):
    # Prepare data for prediction
    input_data = {
        'gender': gender,
        'SeniorCitizen': 1 if senior_citizen == "Yes" else 0,
        'Partner': 1 if partner == "Yes" else 0,
        'Dependents': 1 if dependents == "Yes" else 0,
        'tenure': tenure,
        'PhoneService': 1 if phone_service == "Yes" else 0,
        'MultipleLines': multiple_lines,
        'InternetService': internet_service,
        'OnlineSecurity': online_security,
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'Contract': contract,
        'PaperlessBilling': 1 if paperless_billing == "Yes" else 0,
        'PaymentMethod': payment_method,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges
    }
    
    # Encode categorical variables
    encoding_dict = {
        'gender': {'Male': 1, 'Female': 0},
        'MultipleLines': {'Yes': 2, 'No': 0, 'No phone service': 1},
        'InternetService': {'Fiber optic': 2, 'DSL': 0, 'No': 1},
        'OnlineSecurity': {'Yes': 2, 'No': 0, 'No internet service': 1},
        'OnlineBackup': {'Yes': 2, 'No': 0, 'No internet service': 1},
        'DeviceProtection': {'Yes': 2, 'No': 0, 'No internet service': 1},
        'TechSupport': {'Yes': 2, 'No': 0, 'No internet service': 1},
        'StreamingTV': {'Yes': 2, 'No': 0, 'No internet service': 1},
        'StreamingMovies': {'Yes': 2, 'No': 0, 'No internet service': 1},
        'Contract': {'Two year': 2, 'One year': 1, 'Month-to-month': 0},
        'PaymentMethod': {'Electronic check': 0, 'Mailed check': 1, 'Bank transfer (automatic)': 2, 'Credit card (automatic)': 3}
    }
    
    for key, value in encoding_dict.items():
        input_data[key] = value[input_data[key]]
    
    # Create DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Make prediction
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]
    
    # Display results
    st.divider()
    col_result1, col_result2 = st.columns(2)
    
    with col_result1:
        if prediction == 1:
            st.error("⚠️ **High Churn Risk**")
            st.write(f"Churn Probability: **{probability[1]*100:.2f}%**")
        else:
            st.success("✅ **Low Churn Risk**")
            st.write(f"Churn Probability: **{probability[1]*100:.2f}%**")
    
    with col_result2:
        st.metric("Retention Probability", f"{probability[0]*100:.2f}%")

st.divider()
st.caption("Made with ❤️ using Streamlit")
import streamlit as st
import joblib
import numpy as np

# Load the trained model (make sure the correct path is used)
model = joblib.load('./models/model.pkl')

# Streamlit UI
st.title("Diabetes Prediction")

# Create input fields for the user
Pregnancies = st.number_input('Pregnancies', min_value=0)
Glucose = st.number_input('Glucose')
BloodPressure = st.number_input('BloodPressure')
SkinThickness = st.number_input('SkinThickness')
Insulin = st.number_input('Insulin')
BMI = st.number_input('BMI')
DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction')
Age = st.number_input('Age')

# Create an input tuple
input_data = (Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)

# Button to make prediction
if st.button('Predict'):
    # Convert input data to numpy array and reshape for prediction
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(input_data_reshaped)
    
    if prediction == 0:
        st.write('The person is not diabetic')
    else:
        st.write('The person is diabetic')

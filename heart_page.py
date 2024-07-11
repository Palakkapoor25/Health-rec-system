import streamlit as st
from joblib import load
import numpy as np

# Function to load the machine learning model
@st.cache_data()
def load_model(model_path):
    model = load(model_path)
    return model

# Function to predict heart disease based on input features
def predict_heart_disease(model, age, sex, cp, trestbps, chol, restecg, thalach, exang, oldpeak, slope, thal):
    # Map categorical values to numerical values
    sex = 1 if sex == 'Male' else 0
    cp_mapping = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3}
    cp = cp_mapping.get(cp)
    restecg_mapping = {'Normal': 0, 'ST-T wave abnormality': 1, 'Probable or definite left ventricular hypertrophy': 2}
    restecg = restecg_mapping.get(restecg)
    exang = 1 if exang == 'Yes' else 0
    slope_mapping = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
    slope = slope_mapping.get(slope)
    thal_mapping = {'Normal': 1, 'Fixed Defect': 2, 'Reversible Defect': 3}
    thal = thal_mapping.get(thal)

    # Reshape inputs into a 2D array for prediction
    features = np.array([age, sex, cp, trestbps, chol, restecg, thalach, exang, oldpeak, slope, thal], dtype=np.float64).reshape(1, -1)
    prediction = model.predict(features)
    return prediction[0]

# Main function to run the Streamlit app
def main():
    # Load the machine learning model
    model_path = 'heart.pkl'  # Replace with your model file path
    model = load_model(model_path)

    # Display a title and description
    st.title('Heart Disease Predictor')
    st.markdown('Enter the following information to predict heart disease:')

    # Input fields for user to enter information
    age = st.number_input('Age', min_value=0, max_value=150, value=25)
    sex = st.selectbox('Sex', ['Female', 'Male'])
    cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
    trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=0.0, max_value=300.0, value=120.0)
    chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=0.0, max_value=600.0, value=200.0)
    restecg = st.selectbox('Resting ECG', ['Normal', 'ST-T wave abnormality', 'Probable or definite left ventricular hypertrophy'])
    thalach = st.number_input('Max Heart Rate Achieved', min_value=0, max_value=300, value=150)
    exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
    oldpeak = st.number_input('ST Depression Induced by Exercise Relative to Rest', min_value=0.0, max_value=10.0, value=0.0)
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
    thal = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

    # Button to predict
    if st.button('Predict Heart Disease'):
        # Predict heart disease using the model
        prediction = predict_heart_disease(model, age, sex, cp, trestbps, chol, restecg, thalach, exang, oldpeak, slope, thal)

        # Display prediction result
        if prediction == 1:
            st.error('Heart Disease Detected')
        else:
            st.success('No Heart Disease Detected')

if __name__ == '__main__':
    main()

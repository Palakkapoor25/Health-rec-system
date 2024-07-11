import streamlit as st
from joblib import load
import numpy as np
from functools import lru_cache


# Function to load the machine learning model
@lru_cache(maxsize=None)
def load_model(model_path):
    model = load(model_path)
    return model


# Function to predict diabetes based on input features
def predict_diabetes(model, features):
    # Reshape features into a 2D array for prediction
    features_reshaped = np.array(features).reshape(1, -1)
    prediction = model.predict(features_reshaped)
    return prediction[0]


# Main function to run the Streamlit app
def main():
    # Set page title and icon
    st.set_page_config(page_title='Diabetes Predictor', page_icon=':hospital:')

    # Load the machine learning model
    model_path = 'diabetes1.pkl'  # Replace with your model file path
    model = load_model(model_path)

    # Display a title and description
    st.title('Diabetes Predictor')
    st.markdown('Enter the following information to predict diabetes:')

    # Input fields for user to enter information
    pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, value=0, step=1)
    glucose = st.number_input('Glucose', min_value=0, max_value=200, value=0, step=1)
    blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=200, value=0, step=1)
    skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=100, value=0, step=1)
    insulin = st.number_input('Insulin', min_value=0, max_value=1000, value=0, step=1)
    bmi = st.number_input('BMI', min_value=0.0, max_value=60.0, value=0.0, step=0.1)
    diabetes_pedigree = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.0, value=0.0,
                                        step=0.01)
    age = st.number_input('Age', min_value=0, max_value=150, value=0, step=1)

    # Button to predict
    if st.button('Predict Diabetes'):
        # Gather input features into a dictionary with model feature names
        input_data = {
            'Pregnancies': pregnancies,
            'Glucose': glucose,
            'BloodPressure': blood_pressure,
            'SkinThickness': skin_thickness,
            'Insulin': insulin,
            'BMI': bmi,
            'DiabetesPedigreeFunction': diabetes_pedigree,
            'Age': age
        }

        # Predict diabetes using the model
        # Convert input_data to match model's expected format (list of values in correct order)
        model_features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI',
                          'DiabetesPedigreeFunction', 'Age']
        input_features = [input_data[feature] for feature in model_features]

        prediction = predict_diabetes(model, input_features)

        # Display prediction result
        if prediction == 1:
            st.error('Diabetes Positive')
        else:
            st.success('Diabetes Negative')


if __name__ == '__main__':
    main()

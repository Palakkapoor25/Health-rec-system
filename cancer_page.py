import streamlit as st
import numpy as np
import joblib

def set_background(image_path):
    page_bg_img = '''
    <style>
    body {
        background-image: url("%s");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
    }
    </style>
    ''' % image_path
    st.markdown(page_bg_img, unsafe_allow_html=True)
# Function to load and predict using the model
def predict_cancer(data):
    try:
        model = joblib.load('cancer.pkl')  # Load your trained model
        prediction = model.predict(data)
        return prediction
    except Exception as e:
        st.error(f"Error loading model or making prediction: {e}")
        return None

def main():
    # HTML div for background image
    image_path = './background.jpeg'
    set_background(image_path)

    # Main content of the app
    st.title('Breast Cancer Prediction')

    # Input fields for features
    st.subheader('Enter the following features:')
    radius_mean = st.number_input('Radius Mean', min_value=0.0, max_value=300.0, value=15.0)
    texture_mean = st.number_input('Texture Mean', min_value=0.0, max_value=100.0, value=20.0)
    perimeter_mean = st.number_input('Perimeter Mean', min_value=0.0, max_value=2000.0, value=100.0)
    area_mean = st.number_input('Area Mean', min_value=0.0, max_value=25000.0, value=500.0)
    smoothness_mean = st.number_input('Smoothness Mean', min_value=0.0, max_value=2.0, value=0.1)
    compactness_mean = st.number_input('Compactness Mean', min_value=0.0, max_value=1.0, value=0.2)
    concavity_mean = st.number_input('Concavity Mean', min_value=0.0, max_value=1.0, value=0.3)
    concave_points_mean = st.number_input('Concave Points Mean', min_value=0.0, max_value=1.0, value=0.15)
    symmetry_mean = st.number_input('Symmetry Mean', min_value=0.0, max_value=1.0, value=0.2)
    fractal_dimension_mean = st.number_input('Fractal Dimension Mean', min_value=0.0, max_value=1.0, value=0.08)
    radius_se = st.number_input('Radius SE', min_value=0.0, max_value=30.0, value=1.0)
    texture_se = st.number_input('Texture SE', min_value=0.0, max_value=5.0, value=0.5)
    perimeter_se = st.number_input('Perimeter SE', min_value=0.0, max_value=200.0, value=10.0)
    area_se = st.number_input('Area SE', min_value=0.0, max_value=2500.0, value=100.0)
    smoothness_se = st.number_input('Smoothness SE', min_value=0.0, max_value=0.5, value=0.01)
    compactness_se = st.number_input('Compactness SE', min_value=0.0, max_value=0.5, value=0.02)
    concavity_se = st.number_input('Concavity SE', min_value=0.0, max_value=0.5, value=0.03)
    concave_points_se = st.number_input('Concave Points SE', min_value=0.0, max_value=0.5, value=0.01)
    symmetry_se = st.number_input('Symmetry SE', min_value=0.0, max_value=1.0, value=0.02)
    fractal_dimension_se = st.number_input('Fractal Dimension SE', min_value=0.0, max_value=0.5, value=0.005)
    radius_worst = st.number_input('Radius Worst', min_value=0.0, max_value=300.0, value=25.0)
    texture_worst = st.number_input('Texture Worst', min_value=0.0, max_value=100.0, value=30.0)
    perimeter_worst = st.number_input('Perimeter Worst', min_value=0.0, max_value=2000.0, value=150.0)
    area_worst = st.number_input('Area Worst', min_value=0.0, max_value=25000.0, value=1000.0)
    smoothness_worst = st.number_input('Smoothness Worst', min_value=0.0, max_value=2.0, value=0.15)
    compactness_worst = st.number_input('Compactness Worst', min_value=0.0, max_value=1.0, value=0.3)
    concavity_worst = st.number_input('Concavity Worst', min_value=0.0, max_value=1.0, value=0.4)
    concave_points_worst = st.number_input('Concave Points Worst', min_value=0.0, max_value=1.0, value=0.2)
    symmetry_worst = st.number_input('Symmetry Worst', min_value=0.0, max_value=1.0, value=0.25)
    fractal_dimension_worst = st.number_input('Fractal Dimension Worst', min_value=0.0, max_value=1.0, value=0.08)

    # Button to predict
    if st.button('Submit'):
        # Prepare input data
        input_data = np.array([
            radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
            compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean,
            radius_se, texture_se, perimeter_se, area_se, smoothness_se,
            compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
            radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst,
            compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst
        ]).reshape(1, -1)

        # Predict
        prediction = predict_cancer(input_data)

        if prediction is not None:
            st.subheader('Prediction Result')
            if prediction[0] == 1:
                st.write('The tumor is malignant (cancerous).')
            else:
                st.write('The tumor is benign (not cancerous).')
        else:
            st.error('Failed to make prediction. Please check your input and try again.')

if __name__ == '__main__':
    main()

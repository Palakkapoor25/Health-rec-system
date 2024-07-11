import streamlit as st
import pandas as pd
from joblib import load

# Load your pre-trained model
@st.cache()
def load_model(model_path):
    loaded_model = load(model_path)
    return loaded_model


def main():
    try:
        st.title('Lung Cancer Detection')

        # Load the model
        model_path = 'lung_cancer1.pkl'  # Adjust the path if necessary
        model = load_model(model_path)

        # Sidebar for user inputs
        st.sidebar.title('User Input Parameters')
        gender = st.sidebar.radio('Gender', ['M', 'F'])
        age = st.sidebar.slider('Age', 1, 100, 50)
        smoking = st.sidebar.radio('Smoking', ['1', '2'])  # Assuming 1=Yes, 2=No
        yellow_fingers = st.sidebar.radio('Yellow Fingers', ['1', '2'])
        anxiety = st.sidebar.radio('Anxiety', ['1', '2'])
        peer_pressure = st.sidebar.radio('Peer Pressure', ['1', '2'])
        chronic_disease = st.sidebar.radio('Chronic Disease', ['1', '2'])
        fatigue = st.sidebar.radio('Fatigue', ['1', '2'])
        allergy = st.sidebar.radio('Allergy', ['1', '2'])
        wheezing = st.sidebar.radio('Wheezing', ['1', '2'])
        alcohol_consuming = st.sidebar.radio('Alcohol Consuming', ['1', '2'])
        coughing = st.sidebar.radio('Coughing', ['1', '2'])
        shortness_of_breath = st.sidebar.radio('Shortness of Breath', ['1', '2'])
        swallowing_difficulty = st.sidebar.radio('Swallowing Difficulty', ['1', '2'])
        chest_pain = st.sidebar.radio('Chest Pain', ['1', '2'])

        # Prepare the input data
        input_data = {
            'GENDER': gender,
            'AGE': age,
            'SMOKING': smoking,
            'YELLOW_FINGERS': yellow_fingers,
            'ANXIETY': anxiety,
            'PEER_PRESSURE': peer_pressure,
            'CHRONIC DISEASE': chronic_disease,
            'FATIGUE': fatigue,
            'ALLERGY': allergy,
            'WHEEZING': wheezing,
            'ALCOHOL CONSUMING': alcohol_consuming,
            'COUGHING': coughing,
            'SHORTNESS OF BREATH': shortness_of_breath,
            'SWALLOWING DIFFICULTY': swallowing_difficulty,
            'CHEST PAIN': chest_pain
        }

        input_df = pd.DataFrame([input_data])

        # Make a prediction
        prediction = model.predict(input_df)

        # Display the prediction
        st.write('Based on the input parameters, the model predicts:')
        if prediction[0] == 1:
            st.header('**High Risk of Lung Cancer**')
        else:
            st.header('**Low Risk of Lung Cancer**')

        # Optionally, you can display the input data
        st.subheader('Input Data:')
        st.write(input_df)

    except FileNotFoundError:
        st.error('Model file not found. Please check the file path.')
    except Exception as e:
        st.error(f'Error loading or using the model: {e}')


if __name__ == '__main__':
    main()

# Additional features or information can be added as needed

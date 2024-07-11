import streamlit as st
import joblib

# List of symptoms
SYMPTOMS_LIST = [
    'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering',
    'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue',
    'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_urination',
    'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings',
    'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat',
    'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes',
    'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache',
    'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite',
    'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain',
    'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
    'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
    'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision',
    'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
    'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
    'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region',
    'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness',
    'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels',
    'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
    'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts',
    'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain',
    'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness',
    'spinning_movements', 'loss_of_balance', 'unsteadiness',
    'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort',
    'foul_smell_of_urine', 'continuous_feel_of_urine', 'passage_of_gases',
    'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability',
    'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
    'abnormal_menstruation', 'dischromic_patches', 'watering_from_eyes',
    'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum',
    'rusty_sputum', 'lack_of_concentration', 'visual_disturbances',
    'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma',
    'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption',
    'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf',
    'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads',
    'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails',
    'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze'
]

# Function to predict disease based on symptoms
def predict_disease(symptoms):
    try:
        model = joblib.load('svc.pkl')  # Replace with your model file path
        predicted_disease = model.predict([symptoms])[0]
        return predicted_disease
    except Exception as e:
        st.error(f"Error predicting disease: {e}")
        return None

# Function to fetch disease information
def get_disease_info(disease):
    # Replace with your logic to fetch description, precautions, medication, diet, workout
    description = f"Description for {disease}"
    precaution = f"Precautions for {disease}"
    medication = f"Medication for {disease}"
    diet = f"Diet plan for {disease}"
    workout = f"Workout plan for {disease}"
    return description, precaution, medication, diet, workout

# Main function to run the Streamlit app
def main():
    st.set_page_config(page_title='Symptom Checker App', page_icon=':microscope:')
    st.title('Symptom Checker')

    # Multi-select box for symptoms
    st.subheader('Select 4 symptoms:')
    selected_symptoms = st.multiselect('Symptoms', SYMPTOMS_LIST, default=[])

    # Button to predict disease
    if st.button('Predict Disease'):
        if len(selected_symptoms) == 4:
            predicted_disease = predict_disease(selected_symptoms)
            if predicted_disease:
                st.write(f"Predicted Disease: {predicted_disease}")

                # Fetch disease information
                description, precaution, medication, diet, workout = get_disease_info(predicted_disease)

                # Display options for information
                st.subheader('Information:')
                if st.button('Description'):
                    st.write(description)
                if st.button('Precaution'):
                    st.write(precaution)
                if st.button('Medication'):
                    st.write(medication)
                if st.button('Diet'):
                    st.write(diet)
                if st.button('Workout'):
                    st.write(workout)
            else:
                st.error("Failed to predict disease. Please check your input.")
        else:
            st.warning("Please select exactly 4 symptoms.")

if __name__ == '__main__':
    main()

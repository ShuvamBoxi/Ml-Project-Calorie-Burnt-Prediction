import streamlit as st
from prediction_helper import predict

def calculate_heart_rate(exercise_name, duration_time):
    exercise_hr = {
        "Running": 130,
        "Cycling": 130,
        "Swimming": 125,
        "Walking": 80,
        "Yoga": 80,
        "Strength Training": 130
    }
    return exercise_hr.get(exercise_name, 100) + (duration * 0.5)

def calculate_body_temp(exercise_name, duration_time):
    exercise_temp = {
        "Running": 38.5,
        "Cycling": 38.2,
        "Swimming": 37.8,
        "Walking": 37.5,
        "Yoga": 37.3,
        "Strength Training": 38.0
    }
    return exercise_temp.get(exercise, 37.5) + (duration_time * 0.02)

#set the page configuration and title
st.set_page_config(page_title="Calorie Burnt Prediction", page_icon="🏃")
st.title("Calorie Burnt Prediction Model")

# Assign inputs to the first row with default values
# Row 1: Age, Height, Weight
col1, col2, col3 = st.columns(3)
age = col1.number_input("Age", min_value=10, max_value=100, value=25, step=1)
height = col2.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0, step=0.1)
weight = col3.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0, step=0.1)

# Row 2: Duration, Exercise Type, Heart Rate
col4, col5, col6 = st.columns(3)
duration = col4.number_input("Duration of Training (minutes)", min_value=1.0, max_value=300.0, value=30.0, step=1.0)
exercise = col5.selectbox("Exercise Type", ["Running", "Cycling", "Swimming", "Walking", "Yoga", "Strength Training"])
heart_rate = calculate_heart_rate(exercise, duration)
col6.metric(label="Heart Rate (bpm)", value=f"{heart_rate:.1f}")

# Row 3: Body Temperature, Gender
col7, col8 = st.columns(2)
body_temp = calculate_body_temp(exercise, duration)
col7.metric(label="Body Temperature (°C)", value=f"{body_temp:.1f}")
gender = col8.radio("Gender", ["Male", "Female"])


# Button to calculate risk
if st.button('Calculate Calorie Burn'):
    calorie = predict(age, height, weight, duration, heart_rate, body_temp, gender)

    # Display the results
    st.write(f"Calorie You Burnt: {calorie:.2f}")

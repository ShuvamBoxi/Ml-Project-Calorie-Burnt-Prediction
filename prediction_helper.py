import joblib
import pandas as pd

# Path to the saved model and its components
# Load the model and its components
model = joblib.load(r"artifacts/model_data.joblib")


def prepare_input(age, height, weight, duration, heart_rate, body_temp, gender):
    input_data = {
        'Age': age,
        'Height':height,
        'Weight':weight,
        'Duration':duration,
        'Heart_Rate':heart_rate,
        'Body_Temp':body_temp,
        'Gender_female': 1 if gender == 'Female' else 0,
        'Gender_male': 1 if gender == 'Male' else 0
    }

    df = pd.DataFrame([input_data])

    return df

def predict(age, height, weight, duration, heart_rate, body_temp, gender):
    input_df = prepare_input(age, height, weight, duration, heart_rate, body_temp, gender)
    prediction = model.predict(input_df)
    return float(prediction[0])
import joblib
import numpy as np

# Load the trained model
model = joblib.load("student_model.pkl")


def predict_student(attendance,
                    study_hours,
                    assignments,
                    internal_marks,
                    previous_gpa,
                    internet_usage,
                    gender,
                    extracurricular):

    # Convert text to numbers
    if gender == "Male":
        gender = 1
    else:
        gender = 0

    if extracurricular == "Yes":
        extracurricular = 1
    else:
        extracurricular = 0

    # Create input array
    data = np.array([[
        attendance,
        study_hours,
        assignments,
        internal_marks,
        previous_gpa,
        internet_usage,
        gender,
        extracurricular
    ]])

    # Predict
    prediction = model.predict(data)

    # Probability
    probability = model.predict_proba(data)

    confidence = round(max(probability[0]) * 100, 2)

    if prediction[0] == 1:
        result = "PASS ✅"
    else:
        result = "FAIL ❌"

    return result, confidence
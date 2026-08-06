import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load Dataset
df = pd.read_csv("dataset/student_data.csv")

# Convert text columns into numbers
le_gender = LabelEncoder()
le_extra = LabelEncoder()
le_result = LabelEncoder()

df["Gender"] = le_gender.fit_transform(df["Gender"])
df["Extracurricular"] = le_extra.fit_transform(df["Extracurricular"])
df["Result"] = le_result.fit_transform(df["Result"])

# Input Features
X = df[[
    "Attendance",
    "Study_Hours",
    "Assignments",
    "Internal_Marks",
    "Previous_GPA",
    "Internet_Usage",
    "Gender",
    "Extracurricular"
]]

# Target
y = df["Result"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Test Accuracy
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Save Model
joblib.dump(model, "student_model.pkl")

print("Model Saved Successfully!")
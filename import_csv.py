import sqlite3
import pandas as pd

# Read CSV
df = pd.read_csv("dataset/student_data.csv")

# Rename columns
df.columns = [
    "student_id",
    "name",
    "age",
    "gender",
    "attendance",
    "study_hours",
    "assignments",
    "internal_marks",
    "previous_gpa",
    "internet_usage",
    "extracurricular",
    "result"
]

conn = sqlite3.connect("students.db")

df.to_sql(
    "students",
    conn,
    
    if_exists="replace",
    index=False
)

conn.close()

print("120 Students Imported Successfully!")
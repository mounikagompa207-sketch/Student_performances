def ai_tips(
        attendance,
        study_hours,
        assignments,
        internal_marks,
        previous_gpa
):

    tips = []

    if attendance < 75:
        tips.append("✔ Improve attendance above 75%.")

    if study_hours < 4:
        tips.append("✔ Study at least 5 hours daily.")

    if assignments < 6:
        tips.append("✔ Submit assignments on time.")

    if internal_marks < 50:
        tips.append("✔ Practice previous year papers.")

    if previous_gpa < 6:
        tips.append("✔ Focus on weak subjects and revise regularly.")

    if not tips:
        tips.append("Excellent! Continue your current study routine.")

    return tips
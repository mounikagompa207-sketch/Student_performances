def calculate_score(attendance,
                    study_hours,
                    assignments,
                    internal_marks,
                    previous_gpa):

    score = (
        attendance * 0.25 +
        (study_hours * 10) * 0.20 +
        (assignments * 10) * 0.15 +
        internal_marks * 0.25 +
        (previous_gpa * 10) * 0.15
    )

    return round(score, 2)


def performance_grade(score):

    if score >= 90:
        return "A+ 🌟"

    elif score >= 80:
        return "A ✅"

    elif score >= 70:
        return "B 👍"

    elif score >= 60:
        return "C"

    elif score >= 40:
        return "D"

    return "F ❌"
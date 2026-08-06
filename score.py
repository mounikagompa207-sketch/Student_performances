def calculate_score(attendance,
                    study_hours,
                    assignments,
                    internal_marks,
                    previous_gpa):

    score = 0

    score += attendance * 0.25
    score += (study_hours * 10) * 0.20
    score += (assignments * 10) * 0.15
    score += internal_marks * 0.25
    score += (previous_gpa * 10) * 0.15

    return round(score, 2)


def performance_score(score):

    if score >= 90:
        return "Excellent 🌟"

    elif score >= 75:
        return "Very Good ✅"

    elif score >= 60:
        return "Good 👍"

    elif score >= 40:
        return "Average ⚠"

    else:
        return "Poor ❌"
from datetime import datetime


def calculate_daily_hours(target_score, current_score, days_left):

    if days_left <= 0:
        return 0

    improvement = max(target_score - current_score, 0)

    daily_hours = 2 + (improvement / 5)

    return round(daily_hours, 1)


def goal_progress(current_score, target_score):

    if target_score <= 0:
        return 0

    progress = (current_score / target_score) * 100

    if progress > 100:
        progress = 100

    return round(progress, 2)


def goal_status(progress):

    if progress >= 100:
        return "🎉 Goal Achieved"

    elif progress >= 80:
        return "🔥 Almost There"

    elif progress >= 60:
        return "👍 Good Progress"

    elif progress >= 40:
        return "⚠ Keep Working"

    else:
        return "🚀 Just Started"


def study_recommendation(hours):

    if hours <= 2:
        return "Maintain your current study routine."

    elif hours <= 4:
        return "Study consistently every day."

    elif hours <= 6:
        return "Increase focus and practice coding."

    else:
        return "High effort required. Reduce distractions."


def days_remaining(target_date):

    today = datetime.today().date()

    remaining = (target_date - today).days

    if remaining < 0:
        remaining = 0

    return remaining
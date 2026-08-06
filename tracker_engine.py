def calculate_progress(current_hours, target_hours):

    if target_hours <= 0:
        return 0

    progress = (current_hours / target_hours) * 100

    if progress > 100:
        progress = 100

    return round(progress, 2)


def progress_status(progress):

    if progress >= 100:
        return "🏆 Goal Achieved"

    elif progress >= 80:
        return "🥇 Excellent Progress"

    elif progress >= 60:
        return "🥈 Good Progress"

    elif progress >= 40:
        return "🥉 Average Progress"

    else:
        return "⚠ Needs Improvement"


def progress_color(progress):

    if progress >= 80:
        return "green"

    elif progress >= 60:
        return "blue"

    elif progress >= 40:
        return "orange"

    else:
        return "red"


def remaining_hours(current_hours, target_hours):

    remain = target_hours - current_hours

    if remain < 0:
        remain = 0

    return remain
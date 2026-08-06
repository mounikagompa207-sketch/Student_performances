def calculate_attendance(total_classes, attended_classes):
    """
    Calculate attendance percentage.
    """

    if total_classes <= 0:
        return 0

    attendance = (attended_classes / total_classes) * 100
    return round(attendance, 2)


def attendance_status(attendance):
    """
    Return attendance status.
    """

    if attendance >= 90:
        return "🏆 Excellent"

    elif attendance >= 75:
        return "✅ Good"

    elif attendance >= 60:
        return "⚠ Average"

    else:
        return "❌ Poor"


def attendance_color(attendance):
    """
    Return color for UI.
    """

    if attendance >= 90:
        return "green"

    elif attendance >= 75:
        return "blue"

    elif attendance >= 60:
        return "orange"

    else:
        return "red"


def classes_needed(total_classes, attended_classes, target=75):
    """
    Calculate how many consecutive classes
    must be attended to reach the target percentage.
    """

    if total_classes <= 0:
        return 0

    attendance = calculate_attendance(total_classes, attended_classes)

    if attendance >= target:
        return 0

    future_total = total_classes
    future_attended = attended_classes
    needed = 0

    while (future_attended / future_total) * 100 < target:
        future_total += 1
        future_attended += 1
        needed += 1

    return needed


def can_bunk(total_classes, attended_classes, target=75):
    """
    Calculate how many classes can be missed
    while staying above the target attendance.
    """

    bunk = 0

    future_total = total_classes
    future_attended = attended_classes

    while True:

        future_total += 1

        percentage = (future_attended / future_total) * 100

        if percentage >= target:
            bunk += 1
        else:
            break

    return bunk


def attendance_message(attendance):
    """
    Smart attendance message.
    """

    if attendance >= 90:
        return "Excellent attendance! Keep it up. 🎉"

    elif attendance >= 75:
        return "Good attendance. Maintain consistency. 👍"

    elif attendance >= 60:
        return "Attendance is average. Try attending more classes."

    else:
        return "Attendance is below requirement. Attend every class."
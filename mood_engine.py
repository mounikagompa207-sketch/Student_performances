def detect_mood(stress, sleep, motivation):

    score = stress + sleep + motivation

    if score >= 22:
        return (
            "😊 Happy",
            "Keep maintaining your healthy study routine."
        )

    elif score >= 16:
        return (
            "🙂 Calm",
            "You are doing well. Stay consistent."
        )

    elif score >= 10:
        return (
            "😐 Stressed",
            "Take short breaks and manage your study time."
        )

    else:
        return (
            "😞 Burnout Risk",
            "Please take proper rest and reduce stress."
        )


def mood_color(mood):

    if mood == "😊 Happy":
        return "green"

    elif mood == "🙂 Calm":
        return "blue"

    elif mood == "😐 Stressed":
        return "orange"

    else:
        return "red"


def mood_tips(mood):

    if mood == "😊 Happy":

        return [
            "Keep exercising regularly.",
            "Maintain your study routine.",
            "Help classmates when possible."
        ]

    elif mood == "🙂 Calm":

        return [
            "Stay positive.",
            "Continue daily revision.",
            "Take small breaks."
        ]

    elif mood == "😐 Stressed":

        return [
            "Reduce screen time.",
            "Sleep at least 7-8 hours.",
            "Practice meditation."
        ]

    else:

        return [
            "Talk with your mentor.",
            "Take a proper break.",
            "Sleep well.",
            "Avoid overthinking.",
            "Balance study and relaxation."
        ]
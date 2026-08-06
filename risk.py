def risk_level(score):

    if score >= 80:
        return "🟢 Low Risk"

    elif score >= 60:
        return "🟡 Medium Risk"

    else:
        return "🔴 High Risk"
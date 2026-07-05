def risk_level(score):

    if score >= 90:
        return "LOW"

    elif score >= 75:
        return "MEDIUM"

    elif score >= 50:
        return "HIGH"

    return "VERY HIGH"
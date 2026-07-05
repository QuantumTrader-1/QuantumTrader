def strength_score(score, trend):

    bonus = 0

    if trend == "UPTREND":
        bonus += 10

    elif trend == "DOWNTREND":
        bonus -= 10

    if score >= 90:
        bonus += 10

    elif score >= 75:
        bonus += 5

    return bonus
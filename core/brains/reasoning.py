def build_reasons(score, trend, risk, change):

    reasons = []

    if score >= 75:
        reasons.append("Strong overall technical score")
    elif score >= 60:
        reasons.append("Positive technical setup")
    elif score >= 40:
        reasons.append("Mixed technical signals")
    else:
        reasons.append("Weak technical setup")

    if trend.upper() == "UP":
        reasons.append("Market trend is bullish")

    elif trend.upper() == "DOWN":
        reasons.append("Market trend is bearish")

    else:
        reasons.append("Market is consolidating")

    if change > 3:
        reasons.append("Strong positive momentum")

    elif change < -3:
        reasons.append("Heavy selling pressure")

    if risk.upper() == "LOW":
        reasons.append("Risk profile is favorable")

    elif risk.upper() == "MEDIUM":
        reasons.append("Moderate trading risk")

    else:
        reasons.append("Higher than normal volatility")

    return reasons
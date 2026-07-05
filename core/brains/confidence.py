def calculate_confidence(score, trend, risk):

    confidence = score

    if trend.upper() == "UP":
        confidence += 10

    elif trend.upper() == "DOWN":
        confidence -= 5

    if risk.upper() == "LOW":
        confidence += 5

    elif risk.upper() == "HIGH":
        confidence -= 10

    confidence = max(0, min(100, confidence))

    return confidence
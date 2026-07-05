from core.brains.trend import detect_trend
from core.brains.momentum import momentum_score
from core.brains.volume import volume_score
from core.brains.history import history_score


def calculate_score(history, market):

    score = 0

    # Trend
    trend = detect_trend(history)

    if trend == "UPTREND":
        score += 30

    elif trend == "DOWNTREND":
        score -= 20

    # Momentum
    score += momentum_score(market["change"])

    # Volume
    score += volume_score(market["volume"])

    # Historical Confidence
    score += history_score(history)

    # Clamp score
    score = max(0, min(score, 100))

    return score
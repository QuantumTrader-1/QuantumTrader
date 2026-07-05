def calculate_score(history, market):

    score = 0

    # ---------------------------------
    # Trend
    # ---------------------------------

    if len(history) >= 5:

        prices = [entry["price"] for entry in history[-5:]]

        increasing = all(
            prices[i] > prices[i - 1]
            for i in range(1, len(prices))
        )

        decreasing = all(
            prices[i] < prices[i - 1]
            for i in range(1, len(prices))
        )

        if increasing:
            score += 30

        elif decreasing:
            score -= 20

    # ---------------------------------
    # Momentum
    # ---------------------------------

    change = market["change"]

    if change > 5:
        score += 25

    elif change > 2:
        score += 15

    elif change < -5:
        score -= 25

    # ---------------------------------
    # History Bonus
    # ---------------------------------

    if len(history) >= 10:
        score += 10

    # Clamp score between 0 and 100
    score = max(0, min(score, 100))

    return score
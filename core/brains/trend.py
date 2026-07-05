def detect_trend(history):

    if len(history) < 5:
        return "NEUTRAL"

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
        return "UPTREND"

    if decreasing:
        return "DOWNTREND"

    return "NEUTRAL"
def volatility_score(high, low, price):

    if price <= 0:
        return 0

    volatility = ((high - low) / price) * 100

    if volatility >= 15:
        return 20

    elif volatility >= 10:
        return 15

    elif volatility >= 5:
        return 10

    elif volatility >= 2:
        return 5

    return 0
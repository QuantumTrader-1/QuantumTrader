def liquidity_score(volume, price):

    dollar_volume = volume * price

    if dollar_volume >= 1_000_000_000:
        return 20

    elif dollar_volume >= 100_000_000:
        return 15

    elif dollar_volume >= 10_000_000:
        return 10

    elif dollar_volume >= 1_000_000:
        return 5

    return 0
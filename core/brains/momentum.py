def momentum_score(change):

    if change >= 15:
        return 40

    elif change >= 10:
        return 35

    elif change >= 5:
        return 25

    elif change >= 2:
        return 15

    elif change <= -15:
        return -40

    elif change <= -10:
        return -35

    elif change <= -5:
        return -25

    return 0
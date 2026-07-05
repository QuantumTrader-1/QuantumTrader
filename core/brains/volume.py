def volume_score(volume):

    if volume >= 100_000_000:
        return 25

    elif volume >= 10_000_000:
        return 20

    elif volume >= 1_000_000:
        return 15

    elif volume >= 100_000:
        return 10

    elif volume >= 10_000:
        return 5

    return 0
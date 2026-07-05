def history_score(history):

    observations = len(history)

    if observations >= 100:
        return 30

    elif observations >= 50:
        return 20

    elif observations >= 25:
        return 15

    elif observations >= 10:
        return 10

    elif observations >= 5:
        return 5

    return 0
def trading_signal(score, trend, risk):

    if score >= 90 and trend == "UPTREND" and risk == "LOW":
        return "🟢 STRONG BUY"

    elif score >= 75 and trend == "UPTREND":
        return "🟢 BUY"

    elif score >= 55:
        return "🟡 WATCH"

    elif trend == "DOWNTREND":
        return "🔴 SELL"

    return "⚪ HOLD"
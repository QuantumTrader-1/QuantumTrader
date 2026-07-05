from core.brains.memory import remember, recall
from core.brains.scoring import calculate_score
from core.brains.trend import detect_trend
from core.brains.risk import risk_level
from core.brains.signals import trading_signal

from core.models import CoinAnalysis

from core.config import (
    STRONG_WATCH_SCORE,
    WATCH_SCORE,
    MINIMUM_SCORE_TO_WATCH,
)


class Atlas:

    def __init__(self):
        print("🧠 Atlas AI Initialized")

    def analyze(self, coin, data):

        history = recall(coin)

        trend = detect_trend(history)

        remember(coin, data)

        history = recall(coin)

        score = calculate_score(history, data)

        risk = risk_level(score)

        signal = trading_signal(score, trend, risk)

        if score >= STRONG_WATCH_SCORE:
            recommendation = "STRONG WATCH"

        elif score >= WATCH_SCORE:
            recommendation = "WATCH"

        elif score >= MINIMUM_SCORE_TO_WATCH:
            recommendation = "NEUTRAL"

        else:
            recommendation = "IGNORE"

        return CoinAnalysis(
            symbol=coin,
            price=data["price"],
            change=data["change"],
            score=score,
            recommendation=recommendation,
            signal=signal,
            trend=trend,
            risk=risk,
            volume=data["volume"],
            high=data["high"],
            low=data["low"],
        )
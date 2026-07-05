from core.brains.memory import remember, recall
from core.brains.scoring import calculate_score
from core.brains.trend import detect_trend
from core.brains.risk import risk_level
from core.brains.signals import trading_signal
from core.brains.reasoning import build_reasons
from core.brains.confidence import calculate_confidence

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

        # Load previous history
        history = recall(coin)

        # Detect trend
        trend = detect_trend(history)

        # Save newest data
        remember(coin, data)

        # Reload history
        history = recall(coin)

        # Technical score
        score = calculate_score(history, data)

        # Risk
        risk = risk_level(score)

        # Trading signal
        signal = trading_signal(score, trend, risk)

        # AI confidence
        confidence = calculate_confidence(
            score,
            trend,
            risk
        )

        # AI reasoning
        reasons = build_reasons(
            score,
            trend,
            risk,
            data["change"]
        )

        # Recommendation
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
            confidence=confidence,
            recommendation=recommendation,
            signal=signal,
            trend=trend,
            risk=risk,
            volume=data["volume"],
            high=data["high"],
            low=data["low"],
            reason="\n".join(reasons)
        )
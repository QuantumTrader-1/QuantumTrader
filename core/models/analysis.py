from dataclasses import dataclass


@dataclass
class Analysis:

    symbol: str

    price: float

    change: float

    score: int

    signal: str

    recommendation: str

    risk: str

    trend: str

    volume: float

    high: float

    low: float

    confidence: int = 0

    reason: str = ""
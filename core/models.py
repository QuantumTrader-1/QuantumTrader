from dataclasses import dataclass


@dataclass
class CoinAnalysis:

    symbol: str

    price: float

    change: float

    score: int

    recommendation: str

    trend: str

    risk: str

    volume: float

    high: float

    low: float
from core.brains.atlas import Atlas
from core.models import Analysis


class AtlasService:

    def __init__(self):

        self.atlas = Atlas()

    def analyze_markets(self, markets):

        analyses = []

        for symbol, market in markets:

            result = self.atlas.analyze(symbol, market)

            analysis = Analysis(
                symbol=result.symbol,
                price=result.price,
                change=result.change,
                score=result.score,
                signal=result.signal,
                recommendation=result.recommendation,
                risk=result.risk,
                trend=result.trend,
                volume=result.volume,
                high=result.high,
                low=result.low,
                confidence=result.score,
                reason=""
            )

            analyses.append(analysis)

        return analyses
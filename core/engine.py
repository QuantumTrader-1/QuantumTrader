from core.market import COINS, get_market_data
from core.brains.atlas import Atlas


class QuantumEngine:

    def __init__(self):
        self.atlas = Atlas()

    def scan_market(self):

        results = []

        for coin in COINS:

            market = get_market_data(coin)

            if market is None:
                continue

            analysis = self.atlas.analyze(coin, market)

            if analysis is not None:
                results.append(analysis)

        return results
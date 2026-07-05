from core.brains.atlas import Atlas
from core.watchlist import Watchlist

from core.market import COINS, get_market_data


class QuantumEngine:

    def __init__(self):

        self.atlas = Atlas()
        self.watchlist = Watchlist()

    def scan_market(self):

        self.watchlist.clear()

        results = []

        for coin in COINS:

            market = get_market_data(coin)

            if market is None:
                continue

            analysis = self.atlas.analyze(coin, market)

            self.watchlist.update(analysis)

            results.append(analysis)

        return results

    def top_opportunities(self):

        return self.watchlist.top()
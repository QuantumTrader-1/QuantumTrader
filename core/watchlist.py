from core.models import CoinAnalysis
from core.config import MAX_WATCHLIST


class Watchlist:

    def __init__(self):
        self.coins = []

    def update(self, analysis: CoinAnalysis):
        self.coins.append(analysis)

    def clear(self):
        self.coins.clear()

    def top(self):

        return sorted(
            self.coins,
            key=lambda coin: coin.score,
            reverse=True
        )[:MAX_WATCHLIST]

    def best(self):

        top = self.top()

        if not top:
            return None

        return top[0]
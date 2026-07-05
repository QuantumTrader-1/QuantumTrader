from core.watchlist import Watchlist


class WatchlistService:

    def __init__(self):

        self.watchlist = Watchlist()

    def build_watchlist(self, analyses):

        self.watchlist.clear()

        for analysis in analyses:
            self.watchlist.update(analysis)

        return self.watchlist.top()

    def best_opportunity(self):

        return self.watchlist.best()
from core.services.market_service import MarketService
from core.services.atlas_service import AtlasService
from core.services.watchlist_service import WatchlistService


class QuantumEngine:

    def __init__(self):

        self.market_service = MarketService()
        self.atlas_service = AtlasService()
        self.watchlist_service = WatchlistService()

        self.last_scan = None

    def scan_market(self):

        markets = self.market_service.get_all_markets()

        analyses = self.atlas_service.analyze_markets(markets)

        self.watchlist_service.build_watchlist(analyses)

        self.last_scan = analyses

        return analyses

    def top_opportunities(self):

        return self.watchlist_service.watchlist.top()

    def best_opportunity(self):

        return self.watchlist_service.best_opportunity()
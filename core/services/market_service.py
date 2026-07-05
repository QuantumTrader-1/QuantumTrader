from core.market import COINS, get_market_data


class MarketService:

    def get_all_markets(self):

        markets = []

        for coin in COINS:

            market = get_market_data(coin)

            if market is not None:
                markets.append((coin, market))

        return markets
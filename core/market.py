import requests

from core.brains.atlas import Atlas

COINS = [
    "BTC-USD",
    "ETH-USD",
    "XRP-USD",
    "SOL-USD",
    "IDEX-USD"
]


def get_market_data(product):

    url = f"https://api.exchange.coinbase.com/products/{product}/stats"

    try:

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        last = float(data["last"])
        open_price = float(data["open"])
        high = float(data["high"])
        low = float(data["low"])
        volume = float(data["volume"])

        percent_change = ((last - open_price) / open_price) * 100

        return {
            "price": last,
            "change": percent_change,
            "high": high,
            "low": low,
            "volume": volume,
        }

    except Exception as e:
        print(f"Error getting {product}: {e}")
        return None


def display_market():

    atlas = Atlas()

    print()
    print("=" * 90)
    print("                 QUANTUM TRADER - AI MARKET ANALYSIS")
    print("=" * 90)

    for coin in COINS:

        market = get_market_data(coin)

        if market is None:
            continue

        analysis = atlas.analyze(coin, market)

        print(f"\n{analysis.symbol}")
        print(f"Price          : ${analysis.price:,.4f}")
        print(f"24h Change     : {analysis.change:+.2f}%")
        print(f"Trend          : {analysis.trend}")
        print(f"Quantum Score  : {analysis.score}")
        print(f"Recommendation : {analysis.recommendation}")

        print("-" * 90)

    print("=" * 90)


if __name__ == "__main__":
    display_market()
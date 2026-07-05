import requests
from core.brains.atlas import Atlas

atlas = Atlas()

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

    print("\n")
    print("=" * 80)
    print("                 QUANTUM TRADER - ATLAS MARKET SCANNER")
    print("=" * 80)

    for coin in COINS:

        market = get_market_data(coin)

        if market is None:
            print(f"{coin:<10} Unable to retrieve data")
        else:

            arrow = "🟢" if market["change"] >= 0 else "🔴"

            print(
                f"{coin:<10}"
                f"${market['price']:>12,.4f}"
                f"   {arrow} {market['change']:+7.2f}%"
            )

            # Atlas analyzes and remembers every coin
            atlas.analyze(coin, market)

    print("=" * 80)


if __name__ == "__main__":
    display_market()
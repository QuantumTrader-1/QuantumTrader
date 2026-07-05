from core.config import APP_NAME, VERSION


class Dashboard:

    def display(self, opportunities):

        print("\n")
        print("=" * 140)
        print(f"{APP_NAME} v{VERSION}")
        print("=" * 140)

        print("ATLAS WATCHLIST\n")

        print(
            f"{'Rank':<5}"
            f"{'Coin':<12}"
            f"{'Score':<8}"
            f"{'Signal':<16}"
            f"{'Risk':<12}"
            f"{'Trend':<12}"
            f"{'24h %':<10}"
            f"{'Price':<15}"
            f"{'Recommendation'}"
        )

        print("-" * 140)

        for rank, coin in enumerate(opportunities, start=1):

            print(
                f"{rank:<5}"
                f"{coin.symbol:<12}"
                f"{coin.score:<8}"
                f"{coin.signal:<16}"
                f"{coin.risk:<12}"
                f"{coin.trend:<12}"
                f"{coin.change:+.2f}%".ljust(10)
                + f"${coin.price:,.4f}".ljust(15)
                + f"{coin.recommendation}"
            )

        print("=" * 140)
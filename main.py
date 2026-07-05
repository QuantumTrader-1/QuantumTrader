from core.engine import QuantumEngine
from core.dashboard import Dashboard


def main():

    engine = QuantumEngine()
    dashboard = Dashboard()

    engine.scan_market()

    dashboard.display(engine.top_opportunities())

    best = engine.watchlist.best()

    if best:

        print("\n⭐ BEST OPPORTUNITY")
        print("-" * 90)
        print(f"Coin           : {best.symbol}")
        print(f"Score          : {best.score}")
        print(f"Trend          : {best.trend}")
        print(f"Recommendation : {best.recommendation}")
        print("-" * 90)


if __name__ == "__main__":
    main()
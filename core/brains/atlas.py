from core.brains.memory import remember, recall
from core.brains.scoring import calculate_score


class Atlas:

    def __init__(self):
        print("🧠 Atlas AI Initialized")

    def think(self):
        print("🧠 Atlas is analyzing the crypto market...")

    def analyze(self, coin, data):

        print(f"\n🔍 Analyzing {coin}")

        # Load previous history
        history = recall(coin)

        # Display previous price if available
        if len(history) == 0:
            print("🧠 Atlas: First time seeing this coin.")
        else:
            previous = history[-1]["price"]
            difference = data["price"] - previous

            print(f"🧠 Last remembered price: ${previous:,.4f}")

            if difference > 0:
                print(f"📈 Price increased by ${difference:,.4f}")

            elif difference < 0:
                print(f"📉 Price decreased by ${abs(difference):,.4f}")

            else:
                print("😐 Price unchanged.")

        # Save newest scan
        remember(coin, data)

        # Reload updated history
        history = recall(coin)

        # Calculate Quantum Score
        score = calculate_score(history, data)

        print(f"⭐ Quantum Score: {score}/100")

        # Recommendation
        if score >= 80:
            print("🟢 Recommendation: STRONG BUY WATCH")

        elif score >= 60:
            print("🟡 Recommendation: WATCH CLOSELY")

        elif score >= 40:
            print("🔵 Recommendation: NEUTRAL")

        else:
            print("🔴 Recommendation: IGNORE FOR NOW")
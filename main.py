from core.market import display_market
from core.brains.atlas import Atlas

print("\n🚀 Launching Quantum Trader...\n")

atlas = Atlas()

atlas.think()

display_market()
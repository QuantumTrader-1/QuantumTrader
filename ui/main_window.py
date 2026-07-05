import customtkinter as ctk

from core.engine import QuantumEngine

from ui.header import Header
from ui.sidebar import Sidebar
from ui.market_table import MarketTable
from ui.detail_panel import DetailPanel
from ui.status_bar import StatusBar


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.engine = QuantumEngine()

        self.title("Quantum Trader Genesis")
        self.geometry("1700x950")
        self.minsize(1500, 850)

        # ---------------- Grid ---------------- #

        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=2)

        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=0)

        # ---------------- Header ---------------- #

        self.header = Header(self)

        self.header.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky="ew",
            padx=10,
            pady=(10, 0)
        )

        # ---------------- Sidebar ---------------- #

        self.sidebar = Sidebar(
            self,
            self.scan_market
        )

        self.sidebar.grid(
            row=2,
            column=0,
            sticky="ns",
            padx=(10, 5),
            pady=10
        )

        # ---------------- Market ---------------- #

        self.market = MarketTable(self)

        self.market.grid(
            row=2,
            column=1,
            sticky="nsew",
            padx=5,
            pady=10
        )

        # ---------------- Details ---------------- #

        self.details = DetailPanel(self)

        self.details.grid(
            row=2,
            column=2,
            sticky="nsew",
            padx=(5, 10),
            pady=10
        )

        # ---------------- Status ---------------- #

        self.status = StatusBar(self)

        self.status.grid(
            row=3,
            column=0,
            columnspan=3,
            sticky="ew"
        )

        self.scan_market()

    # ------------------------------------------------

    def coin_selected(self, coin):

        self.details.show_coin(coin)

    # ------------------------------------------------

    def scan_market(self):

        self.status.set_status("🔄 Scanning market...")

        self.engine.scan_market()

        coins = self.engine.top_opportunities()

        self.market.update_table(
            coins,
            self.coin_selected
        )

        best = self.engine.best_opportunity()

        self.sidebar.update_best(best)

        self.details.show_coin(best)

        self.status.set_status(
            f"🟢 Ready • {len(coins)} opportunities"
        )
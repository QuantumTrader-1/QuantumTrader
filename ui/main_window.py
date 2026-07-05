import customtkinter as ctk

from core.engine import QuantumEngine

from ui.header import Header
from ui.toolbar import Toolbar
from ui.sidebar import Sidebar
from ui.dashboard_panel import DashboardPanel
from ui.market_table import MarketTable
from ui.detail_panel import DetailPanel
from ui.status_bar import StatusBar


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.engine = QuantumEngine()

        self.all_coins = []
        self.filtered_coins = []
        self.sort_descending = True

        self.title("Quantum Trader Genesis")
        self.geometry("1700x950")
        self.minsize(1500, 850)

        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=2)
        self.grid_rowconfigure(3, weight=1)

        # Header
        self.header = Header(self)
        self.header.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky="ew",
            padx=10,
            pady=(10, 0)
        )

        # Toolbar
        self.toolbar = Toolbar(
            self,
            self.scan_market,
            self.search_market,
            self.sort_market
        )

        self.toolbar.grid(
            row=1,
            column=0,
            columnspan=3,
            sticky="ew",
            padx=10
        )

        # Dashboard
        self.dashboard = DashboardPanel(self)

        self.dashboard.grid(
            row=2,
            column=1,
            columnspan=2,
            sticky="ew",
            padx=(5, 10),
            pady=(5, 0)
        )

        # Sidebar
        self.sidebar = Sidebar(
            self,
            self.scan_market
        )

        self.sidebar.grid(
            row=2,
            rowspan=2,
            column=0,
            sticky="ns",
            padx=(10, 5),
            pady=10
        )

        # Market Table
        self.market = MarketTable(self)

        self.market.grid(
            row=3,
            column=1,
            sticky="nsew",
            padx=5,
            pady=10
        )

        # Details
        self.details = DetailPanel(self)

        self.details.grid(
            row=3,
            column=2,
            sticky="nsew",
            padx=(5, 10),
            pady=10
        )

        # Status
        self.status = StatusBar(self)

        self.status.grid(
            row=4,
            column=0,
            columnspan=3,
            sticky="ew"
        )

        self.scan_market()

    def coin_selected(self, coin):
        self.details.show_coin(coin)

    def refresh_table(self):

        self.market.update_table(
            self.filtered_coins,
            self.coin_selected
        )

    def scan_market(self):

        self.status.set_status("🔄 Scanning market...")
        self.toolbar.set_status("Scanning...")

        analyses = self.engine.scan_market()

        self.all_coins = self.engine.top_opportunities()
        self.filtered_coins = list(self.all_coins)

        self.refresh_table()

        self.dashboard.update_stats(analyses)

        best = self.engine.best_opportunity()

        if best:
            self.sidebar.update_best(best)
            self.details.show_coin(best)

        self.status.set_status(
            f"🟢 Ready • {len(self.all_coins)} opportunities"
        )

        self.toolbar.set_status(
            f"{len(self.all_coins)} coins loaded"
        )

        self.toolbar.set_market_count(
            len(self.all_coins)
        )

    def search_market(self, text):

        text = text.upper().strip()

        if text == "":
            self.filtered_coins = list(self.all_coins)
        else:
            self.filtered_coins = [
                coin
                for coin in self.all_coins
                if text in coin.symbol.upper()
            ]

        self.refresh_table()

    def sort_market(self):

        self.filtered_coins.sort(
            key=lambda c: c.score,
            reverse=self.sort_descending
        )

        self.sort_descending = not self.sort_descending

        self.refresh_table()
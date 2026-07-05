import customtkinter as ctk

from core.engine import QuantumEngine

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

        self.title("🚀 Quantum Trader Genesis")
        self.geometry("1600x900")

        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=2)
        self.grid_rowconfigure(1, weight=1)

        header = ctk.CTkLabel(
            self,
            text="🚀 QUANTUM TRADER",
            font=("Segoe UI", 34, "bold")
        )

        header.grid(
            row=0,
            column=0,
            columnspan=3,
            pady=(20, 10)
        )

        self.sidebar = Sidebar(
            self,
            self.scan_market
        )

        self.sidebar.grid(
            row=1,
            column=0,
            sticky="ns",
            padx=15,
            pady=15
        )

        self.market = MarketTable(self)

        self.market.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=10,
            pady=15
        )

        self.details = DetailPanel(self)

        self.details.grid(
            row=1,
            column=2,
            sticky="nsew",
            padx=(0, 15),
            pady=15
        )

        self.status = StatusBar(self)

        self.status.grid(
            row=2,
            column=0,
            columnspan=3,
            sticky="ew"
        )

        self.scan_market()

    # --------------------------------------------------

    def coin_selected(self, coin):

        self.details.show_coin(coin)

    # --------------------------------------------------

    def scan_market(self):

        self.status.set_status("🔄 Scanning Coinbase...")

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
            f"🟢 Ready • {len(coins)} coins loaded"
        )
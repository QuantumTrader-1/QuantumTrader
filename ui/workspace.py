import customtkinter as ctk

from ui.dashboard_panel import DashboardPanel
from ui.market_table import MarketTable


class Workspace(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.dashboard = DashboardPanel(self)

        self.dashboard.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=5,
            pady=(5, 0)
        )

        self.market = MarketTable(self)

        self.market.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=5,
            pady=5
        )
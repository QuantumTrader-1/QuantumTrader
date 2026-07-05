import customtkinter as ctk

from ui.widgets.header_row import HeaderRow
from ui.widgets.market_row import MarketRow


class MarketTable(ctk.CTkScrollableFrame):

    def __init__(self, master):
        super().__init__(master)

        self.header = HeaderRow(self)
        self.header.pack(fill="x", pady=(0, 10))

        self.rows = []

    def update_table(self, opportunities, callback=None):

        for row in self.rows:
            row.destroy()

        self.rows.clear()

        for coin in opportunities:

            row = MarketRow(
                self,
                coin,
                callback
            )

            row.pack(
                fill="x",
                padx=5,
                pady=2
            )

            self.rows.append(row)
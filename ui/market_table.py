import customtkinter as ctk
from CTkTable import CTkTable


class MarketTable(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.table = None

    def update_table(self, opportunities):

        if self.table:
            self.table.destroy()

        values = [[
            "Coin",
            "Score",
            "Signal",
            "Risk",
            "Trend",
            "24h %",
            "Price",
            "Recommendation"
        ]]

        for coin in opportunities:

            values.append([
                coin.symbol,
                str(coin.score),
                coin.signal,
                coin.risk,
                coin.trend,
                f"{coin.change:+.2f}%",
                f"${coin.price:,.4f}",
                coin.recommendation
            ])

        self.table = CTkTable(
            master=self,
            values=values
        )

        self.table.pack(fill="both", expand=True)
import customtkinter as ctk


class MarketRow(ctk.CTkFrame):

    def __init__(self, master, coin, callback=None):
        super().__init__(master)

        self.coin = coin
        self.callback = callback

        values = [
            (coin.symbol, 120),
            (str(coin.score), 70),
            (coin.signal, 110),
            (coin.risk, 90),
            (coin.trend, 110),
            (f"{coin.change:+.2f}%", 90),
            (f"${coin.price:,.4f}", 120),
            (coin.recommendation, 180),
        ]

        for text, width in values:
            label = ctk.CTkLabel(
                self,
                text=text,
                width=width,
                anchor="w",
                font=("Segoe UI", 13),
            )
            label.pack(side="left", padx=4, pady=6)

        self.bind("<Button-1>", self.clicked)

        for child in self.winfo_children():
            child.bind("<Button-1>", self.clicked)

    def clicked(self, event):
        if self.callback:
            self.callback(self.coin)
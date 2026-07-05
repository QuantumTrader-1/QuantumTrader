import customtkinter as ctk


class MarketRow(ctk.CTkFrame):

    def __init__(self, master, coin, callback=None):
        super().__init__(
            master,
            corner_radius=8,
            fg_color="#202225"
        )

        self.coin = coin
        self.callback = callback

        signal_color = {
            "BUY": "#2ECC71",
            "HOLD": "#F1C40F",
            "SELL": "#E74C3C"
        }.get(coin.signal.upper(), "white")

        values = [
            (coin.symbol, 120, "white"),
            (str(coin.score), 70, "#58A6FF"),
            (coin.signal, 110, signal_color),
            (coin.risk, 90, "white"),
            (coin.trend, 110, "white"),
            (f"{coin.change:+.2f}%", 90,
             "#2ECC71" if coin.change >= 0 else "#E74C3C"),
            (f"${coin.price:,.4f}", 120, "white"),
            (coin.recommendation, 180, "white"),
        ]

        for text, width, color in values:

            label = ctk.CTkLabel(
                self,
                text=text,
                width=width,
                text_color=color,
                anchor="w",
                font=("Segoe UI", 13)
            )

            label.pack(side="left", padx=4, pady=8)

            label.bind("<Button-1>", self.clicked)

        self.bind("<Button-1>", self.clicked)

        self.bind("<Enter>", self.hover)

        self.bind("<Leave>", self.leave)

    def hover(self, event):

        self.configure(fg_color="#2C313A")

    def leave(self, event):

        self.configure(fg_color="#202225")

    def clicked(self, event):

        self.configure(fg_color="#3B82F6")

        if self.callback:

            self.callback(self.coin)
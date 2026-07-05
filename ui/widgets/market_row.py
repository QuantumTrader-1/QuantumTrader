import customtkinter as ctk


class MarketRow(ctk.CTkFrame):

    selected_row = None

    favorites = set()

    def __init__(self, master, coin, callback=None):
        super().__init__(
            master,
            corner_radius=8,
            fg_color="#202225"
        )

        self.coin = coin
        self.callback = callback

        self.star = ctk.CTkLabel(
            self,
            text="★" if coin.symbol in MarketRow.favorites else "☆",
            width=40,
            text_color="#FFD700",
            cursor="hand2",
            font=("Segoe UI", 18)
        )

        self.star.pack(side="left", padx=(8, 4))

        self.star.bind("<Button-1>", self.toggle_favorite)

        signal_color = {
            "BUY": "#2ECC71",
            "SELL": "#E74C3C",
            "HOLD": "#F1C40F"
        }.get(coin.signal.upper(), "white")

        values = [
            (coin.symbol, 100, "white"),
            (str(coin.score), 70, "#58A6FF"),
            (coin.signal, 110, signal_color),
            (coin.risk, 90, "white"),
            (coin.trend, 110, "white"),
            (
                f"{coin.change:+.2f}%",
                90,
                "#2ECC71" if coin.change >= 0 else "#E74C3C"
            ),
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

    def toggle_favorite(self, event):

        if self.coin.symbol in MarketRow.favorites:
            MarketRow.favorites.remove(self.coin.symbol)
            self.star.configure(text="☆")
        else:
            MarketRow.favorites.add(self.coin.symbol)
            self.star.configure(text="★")

    def hover(self, event):

        if MarketRow.selected_row != self:
            self.configure(fg_color="#2C313A")

    def leave(self, event):

        if MarketRow.selected_row != self:
            self.configure(fg_color="#202225")

    def clicked(self, event):

        if MarketRow.selected_row:
            MarketRow.selected_row.configure(
                fg_color="#202225"
            )

        MarketRow.selected_row = self

        self.configure(fg_color="#2563EB")

        if self.callback:
            self.callback(self.coin)
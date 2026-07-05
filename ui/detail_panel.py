import customtkinter as ctk


class DetailPanel(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.title = ctk.CTkLabel(
            self,
            text="Coin Details",
            font=("Segoe UI", 20, "bold")
        )

        self.title.pack(pady=(15, 10))

        self.details = ctk.CTkTextbox(
            self,
            height=300
        )

        self.details.pack(fill="both", expand=True, padx=15, pady=15)

    def show_coin(self, coin):

        self.details.delete("1.0", "end")

        if coin is None:
            return

        self.details.insert(
            "end",
            f"""
Coin

{coin.symbol}

Price

${coin.price:,.4f}

Score

{coin.score}

Signal

{coin.signal}

Risk

{coin.risk}

Trend

{coin.trend}

Recommendation

{coin.recommendation}

Volume

{coin.volume:,.0f}

24h High

${coin.high:,.4f}

24h Low

${coin.low:,.4f}
"""
        )
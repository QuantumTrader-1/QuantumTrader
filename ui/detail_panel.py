import customtkinter as ctk


class DetailPanel(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            self,
            text="🧠 Atlas AI",
            font=("Segoe UI", 22, "bold")
        )
        title.pack(pady=(15, 10))

        self.signal = ctk.CTkLabel(
            self,
            text="NO SIGNAL",
            font=("Segoe UI", 26, "bold")
        )
        self.signal.pack(pady=(0, 10))

        self.confidence = ctk.CTkProgressBar(self)
        self.confidence.pack(fill="x", padx=20)

        self.confidence.set(0)

        self.confidence_text = ctk.CTkLabel(
            self,
            text="Confidence: 0%"
        )
        self.confidence_text.pack(pady=(5, 15))

        self.info = ctk.CTkTextbox(
            self,
            height=350
        )

        self.info.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

    def show_coin(self, coin):

        self.info.delete("1.0", "end")

        if coin is None:
            return

        signal = coin.signal.upper()

        colors = {
            "BUY": "#2ECC71",
            "SELL": "#E74C3C",
            "HOLD": "#F1C40F"
        }

        self.signal.configure(
            text=signal,
            text_color=colors.get(signal, "white")
        )

        confidence = max(0, min(100, coin.score))

        self.confidence.set(confidence / 100)

        self.confidence_text.configure(
            text=f"Confidence: {confidence}%"
        )

        self.info.insert(
            "end",
            f"""
━━━━━━━━━━━━━━━━━━━━━━

Coin

{coin.symbol}

━━━━━━━━━━━━━━━━━━━━━━

Current Price

${coin.price:,.4f}

24 Hour Change

{coin.change:+.2f}%

━━━━━━━━━━━━━━━━━━━━━━

Risk

{coin.risk}

Trend

{coin.trend}

━━━━━━━━━━━━━━━━━━━━━━

Recommendation

{coin.recommendation}

━━━━━━━━━━━━━━━━━━━━━━

Volume

{coin.volume:,.0f}

24h High

${coin.high:,.4f}

24h Low

${coin.low:,.4f}

━━━━━━━━━━━━━━━━━━━━━━

Atlas Notes

• AI reasoning coming soon

• Trade plans coming soon

• Indicator breakdown coming soon
"""
        )
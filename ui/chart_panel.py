import customtkinter as ctk

from ui.widgets.candlestick_chart import CandlestickChart
from core.services.chart_service import ChartService


class ChartPanel(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.service = ChartService()

        self.current_coin = None

        self.granularity = 3600

        title = ctk.CTkLabel(
            self,
            text="📈 Live Market Chart",
            font=("Segoe UI", 22, "bold")
        )

        title.pack(pady=(15, 5))

        self.coin_label = ctk.CTkLabel(
            self,
            text="Loading...",
            font=("Segoe UI", 18)
        )

        self.coin_label.pack()

        toolbar = ctk.CTkFrame(self)

        toolbar.pack(
            fill="x",
            padx=15,
            pady=(10, 5)
        )

        timeframes = [
            ("1m", 60),
            ("5m", 300),
            ("15m", 900),
            ("1H", 3600),
            ("6H", 21600),
            ("1D", 86400),
        ]

        for text, value in timeframes:

            ctk.CTkButton(
                toolbar,
                text=text,
                width=55,
                command=lambda g=value: self.change_timeframe(g)
            ).pack(
                side="left",
                padx=3,
                pady=5
            )

        self.chart = CandlestickChart(self)

        self.chart.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(5, 15)
        )

    def change_timeframe(self, granularity):

        self.granularity = granularity

        if self.current_coin:

            self.show_coin(self.current_coin)

    def show_coin(self, coin):

        if coin is None:
            return

        self.current_coin = coin

        self.coin_label.configure(
            text=f"{coin.symbol}   ${coin.price:,.4f}"
        )

        df = self.service.get_candles(
            coin.symbol,
            self.granularity
        )

        if df is not None:

            self.chart.plot_dataframe(
                df,
                coin.symbol
            )
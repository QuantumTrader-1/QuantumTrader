import customtkinter as ctk


class ChartPanel(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(
            self,
            text="📈 Live Chart",
            font=("Segoe UI", 22, "bold")
        )

        title.pack(pady=(15, 10))

        self.coin_label = ctk.CTkLabel(
            self,
            text="Select a Coin",
            font=("Segoe UI", 18)
        )

        self.coin_label.pack(pady=5)

        self.chart = ctk.CTkFrame(
            self,
            height=420,
            corner_radius=12
        )

        self.chart.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.placeholder = ctk.CTkLabel(
            self.chart,
            text="Live Chart Coming Soon",
            font=("Segoe UI", 20)
        )

        self.placeholder.place(
            relx=.5,
            rely=.5,
            anchor="center"
        )

    def show_coin(self, coin):

        if coin:

            self.coin_label.configure(
                text=f"{coin.symbol}   ${coin.price:,.4f}"
            )
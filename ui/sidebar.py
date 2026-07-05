import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master, scan_callback):
        super().__init__(master, width=260)

        self.grid_rowconfigure(10, weight=1)

        self.scan_button = ctk.CTkButton(
            self,
            text="🔄 Scan Market",
            command=scan_callback,
            height=42
        )

        self.scan_button.pack(
            fill="x",
            padx=15,
            pady=(20, 15)
        )

        self.best_title = ctk.CTkLabel(
            self,
            text="⭐ Best Opportunity",
            font=("Segoe UI", 18, "bold")
        )

        self.best_title.pack(pady=(10, 5))

        self.best_box = ctk.CTkTextbox(
            self,
            width=220,
            height=260
        )

        self.best_box.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

    def update_best(self, coin):

        self.best_box.delete("1.0", "end")

        if coin is None:
            return

        self.best_box.insert(
            "end",
            f"""⭐ BEST OPPORTUNITY

Coin:
{coin.symbol}

Score:
{coin.score}

Signal:
{coin.signal}

Risk:
{coin.risk}

Trend:
{coin.trend}

Recommendation:
{coin.recommendation}
"""
        )
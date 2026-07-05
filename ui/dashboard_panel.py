import customtkinter as ctk


class DashboardPanel(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.cards = {}

        stats = [
            ("Coins", "0"),
            ("BUY Signals", "0"),
            ("Avg Score", "0"),
            ("Watchlist", "0"),
        ]

        for i, (title, value) in enumerate(stats):

            card = ctk.CTkFrame(self, corner_radius=12)

            card.grid(
                row=0,
                column=i,
                padx=8,
                pady=8,
                sticky="nsew"
            )

            ctk.CTkLabel(
                card,
                text=title,
                font=("Segoe UI", 14)
            ).pack(pady=(10, 0))

            value_label = ctk.CTkLabel(
                card,
                text=value,
                font=("Segoe UI", 24, "bold")
            )

            value_label.pack(pady=(0, 12))

            self.cards[title] = value_label

    def update_stats(self, analyses):

        self.cards["Coins"].configure(
            text=str(len(analyses))
        )

        buys = sum(
            1 for a in analyses
            if a.signal.upper() == "BUY"
        )

        self.cards["BUY Signals"].configure(
            text=str(buys)
        )

        if analyses:

            avg = sum(
                a.score for a in analyses
            ) / len(analyses)

            self.cards["Avg Score"].configure(
                text=f"{avg:.0f}"
            )

        self.cards["Watchlist"].configure(
            text=str(len(analyses))
        )
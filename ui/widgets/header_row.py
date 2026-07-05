import customtkinter as ctk


class HeaderRow(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        columns = [
            ("★", 40),
            ("Coin", 100),
            ("Score", 70),
            ("Signal", 110),
            ("Risk", 90),
            ("Trend", 110),
            ("24h %", 90),
            ("Price", 120),
            ("Recommendation", 180),
        ]

        for text, width in columns:

            ctk.CTkLabel(
                self,
                text=text,
                width=width,
                anchor="w",
                font=("Segoe UI", 14, "bold"),
            ).pack(side="left", padx=4, pady=6)
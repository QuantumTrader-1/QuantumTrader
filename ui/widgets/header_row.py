import customtkinter as ctk


class HeaderRow(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        columns = [
            ("Coin", 120),
            ("Score", 70),
            ("Signal", 110),
            ("Risk", 90),
            ("Trend", 110),
            ("24h %", 90),
            ("Price", 120),
            ("Recommendation", 180),
        ]

        for text, width in columns:
            label = ctk.CTkLabel(
                self,
                text=text,
                width=width,
                anchor="w",
                font=("Segoe UI", 14, "bold"),
            )
            label.pack(side="left", padx=4, pady=6)
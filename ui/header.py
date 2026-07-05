import customtkinter as ctk


class Header(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, height=70)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        title = ctk.CTkLabel(
            self,
            text="🚀 Quantum Trader",
            font=("Segoe UI", 28, "bold")
        )

        title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=15
        )

        status = ctk.CTkLabel(
            self,
            text="🟢 Atlas Online",
            font=("Segoe UI", 16)
        )

        status.grid(
            row=0,
            column=1,
            padx=20
        )
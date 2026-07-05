import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master, scan_callback):
        super().__init__(master, width=220)

        self.scan_callback = scan_callback

        title = ctk.CTkLabel(
            self,
            text="Navigation",
            font=("Segoe UI", 18, "bold")
        )

        title.pack(pady=(20, 15))

        self._nav_button("🏠 Dashboard")
        self._nav_button("📈 Scanner")
        self._nav_button("⭐ Watchlist")
        self._nav_button("💼 Portfolio")
        self._nav_button("📄 Paper Trading")
        self._nav_button("🔔 Alerts")
        self._nav_button("📰 News")
        self._nav_button("🤖 Atlas AI")
        self._nav_button("⚙ Settings")

        ctk.CTkButton(
            self,
            text="🔄 Scan Market",
            command=self.scan_callback,
            height=40
        ).pack(
            side="bottom",
            fill="x",
            padx=10,
            pady=15
        )

    def _nav_button(self, text):

        ctk.CTkButton(
            self,
            text=text,
            fg_color="transparent",
            anchor="w",
            hover_color="#2B2B2B"
        ).pack(
            fill="x",
            padx=10,
            pady=3
        )

    def update_best(self, coin):
        pass
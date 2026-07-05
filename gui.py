import customtkinter as ctk
from CTkTable import CTkTable

from core.engine import QuantumEngine
from core.services.scanner_service import ScannerService


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class QuantumTraderGUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.engine = QuantumEngine()

        self.scanner = ScannerService(
            self.engine,
            self.refresh_display
        )

        # ---------------- Window ---------------- #

        self.title("🚀 Quantum Trader")
        self.geometry("1450x850")
        self.minsize(1200, 700)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_rowconfigure(2, weight=1)

        # ---------------- Header ---------------- #

        title = ctk.CTkLabel(
            self,
            text="🚀 QUANTUM TRADER",
            font=("Segoe UI", 34, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, pady=(20, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Atlas AI • Crypto Intelligence Engine",
            font=("Segoe UI", 16)
        )
        subtitle.grid(row=1, column=0, columnspan=2, pady=(0, 15))

        # ---------------- Sidebar ---------------- #

        self.sidebar = ctk.CTkFrame(self, width=260)
        self.sidebar.grid(
            row=2,
            column=0,
            sticky="ns",
            padx=15,
            pady=15
        )

        self.scan_button = ctk.CTkButton(
            self.sidebar,
            text="🔄 Scan Now",
            command=self.manual_scan,
            height=42
        )

        self.scan_button.pack(fill="x", padx=15, pady=(20, 10))

        self.best_box = ctk.CTkTextbox(
            self.sidebar,
            width=220,
            height=260
        )

        self.best_box.pack(fill="both", padx=15, pady=15)

        # ---------------- Main ---------------- #

        self.main = ctk.CTkFrame(self)
        self.main.grid(
            row=2,
            column=1,
            sticky="nsew",
            padx=(0, 15),
            pady=15
        )

        self.table_frame = ctk.CTkFrame(self.main)
        self.table_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # Initial Scan

        self.engine.scan_market()
        self.refresh_display()

        # Start Background Scanner

        self.scanner.start()

    def manual_scan(self):

        self.engine.scan_market()
        self.refresh_display()

    def refresh_display(self):

        self.best_box.delete("1.0", "end")

        best = self.engine.best_opportunity()

        if best:

            self.best_box.insert(
                "end",
                f"""⭐ BEST OPPORTUNITY

Coin:
{best.symbol}

Score:
{best.score}

Signal:
{best.signal}

Risk:
{best.risk}

Trend:
{best.trend}

Recommendation:
{best.recommendation}
"""
            )

        for widget in self.table_frame.winfo_children():
            widget.destroy()

        values = [[
            "Coin",
            "Score",
            "Signal",
            "Risk",
            "Trend",
            "24h %",
            "Price",
            "Recommendation"
        ]]

        for coin in self.engine.top_opportunities():

            values.append([
                coin.symbol,
                str(coin.score),
                coin.signal,
                coin.risk,
                coin.trend,
                f"{coin.change:+.2f}%",
                f"${coin.price:,.4f}",
                coin.recommendation
            ])

        table = CTkTable(
            master=self.table_frame,
            values=values
        )

        table.pack(fill="both", expand=True)


if __name__ == "__main__":

    app = QuantumTraderGUI()
    app.mainloop()
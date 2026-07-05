import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class CandlestickChart(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.figure = Figure(
            figsize=(7, 5),
            dpi=100,
            facecolor="#2B2B2B"
        )

        self.ax = self.figure.add_subplot(111)

        self.ax.set_facecolor("#2B2B2B")

        self.canvas = FigureCanvasTkAgg(
            self.figure,
            master=self
        )

        self.canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )

    def plot_dataframe(self, df, symbol):

        self.ax.clear()

        self.ax.set_facecolor("#2B2B2B")

        self.ax.plot(
            df["time"],
            df["close"],
            color="#4EA8FF",
            linewidth=2
        )

        self.ax.fill_between(
            df["time"],
            df["close"],
            alpha=.15,
            color="#4EA8FF"
        )

        self.ax.grid(
            alpha=.2
        )

        self.ax.tick_params(
            colors="white"
        )

        self.ax.spines["bottom"].set_color("gray")
        self.ax.spines["left"].set_color("gray")
        self.ax.spines["top"].set_visible(False)
        self.ax.spines["right"].set_visible(False)

        self.ax.set_title(
            symbol,
            color="white",
            fontsize=14
        )

        self.figure.tight_layout()

        self.canvas.draw()
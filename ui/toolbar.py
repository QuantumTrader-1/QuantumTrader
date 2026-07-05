import customtkinter as ctk


class Toolbar(ctk.CTkFrame):

    def __init__(self, master, refresh_callback, search_callback=None):
        super().__init__(master, height=50)

        self.search_callback = search_callback

        self.grid_columnconfigure(1, weight=1)

        self.refresh_button = ctk.CTkButton(
            self,
            text="🔄 Refresh",
            width=120,
            command=refresh_callback
        )

        self.refresh_button.grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.search = ctk.CTkEntry(
            self,
            placeholder_text="Search symbol..."
        )

        self.search.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=10
        )

        self.search.bind("<KeyRelease>", self.search_changed)

        self.market_count = ctk.CTkLabel(
            self,
            text="Markets: 0"
        )

        self.market_count.grid(
            row=0,
            column=2,
            padx=10
        )

        self.status = ctk.CTkLabel(
            self,
            text="Ready"
        )

        self.status.grid(
            row=0,
            column=3,
            padx=10
        )

    def search_changed(self, event):

        if self.search_callback:

            self.search_callback(
                self.search.get()
            )

    def set_status(self, text):

        self.status.configure(text=text)

    def set_market_count(self, count):

        self.market_count.configure(
            text=f"Markets: {count}"
        )
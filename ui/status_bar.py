import customtkinter as ctk


class StatusBar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.label = ctk.CTkLabel(
            self,
            text="🟢 Ready",
            anchor="w",
            font=("Segoe UI", 13)
        )

        self.label.pack(fill="x", padx=10, pady=6)

    def set_status(self, text):
        self.label.configure(text=text)
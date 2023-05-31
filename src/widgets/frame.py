import customtkinter as ctk


class Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)

        self._setup_ui()

    # Private methods
    def _setup_ui(self) -> None:
        pass

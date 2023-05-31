import customtkinter as ctk
from src.services import Color


class Entry(ctk.CTkEntry):
    def __init__(self, master: ctk.CTkFrame, **kwargs):
        super().__init__(master=master, **kwargs)

        self.__setup_ui()

    # Private methods
    def __setup_ui(self) -> None:
        self.configure(
            font=('Arial', 16, 'bold'),
            fg_color=(Color.SLATE_100.value, Color.SLATE_700.value),
            height=40,
            border_width=0,
            corner_radius=50
        )

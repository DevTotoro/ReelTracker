import customtkinter as ctk
from src.services import Color


class Label(ctk.CTkLabel):
    def __init__(self, master: ctk.CTkFrame, **kwargs):
        super().__init__(master=master, **kwargs)

        self.__setup_ui()

    # Private methods
    def __setup_ui(self) -> None:
        self.configure(
            text_color=(Color.SLATE_900, Color.WHITE)
        )

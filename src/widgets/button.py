import customtkinter as ctk
from src.services import Color


class Button(ctk.CTkButton):
    def __init__(self, master: ctk.CTkFrame, text: str, command: callable, **kwargs):
        super().__init__(master=master, text=text, command=command, **kwargs)

        self.__setup_ui()

    # Private methods
    def __setup_ui(self) -> None:
        self.configure(
            font=('Arial', 16, 'bold'),
            fg_color=Color.TEAL_500.value,
            hover_color=Color.TEAL_400.value,
            text_color=Color.WHITE.value,
            height=40,
            corner_radius=50
        )

import customtkinter as ctk


class Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)

        self.__setup_ui()

    # Private methods
    def __setup_ui(self) -> None:
        pass

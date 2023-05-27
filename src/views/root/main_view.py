from .base_root_view import BaseRootView
import customtkinter as ctk


class MainView(BaseRootView):
    def __init__(self, master: ctk.CTk):
        super().__init__(master=master)

        self.__setup_ui()

    # Private methods
    def __setup_ui(self) -> None:
        button = ctk.CTkButton(master=self, text='Hello, World!', command=lambda: print('Hello, World!'))
        button.pack()

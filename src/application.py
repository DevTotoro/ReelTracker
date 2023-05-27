import tkinter as tk
import customtkinter as ctk

from services.theme import Theme


class Application(ctk.CTk):
    def __init__(
            self,
            title: str = 'App',
            width: int = 300,
            height: int = 300,
            resizable: bool = False,
            theme: Theme = Theme()
    ):
        super().__init__()

        self.__theme = theme

        self.title(title)
        self.geometry(f'{width}x{height}')
        self.resizable(resizable, resizable)

        self.__setup_ui()

    def run(self):
        self.mainloop()

    # Private methods
    def __setup_ui(self):
        button = ctk.CTkButton(master=self, text='Hello, World!', command=lambda: print('Hello, World!'))
        button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

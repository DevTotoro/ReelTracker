from tkinter import CENTER as TK_CENTER
import customtkinter as ctk
from abc import ABC, abstractmethod

from src.services import Color


# Abstract class representing a view placed directly on the root window
class BaseRootView(ctk.CTkFrame, ABC):
    def __init__(self, master: ctk.CTk):
        super().__init__(master=master)

        self.configure(fg_color=(Color.WHITE.value, Color.SLATE_800.value))

        self._setup_ui()

    def show(self):
        self.place(relx=0.5, rely=0.5, anchor=TK_CENTER, relwidth=1, relheight=1)

    def hide(self):
        self.place_forget()

    @abstractmethod
    def _setup_ui(self):
        pass

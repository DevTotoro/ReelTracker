from tkinter import CENTER as TK_CENTER
import customtkinter as ctk
from abc import ABC


# Abstract class representing a view placed directly on the root window
class BaseRootView(ctk.CTkFrame, ABC):
    def __init__(self, master: ctk.CTk):
        super().__init__(master=master)

    def show(self):
        self.place(relx=0.5, rely=0.5, anchor=TK_CENTER)

    def hide(self):
        self.place_forget()

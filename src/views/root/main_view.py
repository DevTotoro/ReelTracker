from customtkinter import CTk as ctkWindow
from .base_root_view import BaseRootView
from src.widgets import Frame, Label


class MainView(BaseRootView):
    def __init__(self, master: ctkWindow):
        super().__init__(master=master)

    # Private methods
    def _setup_ui(self) -> None:
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        center_frame = Frame(master=self, fg_color='transparent')
        center_frame.grid(row=0, column=0)

        Label(master=center_frame, text='Main View', font=('Arial', 24, 'bold')) \
            .grid(row=0, column=0, sticky='ew')

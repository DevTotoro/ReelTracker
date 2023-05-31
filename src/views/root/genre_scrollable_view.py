from src.widgets import ScrollableFrame, MoviesFrame, Label
from src.services import Color
import customtkinter as Ctk

class GenreScrollableView(ScrollableFrame):
    counter=0
    controller = {}
    
    def __init__(self, master, name, **kwargs):
        super().__init__(master,  **kwargs)
        self.name = name
        
    def _setup_ui(self) -> None:
        self.grid_columnconfigure(0, weight=1)
    
    def add_item(self, genre):
        Label(self, text=genre, font=Ctk.CTkFont(size=19)).grid(row=self.counter, column=0, padx=20)
        self.controller[genre] = MoviesFrame(master=self, height=150, fg_color=Color.GRAY_3.value)
        self.controller[genre].grid(row=self.counter+1, column=0, sticky='wens', padx=20)
        
        
        self.counter += 2
    
    def clear(self) -> None:
        for widget in self.winfo_children():
            widget.destroy()
        self.counter=0
        
    def show(self) -> None: 
        self.grid(row=1, column=0, sticky='nwes', columnspan=2, rowspan=3)
    
    def hide(self) -> None:
        self.grid_forget()
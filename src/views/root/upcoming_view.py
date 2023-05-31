import customtkinter as Ctk
from .base_root_view import BaseRootView
from src.widgets import Label, ScrollableFrame, Frame
from src.services import Color


class UpcomingView(BaseRootView):
    counter=0
    
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color=Color.GRAY_3.value, **kwargs)
        
    def _setup_ui(self) -> None:
        
        Label(self, text='Upcoming', font=Ctk.CTkFont(size=16)).place(relx=0.05, rely=0.05)
        self.scrollable_frame = ScrollableFrame(self, corner_radius=0, fg_color='transparent', scrollbar_button_color=Color.GRAY_3.value, scrollbar_button_hover_color=Color.GRAY_3.value)
        self.scrollable_frame.place(relx=0.01, rely=0.15, relwidth=0.98, relheight=0.84)

    
    def add_item(self, name, timestamp):
        frame = Frame(self.scrollable_frame, corner_radius=0, height=30, width=280, fg_color='transparent')
        Label(frame, text=name, font=Ctk.CTkFont(size=14)).place(relx=0.05, rely=0.05)
        Label(frame, text=timestamp, font=Ctk.CTkFont(size=16)).place(relx=0.70, rely=0.05)
        frame.grid(row=self.counter, column=0)
        
        self.counter += 1
        
        
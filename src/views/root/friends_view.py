import customtkinter as Ctk
from .base_root_view import BaseRootView
from src.widgets import Label, ScrollableFrame, Friend
from src.services import Color


class FriendsView(BaseRootView):
    counter=0
    
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color=Color.GRAY_3.value, **kwargs)
        
    def _setup_ui(self) -> None:
        Label(self, text='Friends', font=Ctk.CTkFont(size=16)).place(relx=0.05, rely=0.05)
        self.scrollable_frame = ScrollableFrame(self, corner_radius=0, fg_color='transparent', scrollbar_button_color=Color.GRAY_3.value, scrollbar_button_hover_color=Color.GRAY_3.value)
        self.scrollable_frame.place(relx=0.01, rely=0.15, relwidth=0.98, relheight=0.84)

    def add_friend(self, username, status):
        self.friend = Friend(self.scrollable_frame, corner_radius=0, height=50, width=280, username=username, status=status, fg_color='transparent')
        self.friend.grid(row=self.counter, column=0, sticky='ew')
        
        self.counter += 1
        
        
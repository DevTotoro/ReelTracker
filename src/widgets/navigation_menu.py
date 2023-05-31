from src.widgets import Frame
import customtkinter as Ctk
from src.services import Color

class NavigationMenu(Frame):
    controller = None
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        
        self.__setup_ui()

    # Private methods
    def __setup_ui(self) -> None:
        
        self.tabs = {
            'Home': Ctk.CTkButton(self, text='Home', height=40, width=150, corner_radius=4, command=lambda tab_name='Home': self.button_clicked(tab_name), 
                                fg_color=Color.GRAY_3.value, hover_color=Color.GRAY_2.value),
            'Movies': Ctk.CTkButton(self, text='Movies', height=40, width=150, corner_radius=4, command=lambda tab_name='Movies': self.button_clicked(tab_name), 
                                    fg_color=Color.GRAY_3.value, hover_color=Color.GRAY_2.value),
            'Series': Ctk.CTkButton(self, text='Series', height=40, width=150, corner_radius=4, command=lambda tab_name='Series': self.button_clicked(tab_name), 
                                    fg_color=Color.GRAY_3.value, hover_color=Color.GRAY_2.value),
            'Watch List': Ctk.CTkButton(self, text='Watch List', height=40, width=150, corner_radius=4, command=lambda tab_name='Watch List': self.button_clicked(tab_name), 
                                    fg_color=Color.GRAY_3.value, hover_color=Color.GRAY_2.value)
        }
        
        self.tabs['Home'].grid(row=0, column=0)
        self.tabs['Movies'].grid(row=0, column=1)
        self.tabs['Series'].grid(row=0, column=2)
        self.tabs['Watch List'].grid(row=0, column=3)
        
    def button_clicked(self,tab_name):
        for tab in self.tabs.keys():
            
            self.tabs[tab].configure(fg_color=Color.GRAY_3.value)
            self.controller[tab].hide()
        
        self.tabs[tab_name].configure(fg_color=Color.GRAY_1.value)
        self.controller[tab_name].show()
        
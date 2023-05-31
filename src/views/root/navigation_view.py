from .base_root_view import BaseRootView
from src.widgets import NavigationMenu, SearchBar, Image, Label
from src.services import Color


class NavigationView(BaseRootView):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color=Color.GRAY_4.value, **kwargs)
        self.configure(height=70)
        
    def _setup_ui(self) -> None:
        self.navigation_menu = NavigationMenu(master=self, width=500, height=40, corner_radius=0, fg_color='transparent')
        self.navigation_menu.place(relx= 0.02, rely=0.5, anchor='w')
        
        self.search_bar = SearchBar(self, corner_radius=5, fg_color='transparent')
        self.search_bar.place(relx=0.7, rely=0.5, anchor='w', relwidth=0.23, relheight=0.33)
        
        Label(self, text="", image=Image(image_name="profile_icon.png", size=(30, 30)), fg_color="transparent").place(relx=0.95, rely=0.38)
        

    def set_controller(self, controller):
        self.navigation_menu.controller = controller
        
        
        

        
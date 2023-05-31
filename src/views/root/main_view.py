from customtkinter import CTk as ctkWindow
from .base_root_view import BaseRootView
from .navigation_view import NavigationView
from .friends_view import FriendsView
from .upcoming_view import UpcomingView
from .genre_scrollable_view import GenreScrollableView
from src.models import User
from src.services import Color
from src.widgets import Image, SearchFrame



class MainView(BaseRootView):
    def __init__(self, master: ctkWindow, user: User):
        super().__init__(master=master)

        self.__user = user

    # Private methods
    def _setup_ui(self) -> None:
        self.grid_columnconfigure((0,1), weight=4)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure((0,2), weight=1)
        self.grid_rowconfigure((1,3), weight=4)

        self.navigation_view = NavigationView(self, corner_radius=0)
        self.navigation_view.grid(row=0,column=0, sticky='nswe', columnspan=2)
 
        self.friends_view = FriendsView(self, corner_radius=0, border_color=Color.BLACK.value, border_width=2)  
        self.friends_view.grid(row=0, column=2, sticky='nwes', rowspan=2)
        self.friends_view.add_friend('alex', 'online')
        self.friends_view.add_friend('thodoris', 'offline')
        self.friends_view.add_friend('giannis', 'online')
        
        self.upcoming_frame = UpcomingView(self, corner_radius=0, border_color=Color.BLACK.value, border_width=2)
        self.upcoming_frame.grid(row=2, column=2, sticky='nwes', rowspan=2)
        self.upcoming_frame.add_item('The Last Of Us','3d 7h 32m')
        self.upcoming_frame.add_item('The Last Of Us','3d 7h 32m')
        
        self.controller = {
            'Home': GenreScrollableView(self, name='Home', corner_radius=0, fg_color=Color.GRAY_4.value, scrollbar_button_color=Color.GRAY_4.value, scrollbar_button_hover_color=Color.GRAY_4.value),
            'Movies': GenreScrollableView(self, name='Movies', corner_radius=0, fg_color=Color.GRAY_4.value, scrollbar_button_color=Color.GRAY_4.value, scrollbar_button_hover_color=Color.GRAY_4.value),
            'Series': GenreScrollableView(self, name='Series', corner_radius=0, fg_color=Color.GRAY_4.value, scrollbar_button_color=Color.GRAY_4.value, scrollbar_button_hover_color=Color.GRAY_4.value),
            'Watch List': GenreScrollableView(self, name='Watch List', corner_radius=0, fg_color=Color.GRAY_4.value, scrollbar_button_color=Color.GRAY_4.value, scrollbar_button_hover_color=Color.GRAY_4.value)
        }
        
        self.navigation_view.set_controller(self.controller)
        self.navigation_view.navigation_menu.button_clicked('Home')
        self.controller['Home'].add_item('Popular')
        self.controller['Home'].add_item('For You')
        
        image = Image(image_name="image_not_found_icon.jpg", size=(100, 145))
        self.controller['Home'].controller['Popular'].add_item(image)
        self.controller['Home'].controller['Popular'].add_item(image)
        self.controller['Home'].controller['Popular'].add_item(image)
        self.controller['Home'].controller['Popular'].add_item(image)
        self.controller['Home'].controller['Popular'].add_item(image)
        self.controller['Home'].controller['Popular'].add_item(image)
        self.controller['Home'].controller['Popular'].add_item(image)
        self.controller['Home'].controller['Popular'].add_item(image)
        self.controller['Home'].controller['Popular'].add_item(image)
        
        image_50 = Image(image_name="image_not_found_icon.jpg", size=(50, 73))
        self.search_frame =SearchFrame(self, width = 200, height=150, corner_radius=0, fg_color=Color.GRAY_3.value, 
                    scrollbar_button_color=Color.GRAY_3.value, scrollbar_button_hover_color=Color.GRAY_3.value)
        self.navigation_view.search_bar.search_frame = self.search_frame
        
        self.search_frame.add_item(image=image_50, name='Movie Name')
        self.search_frame.add_item(image=image_50, name='Movie Name 2')
        self.search_frame.add_item(image=image_50, name='Movie Name 3')
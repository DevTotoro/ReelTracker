from customtkinter import CTk as ctkWindow
from .base_root_view import BaseRootView
from .navigation_view import NavigationView
from .friends_view import FriendsView
from .upcoming_view import UpcomingView
from .details_view import DetailsView
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
 
        self.friends_view = FriendsView(self, corner_radius=0, border_color=Color.BLACK.value, border_width=2)  
        self.friends_view.grid(row=0, column=2, sticky='nwes', rowspan=2)
        self.friends_view.add_friend('alex', 'online')
        self.friends_view.add_friend('thodoris', 'offline')
        self.friends_view.add_friend('giannis', 'online')
        
        self.upcoming_frame = UpcomingView(self, corner_radius=0, border_color=Color.BLACK.value, border_width=2)
        self.upcoming_frame.grid(row=2, column=2, sticky='nwes', rowspan=2)
        self.upcoming_frame.add_item('The Last Of Us','3d 7h 32m')
        self.upcoming_frame.add_item('The Last Of Us','3d 7h 32m')
        
        self.navigation_controller = {}
        
        home_view = GenreScrollableView(self, name='Home', navigation_controller=self.navigation_controller, corner_radius=0, fg_color=Color.GRAY_4.value, scrollbar_button_color=Color.GRAY_4.value, scrollbar_button_hover_color=Color.GRAY_4.value)
        movies_view = GenreScrollableView(self, name='Movies', navigation_controller=self.navigation_controller, corner_radius=0, fg_color=Color.GRAY_4.value, scrollbar_button_color=Color.GRAY_4.value, scrollbar_button_hover_color=Color.GRAY_4.value)
        series_view = GenreScrollableView(self, name='Series', navigation_controller=self.navigation_controller, corner_radius=0, fg_color=Color.GRAY_4.value, scrollbar_button_color=Color.GRAY_4.value, scrollbar_button_hover_color=Color.GRAY_4.value)
        watchlist_view = GenreScrollableView(self, name='Watch List', navigation_controller=self.navigation_controller, corner_radius=0, fg_color=Color.GRAY_4.value, scrollbar_button_color=Color.GRAY_4.value, scrollbar_button_hover_color=Color.GRAY_4.value)
        details_view = DetailsView(self, navigation_controller=self.navigation_controller, corner_radius=0, fg_color=Color.GRAY_4.value)
        
        self.navigation_controller['Home'] = home_view
        self.navigation_controller['Movies'] = movies_view
        self.navigation_controller['Series'] = series_view
        self.navigation_controller['Watch List'] = watchlist_view
        self.navigation_controller['Details'] = details_view
        
        self.navigation_view = NavigationView(self, corner_radius=0, navigation_controller=self.navigation_controller)
        self.navigation_view.grid(row=0,column=0, sticky='nswe', columnspan=2)
        
                
        self.navigation_controller['Details'].grid(row=1, column=0, sticky='nwes', columnspan=2, rowspan=3)
        self.navigation_view.navigation_menu.button_clicked('Home')
        
        
        image_50 = Image(image_name="image_not_found_icon.jpg", size=(50, 73))
        self.search_frame =SearchFrame(self, navigation_controller=self.navigation_controller, width = 200, height=150, corner_radius=0, fg_color=Color.GRAY_3.value, 
                    scrollbar_button_color=Color.GRAY_3.value, scrollbar_button_hover_color=Color.GRAY_3.value)
        self.navigation_view.search_bar.search_frame = self.search_frame
        
       
import customtkinter
import os
from PIL import Image
from MovieAPI import MovieApi
import tracemalloc
import threading 

from ScrollableFrame import ScrollableFrame
from ScrollableFrameFriends import ScrollableFrameFriends
from ScrollableFrameUpcoming import ScrollableFrameUpcoming
from ScrollableFrameSearch import ScrollableFrameSearch

tracemalloc.start()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
movie_api = MovieApi()
    

class App(customtkinter.CTk):
    # id for threading
    thread_id = 0
    
    
    def __init__(self):
        super().__init__()

        # Configure Main Window
        self.geometry("1200x600")
        self.title("ReelTracker")
        self.resizable(0,0)

        # INITIALIZE OBJECTS
        
        # FRAMES
        self.main_frame = customtkinter.CTkFrame(self, width=1200, height=600, corner_radius=0, fg_color="gray10")
        self.navigation_menu = customtkinter.CTkFrame(self.main_frame, width=400, height=30, corner_radius=0)
        self.friends_frame = customtkinter.CTkFrame(self.main_frame, width=540, height=350, corner_radius=0, border_color= "gray7", 
                                                    border_width=2)
        self.upcoming_frame = customtkinter.CTkFrame(self.main_frame, width=540, height=300, corner_radius=0, border_color= "gray7",
                                                     border_width=2)
        self.scrollable_frame_home = ScrollableFrame(master=self.main_frame, width=800, height=400, fg_color="transparent", 
                                                scrollbar_button_color="gray10", scrollbar_button_hover_color="gray10",is_movies=False)
        self.scrollable_frame_movies = ScrollableFrame(master=self.main_frame, width=800, height=400, fg_color="transparent", 
                                                scrollbar_button_color="gray10", scrollbar_button_hover_color="gray10",is_movies=True)
        self.scrollable_frame_series = ScrollableFrame(master=self.main_frame, width=800, height=400, fg_color="transparent", 
                                                scrollbar_button_color="gray10", scrollbar_button_hover_color="gray10",is_movies=False)
        self.scrollable_frame_watchlist = ScrollableFrame(master=self.main_frame, width=800, height=400, fg_color="transparent", 
                                                scrollbar_button_color="gray10", scrollbar_button_hover_color="gray10",is_movies=False)
        self.scrollable_frame_friends = ScrollableFrameFriends(self.friends_frame, width=538, height=310, corner_radius=0, 
                                                               fg_color="gray13" )
        self.scrollable_frame_Upcoming = ScrollableFrameUpcoming(self.upcoming_frame, width=538, height=260, corner_radius=0, 
                                                                 fg_color="gray13")
        self.search_field_frame = customtkinter.CTkFrame(self.main_frame, width=210, height=20, corner_radius=5, fg_color="transparent")
        self.scrollable_search_frame = ScrollableFrameSearch(self.main_frame, width=194, height=150, corner_radius=0,
                                                            scrollbar_button_color="gray13", scrollbar_button_hover_color="gray13")

        # BUTTONS
        self.home_button = customtkinter.CTkButton(self.navigation_menu, corner_radius=0, text="Home", text_color=("gray10", "gray90"), 
                                                   border_color="gray11", border_width=1, fg_color=("gray75", "gray25"), 
                                                   hover_color=("gray70", "gray30"), command=self.home_button_event)
        self.movies_button = customtkinter.CTkButton(self.navigation_menu, corner_radius=0, text="Movies", text_color=("gray10", "gray90"), 
                                                     border_color="gray11", border_width=1, fg_color="transparent", 
                                                     hover_color=("gray70", "gray30"), command=self.movies_button_event)
        self.series_button = customtkinter.CTkButton(self.navigation_menu, corner_radius=0, text="Series", text_color=("gray10", "gray90"), 
                                                     border_color="gray11", border_width=1, fg_color="transparent", 
                                                     hover_color=("gray70", "gray30"), command=self.series_button_event)
        self.watchlist_button = customtkinter.CTkButton(self.navigation_menu, corner_radius=0, text="Watch List", text_color=("gray10", "gray90"), 
                                                        border_color="gray11", border_width=1, fg_color="transparent", 
                                                        hover_color=("gray70", "gray30"), command=self.watchlist_button_event)
        
        # IMAGES
        self.search_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "search_icon.png")), size=(17, 17))
        self.profile_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "profile_icon.png")), size=(30, 30))
        
        
        # TEXT BOX
        self.search_field = customtkinter.CTkTextbox(self.search_field_frame, width=210, height=20, corner_radius=5, padx=35)
        
        # LABELS
        self.search_image_label = customtkinter.CTkLabel(self.search_field, text="", image=self.search_image)
        self.profile_image_label = customtkinter.CTkLabel(self.main_frame, text="", image=self.profile_image, fg_color="transparent")
        
        self.friends_label = customtkinter.CTkLabel(self.friends_frame, text="Friends", font=customtkinter.CTkFont(size=14), text_color="gray55")
        self.Upcoming_label = customtkinter.CTkLabel(self.upcoming_frame, text="Upcoming", font=customtkinter.CTkFont(size=14), text_color="gray55")
        
        
        # GRID OBJECTS
        
        # FRAMES
        self.main_frame.grid(row=0, column=0, sticky="nw", padx=0, pady=0)
        self.navigation_menu.grid(row=0, column=0, sticky="nw", padx=30, pady=30)
        self.friends_frame.grid(row=0, column=0, sticky="ne")
        self.upcoming_frame.grid(row=0, column=0, sticky="se")
        self.scrollable_frame_home.grid(row=0, column=0, padx=50, pady=100, sticky="nw")
        self.scrollable_frame_movies.grid(row=0, column=0, padx=50, pady=100, sticky="nw")
        self.scrollable_frame_series.grid(row=0, column=0, padx=50, pady=100, sticky="nw")
        self.scrollable_frame_watchlist.grid(row=0, column=0, padx=50, pady=100, sticky="nw")
        self.scrollable_frame_friends.grid(row=0, column=0, sticky="ne", pady=40, padx=2)
        self.scrollable_frame_Upcoming.grid(row=0, column=0, sticky="se", pady=40, padx=2)
        self.search_field_frame.grid(row=0, column=0, sticky="nw", padx=640, pady=30)
        
        
        # BUTTONS
        self.home_button.grid(row=0, column=0)
        self.movies_button.grid(row=0, column=1)
        self.series_button.grid(row=0, column=2)
        self.watchlist_button.grid(row=0, column=3)
        
        # TEXT BOX
        self.search_field.grid(row=0, column=0,  sticky="nw", padx=0, pady=0)
        self.search_field.insert("0.0","Search")
        
        # LABELS
        self.search_image_label.grid(row=0, column=0, sticky="nw", padx=5, pady=0)
        self.profile_image_label.grid(row=0, column=0, sticky="ne", padx=580, pady=30)
        self.friends_label.grid(row=0, column=0, sticky="nw", padx=20, pady=10)
        self.Upcoming_label.grid(row=0, column=0, sticky="nw", padx=20, pady=10)
        
        # BIND EVENTS TO FUNCTIONS
        
        self.main_frame.bind("<Button-1>",self.remove_focus)
        self.friends_frame.bind("<Button-1>",self.remove_focus)
        self.upcoming_frame.bind("<Button-1>",self.remove_focus)
        self.scrollable_frame_home.bind("<Button-1>",self.remove_focus)
        self.scrollable_frame_movies.bind("<Button-1>",self.remove_focus)
        self.scrollable_frame_series.bind("<Button-1>",self.remove_focus)
        self.scrollable_frame_watchlist.bind("<Button-1>",self.remove_focus)
        self.scrollable_frame_friends.bind("<Button-1>",self.remove_focus)
        self.scrollable_frame_Upcoming.bind("<Button-1>",self.remove_focus)
        self.search_field.bind("<Button-1>",self.clear_search_field)
        self.search_field.bind("<Key>", self.key_pressed)
        
        # initialize frames content 
        #self.initialize_home_tab()
        self.initialize_movies_tab()
        self.initialize_series_tab()
        #self.initialize_watchlist_tab()
        
        # hide frames and only show home page
        self.scrollable_frame_movies.grid_forget()
        self.scrollable_frame_series.grid_forget()
        self.scrollable_frame_watchlist.grid_forget()
        
        # ADD ITEMS TO OBJECTS
        self.scrollable_frame_friends.add_friend("Jhon","online")
        self.scrollable_frame_friends.add_friend("Alex","offline")
        self.scrollable_frame_friends.add_friend("Thodoris","online")
        self.scrollable_frame_friends.add_friend("Giannis","online")
        self.scrollable_frame_friends.add_friend("David","offline")
        self.scrollable_frame_friends.add_friend("James","online")
        self.scrollable_frame_friends.add_friend("Tom","online")
        self.scrollable_frame_friends.add_friend("Carlos","offline")
        self.scrollable_frame_friends.add_friend("Peter","online")
 
                
    # Event Handling Functions
    
    # event handler for clicking navigation menu home 
    def home_button_event(self):
        # highlight home tab
        self.home_button.configure(fg_color=("gray75", "gray25"))
        self.movies_button.configure(fg_color="transparent")
        self.series_button.configure(fg_color="transparent")
        self.watchlist_button.configure(fg_color="transparent")
        
        # hide frames
        self.scrollable_frame_movies.grid_forget()
        self.scrollable_frame_series.grid_forget()
        self.scrollable_frame_watchlist.grid_forget()
        
        # show home frame
        self.scrollable_frame_home.grid(row=0, column=0, padx=50, pady=100, sticky="nw")
        
        
    # event handler for clicking navigation menu movies
    def movies_button_event(self):
        # highlight movie tab
        self.movies_button.configure(fg_color=("gray75", "gray25"))
        self.home_button.configure(fg_color="transparent")
        self.series_button.configure(fg_color="transparent")
        self.watchlist_button.configure(fg_color="transparent")
        
        # hide frames
        self.scrollable_frame_home.grid_forget()
        self.scrollable_frame_series.grid_forget()
        self.scrollable_frame_watchlist.grid_forget()
        
        # show movies frame
        self.scrollable_frame_movies.grid(row=0, column=0, padx=50, pady=100, sticky="nw")
        
        
        
    # event handler for clicking navigation menu series 
    def series_button_event(self):
        # highlight series tab
        self.series_button.configure(fg_color=("gray75", "gray25"))
        self.home_button.configure(fg_color="transparent")
        self.movies_button.configure(fg_color="transparent")
        self.watchlist_button.configure(fg_color="transparent")
        
        # hide frames
        self.scrollable_frame_home.grid_forget()
        self.scrollable_frame_movies.grid_forget()
        self.scrollable_frame_watchlist.grid_forget()
        
        # show series frame
        self.scrollable_frame_series.grid(row=0, column=0, padx=50, pady=100, sticky="nw")
        
    
    # event handler for clicking navigation menu watch list       
    def watchlist_button_event(self):
        # highlight watchlist tab
        self.watchlist_button.configure(fg_color=("gray75", "gray25"))
        self.home_button.configure(fg_color="transparent")
        self.movies_button.configure(fg_color="transparent")
        self.series_button.configure(fg_color="transparent")
        
        # hide frames
        self.scrollable_frame_home.grid_forget()
        self.scrollable_frame_movies.grid_forget()
        self.scrollable_frame_series.grid_forget()
        
        # show series frame
        self.scrollable_frame_watchlist.grid(row=0, column=0, padx=50, pady=100, sticky="nw")
        
    # event handler for clicking in search field for the first time
    def clear_search_field(self,e):
        if self.search_field.get("current linestart","current lineend") == "Search":
            self.search_field.delete("current linestart","current lineend")
    
    # event handler for clicking outside of search field
    def remove_focus(self,e):
        self.focus()
    
    # function that initializes watchlist tab
    def initialize_watchlist_tab(self):
        self.scrollable_frame_watchlist.add_item("Continue Watching")
        self.scrollable_frame_watchlist.add_item("Watch Again")
    
    # function that initializes series tab
    def initialize_series_tab(self):
        # for every series genre 
        for key in movie_api.series_genre.keys():
            # create a scrollable frame with label and next button
            self.scrollable_frame_series.add_item(key)
            # search for the first 7 series and add them to frame
            threading.Thread(target=movie_api.search_series_by_genre, args=(movie_api.series_genre[key],self.scrollable_frame_series.scrollable_frame,0,7)).start()
    
    # function that initializes movies tab
    def initialize_movies_tab(self):
        # for every movie genre
        for key in movie_api.movie_genre.keys():
            # create a scrollable frame with label and next button
            self.scrollable_frame_movies.add_item(key)
            # search for the first 7 movies and add them to frame      
            threading.Thread(target=movie_api.search_movies_by_genre, args=(movie_api.movie_genre[key],self.scrollable_frame_movies.scrollable_frame,0,7)).start()

    # function that initializes home tab
    def initialize_home_tab(self):
        self.scrollable_frame_home.add_item("Continue Watching")
        self.scrollable_frame_home.add_item("Watch Again")
        
    # search field key pressed event handler
    def key_pressed(self,e):
        # case: search field empty after hitting backspace
        if len(self.search_field.get("current linestart","current lineend")) == 1 and ord(e.char) == 8:
            # if scrollable search frame is visible
            if self.scrollable_search_frame:
                # hide scrollable search frame 
                self.scrollable_search_frame.grid_forget()      
        else:
            # case: empty field and press key except backspace
            if self.search_field.get("current linestart","current lineend") == "" and ord(e.char) != 8:
                # clear scrollable search frame and set it visible
                self.scrollable_search_frame.clear()
                self.scrollable_search_frame.grid(row=0, column=0, sticky="nw", padx=640, pady=68)
            else:
                # case: we hit a key and none of the above cases hold
                self.scrollable_search_frame.clear()
                
            # set exit_flag for every other running thread
            # we do this to kill every other thread so they dont add random movies
            for thread_id in movie_api.exit_flags.keys():
                exit_flag =  movie_api.exit_flags[thread_id]
                exit_flag.set()
            
            self.thread_id += 1
            # create exit_flag for thread 
            exit_flag = threading.Event()
            # create thread
            thread = threading.Thread(target=movie_api.search_movies, args=(self.search_field.get("current linestart","current lineend")+e.char,self.scrollable_search_frame,0,5,self.thread_id))
            # add current thread exit flag to dictionary
            movie_api.exit_flags[self.thread_id] = exit_flag
            # start thread
            thread.start()
            
            

app = App()
app.mainloop()

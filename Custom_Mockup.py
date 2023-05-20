import tkinter
import customtkinter
import os
from PIL import Image


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class ScrollableFrameFriends(customtkinter.CTkScrollableFrame):
    friends_name = []
    friend_status = []
    padx=30
    pady=0
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
    
    def add_friend(self, name, status, image_path):
        # PLACE PROFILE ICON
        self.profile_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "profile_icon.png")), size=(30, 30))
        self.profile_image_label = customtkinter.CTkLabel(self, text="", image=self.profile_image, fg_color="transparent")
        self.profile_image_label.grid(row=0, column=0, sticky="nw", padx=self.padx, pady=self.pady)
        
        # PLACE STATUS ICON
        self.status_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "online_icon.jpg" if status=="online" else "offline_icon.png")), size=(15, 15) if status=="online" else (10.5,10.5))
        self.status_image_label = customtkinter.CTkLabel(self, text="", image=self.status_image, fg_color="transparent")
        self.status_image_label.grid(row=0, column=0, sticky="nw", padx=self.padx+40 if status =="online" else self.padx+43, pady=self.pady+3)
        
        # PLACE NAME LABEL
        self.name_label = customtkinter.CTkLabel(self, text=name, font=customtkinter.CTkFont(size=14), text_color="gray75")
        self.name_label.grid(row=0, column=0, sticky="nw", padx=self.padx+65, pady=self.pady+3)
        
        # INCREASE PADDING IN Y 
        self.pady += 40
        

class ScrollableFrameUpcoming(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
    
class ScrollableFrameMovies(customtkinter.CTkScrollableFrame):
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
    padx = 0
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.add_item()
        self.add_item()
        self.add_item()
        self.add_item()
        self.add_item()
        self.add_item()
        self.add_item()
        self.add_item()
        self.add_item()
        
    def add_item(self):
        self.movie_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "image_not_found_icon.jpg")), size=(100, 150))
        self.search_image_label = customtkinter.CTkLabel(self, text="", image=self.movie_image)
        self.search_image_label.grid(row=0, column=0, sticky="nw", padx=self.padx)
        self.padx += 110
        
        
class ScrollableFrame(customtkinter.CTkScrollableFrame):
    padx=0
    pady=0
    
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        
        
    def add_item(self, name):
        #PLACE GENRE LABEL OR LIST_NAME LABEL
        self.label = customtkinter.CTkLabel(self, text=name, font=customtkinter.CTkFont(size=19))
        self.label.grid(row=0, column=0, sticky="nw", padx=self.padx, pady=self.pady)
        
        # PLACE IMAGES SCROLLABLE FRAME
        self.scrollable_frame = ScrollableFrameMovies(master=self, height=150, width=780, orientation="horizontal", scrollbar_button_color="gray13", scrollbar_button_hover_color="gray26")
        self.scrollable_frame.grid(row=0, column=0, padx=0, pady=self.pady+30, sticky="new")
        
        # INCREASE PADDING IN Y
        self.pady += 210
        
    

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # Initialize path for icons
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

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
        self.scrollable_frame = ScrollableFrame(master=self.main_frame, width=800, height=400, fg_color="transparent", 
                                                scrollbar_button_color="gray10", scrollbar_button_hover_color="gray10")
        self.scrollable_frame_friends = ScrollableFrameFriends(self.friends_frame, width=538, height=310, corner_radius=0, 
                                                               fg_color="gray13" )
        self.scrollable_frame_Upcoming = ScrollableFrameUpcoming(self.upcoming_frame, width=538, height=260, corner_radius=0, 
                                                                 fg_color="gray13")
        self.search_field_frame = customtkinter.CTkFrame(self.main_frame, width=210, height=20, corner_radius=5)

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
        self.scrollable_frame.grid(row=0, column=0, padx=50, pady=100, sticky="nw")
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
        self.scrollable_frame.bind("<Button-1>",self.remove_focus)
        self.scrollable_frame_friends.bind("<Button-1>",self.remove_focus)
        self.scrollable_frame_Upcoming.bind("<Button-1>",self.remove_focus)
        self.search_field.bind("<Button-1>",self.clear_search_field)
        
        
        # ADD ITEMS TO OBJECTS
        
        self.scrollable_frame.add_item("Continue Watching")
        self.scrollable_frame.add_item("Watch Again")
        self.scrollable_frame_friends.add_friend("Jhon","online",image_path=image_path)
        self.scrollable_frame_friends.add_friend("Alex","offline",image_path=image_path)
        self.scrollable_frame_friends.add_friend("Thodoris","online",image_path=image_path)
        self.scrollable_frame_friends.add_friend("Giannis","online",image_path=image_path)
        self.scrollable_frame_friends.add_friend("David","offline",image_path=image_path)
        self.scrollable_frame_friends.add_friend("James","online",image_path=image_path)
        self.scrollable_frame_friends.add_friend("Tom","online",image_path=image_path)
        self.scrollable_frame_friends.add_friend("Carlos","offline",image_path=image_path)
        self.scrollable_frame_friends.add_friend("Peter","online",image_path=image_path)
 
    # Event Handling Functions
    def home_button_event(self):
        self.home_button.configure(fg_color=("gray75", "gray25"))
        self.movies_button.configure(fg_color="transparent")
        self.series_button.configure(fg_color="transparent")
        self.watchlist_button.configure(fg_color="transparent")

    def movies_button_event(self):
        self.movies_button.configure(fg_color=("gray75", "gray25"))
        self.home_button.configure(fg_color="transparent")
        self.series_button.configure(fg_color="transparent")
        self.watchlist_button.configure(fg_color="transparent")
        
    def series_button_event(self):
        self.series_button.configure(fg_color=("gray75", "gray25"))
        self.home_button.configure(fg_color="transparent")
        self.movies_button.configure(fg_color="transparent")
        self.watchlist_button.configure(fg_color="transparent")
            
    def watchlist_button_event(self):
        self.watchlist_button.configure(fg_color=("gray75", "gray25"))
        self.home_button.configure(fg_color="transparent")
        self.movies_button.configure(fg_color="transparent")
        self.series_button.configure(fg_color="transparent")
        
    def clear_search_field(self,e):
        self.search_field.delete("current linestart","current lineend")
    
    def remove_focus(self,e):
        self.focus()
        

app = App()
app.mainloop()
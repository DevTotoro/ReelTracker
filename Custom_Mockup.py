import tkinter
import customtkinter
import os
from PIL import Image


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class ScrollableFrame(customtkinter.CTkScrollableFrame):
    padx=0
    pady=0
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        
        
    def add_item(self, name, list):
        self.label = customtkinter.CTkLabel(self, text=name, font=customtkinter.CTkFont(size=19))
        self.label.grid(row=0, column=0, sticky="nw", padx=self.padx, pady=self.pady)
        
        self.pady += 30
        
        self.scrollable_frame = ScrollableFrame(master=self, height=150, width=780, orientation="horizontal", scrollbar_button_color="gray13", scrollbar_button_hover_color="gray13")
        self.scrollable_frame.grid(row=0, column=0, padx=0, pady=self.pady, sticky="new")
        
        self.pady += 180
        
    

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1200x600")
        
        
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # create navigation frame
        self.navigation_menu = customtkinter.CTkFrame(self, width=400, height=30, corner_radius=0)
        self.navigation_menu.grid(row=0, column=0, sticky="nw", padx=30, pady=30)
        self.navigation_menu.grid_rowconfigure(0, weight=1)
        self.navigation_menu.grid_columnconfigure(4,weight=1)
        
        
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "search_icon.png")), size=(17, 17))
        
        
        self.home_button = customtkinter.CTkButton(self.navigation_menu, corner_radius=0, text="Home", text_color=("gray10", "gray90"), border_color="gray11", 
                                                   border_width=1, fg_color=("gray75", "gray25"), hover_color=("gray70", "gray30"), command=self.home_button_event)
        self.home_button.grid(row=0, column=0)
        
        self.movies_button = customtkinter.CTkButton(self.navigation_menu, corner_radius=0, text="Movies", text_color=("gray10", "gray90"), border_color="gray11", 
                                                   border_width=1, fg_color="transparent", hover_color=("gray70", "gray30"), command=self.movies_button_event)
        self.movies_button.grid(row=0, column=1)
        
        self.series_button = customtkinter.CTkButton(self.navigation_menu, corner_radius=0, text="Series", text_color=("gray10", "gray90"), border_color="gray11", 
                                                   border_width=1, fg_color="transparent", hover_color=("gray70", "gray30"), command=self.series_button_event)
        self.series_button.grid(row=0, column=2)
        
        self.watchlist_button = customtkinter.CTkButton(self.navigation_menu, corner_radius=0, text="Watch List", text_color=("gray10", "gray90"), border_color="gray11",
                                                   border_width=1, fg_color="transparent", hover_color=("gray70", "gray30"), command=self.watchlist_button_event)
        self.watchlist_button.grid(row=0, column=3)
        
        
        self.search_field = customtkinter.CTkTextbox(self, width=210, height=20, corner_radius=5, padx=35)
        self.search_field.grid(row=0, column=0,  sticky="nw", padx=640, pady=30)
        self.search_field.insert("0.0","Search")
        
        
        self.image_label = customtkinter.CTkLabel(self.search_field, text="", image=self.logo_image)
        self.image_label.grid(row=0, column=0, sticky="nw", padx=5, pady=0)
        
        self.scrollable_frame = ScrollableFrame(master=self, width=800, height=400, fg_color="transparent", scrollbar_button_color="gray10", scrollbar_button_hover_color="gray10")
        self.scrollable_frame.grid(row=0, column=0, padx=50, pady=100, sticky="nw")
        
        self.scrollable_frame.add_item("Continue Watching",[])
        self.scrollable_frame.add_item("Watch Again",[])
        
        
        
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
        

app = App()
app.mainloop()
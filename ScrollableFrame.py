import customtkinter
import threading
from PIL import Image
from MovieAPI import MovieApi
import os 

from ScrollableFrameMovies import ScrollableFrameMovies


movie_api = MovieApi()
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

# this is the class for scrollable frame that holds genres
class ScrollableFrame(customtkinter.CTkScrollableFrame):
    # we need to keep track of the padding so we can position the objects inside the frame correctly
    padx=0
    pady=0
    
    # we need to now if this frame holds movies or series 
    is_movies = False
    
    # this is a dictionary that relates genres to movies/series scrollable frame
    genre_to_scrollable_frame = {}
    
    def __init__(self, master, is_movies, **kwargs):
        super().__init__(master, **kwargs)
        self.is_movies = is_movies
        
        
    def add_item(self, name):
        #PLACE GENRE LABEL 
        self.label = customtkinter.CTkLabel(self, text=name, font=customtkinter.CTkFont(size=19))
        self.label.grid(row=0, column=0, sticky="nw", padx=self.padx, pady=self.pady)
        
        # PLACE IMAGES SCROLLABLE FRAME
        self.scrollable_frame = ScrollableFrameMovies(master=self, height=150, width=780, orientation="horizontal", scrollbar_button_color="gray13", scrollbar_button_hover_color="gray13")
        self.scrollable_frame.grid(row=0, column=0, padx=0, pady=self.pady+30, sticky="new")
        self.genre_to_scrollable_frame[name] = self.scrollable_frame
        
        # PLACE NEXT BUTTON 
        self.next_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "next_icon.png")), size=(30, 30))
        self.next_button = customtkinter.CTkButton(self, width=30, height=174, fg_color="gray19", image=self.next_image, compound=customtkinter.CENTER, command=lambda: self.next_button_clicked(name))
        self.next_button.grid(row=0, column=0, pady=self.pady+30, padx=770, sticky='nw')
        self.next_button.bind("<Button-3>", lambda event, genre=name: self.prev_button_clicked(genre=genre))
        
        # INCREASE PADDING IN Y
        self.pady += 210
    
    # THIS FUNCTION CLEARS THE MAIN SCROLLABLE FRAME
    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()
            
        self.padx=0
        self.pady=0
        
    # EVENT HANDLER FOR NEXT BUTTON WHEN RIGHT CLICK
    def prev_button_clicked(self,genre):
        if self.genre_to_scrollable_frame[genre].start > 0:
            self.genre_to_scrollable_frame[genre].clear()
            self.genre_to_scrollable_frame[genre].start -= 7
            self.genre_to_scrollable_frame[genre].end  -= 7
            if self.is_movies:
                threading.Thread(target=movie_api.search_movies_by_genre, args=(movie_api.movie_genre[genre],self.genre_to_scrollable_frame[genre],self.genre_to_scrollable_frame[genre].start,self.genre_to_scrollable_frame[genre].end)).start()
            else:
                threading.Thread(target=movie_api.search_series_by_genre, args=(movie_api.series_genre[genre],self.genre_to_scrollable_frame[genre],self.genre_to_scrollable_frame[genre].start,self.genre_to_scrollable_frame[genre].end)).start()
    
    # EVENT HANDLER FOR NEXT BUTTON WHEN LEFT CLICK
    def next_button_clicked(self,genre):
        self.genre_to_scrollable_frame[genre].clear()
        self.genre_to_scrollable_frame[genre].start += 7
        self.genre_to_scrollable_frame[genre].end  += 7
        if self.is_movies:
            threading.Thread(target=movie_api.search_movies_by_genre, args=(movie_api.movie_genre[genre],self.genre_to_scrollable_frame[genre],self.genre_to_scrollable_frame[genre].start,self.genre_to_scrollable_frame[genre].end)).start()
        else: 
            threading.Thread(target=movie_api.search_series_by_genre, args=(movie_api.series_genre[genre],self.genre_to_scrollable_frame[genre],self.genre_to_scrollable_frame[genre].start,self.genre_to_scrollable_frame[genre].end)).start()

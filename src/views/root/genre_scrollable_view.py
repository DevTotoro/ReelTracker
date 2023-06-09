from src.widgets import ScrollableFrame, MoviesFrame, Label, Image
from src.services import Color
import customtkinter as Ctk
from src.services import async_get
from os import getenv
from PIL import Image as img
from io import BytesIO
import threading 

class GenreScrollableView(ScrollableFrame):
    lock = threading.Lock()
    def __init__(self, master, name, **kwargs):
        self.name = name
        self.counter=0
        self.controller = {}
        
        super().__init__(master,  **kwargs)
        
        
    def _setup_ui(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        
        def get_genre(response):
            data = response.json()
            if 'genres' in data: 
                genres = data['genres']
            
            for genre in genres:
                self.add_item(genre)
                
                
        if self.name == 'Series':
            async_get(
                url=f'{getenv("API_URL")}/genre/series',
                callback=get_genre
            )
        elif self.name == 'Movies':
            async_get(
                url=f'{getenv("API_URL")}/genre/movies',
                callback=get_genre
            )
            
        
            
    def add_item(self, genre):
        with self.lock:
            Label(self, text=genre['name'], font=Ctk.CTkFont(size=19)).grid(row=self.counter, column=0, padx=20)
            self.controller[genre['id']] = MoviesFrame(master=self, name=self.name, genre_id=genre['id'], navigation_controller=self.navigation_controller, height=150, fg_color=Color.GRAY_3.value)
            self.controller[genre['id']].grid(row=self.counter+1, column=0, sticky='wens', padx=20)
            self.counter += 2
        
        def add_movies(response):
            data = response.json()
            if 'results' in data:
                results = data['results']
                for movie in results[:8]:
                    poster_path = movie['poster_path']
                    base_image_url = 'https://image.tmdb.org/t/p/w154'  
                    image_url = f'{base_image_url}{poster_path}' if poster_path else None
                    
                    def image_callback(response,id):
                        with self.lock:
                            image = Ctk.CTkImage(img.open(BytesIO(response.content)), size=(100, 145))
                            self.controller[genre['id']].add_item(image,id)
                            
                    
                    if image_url:
                        # download image
                        async_get(image_url, callback=lambda response, id=movie['id']: image_callback(response,id))
                        
        if self.name == 'Movies':
            async_get(
                url=f'{getenv("API_URL")}/movie/genre?genreId={genre["id"]}&page=1',
            
                callback=add_movies
            )
        elif self.name == 'Series':
            async_get(
                url=f'{getenv("API_URL")}/tv/genre?genreId={genre["id"]}&page=1',
            
                callback=add_movies
            )
        
    
    def clear(self) -> None:
        for widget in self.winfo_children():
            widget.destroy()
        self.counter=0
        
    def show(self) -> None: 
        self.grid(row=1, column=0, sticky='nwes', columnspan=2, rowspan=3)
    
    def hide(self) -> None:
        self.grid_forget()
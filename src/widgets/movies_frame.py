from src.widgets import Frame, Image
import customtkinter as Ctk
from src.services import Color
import threading
from src.services import async_get
from os import getenv
from PIL import Image as img
from io import BytesIO

class MoviesFrame(Frame):
    counter=0
    movies = {}
    lock = threading.Lock()
    def __init__(self, master, name, genre_id, **kwargs):
        self.name=name
        self.page=1
        self.genre_id = genre_id
        super().__init__(master, **kwargs)
         
    def _setup_ui(self) -> None:
        self.columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=3)
        self.columnconfigure(10, weight=1)
        self.rowconfigure(0, weight=1)
        
        next_image = Image(image_name="next_icon.png", size=(30, 40))
        button = Ctk.CTkButton(self, text="", image=next_image , height=150, width=35, corner_radius=0, fg_color=Color.GRAY_2.value,
                      command=self.next_button_left_clicked)
        button.grid(row=0, column=10, sticky='e')
        button.bind('<Button-3>', self.next_button_right_clicked)
        
    
    def add_item(self, image, id):
        Ctk.CTkButton(self, text="", image=image, corner_radius=0, width=100, fg_color=Color.GRAY_3.value, hover_color=Color.GRAY_2.value, command=lambda id=id: self.movie_clicked(id)).grid(row=0, column=self.counter, sticky='w')
        self.counter +=1
            
            
    
    def clear(self) -> None:
        for widget in self.winfo_children():
            widget.destroy()
        self.counter=0
    
    def movie_clicked(self, id):
        self.navigation_controller['Details'].change_details(id)
 
        
    
    def next_button_right_clicked(self,e):
        if self.page != 1:
            self.clear()
            next_image = Image(image_name="next_icon.png", size=(30, 40))
            button = Ctk.CTkButton(self, text="", image=next_image , height=150, width=35, corner_radius=0, fg_color=Color.GRAY_2.value,
                        command=self.next_button_left_clicked)
            button.grid(row=0, column=10, sticky='e')
            button.bind('<Button-3>', self.next_button_right_clicked)
            self.page -=1
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
                                self.add_item(image,id)
                                

                        if image_url:
                            # download image
                            async_get(image_url, callback=lambda response, id=movie['id']: image_callback(response,id))
                            
            if self.name == 'Movies':
                async_get(
                    url=f'{getenv("API_URL")}/movie/genre?genreId={self.genre_id}&page={self.page}',
                
                    callback=add_movies
                )
            elif self.name == 'Series':
                async_get(
                    url=f'{getenv("API_URL")}/tv/genre?genreId={self.genre_id}&page={self.page}',
                
                    callback=add_movies
                )
            
            
    def next_button_left_clicked(self):
        self.clear()
        next_image = Image(image_name="next_icon.png", size=(30, 40))
        button = Ctk.CTkButton(self, text="", image=next_image , height=150, width=35, corner_radius=0, fg_color=Color.GRAY_2.value,
                      command=self.next_button_left_clicked)
        button.grid(row=0, column=10, sticky='e')
        button.bind('<Button-3>', self.next_button_right_clicked)
        self.page += 1
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
                            self.add_item(image,id)
                            

                    if image_url:
                        # download image
                        async_get(image_url, callback=lambda response, id=movie['id']: image_callback(response,id))
                        
        if self.name == 'Movies':
            async_get(
                url=f'{getenv("API_URL")}/movie/genre?genreId={self.genre_id}&page={self.page}',
            
                callback=add_movies
            )
        elif self.name == 'Series':
            async_get(
                url=f'{getenv("API_URL")}/tv/genre?genreId={self.genre_id}&page={self.page}',
            
                callback=add_movies
            )
        # search previous 9 movies or series by genre
        # dispay results
        
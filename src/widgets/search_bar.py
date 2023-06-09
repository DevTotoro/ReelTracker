from src.widgets import  Label, Frame, TextBox, Image
from src.services import Color
from src.services import async_get
from os import getenv
import customtkinter as Ctk
from PIL import Image as img
from io import BytesIO
import threading


class SearchBar(Frame):
    search_frame = None
    lock = threading.Lock()
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self._setup_ui()
        
    def _setup_ui(self) -> None:
        self.search_field = TextBox(self, corner_radius=10, padx=25, fg_color=Color.GRAY_3.value)
        self.search_field.place(relwidth=1, relheight=1)
        self.search_field.insert("0.0","Search")
        self.search_field.bind("<Button-1>",self.clear_search_field)
        self.search_field.bind('<Key>', command=lambda event: self.key_pressed(event))
        
        self.search_image_label = Label(self, text="", image=Image(image_name="search_icon.png", size=(17, 17)), fg_color=Color.GRAY_3.value, bg_color=Color.GRAY_3.value)
        self.search_image_label.place(relx=0.02, rely=0.13)
        
    def clear_search_field(self,e):
        if self.search_field.get("current linestart","current lineend") == "Search":
            self.search_field.delete("current linestart","current lineend")
    
    def key_pressed(self,e):
        # case: search field empty after hitting backspace
        if len(self.search_field.get("current linestart","current lineend")) == 1 and ord(e.char) == 8:
            if bool(self.search_frame.winfo_ismapped()):
                self.search_frame.place_forget()  
        else:
            # case: empty field and press key except backspace
            if self.search_field.get("current linestart","current lineend") == "" and ord(e.char) != 8:
               self.search_frame.clear()
               self.search_frame.place(relx=0.54, rely=0.13)
            # case: we hit a key and none of the above cases hold
            elif self.search_field.get("current linestart","current lineend") != "" or ord(e.char) != 8:
                self.search_frame.clear()
            
            def search_callback(response):
                data = response.json()
                movies = data['movies']
                series = data['series']
                if 'results'in movies:
                    results = movies['results']
                    for movie in results[:3]:
                        poster_path = movie['poster_path']
                        base_image_url = 'https://image.tmdb.org/t/p/w154'  
                        image_url = f'{base_image_url}{poster_path}' if poster_path else None
                        
                        def image_callback(response, name, id):
                            with self.lock:
                                image = Ctk.CTkImage(img.open(BytesIO(response.content)), size=(50, 73))
                                self.search_frame.add_item(image, name, id)
                                
                        
                        if image_url:
                            # download image
                            async_get(image_url, callback=lambda response, id=movie['id'], name=movie['title']: image_callback(response,name,id))
                            
                if 'results' in series:
                    results = series['results']    
                    for serie in results[:3]:
                        poster_path = serie['poster_path']
                        base_image_url = 'https://image.tmdb.org/t/p/w154'  
                        image_url = f'{base_image_url}{poster_path}' if poster_path else None
                        
                        def image_callback(response, name, id):
                            with self.lock:
                                image = Ctk.CTkImage(img.open(BytesIO(response.content)), size=(50, 73))
                                self.search_frame.add_item(image,name,id)
                                
                        
                        if image_url:
                            # download image
                            async_get(image_url, callback=lambda response, id=serie['id'], name=serie['name']: image_callback(response ,name, id))


            async_get(
                url = f'{getenv("API_URL")}/search?query={self.search_field.get("current linestart","current lineend")+e.char}&page=1',
                callback=search_callback
            )
           
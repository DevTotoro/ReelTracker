import customtkinter as Ctk
from .base_root_view import BaseRootView
from src.widgets import Label, ScrollableFrame, Friend, Image
from src.services import Color
from src.services import async_get
from os import getenv
from PIL import Image as img
from io import BytesIO

class DetailsView(BaseRootView):
    navigation_controller = None
    star_image = []
    movie_image = Image(image_name="image_not_found_icon.jpg", size=(140, 200))
    star_icon = Image(image_name='star_icon.png', size=(20,20))
    star_icon_not = Image(image_name='~star_icon.jpg', size=(30,30))
    def __init__(self, master, navigation_controller=None, **kwargs):
        super().__init__(master, **kwargs)
        self.navigation_controller = navigation_controller
        
    def _setup_ui(self) -> None:
        self.picture = Label(self, text='', image=self.movie_image)
        self.picture.place(relx=0.05, rely=0.02)
        
        self.title = Label(self, text='Lord Of The Rings: The Two Towers', font=Ctk.CTkFont(weight='bold', size=18, family='arial'))
        self.title.place(relx=0.22, rely=0.02)
        self.rating = Label(self, text='8.8', font=Ctk.CTkFont(weight='bold', size=18, family='arial'))
        self.rating.place(relx=0.22, rely=0.07)
        
        self.star_image.append(Label(self, text='', image= self.star_icon))
        self.star_image[0].place(relx=0.26, rely=0.065)
        self.star_image.append(Label(self, text='', image= self.star_icon))
        self.star_image[1].place(relx=0.283, rely=0.065)
        self.star_image.append(Label(self, text='', image= self.star_icon))
        self.star_image[2].place(relx=0.306, rely=0.065)
        self.star_image.append(Label(self, text='', image= self.star_icon))
        self.star_image[3].place(relx=0.329, rely=0.065)
        self.star_image.append(Label(self, text='', image= self.star_icon_not))
        self.star_image[4].place(relx=0.352, rely=0.065)
        
        self.description = Label(self, wraplength=370, justify="left", text='While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, the divided fellowship makes a stand against Sauron\' new ally, Saruman, and his hordes of Isengard')
        self.description.place(relx=0.22, rely=0.13)
        
        Label(self, text='Director', font=Ctk.CTkFont(weight='bold', size=11, family='arial')).place(relx=0.22, rely=0.291)
        self.director = Label(self, text='Peter Jackson', font=Ctk.CTkFont(size=11, family='arial'))
        self.director.place(relx=0.29, rely=0.291)
        
        Label(self, text='Stars', font=Ctk.CTkFont(weight='bold', size=11, family='arial')).place(relx=0.22, rely=0.32)
        self.stars = Label(self, text='Elijah Wood - Ian McKellen - Viggo Mortensen', font=Ctk.CTkFont(size=11, family='arial'))
        self.stars.place(relx=0.29, rely=0.321)
        
        Label(self, text='Reviews', font=Ctk.CTkFont(weight='bold', size=22, family='arial')).place(relx=0.05, rely=0.38)
        self.reviews = Label(self, fg_color=Color.GRAY_3.value, wraplength=330, justify="left", text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quam velit, vulputate eu phareta nec, mattis ac neque. Duis vulputate commodo lectus, ac blandit elit tincidunt id.')
        self.reviews.place(relx=0.05, rely=0.45, relheight=0.2, relwidth=0.35)
        
        Label(self, text='Comments', font=Ctk.CTkFont(weight='bold', size=22, family='arial')).place(relx=0.45, rely=0.38)
        self.comments = Label(self, fg_color=Color.GRAY_3.value, wraplength=330, justify="left", text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quam velit, vulputate eu phareta nec, mattis ac neque. Duis vulputate commodo lectus, ac blandit elit tincidunt id.')
        self.comments.place(relx=0.45, rely=0.45, relheight=0.2, relwidth=0.35)
    
    def change_details(self,id):
        
        def add_details(response):
            data = response.json()
            if 'error' not in data:        
                poster_path = data['poster_path']
                base_image_url = 'https://image.tmdb.org/t/p/w154'  
                image_url = f'{base_image_url}{poster_path}' if poster_path else None
                
                def image_callback(response):
                    image = Ctk.CTkImage(img.open(BytesIO(response.content)), size=(140, 200))
                    self.picture.configure(image=image)
                
                
                if image_url:
                    # download image
                    async_get(image_url, callback=image_callback)
                if 'title' in data:
                    self.title.configure(text=data['title'])
                else:
                    self.title.configure(text=data['name'])
                    
                self.rating.configure(text=round(data['vote_average'],2))
                self.description.configure(text=data['overview'] if len(data['overview']) <= 250 else data['overview'][:250] + '...')
                stars = int(round(data['vote_average'],2)/2)
                
                for i in range(5):
                    self.star_image[i].configure(image=self.star_icon_not)
                    
                for i in range(stars):
                    self.star_image[i].configure(image=self.star_icon)
                reviews = data['reviews']['results']
                if reviews:
                    self.reviews.configure(text= reviews[0]['content'] if len(reviews[0]['content']) <= 130 else reviews[0]['content'][:130] + '...')
                self.navigation_controller['Details'].show()
            
        async_get(
                url=f'{getenv("API_URL")}/movie/details/{id}',
            
                callback=add_details
            )
        
        async_get(
                url=f'{getenv("API_URL")}/tv/details/{id}',
            
                callback=add_details
            )

        
    def show(self):
        self.grid(row=1, column=0, sticky='nwes', columnspan=2, rowspan=3)   
    
    def hide(self):
        self.grid_forget()
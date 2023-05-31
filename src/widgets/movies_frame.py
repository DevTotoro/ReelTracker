from src.widgets import Frame, Image
import customtkinter as Ctk
from src.services import Color


class MoviesFrame(Frame):
    counter=0
    def __init__(self, master, **kwargs):
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
        
    
    def add_item(self, image):
        Ctk.CTkButton(self, text="", image=image, corner_radius=0, width=100, fg_color=Color.GRAY_3.value, hover_color=Color.GRAY_2.value, command=self.movie_clicked).grid(row=0, column=self.counter, sticky='w')
        
        self.counter +=1
    
    def clear(self) -> None:
        for widget in self.winfo_children():
            widget.destroy()
        self.counter=0
    
    def movie_clicked(self):
        print('Movie Clicked')
        # show movie details view
        # display details
    
    def next_button_right_clicked(self,e):
        print('Right Clicked Next Button')
        #if this isnt the first page
            # self.clear()
            # search next 9 movies or series by genre
            # display results
            
    def next_button_left_clicked(self):
        print('Left Clicked Next Button')
        # self.clear()
        # search previous 9 movies or series by genre
        # dispay results
        
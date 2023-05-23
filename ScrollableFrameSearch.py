import customtkinter

# this is the frame that is being displayed when we search something
class ScrollableFrameSearch(customtkinter.CTkScrollableFrame):
    # same logic 
    pady=0
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        
    # function that adds movie/series image to the frame   
    def add_item(self, name, image):
        self.movie_image = customtkinter.CTkImage(image, size=(50, 75))
        self.movie_image_label = customtkinter.CTkLabel(self, text="", image=self.movie_image)
        self.movie_image_label.grid(row=0, column=0, sticky="nw", padx=5, pady=self.pady+5)
       
        self.movie_name_label = customtkinter.CTkLabel(self, text=name, font=customtkinter.CTkFont(size=10), text_color="gray75", width=50, height=75, wraplength=120, justify="left")
        self.movie_name_label.grid(row=0, column=0, sticky="nw", padx=75, pady=self.pady+5) 
        
        self.pady += 80
        
    # function that clears frame     
    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()
            
        self.pady=0
        

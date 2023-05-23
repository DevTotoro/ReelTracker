import customtkinter

# this is the class for scrollable frame of a specific genre
class ScrollableFrameMovies(customtkinter.CTkScrollableFrame):
    # we need to keep track of the padding to place the images correctly
    padx = 0
    
    # this variables keep track of the range of 7 images that are displayed in the frame 
    start=0
    end=7
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
    # function to clear the frame
    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.padx=0
        
    # function that add image to the frame    
    def add_item(self,name,image):
        self.movie_image = customtkinter.CTkImage(image, size=(100, 150))
        self.search_image_label = customtkinter.CTkLabel(self, text="", image=self.movie_image)
        self.search_image_label.grid(row=0, column=0, sticky="nw", padx=self.padx)
        self.padx += 110
        
        
    
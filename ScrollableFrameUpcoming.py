import customtkinter


# this is the class for upcoming frame
class ScrollableFrameUpcoming(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
    # function that clears frame
    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.padx=30
        self.pady=0
        
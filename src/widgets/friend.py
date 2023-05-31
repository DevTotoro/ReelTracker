from src.widgets import Frame, Label, Image
import customtkinter

class Friend(Frame):
    
    def __init__(self, master, username, status, **kwargs):
        self.username=username
        self.status=status
        super().__init__(master, **kwargs)
        
    
    def _setup_ui(self) -> None:
        self.profile_image = Image(image_name="profile_icon.png", size=(30, 30))
        Label(self, text="", image=self.profile_image, fg_color="transparent").place(relx=0.07, rely=0.17)
        
        self.status_image = Image(image_name="online_icon.jpg" if self.status=="online" else "offline_icon.png", size=(15, 15) if self.status=="online" else (10.5,10.5))
        Label(self, text="", image=self.status_image, fg_color="transparent").place(relx = 0.21 if self.status =="online" else 0.22, rely=0.23)
        
        Label(self, text=self.username, font=customtkinter.CTkFont(size=14)).place(relx=0.3, rely=0.21)
        
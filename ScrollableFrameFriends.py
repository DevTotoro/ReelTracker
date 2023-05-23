import customtkinter
from PIL import Image
import os

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

# this is the class for friends frame
class ScrollableFrameFriends(customtkinter.CTkScrollableFrame):
    # same logic with the other classes
    padx=30
    pady=0
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
    # function that clears the frame
    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()
            
        self.padx=30
        self.pady=0
            
    # function that adds friend to the frame
    def add_friend(self, name, status):
        # Initialize row frame
        self.friend_row_frame = customtkinter.CTkFrame(self, width=538, height=40, corner_radius=0)
        self.friend_row_frame.grid(row=0, column=0, sticky="nw", pady=self.pady)
        
        # PLACE PROFILE ICON
        self.profile_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "profile_icon.png")), size=(30, 30))
        self.profile_image_label = customtkinter.CTkLabel(self.friend_row_frame, text="", image=self.profile_image, fg_color="transparent")
        self.profile_image_label.grid(row=0, column=0, sticky="nw", padx=self.padx)
        
        # PLACE STATUS ICON
        self.status_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "online_icon.jpg" if status=="online" else "offline_icon.png")), size=(15, 15) if status=="online" else (10.5,10.5))
        self.status_image_label = customtkinter.CTkLabel(self.friend_row_frame, text="", image=self.status_image, fg_color="transparent")
        self.status_image_label.grid(row=0, column=0, sticky="nw", padx=self.padx+40 if status =="online" else self.padx+43, pady=3)
        
        # PLACE NAME LABEL
        self.name_label = customtkinter.CTkLabel(self.friend_row_frame, text=name, font=customtkinter.CTkFont(size=14), text_color="gray75")
        self.name_label.grid(row=0, column=0, sticky="nw", padx=self.padx+65, pady=3)
        
        # INCREASE PADDING IN Y 
        self.pady += 40
    
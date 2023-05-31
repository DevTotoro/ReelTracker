from typing import Tuple
import customtkinter as Ctk
import os
from PIL import Image as img


class Image(Ctk.CTkImage):
    image_path = os.path.join(os.path.dirname(os.path.dirname((os.path.realpath(__file__)))), "icons")
    
    def __init__(self, image_name, **kwargs):
        super().__init__(light_image=img.open(os.path.join(self.image_path, image_name)), **kwargs)
        
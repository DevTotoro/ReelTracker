from src.widgets import ScrollableFrame, Image, Label, Frame
from src.services import Color

class SearchFrame(ScrollableFrame):
    counter = 0
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
    def _setup_ui(self) -> None:
        pass
    
    def add_item(self, image: Image, name):
        frame = Frame(self, height=85, fg_color=Color.GRAY_3.value)
        Label(frame, text='', image=image).place(relx=0.08, rely=0.1)
        Label(frame, text=name, wraplength=120, justify="left").place(relx= 0.4, rely=0.1, relwidth=0.57, relheight=0.49)
        frame.grid(row=self.counter, column=0, sticky='we')
        
        self.counter += 1
        
    def clear(self) -> None:
        for widget in self.winfo_children():
            widget.destroy()
        self.counter=0
        
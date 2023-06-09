from src.widgets import ScrollableFrame, Image, Label, Frame
from src.services import Color

class SearchFrame(ScrollableFrame):
    counter = 0
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
    def _setup_ui(self) -> None:
        pass
    
    def add_item(self, image: Image, name, id):
        self.frame = Frame(self, height=85, fg_color=Color.GRAY_3.value, corner_radius=0)
        
        self.image = Label(self.frame, text='', image=image)
        self.image.place(relx=0.08, rely=0.1)
        
        self.label = Label(self.frame, text=name, wraplength=120, justify="left")
        self.label.place(relx= 0.4, rely=0.1, relwidth=0.57, relheight=0.49)
        
        self.frame.grid(row=self.counter, column=0, sticky='we')
        self.frame.bind('<Enter>', lambda event, frame=self.frame: self.hover(event,frame=frame))
        self.image.bind('<Enter>', lambda event, frame=self.frame: self.hover(event,frame=frame))
        self.label.bind('<Enter>', lambda event, frame=self.frame: self.hover(event,frame=frame))
        
        self.frame.bind('<Leave>', lambda event, frame=self.frame: self.un_hover(event,frame=frame))
        
        self.frame.bind('<Button-1>', lambda event, id=id: self.frame_clicked(event, id))
        self.image.bind('<Button-1>', lambda event, id=id: self.frame_clicked(event, id))
        self.label.bind('<Button-1>', lambda event, id=id: self.frame_clicked(event, id))
        self.counter += 1
        
    def clear(self) -> None:
        for widget in self.winfo_children():
            widget.destroy()
        self.counter=0
        
    def hover(self,e,frame):
        frame.configure(fg_color = Color.GRAY_2.value)
    
    def un_hover(self, e, frame):
        frame.configure(fg_color = Color.GRAY_3.value)
        
    def frame_clicked(self, e, id):
        for key in self.navigation_controller.keys():
            self.navigation_controller[key].hide()
        
        self.navigation_controller['Details'].change_details(id)
        
        
        
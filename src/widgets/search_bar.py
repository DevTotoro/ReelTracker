from src.widgets import  Label, Frame, TextBox, Image
from src.services import Color


class SearchBar(Frame):
    search_frame = None
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self._setup_ui()
        
    def _setup_ui(self) -> None:
        self.search_field = TextBox(self, corner_radius=10, padx=25, fg_color=Color.GRAY_3.value)
        self.search_field.place(relwidth=1, relheight=1)
        self.search_field.insert("0.0","Search")
        self.search_field.bind("<Button-1>",self.clear_search_field)
        self.search_field.bind('<Key>', command=lambda event: self.key_pressed(event))
        
        self.search_image_label = Label(self, text="", image=Image(image_name="search_icon.png", size=(17, 17)), fg_color=Color.GRAY_3.value, bg_color=Color.GRAY_3.value)
        self.search_image_label.place(relx=0.02, rely=0.13)
        
    def clear_search_field(self,e):
        if self.search_field.get("current linestart","current lineend") == "Search":
            self.search_field.delete("current linestart","current lineend")
    
    def key_pressed(self,e):
        # case: search field empty after hitting backspace
        if len(self.search_field.get("current linestart","current lineend")) == 1 and ord(e.char) == 8:
            print('search field cleared')
            if bool(self.search_frame.winfo_ismapped()):
                self.search_frame.place_forget()  
        else:
            # case: empty field and press key except backspace
            if self.search_field.get("current linestart","current lineend") == "" and ord(e.char) != 8:
               print('first key pressed')
               # self.search_frame.clear()
               self.search_frame.place(relx=0.54, rely=0.13)
            # case: we hit a key and none of the above cases hold
            elif self.search_field.get("current linestart","current lineend") != "" or ord(e.char) != 8:
                print('another key pressed')
                # self.search_frame.clear()
            
            # kill existing threads (this can be done in the wrapper)
            # search for movies and series by name
            # for movies in results:
                # self.search_frame.add_item(image, name)
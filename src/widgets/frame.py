import customtkinter as ctk


class Frame(ctk.CTkFrame):
    navigation_controller = None
    def __init__(self, master, navigation_controller=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.navigation_controller = navigation_controller 
        self._setup_ui()

    # Private methods
    def _setup_ui(self) -> None:
        pass

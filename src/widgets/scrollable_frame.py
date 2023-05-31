import customtkinter as ctk


class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)

        self._setup_ui()

    # Private methods
    def _setup_ui(self) -> None:
        pass
    
    def clear(self) -> None:
        for widget in self.winfo_children():
            widget.destroy()
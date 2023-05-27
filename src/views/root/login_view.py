from .base_root_view import BaseRootView
import customtkinter as ctk


class LoginView(BaseRootView):
    def __init__(self, master: ctk.CTk, on_login_success: callable, on_register_clicked: callable):
        super().__init__(master=master)

        self.__on_login_success = on_login_success
        self.__on_register_clicked = on_register_clicked

        self.__setup_ui()

    # Private methods
    def __setup_ui(self) -> None:
        button = ctk.CTkButton(master=self, text='Login', command=self.__on_login_clicked)
        button.pack(pady=5)

        button = ctk.CTkButton(master=self, text='Register', command=self.__on_register_clicked)
        button.pack(pady=5)

    # Callbacks
    def __on_login_clicked(self) -> None:
        self.__on_login_success()

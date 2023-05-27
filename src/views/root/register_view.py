import customtkinter as ctk
from .base_root_view import BaseRootView
from src.widgets import Button, Entry


class RegisterView(BaseRootView):
    def __init__(self, master: ctk.CTk, on_register_success: callable, on_login_clicked: callable):
        super().__init__(master=master)

        self.__on_register_success = on_register_success
        self.__on_login_clicked = on_login_clicked

        self.__setup_ui()

    # Private methods
    def __setup_ui(self) -> None:
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        center_frame = ctk.CTkFrame(master=self, fg_color='transparent')
        center_frame.grid(row=0, column=0)

        # Title
        ctk.CTkLabel(master=center_frame, text='Register', font=('Arial', 24, 'bold')) \
            .grid(row=0, column=0, pady=40, sticky='ew')

        # Input fields
        self.__email_input = Entry(master=center_frame, placeholder_text='Email')
        self.__email_input.grid(row=1, column=0, pady=5, sticky='ew')

        self.__username_input = Entry(master=center_frame, placeholder_text='Username')
        self.__username_input.grid(row=2, column=0, pady=5, sticky='ew')

        self.__password_input = Entry(master=center_frame, placeholder_text='Password', show='·')
        self.__password_input.grid(row=3, column=0, pady=5, sticky='ew')

        # Feedback label
        self.__feedback_label = ctk.CTkLabel(
            master=center_frame,
            text='We will never share your information with anyone.'
        )
        self.__feedback_label.grid(row=4, column=0, pady=5, sticky='ew')

        # Register button
        Button(master=center_frame, text='Register', command=self.__on_register_clicked) \
            .grid(row=5, column=0, pady=5, sticky='ew')

        # Login button
        Button(master=center_frame, text='Login', command=self.__on_login_clicked) \
            .grid(row=6, column=0, pady=5, sticky='ew')

    # Callbacks
    def __on_register_clicked(self) -> None:
        self.__on_register_success()

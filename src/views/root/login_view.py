from customtkinter import CTk as ctkWindow
from os import getenv
from .base_root_view import BaseRootView
from src.widgets import Frame, Label, Entry, Button
from src.services import async_post
from src.models import User


class LoginView(BaseRootView):
    def __init__(self, master: ctkWindow, user: User, on_login_success: callable, on_register_clicked: callable):
        self.__on_login_success = on_login_success
        self.__on_register_clicked = on_register_clicked

        self.__user = user

        super().__init__(master=master)

    # Private methods
    def _setup_ui(self) -> None:
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        center_frame = Frame(master=self, fg_color='transparent')
        center_frame.grid(row=0, column=0)

        # Title (Also configures the width of the frame)
        Label(master=center_frame, text='Login', font=('Arial', 24, 'bold'), width=400) \
            .grid(row=0, column=0, pady=40, sticky='ew')

        # Input fields
        self.__username_input = Entry(master=center_frame, placeholder_text='Username')
        self.__username_input.grid(row=1, column=0, pady=5, sticky='ew')

        self.__password_input = Entry(master=center_frame, placeholder_text='Password', show='·')
        self.__password_input.grid(row=2, column=0, pady=5, sticky='ew')

        # Feedback label
        self.__feedback_label = Label(master=center_frame, text='We will never share your information with anyone.')
        self.__feedback_label.grid(row=3, column=0, pady=5, sticky='ew')

        # Login button
        Button(master=center_frame, text='Login', command=self.__on_login_clicked) \
            .grid(row=4, column=0, pady=5, sticky='ew')

        # Register button
        Button(master=center_frame, text='Register', command=self.__on_register_clicked) \
            .grid(row=5, column=0, pady=5, sticky='ew')

    # Callbacks
    def __on_login_clicked(self) -> None:
        self.__feedback_label.configure(text='Logging in...')

        async_post(
            url=f'{getenv("API_URL")}/auth/login',
            json={
                'username': self.__username_input.get(),
                'password': self.__password_input.get()
            },
            callback=self.__on_login_request_complete
        )

    def __on_login_request_complete(self, response) -> None:
        # TODO: Handle errors

        match response.status_code:
            case 200:
                self.__feedback_label.configure(text='Login successful!', text_color='green')

                self.__user.login(response.json()['token'])

                self.__on_login_success()
            case 400:
                self.__feedback_label.configure(text=response.json()['error'], text_color='red')
            case 401:
                self.__feedback_label.configure(text=response.json()['error'], text_color='red')
            case _:
                self.__feedback_label.configure(text='An unknown error occurred.', text_color='red')

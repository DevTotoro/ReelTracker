import customtkinter as ctk

from src.views.root import BaseRootView, LoginView, RegisterView, MainView

from src.services import Theme


class Application(ctk.CTk):
    def __init__(
            self,
            title: str = 'App',
            width: int = 300,
            height: int = 300,
            resizable: bool = False,
            theme: Theme = Theme()
    ):
        super().__init__()

        self.__theme = theme

        self.title(title)
        self.geometry(f'{width}x{height}')
        self.resizable(resizable, resizable)

        self.__setup_ui()

    def run(self) -> None:
        self.__show_root_view(self.__root_views['login'])

        self.mainloop()

    # Private methods
    def __setup_ui(self) -> None:
        self.__setup_root_views()

    def __setup_root_views(self) -> None:
        self.__root_views = {
            'login': LoginView(
                master=self,
                on_login_success=lambda: self.__show_root_view(self.__root_views['main']),
                on_register_clicked=lambda: self.__show_root_view(self.__root_views['register'])
            ),
            'register': RegisterView(
                master=self,
                on_register_success=lambda: self.__show_root_view(self.__root_views['main']),
                on_login_clicked=lambda: self.__show_root_view(self.__root_views['login'])
            ),
            'main': MainView(master=self)
        }

    def __show_root_view(self, view: BaseRootView) -> None:
        """
        Hide all root views and show the given view.

        :param view: The view to show.
        """

        for root_view in self.__root_views.values():
            root_view.hide()

        view.show()

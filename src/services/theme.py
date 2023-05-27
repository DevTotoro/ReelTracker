from enum import Enum
from customtkinter import set_appearance_mode, set_default_color_theme


class AppearanceMode(Enum):
    SYSTEM = 'system'
    LIGHT = 'light'
    DARK = 'dark'


class ColorTheme(Enum):
    BLUE = 'blue'
    DARK_BLUE = 'dark-blue'
    GREEN = 'green'


class Theme:
    appearance_mode = AppearanceMode.SYSTEM
    color_theme = ColorTheme.DARK_BLUE

    def __init__(
            self,
            appearance_mode: AppearanceMode = AppearanceMode.SYSTEM,
            color_theme: ColorTheme = ColorTheme.DARK_BLUE
    ):
        self.set_appearance_mode(appearance_mode)
        self.set_color_theme(color_theme)

    def set_appearance_mode(self, mode: AppearanceMode) -> None:
        """
        Sets the appearance mode of the application.

        :param mode: The appearance mode to set.
        """

        self.appearance_mode = mode
        set_appearance_mode(mode.value)

    def set_color_theme(self, theme: ColorTheme) -> None:
        """
        Sets the color theme of the application.

        :param theme: The color theme to set.
        """

        self.color_theme = theme
        set_default_color_theme(theme.value)

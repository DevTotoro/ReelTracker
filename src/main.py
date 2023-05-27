from services.theme import AppearanceMode, ColorTheme, Theme
from application import Application


if __name__ == '__main__':
    theme = Theme(appearance_mode=AppearanceMode.SYSTEM, color_theme=ColorTheme.DARK_BLUE)

    app = Application(title='ReelTracker', width=300, height=300, resizable=False, theme=theme)
    app.run()

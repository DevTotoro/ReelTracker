from src.services import AppearanceMode, ColorTheme, Theme
from src.application import Application
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()

    theme = Theme(appearance_mode=AppearanceMode.SYSTEM, color_theme=ColorTheme.DARK_BLUE)

    app = Application(title='ReelTracker', width=1280, height=720, resizable=True, theme=theme)
    app.run()

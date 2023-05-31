from src.application import Application
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()

    app = Application(title='ReelTracker', width=1280, height=720, resizable=True)
    app.run()

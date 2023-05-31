from src.services import async_post


class User:
    def __init__(self):
        self.token = None

    def login(self, token: str) -> None:
        self.token = token

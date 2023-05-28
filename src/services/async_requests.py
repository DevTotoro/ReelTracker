import requests as req
import threading as th


def async_get(url: str, params: dict = None, headers: dict = None, callback: callable = None) -> None:
    def __get() -> None:
        response = req.get(url, params=params, headers=headers)
        if callback is not None:
            callback(response)

    th.Thread(target=__get).start()


def async_post(url: str, data: dict = None, headers: dict = None, callback: callable = None) -> None:
    def __post() -> None:
        response = req.post(url, data=data, headers=headers)
        if callback is not None:
            callback(response)

    th.Thread(target=__post).start()

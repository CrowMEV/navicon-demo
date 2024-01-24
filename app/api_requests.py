import requests


def get_json(url: str) -> dict:
    r = requests.get(url)
    return r.json()

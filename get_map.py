import requests


def get_map_data(x, y, mode):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={x},{y}&spn=0.002,0.002&l={mode}"
    return requests.get(map_request).content

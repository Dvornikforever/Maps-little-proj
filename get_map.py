import pygame
from constants import SIZE
import requests
from PIL import Image
import io
import base64
from byte_array import byte_data


def get_map_data(x, y, mode):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={x},{y}&spn=0.002,0.002&l={mode}"
    return requests.get(map_request).content


def turn_into_image(x, y, mode):
    b = base64.b64decode(get_map_data(x, y, mode))
    return Image.open(io.BytesIO(b))

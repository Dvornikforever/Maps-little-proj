import requests
import pygame
from constants import SIZE


def get_map_data(x, y, mode):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={x},{y}&spn=0.002,0.002&l={mode}"
    return requests.get(map_request).content


def turn_into_image(x, y, mode):
    return pygame.image.frombytes(get_map_data(x, y, mode), SIZE, 'jpg', flipped=False)

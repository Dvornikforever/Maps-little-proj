import sys
import pygame
import os

from constants import *
from get_map import get_map_data

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
last_size = screen.get_size()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(get_map_data(START_POS[0], START_POS[1], START_MODE))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    clock.tick(FPS)
    # Удаляем за собой файл с изображением.
    os.remove(map_file)

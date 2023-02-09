import sys
import pygame

from constanst import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
last_size = screen.get_size()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(FPS)

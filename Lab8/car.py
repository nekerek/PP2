import pygame
from pygame.locals import *
import sys


pygame.init()
FPS = pygame.time.Clock()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car game")

#Game loop begins
while (1):


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    FPS.tick(60)
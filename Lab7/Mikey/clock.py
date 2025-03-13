import pygame
import sys

pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Basic Pygame Window")

while True:
    pygame.draw.circle(screen, 'red', center, 25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.display.flip()

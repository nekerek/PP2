import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Red Circle")

circle_x = 400
circle_y = 300
circle_speed = 20

while True:
    screen.fill('white')
    pygame.draw.circle(screen, "blue", (circle_x, circle_y), 50)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and circle_x > 50:
        circle_x -= circle_speed
    elif keys[pygame.K_RIGHT] and circle_x < 750:
        circle_x += circle_speed
    elif keys[pygame.K_UP] and circle_y > 50:
        circle_y -= circle_speed
    elif keys[pygame.K_DOWN] and circle_y < 550:
        circle_y += circle_speed

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(20)







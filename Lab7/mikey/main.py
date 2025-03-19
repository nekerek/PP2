import pygame
import sys
import datetime



pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mikey Clock")
clock = pygame.image.load('Lab7/mikey/clock.png').convert_alpha()
min_hand = pygame.image.load('Lab7/mikey/min_hand.png').convert_alpha()
sec_hand = pygame.image.load('Lab7/mikey/sec_hand.png').convert_alpha()

center_x, center_y = 400, 300

def blit_rotate_center(image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pivot)
    screen.blit(rotated_image, new_rect.topleft)



while True:

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second
    
    screen.blit(clock, (0, 0))
    
    minute_angle = -(minutes * 6)  
    second_angle = -(seconds * 6) 

    blit_rotate_center(min_hand, minute_angle, (center_x, center_y))
    blit_rotate_center(sec_hand, second_angle, (center_x, center_y))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

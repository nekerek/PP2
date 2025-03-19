import pygame
import os
import sys

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

bg = pygame.image.load('Lab7/music/nggyu.jpg').convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

music_folder = "Lab7/music"
tracks = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
track_index = 0

paused = False
running = True
clock = pygame.time.Clock()

while running:
    screen.blit(bg, (0, 0))
    
    font = pygame.font.Font(None, 24)
    text = font.render(f"{tracks[track_index]}", True, 'white')
    screen.blit(text, (100, 450))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            pygame.mixer.music.load(os.path.join(music_folder, tracks[track_index]))
            pygame.mixer.music.play()
            paused = False
             
        elif keys[pygame.K_s]:  
            pygame.mixer.music.stop()
            paused = True

        elif keys[pygame.K_n]:  
            track_index = (track_index + 1) % len(tracks)
            pygame.mixer.music.load(os.path.join(music_folder, tracks[track_index]))
            pygame.mixer.music.play()

        elif keys[pygame.K_b]:  
            track_index = (track_index - 1) % len(tracks)
            pygame.mixer.music.load(os.path.join(music_folder, tracks[track_index]))
            pygame.mixer.music.play()

    clock.tick(20)

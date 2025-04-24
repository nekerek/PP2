import pygame
import sys
import math

pygame.init()

FPS = 60                              # Количество кадров в секунду
FramePerSec = pygame.time.Clock()     # Объект таймера для управления FPS

# Цвета в формате RGB
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Размеры экрана и игровые переменные
SCREEN_WIDTH = 800                   # Ширина окна
SCREEN_HEIGHT = 600                  # Высота окна

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Создаём окно

radius = 15  # Размер кисти/фигур
color = (0, 0, 255)  # Цвет по умолчанию (синий)
tool = 'free'  # Текущий инструмент
points = []  # Список точек для свободного рисования

# Функция сглаживания линии между точками
def drawLineBetween(screen, index, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

# Функция рисования квадрата
def draw_square(screen, center, size, color):
    x, y = center
    side = size * 2
    pygame.draw.rect(screen, color, (x - size, y - size, side, side), 2)

# Функция рисования прямоугольного треугольника
def draw_right_triangle(screen, center, size, color):
    x, y = center
    points = [(x, y), (x, y + size), (x + size, y + size)]
    pygame.draw.polygon(screen, color, points, 2)

# Функция рисования равностороннего треугольника
def draw_equilateral_triangle(screen, center, size, color):
    x, y = center
    h = size * math.sqrt(3)
    points = [(x, y - h / 2), (x - size, y + h / 2), (x + size, y + h / 2)]
    pygame.draw.polygon(screen, color, points, 2)

# Функция рисования ромба
def draw_rhombus(screen, center, size, color):
    x, y = center
    points = [(x, y - size), (x + size, y), (x, y + size), (x - size, y)]
    pygame.draw.polygon(screen, color, points, 2)

while True:
    pressed = pygame.key.get_pressed()  # Состояние клавиш
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Закрытие окна
            pygame.quit()
            sys.exit()
        #Переключение цвета и инструмента
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:     # Клавиша R — красный цвет
                color = RED
                tool = 'free'
            elif event.key == pygame.K_g:   # G — зелёный
                color = GREEN
                tool = 'free'
            elif event.key == pygame.K_b:   # B — синий
                color = BLUE
                tool = 'free'
            elif event.key == pygame.K_y:   # Y — жёлтый
                color = YELLOW
                tool = 'free'
            elif event.key == pygame.K_e:   # E — ластик (рисует чёрным)
                color = BLACK
                tool = 'eraser'
            elif event.key == pygame.K_c:   # C — инструмент "круг"
                tool = 'circle'
            elif event.key == pygame.K_t:   # T — инструмент "прямоугольник"
                tool = 'rect'
            elif event.key == pygame.K_q:   # Q — инструмент "квадрат"
                tool = 'square'
            elif event.key == pygame.K_w:   # W — инструмент "прямоугольный треугольник"
                tool = 'right_triangle'
            elif event.key == pygame.K_z:   # Z — инструмент "правильный треугольник"
                tool = 'equilateral_triangle'
            elif event.key == pygame.K_v:   # V — инструмент "ромбик"
                tool = 'rhombus'
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:   # скролл верх
                radius = min(200, radius + 1)
            elif event.button == 5: # скролл вниз
                radius = max(1, radius - 1)
            elif event.button == 1: # лкм
                start_pos = event.pos
                if tool == 'circle':
                    pygame.draw.circle(screen, color, start_pos, radius)
                elif tool == 'rect':
                    pygame.draw.rect(screen, color, (*start_pos, radius * 2, radius))
                elif tool == 'square':
                    draw_square(screen, start_pos, radius, color)
                elif tool == 'right_triangle':
                    draw_right_triangle(screen, start_pos, radius, color)
                elif tool == 'equilateral_triangle':
                    draw_equilateral_triangle(screen, start_pos, radius, color)
                elif tool == 'rhombus':
                    draw_rhombus(screen, start_pos, radius, color)
                else:
                    points.append(start_pos)
                    points = points[-256:]
        
        if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            position = event.pos
            if tool == 'free' or tool == 'eraser':
                points.append(position)
                points = points[-256:]
    
    i = 0
    while i < len(points) - 1:
        drawLineBetween(screen, i, points[i], points[i + 1], radius, color)
        i += 1
    
    pygame.display.flip()
    FramePerSec.tick(FPS)

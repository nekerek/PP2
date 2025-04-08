import pygame 
import sys

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

radius = 15  # Начальный радиус кисти
color = BLUE  # Начальный цвет (синий)
tool = 'free'  # Текущий инструмент: 'free' (свободное рисование), 'circle', 'rect', 'eraser'
points = []  # Список точек для рисования линии

# Функция сглаживания линии между двумя точками
def drawLineBetween(screen, index, start, end, width, color):
    dx = start[0] - end[0]  # Разница по X
    dy = start[1] - end[1]  # Разница по Y
    iterations = max(abs(dx), abs(dy))  # Определяем количество шагов
    for i in range(iterations):  # Рисуем точку на каждом шаге
        progress = i / iterations  # От 0 до 1
        aprogress = 1 - progress  # Обратный прогресс
        x = int(aprogress * start[0] + progress * end[0])  # Интерполяция координаты X
        y = int(aprogress * start[1] + progress * end[1])  # Интерполяция координаты Y
        pygame.draw.circle(screen, color, (x, y), width)  # Рисуем круг в промежуточной точке

# Главный игровой цикл
while True:
    pressed = pygame.key.get_pressed()  # Получаем список всех нажатых клавиш
    alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]  # Проверка, удерживается ли Alt
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]  # Проверка, удерживается ли Ctrl
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            # Переключение цвета и инструмента
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
                    pygame.draw.rect(screen, color, (*start_pos, radius * 2, radius * 2))
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
    
    pygame.display.update()

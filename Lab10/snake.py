import pygame
import sys
import time
import random
import psycopg2

# Параметры базы данных
DataBase = {
    'host': 'localhost',        # адрес сервера БД
    'port': 5432,               # порт PostgreSQL
    'database': 'university',   # имя базы данных
    'user': 'postgres',         # пользователь
    'password': '12345678'      # пароль
}

# Инициализация базы данных

def init_db():
    conn = psycopg2.connect(**DataBase)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            level INTEGER DEFAULT 1,
            score INTEGER DEFAULT 0,
            saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    )
    conn.commit()
    return conn, cur

# Ввод имени пользователя
username = input("Введите имя пользователя: ")
conn, cur = init_db()
cur.execute("SELECT id FROM users WHERE username = %s", (username,))
row = cur.fetchone()
if row:
    user_id = row[0]
    cur.execute("SELECT level, score FROM users WHERE id = %s", (user_id,))
    rec = cur.fetchone()
    if rec:
        level, score = rec
        print(f"С возвращением {username}, уровень {level}, счёт {score}")
    else:
        level, score = 1, 0
else:
    cur.execute("INSERT INTO users(username) VALUES(%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    level, score = 1, 0
conn.commit()

# Настройка Pygame
pygame.init()
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake')

levels = [
    {'threshold': 0,   'speed': 10, 'walls': False},
    {'threshold': 50,  'speed': 12, 'walls': False},
    {'threshold': 100, 'speed': 15, 'walls': True},
    {'threshold': 200, 'speed': 18, 'walls': True},
    {'threshold': 300, 'speed': 22, 'walls': True},
]

def get_level(score):
    idx = 0
    for i, lvl in enumerate(levels):
        if score >= lvl['threshold']:
            idx = i
    return idx

snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

target_fruit = lambda: [random.randrange(1, SCREEN_WIDTH // 10) * 10,
                        random.randrange(1, SCREEN_HEIGHT // 10) * 10]
fruit_position = target_fruit()
fruit_spawn = True

direction = 'RIGHT'
change_to = direction
paused = False
font = pygame.font.SysFont('timesnewroman', 20)

def show_info():
    lvl_idx = get_level(score)
    info = f'User:{username} Score:{score} Level:{lvl_idx + 1}'
    surf = font.render(info, True, WHITE)
    game_window.blit(surf, (10, 10))

def draw_walls(enabled):
    if enabled:
        t = 20
        pygame.draw.rect(game_window, RED, (0, 0, SCREEN_WIDTH, t))
        pygame.draw.rect(game_window, RED, (0, 0, t, SCREEN_HEIGHT))
        pygame.draw.rect(game_window, RED, (0, SCREEN_HEIGHT - t, SCREEN_WIDTH, t))
        pygame.draw.rect(game_window, RED, (SCREEN_WIDTH - t, 0, t, SCREEN_HEIGHT))

def game_over():
    lvl_idx = get_level(score)
    cur.execute(
        "UPDATE users SET level=%s, score=%s WHERE id=%s",
        (lvl_idx + 1, score, user_id)
    )
    conn.commit()
    over = font.render(f'Игра окончена! Итоговый счёт:{score}', True, RED)
    rect = over.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    game_window.blit(over, rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
            if not paused:
                if event.key == pygame.K_UP and direction != 'DOWN': change_to = 'UP'
                if event.key == pygame.K_DOWN and direction != 'UP': change_to = 'DOWN'
                if event.key == pygame.K_LEFT and direction != 'RIGHT': change_to = 'LEFT'
                if event.key == pygame.K_RIGHT and direction != 'LEFT': change_to = 'RIGHT'

    if paused:
        p = font.render('ПАУЗА - P для продолж.', True, RED)
        game_window.blit(p, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        FramePerSec.tick(5)
        continue

    lvl_idx = get_level(score)
    cfg = levels[lvl_idx]
    snake_speed = cfg['speed']
    show_walls = cfg['walls']

    direction = change_to
    if direction == 'UP': snake_position[1] -= 10
    if direction == 'DOWN': snake_position[1] += 10
    if direction == 'LEFT': snake_position[0] -= 10
    if direction == 'RIGHT': snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    if snake_position == fruit_position:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = target_fruit()
        fruit_spawn = True

    game_window.fill(BLACK)
    draw_walls(show_walls)
    for pos in snake_body:
        pygame.draw.rect(game_window, GREEN, (pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, WHITE, (fruit_position[0], fruit_position[1], 10, 10))

    show_info()

    w_off = 10 if show_walls else 0
    if (snake_position[0] < w_off or snake_position[0] >= SCREEN_WIDTH - w_off or
        snake_position[1] < w_off or snake_position[1] >= SCREEN_HEIGHT - w_off):
        game_over()
    for block in snake_body[1:]:
        if snake_position == block: game_over()

    pygame.display.flip()
    FramePerSec.tick(snake_speed)
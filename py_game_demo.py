import pygame
import random

WIDTH = 400
HEIGHT = 400
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
# Рендеринг
screen.fill(WHITE)
pygame.draw.line(screen, BLACK,
                 [10, 30],
                 [290, 15], 10)

# Цикл игры
running = True

while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление



    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
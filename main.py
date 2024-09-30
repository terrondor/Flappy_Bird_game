import pygame
from pygame.locals import *


pygame.init()

clock = pygame.time.Clock()
fps = 60

screenWidth = 864
screenHeight = 936

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Flappy bird')

ground_scroll = 0
scroll_speed = 4

# Загрузка картинок
bg = pygame.image.load('bg.png')
ground_ing = pygame.image.load('ground.png')

run = True
while run:
    clock.tick(fps)

    # Рисум бекграунд
    screen.blit(bg, (0, 0))
    # Рисуем землю и подстраиваем ее
    screen.blit(ground_ing, (ground_scroll, 768))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

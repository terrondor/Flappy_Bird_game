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


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.counter += 1
        flap_cooldown = 5

        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]


bird_group = pygame.sprite.Group()

flappy = Bird(100, int(screenHeight / 2))

bird_group.add(flappy)

run = True
while run:
    clock.tick(fps)

    # Рисум бекграунд
    screen.blit(bg, (0, 0))

    bird_group.draw(screen)
    bird_group.update()
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

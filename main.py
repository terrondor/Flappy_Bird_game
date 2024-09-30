import pygame
import time
import random

from pygame.examples.cursors import image

black = (0, 0, 0)
white = (255, 255, 255)
blue = (34, 139, 34)
green = (64, 224, 208)

pygame.init()

surfaceWidth = 800
surfaceHeight = 600
surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption('Flappy bird')
clock = pygame.time.Clock()

img = pygame.image.load('flap.png')
img_width = img.get_size()[0]
img_height = img.get_size()[1]


def show_score(current_score):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Score: ' + str(current_score), True, white)
    surface.blit(text, [3, 3])


def create_block(x_block, y_block, block_width, block_height, gap):
    pygame.draw.rect(surface, blue, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface, green, [x_block, y_block + block_height + gap, block_width, surfaceHeight])


def makeTextObject(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def reply_or_quit():
    for event in pygame.event.get([pygame.QUIT, pygame.KEYDOWN]):
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type==pygame.KEYDOWN:
            continue

        return event.key
    return None


def bird(x, y, image):
    surface.blit(image, (x, y))


def main():
    x = 150
    y = 200
    y_move = 0

    x_block = surfaceWidth
    y_block = 0

    block_width = 50
    block_height = random.randint(0, surfaceHeight / 2)
    gap = img_height * 5

    # speed of block
    block_move = 5

    score = 0
    game_over = False

    # Game loop
    while not game_over:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over = True

            # keydown когда кнопка нажата и keyup когда она отпущена
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    y_move = -5

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    y_move = 5

        y = y + y_move

        surface.fill(blue)
        bird(x, y, image)
        show_score(score)
        # Update the display
        pygame.display.update()
        clock.tick(80)

    pygame.quit()
    quit()


main()
pygame.quit()
quit()

import pygame
from pygame.locals import *


def drawBlock():
    surface.fill((110, 110, 5))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

if __name__ == '__main__':
    pygame.init()

    surface = pygame.display.set_mode((600,400))
    surface.fill((110, 110, 5))

    block = pygame.image.load('resources/block.jpg').convert()
    block_x = 100
    block_y = 100
    surface.blit(block, (block_x, block_y))

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_q:
                    running = False
                if event.key == K_UP:
                    block_y -= 8
                    drawBlock()
                if event.key == K_DOWN:
                    block_y += 8
                    drawBlock()
                if event.key == K_RIGHT:
                    block_x += 8
                    drawBlock()
                if event.key == K_LEFT:
                    block_x -= 8
                    drawBlock()

            elif event.type == QUIT:
                running = False
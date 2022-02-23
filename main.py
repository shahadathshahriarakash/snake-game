import pygame
from pygame.locals import *
import time


class Snake:
    def __init__(self, surface):
        self.surface = surface
        self.block = pygame.image.load('resources/block.jpg').convert()
        self.x = 100
        self.y = 100
        self.direction = 'UP'

    def drawSnake(self):
        self.surface.fill((110, 110, 5))
        self.surface.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def moveUP(self):
        self.direction = 'UP'

    def moveDOWN(self):
        self.direction = 'DOWN'

    def moveRIGHT(self):
        self.direction = 'RIGHT'

    def moveLEFT(self):
        self.direction = 'LEFT'

    def autoWALK(self):
        if self.direction == 'UP':
            self.y -= 10
        if self.direction == 'DOWN':
            self.y += 10
        if self.direction == 'RIGHT':
            self.x += 10
        if self.direction == 'LEFT':
            self.x -= 10

        self.drawSnake()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((600, 400))
        self.surface.fill((110, 110, 5))
        self.snake = Snake(self.surface)
        self.snake.drawSnake()

    def runGame(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    if event.key == K_q:
                        running = False

                    if event.key == K_UP:
                        self.snake.moveUP()

                    if event.key == K_DOWN:
                        self.snake.moveDOWN()

                    if event.key == K_RIGHT:
                        self.snake.moveRIGHT()

                    if event.key == K_LEFT:
                        self.snake.moveLEFT()

                elif event.type == QUIT:
                    running = False

            self.snake.autoWALK()
            time.sleep(0.1)

if __name__ == '__main__':
    game = Game()
    game.runGame()
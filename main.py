import pygame
from pygame.locals import *


class Snake:
    def __init__(self, surface):
        self.surface = surface
        self.block = pygame.image.load('resources/block.jpg').convert()
        self.x = 100
        self.y = 100

    def drawSnake(self):
        self.surface.fill((110, 110, 5))
        self.surface.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def moveUP(self):
        self.y -= 10
        self.drawSnake()

    def moveDOWN(self):
        self.y += 10
        self.drawSnake()

    def moveRIGHT(self):
        self.x += 10
        self.drawSnake()

    def moveLEFT(self):
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

if __name__ == '__main__':
    game = Game()
    game.runGame()
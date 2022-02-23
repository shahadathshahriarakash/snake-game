import pygame
from pygame.locals import *
import time

class Apple:
    def __init__(self, surface):
        self.surface = surface
        self.apple = pygame.image.load('resources/apple.jpg').convert()
        self.x = 120
        self.y = 120

    def drawApple(self):
        self.surface.blit(self.apple, (self.x, self.y))
        pygame.display.flip()

class Snake:
    def __init__(self, surface, length):
        self.size = 40
        self.length = length
        self.surface = surface
        self.block = pygame.image.load('resources/block.jpg').convert()
        self.x = [self.size]*self.length
        self.y = [self.size]*self.length
        self.direction = 'UP'

    def drawSnake(self):
        self.surface.fill((110, 110, 5))
        for i in range(self.length):
            self.surface.blit(self.block, (self.x[i], self.y[i]))
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
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'UP':
            self.y[0] -= self.size
        if self.direction == 'DOWN':
            self.y[0] += self.size
        if self.direction == 'RIGHT':
            self.x[0] += self.size
        if self.direction == 'LEFT':
            self.x[0] -= self.size

        self.drawSnake()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((600, 400))
        self.surface.fill((110, 110, 5))
        self.snake = Snake(self.surface, 4)
        self.snake.drawSnake()
        self.apple = Apple(self.surface)
        self.apple.drawApple()

    def draw(self):
        self.snake.autoWALK()
        self.apple.drawApple()

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

            self.draw()
            time.sleep(0.2)

if __name__ == '__main__':
    game = Game()
    game.runGame()
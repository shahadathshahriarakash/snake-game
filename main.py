import pygame
from pygame.locals import *
import time
import random

size = 40

class Apple:
    def __init__(self, surface):
        self.surface = surface
        self.apple = pygame.image.load('resources/apple.jpg').convert()
        self.x = 120
        self.y = 120

    def drawApple(self):
        self.surface.blit(self.apple, (self.x, self.y))
        pygame.display.flip()

    def reAppear(self):
        self.x = random.randint(0, 24)*size
        self.y = random.randint(0, 14)*size

class Snake:
    def __init__(self, surface, length):
        self.length = length
        self.surface = surface
        self.block = pygame.image.load('resources/block.jpg').convert()
        self.x = [size]*self.length
        self.y = [size]*self.length
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
            self.y[0] -= size
        if self.direction == 'DOWN':
            self.y[0] += size
        if self.direction == 'RIGHT':
            self.x[0] += size
        if self.direction == 'LEFT':
            self.x[0] -= size

        self.drawSnake()

    def incrementLenght(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 600))
        self.surface.fill((110, 110, 5))
        self.snake = Snake(self.surface, 1)
        self.snake.drawSnake()
        self.apple = Apple(self.surface)
        self.apple.drawApple()

    def isCollision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True

        return False

    def draw(self):
        self.snake.autoWALK()
        self.apple.drawApple()
        self.displayScore()
        pygame.display.flip()

        if self.isCollision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.incrementLenght()
            self.apple.reAppear()

    def displayScore(self):
        font = pygame.font.SysFont('Arial', 30)
        score = font.render(f'SCORE {(self.snake.length - 1)}', True, (255, 255, 255))
        self.surface.blit(score, (850, 5))

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
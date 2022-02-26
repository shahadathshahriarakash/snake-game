import pygame
from pygame.locals import *
import time
import random

size = 20

class Food:
    def __init__(self, surface):
        self.surface = surface
        self.apple = pygame.image.load('resources/food.png').convert()
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
        self.block = pygame.image.load('resources/snake.png').convert()
        self.x = [size]*self.length
        self.y = [size]*self.length
        self.direction = 'DOWN'

    def drawSnake(self):
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
        pygame.mixer.init()
        self.playBGM()
        self.surface = pygame.display.set_mode((500, 500))
        self.snake = Snake(self.surface, 1)
        self.snake.drawSnake()
        self.apple = Food(self.surface)
        self.apple.drawApple()

    def playBGM(self):
        pygame.mixer.music.load('resources/bgm.wav')
        pygame.mixer.music.play(-1, 0)

    def playSoundEffects(self, soundName):
        if soundName == 'gameover':
            sound = pygame.mixer.Sound('resources/gameover.wav')
        elif soundName == 'points':
            sound = pygame.mixer.Sound('resources/points.wav')

        pygame.mixer.Sound.play(sound)

    def renderBGI(self):
        bg = pygame.image.load('resources/background.jpg')
        self.surface.blit(bg, (0, 0))

    def renderGameOver(self):
        bg = pygame.image.load('resources/gameover.jpg')
        self.surface.blit(bg, (0, 0))

    def renderPause(self):
        bg = pygame.image.load('resources/pause.jpg')
        self.surface.blit(bg, (0, 0))
        pygame.mixer.music.pause()

    def Pause(self):
        self.pause = True
        self.renderPause()
        font = pygame.font.SysFont('freesansbold.ttf', 50)
        line = font.render(f'SCORE {(self.snake.length - 1)}', True, (48, 71, 94))
        self.surface.blit(line, (50, 150))
        pygame.display.flip()

    def resetGame(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Food(self.surface)

    def isCollision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True

        return False

    def draw(self):
        self.renderBGI()
        self.snake.autoWALK()
        self.apple.drawApple()
        self.displayScore()
        pygame.display.flip()

        if self.isCollision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.playSoundEffects('points')
            self.snake.incrementLenght()
            self.apple.reAppear()

        for i in range(1, self.snake.length):
            if self.isCollision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.playSoundEffects('gameover')
                raise 'Game Over'

    def displayScore(self):
        font = pygame.font.SysFont('freesansbold.ttf', 30)
        score = font.render(f'{(self.snake.length - 1)}', True, (48, 71, 94))
        self.surface.blit(score, (3, 0))


    def displayGameOver(self):
        self.renderGameOver()
        font = pygame.font.SysFont('freesansbold.ttf', 50)
        line = font.render(f'SCORE {(self.snake.length - 1)}', True, (48, 71, 94))
        self.surface.blit(line, (50, 350))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def runGame(self):
        running = True
        self.pause = False

        while running:
            for event in pygame.event.get():

                if event.type == KEYDOWN:

                    if event.key == K_q:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        self.pause = False

                    if not self.pause:

                        if event.key == K_UP:
                            self.snake.moveUP()

                        if event.key == K_DOWN:
                            self.snake.moveDOWN()

                        if event.key == K_RIGHT:
                            self.snake.moveRIGHT()

                        if event.key == K_LEFT:
                            self.snake.moveLEFT()

                        if event.key == K_m:
                            self.Pause()

                elif event.type == QUIT:
                    running = False

            try:
                if not self.pause:
                    self.draw()

            except Exception as e:
                self.displayGameOver()
                self.pause = True
                self.resetGame()

            time.sleep(0.10)

if __name__ == '__main__':
    game = Game()
    game.runGame()
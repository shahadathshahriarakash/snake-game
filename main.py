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
        font = pygame.font.SysFont('Arial', 15)
        score = font.render(f'SCORE {(self.snake.length - 1)}', True, (255, 0, 179))
        self.surface.blit(score, (425, 3))

    def displayGameOver(self):
        self.renderBGI()
        font = pygame.font.SysFont('Arial', 20)
        line1 = font.render('!!! GAME IS OVER !!!', True, (235, 132, 7))
        self.surface.blit(line1, (250, 200))
        line2 = font.render(f'Your Score is: {(self.snake.length - 1)}', True, (255, 0, 179))
        self.surface.blit(line2, (300, 250))
        line3 = font.render('Press ENTER to play again.', True, (7, 235, 45))
        self.surface.blit(line3, (300, 300))
        line4 = font.render('Press q to exit the game.', True, (235, 7, 7))
        self.surface.blit(line4, (300, 350))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def runGame(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    if event.key == K_q:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:

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

            try:
                if not pause:
                    self.draw()

            except Exception as e:
                self.displayGameOver()
                pause = True
                self.resetGame()

            time.sleep(0.10)

if __name__ == '__main__':
    game = Game()
    game.runGame()
# Importing Lib

import pygame
from pygame.locals import *
import time
import random

# Global size fot objects

size = 20

# Creating Food

class Food:
    def __init__(self, surface):
        self.surface = surface
        self.apple = pygame.image.load('resources/food.png').convert()
        self.x = 120
        self.y = 120

    # Drawing food in display

    def drawApple(self):
        self.surface.blit(self.apple, (self.x, self.y))
        pygame.display.flip()

    # Reappearing food after eating at random position

    def reAppear(self):
        self.x = random.randint(0, 24)*size
        self.y = random.randint(0, 14)*size

# Creating Food

class Snake:
    def __init__(self, surface, length):
        self.length = length
        self.surface = surface
        self.block = pygame.image.load('resources/snake.png').convert()
        self.x = [size]*self.length
        self.y = [size]*self.length
        self.direction = 'DOWN'

    # Drawing snake

    def drawSnake(self):
        for i in range(self.length):
            self.surface.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    # Snakes movement

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

    # Increasing snake size after eating food

    def incrementLenght(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

# Main Game

class Game:

    # Drawing window

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('snakePy by shahadathshahr2')
        pygame.mixer.init()
        self.playBGM()
        self.surface = pygame.display.set_mode((500, 500))
        self.snake = Snake(self.surface, 1)
        self.snake.drawSnake()
        self.apple = Food(self.surface)
        self.apple.drawApple()

    # Adding Background Music

    def playBGM(self):
        pygame.mixer.music.load('resources/bgm.wav')
        pygame.mixer.music.play(-1, 0)

    # Adding Sound Effects

    def playSoundEffects(self, soundName):
        global sound
        if soundName == 'gameover':
            sound = pygame.mixer.Sound('resources/gameover.wav')
        elif soundName == 'points':
            sound = pygame.mixer.Sound('resources/points.wav')

        pygame.mixer.Sound.play(sound)

    # Rendering objects

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

    # Pause function

    def Pause(self):
        self.pause = True
        self.renderPause()
        font = pygame.font.SysFont('freesansbold.ttf', 50)
        line = font.render(f'SCORE {(self.snake.length - 1)}', True, (48, 71, 94))
        self.surface.blit(line, (50, 150))
        pygame.display.flip()

    # Reset function for reset the game after game over

    def resetGame(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Food(self.surface)

    # Collision Rule

    def isCollision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True

        return False

    # Main drawing function

    def draw(self):
        self.renderBGI()
        self.snake.autoWALK()
        self.apple.drawApple()
        self.displayScore()
        pygame.display.flip()

        # Snake eat food logic

        if self.isCollision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.playSoundEffects('points')
            self.snake.incrementLenght()
            self.apple.reAppear()

        # Snake touch itself logic game over logic

        for i in range(1, self.snake.length):
            if self.isCollision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.playSoundEffects('gameover')
                raise 'Game Over'

        # Snake touch boundary logic game over logic

        if not (0 <= self.snake.x[0] <= 500 and 0 <= self.snake.y[0] <= 500):
            self.playSoundEffects('gameover')
            raise "Hit the boundry error"

    # Score displaying function

    def displayScore(self):
        font = pygame.font.SysFont('freesansbold.ttf', 30)
        score = font.render(f'{(self.snake.length - 1)}', True, (48, 71, 94))
        self.surface.blit(score, (3, 0))

    # Game over displaying function

    def displayGameOver(self):
        self.renderGameOver()
        font = pygame.font.SysFont('freesansbold.ttf', 50)
        line = font.render(f'SCORE {(self.snake.length - 1)}', True, (48, 71, 94))
        self.surface.blit(line, (50, 350))
        pygame.mixer.music.pause()
        pygame.display.flip()

    # Main run function

    def runGame(self):
        running = True
        self.pause = False

        # Event Loop

        while running:
            for event in pygame.event.get():

                # Setting controls

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

                        if event.key == K_w:
                            self.snake.moveUP()

                        if event.key == K_s:
                            self.snake.moveDOWN()

                        if event.key == K_d:
                            self.snake.moveRIGHT()

                        if event.key == K_a:
                            self.snake.moveLEFT()

                        if event.key == K_m:
                            self.Pause()

                        if event.key == K_ESCAPE:
                            self.Pause()

                elif event.type == QUIT:
                    running = False

            # Finding for game over logic

            try:
                if not self.pause:
                    self.draw()

            except Exception as e:
                self.displayGameOver()
                self.pause = True
                self.resetGame()

            time.sleep(0.13)

# Call the main functions to run the game

if __name__ == '__main__':
    game = Game()
    game.runGame()
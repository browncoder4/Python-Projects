import pygame
from pygame.locals import *
import time
import random

pygame.init()

red = (255, 0, 0)
blue = (51, 153, 255)
grey = (192, 192, 192)
green = (51, 102, 0)

width = 600
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

snake_size = 10
snake_speed = 15

fontStyle = pygame.font.SysFont("calibri", 26)
scoreFont = pygame.font.SysFont("comicsansms", 30)

def score_display(score):
    value = scoreFont.render(f"SCORE: {score}", True, red)
    window.blit(value, [0, 0])

def our_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, blue, [x[0], x[1], snake_size, snake_size])

def message(msg, color):
    msg_display = fontStyle.render(msg, True, color)
    window.blit(msg_display, [width / 6, height / 3])

def gameLoop():
    gameOver = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not gameOver:
        while game_close:
            window.fill(grey)
            message("You lost! Press P-Play Again or Q-Quit", red)
            score_display(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_size
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_size

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(grey)

        pygame.draw.rect(window, green, [foodx, foody, snake_size, snake_size])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_size, snake_list)
        score_display(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()

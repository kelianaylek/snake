import pygame
import time
import random
from display import *
from colors import *

pygame.init()

from fonts import *
from score import Your_score
from snake import our_snake
from message import message

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

def gameLoop():
    game_over = False
    game_close = False
    baseTime = 0
    gameIsPaused = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("Game Over ! C pour restart, Q pour quitter", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    x1_change = -snake_block
                    y1_change = 0
                    lastDirection = "left"
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                    lastDirection = "right"
                elif event.key == pygame.K_z:
                    y1_change = -snake_block
                    x1_change = 0
                    lastDirection = "up"
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0
                    lastDirection = "down"

                elif event.key == pygame.K_a:
                    if gameIsPaused == False:
                        gameIsPaused = True
                        x1_change = 0
                        y1_change = 0
                    elif gameIsPaused == True:
                        gameIsPaused = False
                        if lastDirection == "left":
                            x1_change = -snake_block
                            y1_change = 0
                        elif lastDirection == "right":
                            x1_change = snake_block
                            y1_change = 0
                        elif lastDirection == "up":
                            y1_change = -snake_block
                            x1_change = 0
                        elif lastDirection == "down":
                            y1_change = snake_block
                            x1_change = 0

                elif event.key == pygame.K_SPACE:
                    gameIsPaused = False
                    if lastDirection == "up":
                        y1 += -40
                    elif lastDirection == "down":
                        y1 += 40
                    elif lastDirection == "left":
                        x1 += -40
                    elif lastDirection == "right":
                        x1 += 40


        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        if gameIsPaused is False:
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True



        if gameIsPaused is False:
            baseTime += 0.065
        else:
            pauseMessage = score_font.render("Pause", True, white)
            dis.blit(pauseMessage, [250, 150])

        timeRender = score_font.render("time: " + str(round((baseTime))), True, white)
        dis.blit(timeRender, [450, 0])



        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
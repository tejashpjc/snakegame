import pygame
import time
import random

pygame.init()

# size of window
width = 600
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# the colors

black =  (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
apple_red = (255, 0, 0)

# settings of the snake

snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()

font = pygame.font.SysFont("bahnschrift", 20)

def message(msg, color, x, y):
    mesg = font.render(msg, True, color)
    window.blit(mesg, [x, y])

def game_loop():
    game_over = False
    game_close = False
    
    x = width / 2
    y = height / 2
    x_change = 0
    y_change = 0
    
    snake = []
    length = 1
    
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    
    bomb_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    bomb_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    
    while not game_over:
        while game_close:
            window.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red, width / 6, height / 3)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0
        
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        
        x += x_change
        y += y_change
        window.fill(black)
        pygame.draw.rect(window, apple_red, [food_x, food_y, snake_block, snake_block])
        pygame.draw.rect(window, red, [bomb_x, bomb_y, snake_block, snake_block])
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake.append(snake_head)
        if len(snake) > length:
            del snake[0]
        
        for segment in snake[:-1]:
            if segment == snake_head:
                game_close = True
        
        for part in snake:
            pygame.draw.rect(window, green, [part[0], part[1], snake_block, snake_block])
        
        pygame.display.update()
        
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length += 1
        
        if x == bomb_x and y == bomb_y:
            game_close = True
        
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

    game_loop()
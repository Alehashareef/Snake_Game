import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set display dimensions
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Load background music
pygame.mixer.init()
pygame.mixer.music.load("background.mp3.mp3")  # Make sure to have a background.mp3 file
pygame.mixer.music.play(-1)  # Loop the music indefinitely

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
yellow = (255, 255, 0)
green = (0, 255, 0)

# Snake block size & speed
block_size = 10
speed = 10

# Font settings
font = pygame.font.SysFont("bahnschrift", 25)

def show_score(score):
    value = font.render(f"Score: {score}", True, white)
    win.blit(value, [10, 10])

def message(msg, color):
    text = font.render(msg, True, color)
    win.blit(text, [width // 3, height // 3])
    pygame.display.update()
    time.sleep(2)

def start_screen():
    win.fill(black)
    message("Welcome To Snake Game!", green)
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                waiting = False

def game_loop():
    start_screen()
    while True:
        game_over = False
        x, y = width // 2, height // 2
        x_change, y_change = block_size, 0  # Snake starts moving right
        
        snake = [[x, y], [x - block_size, y], [x - (2 * block_size), y], [x - (3 * block_size), y]]  # Start with four blocks
        length = 4
        score = 0  # Initialize score as zero
        
        food_x = random.randint(0, (width - block_size) // block_size) * block_size
        food_y = random.randint(0, (height - block_size) // block_size) * block_size
        
        clock = pygame.time.Clock()
        
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and x_change == 0:
                        x_change = -block_size
                        y_change = 0
                    elif event.key == pygame.K_RIGHT and x_change == 0:
                        x_change = block_size
                        y_change = 0
                    elif event.key == pygame.K_UP and y_change == 0:
                        y_change = -block_size
                        x_change = 0
                    elif event.key == pygame.K_DOWN and y_change == 0:
                        y_change = block_size
                        x_change = 0
            
            x += x_change
            y += y_change
            if x >= width or x < 0 or y >= height or y < 0:
                game_over = True
            
            win.fill(black)
            pygame.draw.rect(win, red, [food_x, food_y, block_size, block_size])
            
            snake.append([x, y])
            if len(snake) > length:
                del snake[0]
            
            for segment in snake[:-1]:
                if segment == [x, y]:
                    game_over = True
            
            for i, part in enumerate(snake):
                if i == len(snake) - 1:
                    pygame.draw.rect(win, yellow, [part[0], part[1], block_size, block_size])
                    pygame.draw.circle(win, green, (part[0] + 3, part[1] + 3), 2)  # Left eye
                    pygame.draw.circle(win, green, (part[0] + 7, part[1] + 3), 2)  # Right eye
                elif i == 0:
                    pygame.draw.circle(win, green, (part[0] + 5, part[1] + 5), block_size // 2)  # Tail as a green circle
                else:
                    pygame.draw.rect(win, yellow, [part[0], part[1], block_size, block_size])
            
            show_score(score)
            pygame.display.update()
            
            if x == food_x and y == food_y:
                food_x = random.randint(0, (width - block_size) // block_size) * block_size
                food_y = random.randint(0, (height - block_size) // block_size) * block_size
                length += 1
                score += 1  # Increase score when food is eaten
            
            clock.tick(speed)
        
        message("Game Over!", red)
        start_screen()

game_loop()

import pygame
import random

game_window = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("Smart Snakes")
pygame.display.set_mode((1100, 650))

pygame.init()
pygame.mixer.music.play()
pygame.display.update()


# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)


game_over = False
exit_game = False
snake_x = 45
snake_y = 55
snake_size_x = 40
snake_size_y = 40

food_size = 40
fps = 60
velocity_x = 0
velocity_y = 0
food_x = random.randint(0, 1100)
food_y = random.randint(0, 650)
score = 0


clock = pygame.time.Clock()


while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x += 10
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x -= 10
                velocity_y = 0

            if event.key == pygame.K_DOWN:
                velocity_y += 10
                velocity_x = 0

            if event.key == pygame.K_UP:
                velocity_y -= 10
                velocity_x = 0
    
    snake_x += velocity_x
    snake_y += velocity_y
    
    if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:
        score += 1
        print(f"Score: {score}")
        food_x = random.randint(0, 1100)
        food_y = random.randint(0, 650)
        snake_size_x += 40
        pygame.display.update()
    game_window.fill(white)
    pygame.draw.rect(game_window, red, [food_x, food_y, food_size, food_size])
    pygame.draw.rect(game_window, black, [snake_x, snake_y, snake_size_x, snake_size_y])
    pygame.display.update()
    clock.tick(fps)

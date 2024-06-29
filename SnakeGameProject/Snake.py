import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Window size
window_x = 720
window_y = 480
screen = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("SPOOK GAMES")

# Game variables
clock = pygame.time.Clock()
running = True
score = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
fruits_position = []  # List to hold the positions of multiple fruits
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

direction_of_snake = "RIGHT"
move_to = direction_of_snake
FruitSpawned = True

# Function to spawn fruits
def spawn_fruits(count):
    for _ in range(count):
        new_fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
        fruits_position.append(new_fruit_position)

# Function to display score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)

# Function to handle game over
def Game_Over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, "Red")
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main game loop
while running:
    screen.fill("purple")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_to = "UP"
            elif event.key == pygame.K_DOWN:
                move_to = "DOWN"
            elif event.key == pygame.K_RIGHT:
                move_to = "RIGHT"
            elif event.key == pygame.K_LEFT:
                move_to = "LEFT"

    # Handle snake movement direction
    if move_to == "UP" and direction_of_snake != 'DOWN':
        direction_of_snake = 'UP'
    elif move_to == "DOWN" and direction_of_snake != "UP":
        direction_of_snake = "DOWN"
    elif move_to == "LEFT" and direction_of_snake != "RIGHT":
        direction_of_snake = "LEFT"
    elif move_to == "RIGHT" and direction_of_snake != "LEFT":
        direction_of_snake = "RIGHT"

    # Update snake position based on direction
    if direction_of_snake == 'UP':
        player_pos[1] -= 10
    elif direction_of_snake == 'DOWN':
        player_pos[1] += 10
    elif direction_of_snake == 'LEFT':
        player_pos[0] -= 10
    elif direction_of_snake == 'RIGHT':
        player_pos[0] += 10

    # Check collision with fruits
    for fruit_position in fruits_position:
        if player_pos[0] == fruit_position[0] and player_pos[1] == fruit_position[1]:
            score += 10
            fruits_position.remove(fruit_position)
            spawn_fruits(1)  # Spawn a new fruit when one is eaten

    # Update snake body and fruit drawing
    snake_body.insert(0, list(player_pos))
    snake_body.pop()

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(screen, "Red", pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw fruits
    for fruit_position in fruits_position:
        pygame.draw.rect(screen, "white", pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # GControls when the body of the snake touches corners of the application and quits the game
    if snake_body[0][0] < 0 or snake_body[0][0] > window_x - 10 or snake_body[0][1] < 0 or snake_body[0][1] > window_y - 10:
        Game_Over()

    for block in snake_body[1:]:
        if player_pos[0] == block[0] and player_pos[1] == block[1]:
            Game_Over()

    # Display score
    show_score(1, 'white', 'times new roman', 20)

    # Update the screen
    pygame.display.update()

    # Cap the frame rate
    clock.tick(15)

# Quit pygame properly
pygame.quit()

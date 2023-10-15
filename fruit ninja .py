import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
FRUIT_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue
BASKET_COLOR = (50, 50, 50)
FONT = pygame.font.Font(None, 36)

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Ninja")

# Fruit settings
fruit_width, fruit_height = 80, 80
fruit_speed = 5
fruits = []

# Score
score = 0

# Game over flag
game_over = False

# Functions
def draw_fruit(x, y, color):
    pygame.draw.ellipse(screen, color, (x, y, fruit_width, fruit_height))

def display_score(score):
    score_text = FONT.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

def game_over_screen():
    game_over_text = FONT.render("Game Over", True, WHITE)
    score_text = FONT.render("Your Score: " + str(score), True, WHITE)
    restart_text = FONT.render("Press any key to Restart", True, WHITE)

    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    screen.blit(score_text, (WIDTH // 2 - 80, HEIGHT // 2))
    screen.blit(restart_text, (WIDTH // 2 - 120, HEIGHT // 2 + 50))

# Game loop
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # Restart the game
            score = 0
            fruits = []
            game_over = False

    if not game_over:
        # Generate new fruits
        if len(fruits) < 5:
            fruit_x = random.randint(0, WIDTH - fruit_width)
            fruit_color = random.choice(FRUIT_COLORS)
            fruits.append([fruit_x, HEIGHT, fruit_color])

        # Move fruits
        for fruit in fruits:
            fruit[1] -= fruit_speed

        # Check for collisions with the mouse cursor
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for fruit in fruits:
            if (
                mouse_x > fruit[0] and
                mouse_x < fruit[0] + fruit_width and
                mouse_y > fruit[1] and
                mouse_y < fruit[1] + fruit_height
            ):
                fruits.remove(fruit)
                score += 1

        # Remove fruits that go out of the screen
        fruits = [fruit for fruit in fruits if fruit[1] > 0]

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the fruits
        for fruit in fruits:
            draw_fruit(fruit[0], fruit[1], fruit[2])

        # Display the score
        display_score(score)

    else:
        # Display game over screen with final statistics
        game_over_screen()

        # Wait for any key press to close the game or restart
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Restart the game
                score = 0
                fruits = []
                game_over = False

    pygame.display.flip()
    clock.tick(FPS)

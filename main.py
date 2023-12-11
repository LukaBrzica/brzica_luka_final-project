# File created by Luka Brzica on 11/26

'''
Project idea:
Create a retro soccer game 

Goals:
create players you can control 
goals and scoreboard 
pvp
'''
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1024, 768
FPS = 60
CELL_SIZE = 20
PLAYER_SIZE = 50
GOAL_WIDTH = 100
GOAL_AREA_WIDTH = 30
SCOREBOARD_HEIGHT = 50  # Height of the scoreboard
FAN_RADIUS = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GOLD = (255, 223, 0)
BLUE = (0,0,255)
FAN_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]

# Create the Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SOCCERPONG")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 36)

# Score variables
score_team_a = 0
score_team_b = 0

# Player variables
player_speed = 8  # Increase player speed
player_a_pos = [WIDTH // 4, HEIGHT // 2]
player_b_pos = [3 * WIDTH // 4, HEIGHT // 2]

# Fans variables
fan_positions_top = [(x, 50) for x in range(30, WIDTH, 40)]  # Adjusted for horizontal arrangement
fan_positions_bottom = [(x, HEIGHT - 50) for x in range(30, WIDTH, 40)]  # Adjusted for horizontal arrangement

# Ball variables
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [8, 8]  # Increase ball speed

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_a_pos[1] > 0:
        player_a_pos[1] -= player_speed
    if keys[pygame.K_s] and player_a_pos[1] < HEIGHT - PLAYER_SIZE:
        player_a_pos[1] += player_speed
    if keys[pygame.K_a] and player_a_pos[0] > 0:
        player_a_pos[0] -= player_speed
    if keys[pygame.K_d] and player_a_pos[0] < WIDTH // 2 - PLAYER_SIZE:
        player_a_pos[0] += player_speed

    if keys[pygame.K_UP] and player_b_pos[1] > 0:
        player_b_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_b_pos[1] < HEIGHT - PLAYER_SIZE:
        player_b_pos[1] += player_speed
    if keys[pygame.K_LEFT] and player_b_pos[0] > WIDTH // 2:
        player_b_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_b_pos[0] < WIDTH - PLAYER_SIZE:
        player_b_pos[0] += player_speed

    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Ball collision with walls
    if ball_pos[0] <= 0 or ball_pos[0] >= WIDTH:
        ball_speed[0] = -ball_speed[0]

    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Ball collision with players
    if (
        player_a_pos[0] < ball_pos[0] < player_a_pos[0] + PLAYER_SIZE
        and player_a_pos[1] < ball_pos[1] < player_a_pos[1] + PLAYER_SIZE
    ) or (
        player_b_pos[0] < ball_pos[0] < player_b_pos[0] + PLAYER_SIZE
        and player_b_pos[1] < ball_pos[1] < player_b_pos[1] + PLAYER_SIZE
    ):
        ball_speed[0] = -ball_speed[0]
        ball_speed[1] = random.choice([-5, 5])  # Randomize vertical direction

    # Ball collision with goals
    if 0 < ball_pos[0] < GOAL_AREA_WIDTH and (HEIGHT - GOAL_WIDTH) // 2 < ball_pos[1] < (
        HEIGHT + GOAL_WIDTH
    ) // 2:
        # Team B scores
        score_team_b += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [5, 5]

    if WIDTH - GOAL_AREA_WIDTH < ball_pos[0] < WIDTH and (HEIGHT - GOAL_WIDTH) // 2 < ball_pos[1] < (
        HEIGHT + GOAL_WIDTH
    ) // 2:
        # Team A scores
        score_team_a += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [-5, 5]

    # Draw the soccer field
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (0, 0, WIDTH, HEIGHT))
    
    #Draw the semicrcle 
    pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 50, 2)

    # Draw the goals
    pygame.draw.rect(screen, WHITE, (0, (HEIGHT - GOAL_WIDTH) // 2, GOAL_AREA_WIDTH, GOAL_WIDTH))
    pygame.draw.rect(
        screen, WHITE, (WIDTH - GOAL_AREA_WIDTH, (HEIGHT - GOAL_WIDTH) // 2, GOAL_AREA_WIDTH, GOAL_WIDTH)
    )

    # Draw the players
    pygame.draw.rect(screen, BLACK, (player_a_pos[0], player_a_pos[1], PLAYER_SIZE, PLAYER_SIZE))
    pygame.draw.rect(screen, GOLD, (player_a_pos[0] + 2, player_a_pos[1] + 2, PLAYER_SIZE - 4, PLAYER_SIZE - 4))

    pygame.draw.rect(screen, RED, (player_b_pos[0], player_b_pos[1], PLAYER_SIZE, PLAYER_SIZE))
    pygame.draw.rect(screen, BLUE, (player_b_pos[0] + 2, player_b_pos[1] + 2, PLAYER_SIZE - 4, PLAYER_SIZE - 4))

    # Draw the ball
    pygame.draw.circle(screen, BLACK, (int(ball_pos[0]), int(ball_pos[1])), 10)

    # Draw the scoreboard
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, 50))
    text_team_a = font.render("REAL MADRID: {}".format(score_team_a), True, WHITE)
    text_team_b = font.render("BARCELONA: {}".format(score_team_b), True, WHITE)
    screen.blit(text_team_a, (100, 25))
    screen.blit(text_team_b, (WIDTH - 200, 25))

# Draw the fans
    for fan_pos in fan_positions_top + fan_positions_bottom:
        pygame.draw.circle(screen, random.choice(FAN_COLORS), fan_pos, FAN_RADIUS)

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
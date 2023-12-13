# File created by Luka Brzica on 11/26

'''
Project idea:
Create a retro pong soccer game 

Goals:
create players you can control 
goals and scoreboard 
pvp
'''
# Importing pygame, the system, and random.
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Settings
WIDTH, HEIGHT = 1024, 768 # Size of the screen
FPS = 60 # Frames per second used in the game
CELL_SIZE = 20 # The cell represents the width and the height of the of a grid like structure
PLAYER_SIZE = 50 # Area of the player
GOAL_WIDTH = 100 # Width of the goal
GOAL_AREA_WIDTH = 30 # Area of the goal
SCOREBOARD_HEIGHT = 50  # Height of the scoreboard
FAN_RADIUS = 10 # Radius of the circluar fan

# Colors
# Each color corresponds to the "RGB" method in order to produce a certain color
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GOLD = (255, 223, 0)
BLUE = (0,0,255)
FAN_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]
# Fan multiple color characters

# Create the Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SOCCERPONG") # Indicates the name of the game title at teh top of the opened window
clock = pygame.time.Clock() # Creates a clock object in Pygame, which is commonly used to control the frame rate of your game

# Fonts
# Notifies the game of the size and font of the text that will be displayed
# No font and 36 size
font = pygame.font.Font(None, 36)

# Score variables / Starting score of the teams
score_team_a = 0
score_team_b = 0

# Player variables
player_speed = 8  # Changes the player speed, you can adjust by changing the number  
player_a_pos = [WIDTH // 4, HEIGHT // 2] # Sets the starting position of player A
player_b_pos = [3 * WIDTH // 4, HEIGHT // 2] # Sets the starting position of player B

# Fans variables
fan_positions_top = [(x, 50) for x in range(30, WIDTH, 40)]  # Horizontal arrangement of fans on the top that line  up
fan_positions_bottom = [(x, HEIGHT - 50) for x in range(30, WIDTH, 40)]  # Horizontal arrangement of the fans that line up at the bottom of the field

# Ball variables
ball_pos = [WIDTH // 2, HEIGHT // 2] # Ball starting position
ball_speed = [8, 8]  # Ball speed

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# In this code it sets the game as true which allows it to run and continue running until you close the tab which is viewed as quit and the code interprets as false, stopping the game from continuing to run 

    # Player controls
    keys = pygame.key.get_pressed()
    # Means that the value of the key being pressed is true, so the game interprets it 
    if keys[pygame.K_w] and player_a_pos[1] > 0:
        #If the key "w" is pressed and Player A position is greater than 0, player A can move upward on the y-cordinate
        player_a_pos[1] -= player_speed
    # The y-cordinate of Player A is decreased by the value of the "player_speed," moving the player at the speed selected.
    if keys[pygame.K_s] and player_a_pos[1] < HEIGHT - PLAYER_SIZE:
    # This checks that when the key "s" is presed the height of player A is less than the "HEIGHT - PLAYER_SIZE", it would then allow the player to move downward on the y-axis
        player_a_pos[1] += player_speed
    # If it is met, the y-cordinate of Player A is increased by the value of the players speed essentially moving player A downwards 
    if keys[pygame.K_a] and player_a_pos[0] > 0:
        player_a_pos[0] -= player_speed
    # If the key "a" is pressed player A's position will move left as fast as the variable you input for speed
    if keys[pygame.K_d] and player_a_pos[0] < WIDTH // 2 - PLAYER_SIZE:
        player_a_pos[0] += player_speed
    # If the key "d" is pressed player A's position will move right as fast as the input for player speed is
    # In the line "WIDTH // 2 - PLAYER_SIZE" this condition ensures that Player A doesn't move beyond the middle of the screen (up to half of the screen width minus the player size)


# Same thing as above just for the arrow keys 
    if keys[pygame.K_UP] and player_b_pos[1] > 0:
        player_b_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_b_pos[1] < HEIGHT - PLAYER_SIZE:
        player_b_pos[1] += player_speed
    if keys[pygame.K_LEFT] and player_b_pos[0] > WIDTH // 2: #This line of code also prevents player B from moving across the halfway point of the screen just as talked about above
        player_b_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_b_pos[0] < WIDTH - PLAYER_SIZE:
        player_b_pos[0] += player_speed


# Move the ball
    ball_pos[0] += ball_speed[0] # Ball starting position
    ball_pos[1] += ball_speed[1] # Ball starting position direction of moving and speed

# Ball collision with walls
    if ball_pos[0] <= 0 or ball_pos[0] >= WIDTH:
        ball_speed[0] = -ball_speed[0]
        # This code handles the bouncing behavior of the ball when it reaches the left or right boundaries of the game window, making it change its horizontal direction

    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT:
        ball_speed[1] = -ball_speed[1]
        # This code does the same thing as above but changes its vertical direction on collision instead of horizontal 

# Ball collision with players
    if (
        player_a_pos[0] < ball_pos[0] < player_a_pos[0] + PLAYER_SIZE # Checks if the x-coordinate of the ball is within the horizontal boundaries of player A
        and player_a_pos[1] < ball_pos[1] < player_a_pos[1] + PLAYER_SIZE # Checks if the y-coordinate of the ball is within the vertical boundaries of player A
) or (
        player_b_pos[0] < ball_pos[0] < player_b_pos[0] + PLAYER_SIZE # Checks the same thing as above but just for player B
        and player_b_pos[1] < ball_pos[1] < player_b_pos[1] + PLAYER_SIZE # ^
    ):
        ball_speed[0] = -ball_speed[0] # This line reverses the horizontal direction of the ball by negating its x-component of speed
        ball_speed[1] = random.choice([-5, 5])  # Randomize vertical direction

# Ball collision with goals
    if 0 < ball_pos[0] < GOAL_AREA_WIDTH and (HEIGHT - GOAL_WIDTH) // 2 < ball_pos[1] < (
        HEIGHT + GOAL_WIDTH) // 2:
        # This code specifies the position the ball has to be in for it to be able to be counted as a goal
# Team B scores
        score_team_b += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [5, 5]

    if WIDTH - GOAL_AREA_WIDTH < ball_pos[0] < WIDTH and (HEIGHT - GOAL_WIDTH) // 2 < ball_pos[1] < (
        HEIGHT + GOAL_WIDTH) // 2:
        # This code means that the ball has entered the goal area on the right side of the field. This triggers the scoring for Team B, increments their score and resets the ball's position to the center
# Team A scores
        score_team_a += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [-5, 5]
        # This code does the same as it does for team B as it does for team A

# Draw the soccer field
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (0, 0, WIDTH, HEIGHT))
    # Position of the grass drawn on the field
    
# Draw the semicrcle 
    pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 50, 2)
    # Position of the semicrcle that is drawn onto the field

# Draw the white line across the middle
    line_width = 2
    pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), line_width)
    # Position of the white line that is drawn vertically across teh field to make it seem more realistic 

# Draw the goals
    pygame.draw.rect(screen, WHITE, (0, (HEIGHT - GOAL_WIDTH) // 2, GOAL_AREA_WIDTH, GOAL_WIDTH))
    pygame.draw.rect(
        screen, WHITE, (WIDTH - GOAL_AREA_WIDTH, (HEIGHT - GOAL_WIDTH) // 2, GOAL_AREA_WIDTH, GOAL_WIDTH))
    # Draws the goals for the users to visualize where their target is

# Draw the players
    pygame.draw.rect(screen, BLACK, (player_a_pos[0], player_a_pos[1], PLAYER_SIZE, PLAYER_SIZE))
    pygame.draw.rect(screen, GOLD, (player_a_pos[0] + 2, player_a_pos[1] + 2, PLAYER_SIZE - 4, PLAYER_SIZE - 4))

    pygame.draw.rect(screen, RED, (player_b_pos[0], player_b_pos[1], PLAYER_SIZE, PLAYER_SIZE))
    pygame.draw.rect(screen, BLUE, (player_b_pos[0] + 2, player_b_pos[1] + 2, PLAYER_SIZE - 4, PLAYER_SIZE - 4))
    # This code draws out every player and the colors corespond with teh teams 
    # Barcelona being Red and Blue and Madrid being Gold and Black
    # It also covers up which parts of the players get colored over with gold being the middle for Madrid and blue being the middle for Barcelona

# Draw the ball
    pygame.draw.circle(screen, BLACK, (int(ball_pos[0]), int(ball_pos[1])), 10)

# Draw the scoreboard
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, 50))
    text_team_a = font.render("REAL MADRID: {}".format(score_team_a), True, WHITE)
    text_team_b = font.render("BARCELONA: {}".format(score_team_b), True, WHITE)
    screen.blit(text_team_a, (100, 25))
    screen.blit(text_team_b, (WIDTH - 200, 25))
    # This code draws a black rectangle at the top of the screen to serve as the background for the scoreboard 
    # It also renders text for both Team A and Team B (including their scores) 
    # And then places these text elements at specified positions on the screen

# Draw the fans
    for fan_pos in fan_positions_top + fan_positions_bottom: # Where to draw the fans
        pygame.draw.circle(screen, random.choice(FAN_COLORS), fan_pos, FAN_RADIUS) # Initiates the system to draw the fans

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    clock.tick(FPS)

# Quit Pygame adn close the system
pygame.quit()
sys.exit()
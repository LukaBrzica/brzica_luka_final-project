
# Importing pygame, the system, and random.
import pygame
import sys
import random

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
clock = pygame.time.Clock() 

# Player variables
player_speed = 8  # Increase player speed
player_a_pos = [WIDTH // 4, HEIGHT // 2]
player_b_pos = [3 * WIDTH // 4, HEIGHT // 2]

# Fans variables
fan_positions_top = [(x, 50) for x in range(30, WIDTH, 40)]  # Horizontal arrangement of fans on the top that line  up
fan_positions_bottom = [(x, HEIGHT - 50) for x in range(30, WIDTH, 40)]  # Horizontal arrangement of the fans that line up at the bottom of the field

# Ball variables
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [8, 8]  # Increase ball speed


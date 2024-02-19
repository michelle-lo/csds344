'''
Creating a top down visual represetaion of the traffic lights in a 4 way intersection using pygame.
Includes both traffic lights, pedestrian lights, as well as cars represented as arrows.
'''
import pygame

pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600

# Colors
white = (255, 255, 255)
red_on = (255, 0, 0)
red_off = (255, 153, 153)
green_on = (0, 255, 0)
green_off = (153, 255, 153)
yellow_on = (255, 255, 0)
yellow_off = (255, 255, 153)
black = (0, 0, 0) 
gray = (128, 128, 128)
road = (105,105,105)

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Intersection')

# Create the intersection
def draw_intersection():
    # Draw the intersection
    pygame.draw.rect(window, road, (WIDTH/2 - 100, 0, 200, HEIGHT))
    pygame.draw.rect(window, road, (0, HEIGHT/2 - 100, WIDTH, 200))
    pygame.draw.lines(window, white, False, [(WIDTH/2, 0), (WIDTH/2, HEIGHT/2 - 100)], 2)

# Run the intersection
def run_intersection():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        window.fill((128,128,128))
        draw_intersection()
        pygame.display.update()

run_intersection()
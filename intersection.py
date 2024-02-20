'''
Creating a top down visual represetaion of the traffic lights in a 4 way intersection using pygame.
Includes both traffic lights, pedestrian lights, as well as cars represented as arrows.
'''
import pygame

pygame.init()

# Constants
WIDTH = 1200
HEIGHT = 900

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
sidewalk = (100,100,100)
road = (80,80,80)

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Intersection')

# Create the intersection
def draw_intersection():
    # Draw the intersection
    pygame.draw.rect(window, road, (WIDTH/2 - 100, 0, 200, HEIGHT))
    pygame.draw.rect(window, road, (0, HEIGHT/2 - 100, WIDTH, 200))
    pygame.draw.lines(window, white, False, [(WIDTH/2, 0), (WIDTH/2, HEIGHT/2 - 100)], 2)
    pygame.draw.lines(window, white, False, [(WIDTH/2, HEIGHT), (WIDTH/2, HEIGHT/2 + 100)], 2)
    pygame.draw.lines(window, white, False, [(0, HEIGHT/2), (WIDTH/2 - 100, HEIGHT/2)], 2)
    pygame.draw.lines(window, white, False, [(WIDTH, HEIGHT/2), (WIDTH/2 + 100, HEIGHT/2)], 2)

    # Draw sidewalks
    pygame.draw.rect(window, sidewalk, (WIDTH/2 - 200, 0, 100, HEIGHT/2 - 100))
    pygame.draw.rect(window, sidewalk, (0, HEIGHT/2 - 200, WIDTH/2 - 100, 100))
    pygame.draw.rect(window, sidewalk, (WIDTH/2 + 100, HEIGHT/2 - 200, WIDTH/2 - 100, 100))
    pygame.draw.rect(window, sidewalk, (0, HEIGHT/2 + 100, WIDTH/2 - 100, 100))
    pygame.draw.rect(window, sidewalk, (WIDTH/2 + 100, 0, 100, HEIGHT/2 - 100))
    pygame.draw.rect(window, sidewalk, (WIDTH/2 - 200, HEIGHT/2 + 100, 100, HEIGHT/2 - 100))
    pygame.draw.rect(window, sidewalk, (WIDTH/2 + 100, HEIGHT/2 + 100, 100, HEIGHT/2 - 100))
    pygame.draw.rect(window, sidewalk, (WIDTH/2 + 100, HEIGHT/2 + 100, WIDTH/2 -100 , 100))



# Draw the traffic lights (one on each side of the intersection)
def draw_traffic_lights():
    # Draw the traffic lights
    # North
    pygame.draw.rect(window, black, (WIDTH/2 - 25, HEIGHT/2 - 160, 50, 120))
    pygame.draw.circle(window, gray, (WIDTH/2, HEIGHT/2 - 140), 15)
    pygame.draw.circle(window, gray, (WIDTH/2, HEIGHT/2 - 100), 15)
    pygame.draw.circle(window, gray, (WIDTH/2, HEIGHT/2 - 60), 15)

    # South
    pygame.draw.rect(window, black, (WIDTH/2 - 25, HEIGHT/2 + 40, 50, 120))
    pygame.draw.circle(window, gray, (WIDTH/2, HEIGHT/2 + 60), 15)
    pygame.draw.circle(window, gray, (WIDTH/2, HEIGHT/2 + 100), 15)
    pygame.draw.circle(window, gray, (WIDTH/2, HEIGHT/2 + 140), 15)

    # West
    pygame.draw.rect(window, black, (WIDTH/2 - 160, HEIGHT/2 - 25, 120, 50))
    pygame.draw.circle(window, gray, (WIDTH/2 - 140, HEIGHT/2), 15)
    pygame.draw.circle(window, gray, (WIDTH/2 - 100, HEIGHT/2), 15)
    pygame.draw.circle(window, gray, (WIDTH/2 - 60, HEIGHT/2), 15)
    
    
    # East
    pygame.draw.rect(window, black, (WIDTH/2 + 40, HEIGHT/2 - 25, 120, 50))
    pygame.draw.circle(window, gray, (WIDTH/2 + 60, HEIGHT/2), 15)
    pygame.draw.circle(window, gray, (WIDTH/2 + 100, HEIGHT/2), 15)
    pygame.draw.circle(window, gray, (WIDTH/2 + 140, HEIGHT/2), 15)




# Run the intersection simulation
def run_intersection():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False    
        window.fill((128,128,128))
        draw_intersection()
        draw_traffic_lights()

        pygame.display.update()

run_intersection()
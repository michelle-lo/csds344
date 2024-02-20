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
red_off = (233, 184, 184)
green_on = (0, 255, 0)
green_off = (184, 233, 184)
yellow_on = (255, 255, 0)
yellow_off = (233, 233, 153)
black = (0, 0, 0) 
gray = (128, 128, 128)
sidewalk = (100,100,100)
road = (80,80,80)

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Intersection')

# Create the lights
class Light:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.radius = 15
        self.draw()
    def set_color(self, color):
        self.color = color
        self.draw()
    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

# Create the intersection
def draw_intersection():
    window.fill((128,128,128))
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
    # North
    pygame.draw.rect(window, black, (WIDTH/2 - 25, HEIGHT/2 - 160, 50, 120))

    # South
    pygame.draw.rect(window, black, (WIDTH/2 - 25, HEIGHT/2 + 40, 50, 120))

    # West
    pygame.draw.rect(window, black, (WIDTH/2 - 160, HEIGHT/2 - 25, 120, 50))

    # East
    pygame.draw.rect(window, black, (WIDTH/2 + 40, HEIGHT/2 - 25, 120, 50))
    



# Run the intersection simulation
def run_intersection():
    draw_intersection()
    draw_traffic_lights()

    # North
    north_red = Light(gray, WIDTH/2, HEIGHT/2 - 60)
    north_yellow = Light(gray, WIDTH/2, HEIGHT/2 - 100)
    north_green = Light(gray, WIDTH/2, HEIGHT/2 - 140)

    # South
    south_red = Light(gray, WIDTH/2, HEIGHT/2 + 60)
    south_yellow = Light(gray, WIDTH/2, HEIGHT/2 + 100)
    south_green = Light(gray, WIDTH/2, HEIGHT/2 + 140)

    # West
    west_red = Light(gray, WIDTH/2 - 60, HEIGHT/2)
    west_yellow = Light(gray, WIDTH/2 - 100, HEIGHT/2)
    west_green = Light(gray, WIDTH/2 - 140, HEIGHT/2)

    # East
    east_red = Light(gray, WIDTH/2 + 60, HEIGHT/2)
    east_yellow = Light(gray, WIDTH/2 + 100, HEIGHT/2)
    east_green = Light(gray, WIDTH/2 + 140, HEIGHT/2)

    pygame.display.update()

    current = 0
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

        if (current == 0): #North and South Green
            north_green.set_color(green_on)
            south_green.set_color(green_on)

            north_red.set_color(gray)
            south_red.set_color(gray)

            west_red.set_color(red_on)
            east_red.set_color(red_on)

            west_yellow.set_color(gray)
            east_yellow.set_color(gray)
            
            current = 1
            delay = 900
        elif (current == 1): #North and South Yellow
            north_yellow.set_color(yellow_on)
            south_yellow.set_color(yellow_on)

            north_green.set_color(gray)
            south_green.set_color(gray)

            current = 2
            delay = 300
        elif (current == 2): #East and West Green
            west_green.set_color(green_on)
            east_green.set_color(green_on)

            west_red.set_color(gray)
            east_red.set_color(gray)

            north_red.set_color(red_on)
            south_red.set_color(red_on)

            north_yellow.set_color(gray)
            south_yellow.set_color(gray)

            current = 3
            delay = 900
        elif (current == 3): #East and West Yellow
            west_yellow.set_color(yellow_on)
            east_yellow.set_color(yellow_on)

            west_green.set_color(gray)
            east_green.set_color(gray)

            current = 0
            delay = 300
        else:
            current = 0
            delay = 300
        pygame.display.update()            #and show it all
        pygame.time.wait(delay)
        clock.tick(3)


run_intersection()
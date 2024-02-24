'''
Creating a top down visual represetaion of the traffic lights in a 4 way intersection using pygame.
Includes both traffic lights, pedestrian lights, as well as cars represented as arrows.
'''
import pygame
import time

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

# Timings
go_time = 6000 #3000
yellow_time = 2000 #1000
pedestrian_time = 2000 #1000
turn_time = 3000

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
        

def draw_dotted_line(start, end, width = 2, dash_length = 10):
    x1, y1 = start
    x2, y2 = end
    

    if(x1 == x2):
        sliced = abs(y1 - y2)%dash_length
        ycoord = [y for y in range(int(y1),int(y2), int(dash_length)  if y1 < y2 else int(-dash_length))]
        xcoord = [x1]*len(ycoord)
    elif(y1 == y2):
        xcoord = [x for x in range(int(x1),int(x2), int(dash_length) if x1 < x2 else int(-dash_length))]
        ycoord = [y1]*len(xcoord)

    next_coord = list(zip(xcoord[1::2],ycoord[1::2]))
    last_coord = list(zip(xcoord[1::2],ycoord[1::2]))
    for (x1, y1), (x2, y2) in zip(next_coord, last_coord):
        pygame.draw.line(window, white, (round(x1), round(y1)), (round(x2), round(y2)), width)

# Create the intersection
def draw_intersection():
    window.fill((128,128,128))
    # Draw the intersection
    pygame.draw.rect(window, road, (WIDTH/2 - 100, 0, 200, HEIGHT))
    pygame.draw.rect(window, road, (0, HEIGHT/2 - 100, WIDTH, 200))

    pygame.draw.lines(window, white, False, [(WIDTH/2 + 30, 0), (WIDTH/2 + 30, HEIGHT/2 - 100)], 2) # Top
    pygame.draw.lines(window, white, False, [(WIDTH/2 - 30, HEIGHT), (WIDTH/2 - 30, HEIGHT/2 + 100)], 2) # Bottom
    pygame.draw.lines(window, white, False, [(0, HEIGHT/2 - 30), (WIDTH/2 - 100, HEIGHT/2 - 30)], 2) # Left
    pygame.draw.lines(window, white, False, [(WIDTH, HEIGHT/2 + 30), (WIDTH/2 + 100, HEIGHT/2 + 30)], 2) # Right

    draw_dotted_line((WIDTH/2 - 30, 0), (WIDTH/2 - 30, HEIGHT/2 - 100)) #Top
    draw_dotted_line((WIDTH/2 + 30, HEIGHT), (WIDTH/2 + 30, HEIGHT/2 + 100)) #Bottom
    draw_dotted_line((0, HEIGHT/2 + 30), (WIDTH/2 - 100, HEIGHT/2 + 30)) #Left
    draw_dotted_line((WIDTH, HEIGHT/2 - 30), (WIDTH/2 + 100, HEIGHT/2 - 30)) # Right

    x_shift =  WIDTH/2 - 250 
    y_shift = HEIGHT/2 - 15
    xs2 =  WIDTH/2 + 15
    ys2 = HEIGHT/2 - 250
    xs3 =  WIDTH/2 + 250
    ys3 = HEIGHT/2 +15
    xs4 =  WIDTH/2 - 15
    ys4 = HEIGHT/2 + 250

    #Arrows
    pygame.draw.polygon(window, white, ((0+x_shift, 20+y_shift), (0+x_shift, 30+y_shift), (30+x_shift, 30+y_shift), (30+x_shift, 10+y_shift), (40+x_shift, 10+y_shift), (25+x_shift, 0+y_shift), (10+x_shift, 10+y_shift), (20+x_shift, 10+y_shift), (20+x_shift, 20+y_shift)))
    pygame.draw.polygon(window, white, ((-20+xs2, 0+ys2), (-30+xs2, 0+ys2), (-30+xs2, 30+ys2), (-10+xs2, 30+ys2), (-10+xs2, 40+ys2), (0+xs2, 25+ys2), (-10+xs2, 10+ys2), (-10+xs2, 20+ys2), (-20+xs2, 20+ys2)))
    pygame.draw.polygon(window, white, ((0+xs3, -20+ys3), (0+xs3, -30+ys3), (-30+xs3, -30+ys3), (-30+xs3, -10+ys3), (-40+xs3, -10+ys3), (-25+xs3, 0+ys3), (-10+xs3, -10+ys3), (-20+xs3, -10+ys3), (-20+xs3, -20+ys3)))
    pygame.draw.polygon(window, white, ((20+xs4, 0+ys4), (30+xs4, 0+ys4), (30+xs4, -30+ys4), (10+xs4, -30+ys4), (10+xs4, -40+ys4), (0+xs4, -25+ys4), (10+xs4, -10+ys4), (10+xs4, -20+ys4), (20+xs4, -20+ys4)))

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
    pygame.draw.rect(window, black, (WIDTH/2  - 90, HEIGHT/2 - 160, 50, 120))
    # pygame.draw.rect(window, black, (WIDTH/2 + 200, HEIGHT/2 + 200, 50, 120))
    xs1 = WIDTH/2 - 15
    ys1 = HEIGHT/2 - 75
    pygame.draw.polygon(window, gray, ((0+xs1,10+ys1),(0+xs1,20+ys1),(20+xs1,20+ys1),(20+xs1,25+ys1),(30+xs1,15+ys1),(20+xs1,5+ys1),(20+xs1,10+ys1)))

    # South
    pygame.draw.rect(window, black, (WIDTH/2 - 25, HEIGHT/2 + 40, 50, 120))
    pygame.draw.rect(window, black, (WIDTH/2 + 40, HEIGHT/2 + 40, 50, 120))
    # pygame.draw.rect(window, black, (WIDTH/2 - 250, HEIGHT/2 - 320, 50, 120))

    # West
    pygame.draw.rect(window, black, (WIDTH/2 - 160, HEIGHT/2 - 25, 120, 50))
    pygame.draw.rect(window, black, (WIDTH/2 - 160, HEIGHT/2 + 40, 120, 50))
    # pygame.draw.rect(window, black, (WIDTH/2 + 200, HEIGHT/2 - 250, 120, 50))


    # East
    pygame.draw.rect(window, black, (WIDTH/2 + 40, HEIGHT/2 - 25, 120, 50))
    pygame.draw.rect(window, black, (WIDTH/2 + 40, HEIGHT/2 - 90, 120, 50))
    # pygame.draw.rect(window, black, (WIDTH/2 - 320, HEIGHT/2 + 200, 120, 50))
    

# Run the intersection simulation
def run_intersection():
    draw_intersection()
    draw_traffic_lights()

    # North
    north_red = Light(gray, WIDTH/2, HEIGHT/2 - 60)
    north_yellow = Light(gray, WIDTH/2, HEIGHT/2 - 100)
    north_green = Light(gray, WIDTH/2, HEIGHT/2 - 140)

    #North Arrow
    north_back_red = Light(gray, WIDTH/2  - 65, HEIGHT/2 - 60)
    north_back_yellow = Light(gray, WIDTH/2  - 65, HEIGHT/2 - 100)
    north_back_green = Light(gray, WIDTH/2  - 65, HEIGHT/2 - 140)

    #North Backup
    # north_back_red = Light(gray, WIDTH/2 + 225, HEIGHT/2 + 220)
    # north_back_yellow = Light(gray, WIDTH/2 + 225, HEIGHT/2 + 260)
    # north_back_green = Light(gray, WIDTH/2 + 225, HEIGHT/2 + 300)


    # South
    south_red = Light(gray, WIDTH/2, HEIGHT/2 + 60)
    south_yellow = Light(gray, WIDTH/2, HEIGHT/2 + 100)
    south_green = Light(gray, WIDTH/2, HEIGHT/2 + 140)

    # South Arrow
    south_back_red = Light(gray, WIDTH/2 + 65, HEIGHT/2 + 60)
    south_back_yellow = Light(gray, WIDTH/2 + 65, HEIGHT/2 + 100)
    south_back_green = Light(gray, WIDTH/2 + 65, HEIGHT/2 + 140)

    # South Backup
    # south_back_red = Light(gray, WIDTH/2 - 225, HEIGHT/2 - 220)
    # south_back_yellow = Light(gray, WIDTH/2 - 225, HEIGHT/2 - 260)
    # south_back_green = Light(gray, WIDTH/2 - 225, HEIGHT/2 - 300)


    # West
    west_red = Light(gray, WIDTH/2 - 60, HEIGHT/2)
    west_yellow = Light(gray, WIDTH/2 - 100, HEIGHT/2)
    west_green = Light(gray, WIDTH/2 - 140, HEIGHT/2)

    # West Arrow
    west_back_red = Light(gray, WIDTH/2 - 60, HEIGHT/2 + 65)
    west_back_yellow = Light(gray, WIDTH/2 - 100, HEIGHT/2 + 65)
    west_back_green = Light(gray, WIDTH/2 - 140, HEIGHT/2 + 65)

    # # West Backup
    # west_back_red = Light(gray, WIDTH/2 + 220, HEIGHT/2 - 225)
    # west_back_yellow = Light(gray, WIDTH/2 + 260, HEIGHT/2 - 225)
    # west_back_green = Light(gray, WIDTH/2 + 300, HEIGHT/2 - 225)


    # East
    east_red = Light(gray, WIDTH/2 + 60, HEIGHT/2)
    east_yellow = Light(gray, WIDTH/2 + 100, HEIGHT/2)
    east_green = Light(gray, WIDTH/2 + 140, HEIGHT/2)

    # East Arrow
    east_back_red = Light(gray, WIDTH/2 + 60, HEIGHT/2 - 65)
    east_back_yellow = Light(gray, WIDTH/2 + 100, HEIGHT/2 - 65)
    east_back_green = Light(gray, WIDTH/2 + 140, HEIGHT/2 - 65)

    # East Backup
    # east_back_red = Light(gray, WIDTH/2 - 220, HEIGHT/2 + 225)
    # east_back_yellow = Light(gray, WIDTH/2 - 260, HEIGHT/2 + 225)
    # east_back_green = Light(gray, WIDTH/2 - 300, HEIGHT/2 + 225)

    # Pedestrian Lights
    southwest_vertical = pygame.Rect(WIDTH/2 - 225, HEIGHT/2 + 100, 80, 20)
    northwest_vertical = pygame.Rect(WIDTH/2 - 225, HEIGHT/2 - 120, 80, 20)
    southeast_vertical = pygame.Rect(WIDTH/2 + 140, HEIGHT/2 + 100, 80, 20)
    northeast_vertical = pygame.Rect(WIDTH/2 + 140, HEIGHT/2 - 120, 80, 20)

    northeast_horizontal = pygame.Rect(WIDTH/2 - 120, HEIGHT/2 - 200, 20, 80)
    northwest_horizontal = pygame.Rect(WIDTH/2 + 100, HEIGHT/2 - 200, 20, 80)
    southwest_horizontal = pygame.Rect(WIDTH/2 - 120, HEIGHT/2 + 120, 20, 80)
    southeast_horizontal = pygame.Rect(WIDTH/2 + 100, HEIGHT/2 + 120, 20, 80)

    current = 0
    clock = pygame.time.Clock()
    flash_red = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if (current == 0): # All Red
            north_red.set_color(red_on)
            south_red.set_color(red_on)
            xs1 = WIDTH/2 - 15
            ys1 = HEIGHT/2 - 75
            pygame.draw.polygon(window, black, ((0+xs1,10+ys1),(0+xs1,20+ys1),(20+xs1,20+ys1),(20+xs1,25+ys1),(30+xs1,15+ys1),(20+xs1,5+ys1),(20+xs1,10+ys1)))
            xs1 = WIDTH/2 + 14
            ys1 = HEIGHT/2 + 45
            pygame.draw.polygon(window, black, ((0+xs1,10+ys1),(0+xs1,20+ys1),(-20+xs1,20+ys1),(-20+xs1,25+ys1),(-30+xs1,15+ys1),(-20+xs1,5+ys1),(-20+xs1,10+ys1)))

            north_back_red.set_color(red_on)
            south_back_red.set_color(red_on)

            west_red.set_color(red_on)
            east_red.set_color(red_on)
            xs1 = WIDTH/2 - 75
            ys1 = HEIGHT/2 - 15
            pygame.draw.polygon(window, black, ((10+xs1,0+ys1),(20+xs1,0+ys1),(20+xs1,20+ys1),(25+xs1,20+ys1),(15+xs1,30+ys1),(5+xs1,20+ys1),(10+xs1,20+ys1)))
            xs1 = WIDTH/2 + 75
            ys1 = HEIGHT/2 - 15
            pygame.draw.polygon(window, black, ((-10+xs1,0+ys1),(-20+xs1,0+ys1),(-20+xs1,20+ys1),(-25+xs1,20+ys1),(-15+xs1,30+ys1),(-5+xs1,20+ys1),(-10+xs1,20+ys1)))

            west_back_red.set_color(red_on)
            east_back_red.set_color(red_on)

            west_yellow.set_color(gray)
            east_yellow.set_color(gray)

            west_back_yellow.set_color(gray)
            east_back_yellow.set_color(gray)
            
            # Pedestrian Lights
            pygame.draw.rect(window, red_on, southwest_vertical)
            pygame.draw.rect(window, red_on, northwest_vertical)
            pygame.draw.rect(window, red_on, southeast_vertical)
            pygame.draw.rect(window, red_on, northeast_vertical)

            pygame.draw.rect(window, red_on, northeast_horizontal)
            pygame.draw.rect(window, red_on, northwest_horizontal)
            pygame.draw.rect(window, red_on, southwest_horizontal)
            pygame.draw.rect(window, red_on, southeast_horizontal)
            current = 1
            delay = pedestrian_time

        elif (current == 1): # vertical LT green
            north_red.set_color(gray)
            south_red.set_color(gray)
            north_green.set_color(green_on)
            south_green.set_color(green_on)
            xs3 = WIDTH/2 - 15
            ys3 = HEIGHT/2 - 75 - 40 - 40
            pygame.draw.polygon(window, black, ((0+xs3,10+ys3),(0+xs3,20+ys3),(20+xs3,20+ys3),(20+xs3,25+ys3),(30+xs3,15+ys3),(20+xs3,5+ys3),(20+xs3,10+ys3)))
            xs1 = WIDTH/2 + 14
            ys1 = HEIGHT/2 + 45 + 40 + 40
            pygame.draw.polygon(window, black, ((0+xs1,10+ys1),(0+xs1,20+ys1),(-20+xs1,20+ys1),(-20+xs1,25+ys1),(-30+xs1,15+ys1),(-20+xs1,5+ys1),(-20+xs1,10+ys1)))
            

            current = 2
            delay = turn_time
            
        elif (current == 2): # vertical LT yellow
            north_green.set_color(gray)
            south_green.set_color(gray)
            north_yellow.set_color(yellow_on)
            south_yellow.set_color(yellow_on)
            xs2 = WIDTH/2 - 15
            ys2 = HEIGHT/2 - 75 - 40
            pygame.draw.polygon(window, black, ((0+xs2,10+ys2),(0+xs2,20+ys2),(20+xs2,20+ys2),(20+xs2,25+ys2),(30+xs2,15+ys2),(20+xs2,5+ys2),(20+xs2,10+ys2)))
            xs1 = WIDTH/2 + 14
            ys1 = HEIGHT/2 + 45 + 40 
            pygame.draw.polygon(window, black, ((0+xs1,10+ys1),(0+xs1,20+ys1),(-20+xs1,20+ys1),(-20+xs1,25+ys1),(-30+xs1,15+ys1),(-20+xs1,5+ys1),(-20+xs1,10+ys1)))
            
            current = 3
            delay = yellow_time

        elif (current == 3): # vertical LT red
            north_yellow.set_color(gray)
            south_yellow.set_color(gray)
            north_red.set_color(red_on)
            south_red.set_color(red_on)
            xs1 = WIDTH/2 - 15
            ys1 = HEIGHT/2 - 75
            pygame.draw.polygon(window, black, ((0+xs1,10+ys1),(0+xs1,20+ys1),(20+xs1,20+ys1),(20+xs1,25+ys1),(30+xs1,15+ys1),(20+xs1,5+ys1),(20+xs1,10+ys1)))
            xs1 = WIDTH/2 + 14
            ys1 = HEIGHT/2 + 45
            pygame.draw.polygon(window, black, ((0+xs1,10+ys1),(0+xs1,20+ys1),(-20+xs1,20+ys1),(-20+xs1,25+ys1),(-30+xs1,15+ys1),(-20+xs1,5+ys1),(-20+xs1,10+ys1)))
            
            current = 4
            delay = pedestrian_time

        elif (current == 4): #North and South Green
            north_back_green.set_color(green_on)
            south_back_green.set_color(green_on)

            north_back_red.set_color(gray)
            south_back_red.set_color(gray)

            # Pedestrian Lights
            pygame.draw.rect(window, green_on, southwest_vertical)
            pygame.draw.rect(window, green_on, northwest_vertical)
            pygame.draw.rect(window, green_on, southeast_vertical)
            pygame.draw.rect(window, green_on, northeast_vertical)

            pygame.draw.rect(window, red_on, northeast_horizontal)
            pygame.draw.rect(window, red_on, northwest_horizontal)
            pygame.draw.rect(window, red_on, southwest_horizontal)
            pygame.draw.rect(window, red_on, southeast_horizontal)

            current = 5
            delay = go_time

        elif (current == 5): #North and South Yellow
            north_back_yellow.set_color(yellow_on)
            south_back_yellow.set_color(yellow_on)

            north_back_green.set_color(gray)
            south_back_green.set_color(gray)

            # consider adding timer?
            delay = yellow_time
            recorded_time =  pygame.time.get_ticks()
            end_time = recorded_time + delay
        
            while (recorded_time <= end_time):
                flash_red = not flash_red

                if flash_red:
                    pygame.draw.rect(window, red_on, southwest_vertical)
                    pygame.draw.rect(window, red_on, northwest_vertical)
                    pygame.draw.rect(window, red_on, southeast_vertical)
                    pygame.draw.rect(window, red_on, northeast_vertical)
                else:
                    pygame.draw.rect(window, black, southwest_vertical)
                    pygame.draw.rect(window, black, northwest_vertical)
                    pygame.draw.rect(window, black, southeast_vertical)
                    pygame.draw.rect(window, black, northeast_vertical)

                pygame.display.update()
                recorded_time =  pygame.time.get_ticks()
                pygame.time.wait(300)
                
            delay = 0

            current = 6

        elif (current == 6): #All Red
            north_back_red.set_color(red_on)
            south_back_red.set_color(red_on)

            west_back_red.set_color(red_on)
            east_back_red.set_color(red_on)

            north_back_yellow.set_color(gray)
            south_back_yellow.set_color(gray)

            # Pedestrian Lights
            pygame.draw.rect(window, red_on, southwest_vertical)
            pygame.draw.rect(window, red_on, northwest_vertical)
            pygame.draw.rect(window, red_on, southeast_vertical)
            pygame.draw.rect(window, red_on, northeast_vertical)

            pygame.draw.rect(window, red_on, northeast_horizontal)
            pygame.draw.rect(window, red_on, northwest_horizontal)
            pygame.draw.rect(window, red_on, southwest_horizontal)
            pygame.draw.rect(window, red_on, southeast_horizontal)

            current = 7
            delay = pedestrian_time

        elif (current == 7): # horizontal LT green
            east_green.set_color(green_on)
            west_green.set_color(green_on)
            east_red.set_color(gray)
            west_red.set_color(gray)
            xs1 = WIDTH/2 - 75 - 40 - 40
            ys1 = HEIGHT/2 - 15
            pygame.draw.polygon(window, black, ((10+xs1,0+ys1),(20+xs1,0+ys1),(20+xs1,20+ys1),(25+xs1,20+ys1),(15+xs1,30+ys1),(5+xs1,20+ys1),(10+xs1,20+ys1)))
            xs1 = WIDTH/2 + 75 + 40 + 40
            ys1 = HEIGHT/2 - 15
            pygame.draw.polygon(window, black, ((-10+xs1,0+ys1),(-20+xs1,0+ys1),(-20+xs1,20+ys1),(-25+xs1,20+ys1),(-15+xs1,30+ys1),(-5+xs1,20+ys1),(-10+xs1,20+ys1)))

            current = 8
            delay = turn_time
            
        elif (current == 8): # horizontal LT yellow
            east_green.set_color(gray)
            west_green.set_color(gray)
            east_yellow.set_color(yellow_on)
            west_yellow.set_color(yellow_on)
            xs1 = WIDTH/2 - 75 - 40
            ys1 = HEIGHT/2 - 15
            pygame.draw.polygon(window, black, ((10+xs1,0+ys1),(20+xs1,0+ys1),(20+xs1,20+ys1),(25+xs1,20+ys1),(15+xs1,30+ys1),(5+xs1,20+ys1),(10+xs1,20+ys1)))
            xs1 = WIDTH/2 + 75 + 40
            ys1 = HEIGHT/2 - 15
            pygame.draw.polygon(window, black, ((-10+xs1,0+ys1),(-20+xs1,0+ys1),(-20+xs1,20+ys1),(-25+xs1,20+ys1),(-15+xs1,30+ys1),(-5+xs1,20+ys1),(-10+xs1,20+ys1)))

            current = 9
            delay = yellow_time

        elif (current == 9): # horizontal LT red
            east_yellow.set_color(gray)
            west_yellow.set_color(gray)
            east_red.set_color(red_on)
            west_red.set_color(red_on)
            xs1 = WIDTH/2 - 75
            ys1 = HEIGHT/2 - 15
            pygame.draw.polygon(window, black, ((10+xs1,0+ys1),(20+xs1,0+ys1),(20+xs1,20+ys1),(25+xs1,20+ys1),(15+xs1,30+ys1),(5+xs1,20+ys1),(10+xs1,20+ys1)))
            xs1 = WIDTH/2 + 75
            ys1 = HEIGHT/2 - 15
            pygame.draw.polygon(window, black, ((-10+xs1,0+ys1),(-20+xs1,0+ys1),(-20+xs1,20+ys1),(-25+xs1,20+ys1),(-15+xs1,30+ys1),(-5+xs1,20+ys1),(-10+xs1,20+ys1)))

            current = 10
            delay = pedestrian_time


        elif (current == 10): #East and West Green
            west_back_green.set_color(green_on)
            east_back_green.set_color(green_on)

            west_back_red.set_color(gray)
            east_back_red.set_color(gray)

            north_back_red.set_color(red_on)
            south_back_red.set_color(red_on)

            north_back_yellow.set_color(gray)
            south_back_yellow.set_color(gray)

            # Pedestrian Lights
            pygame.draw.rect(window, red_on, southwest_vertical)
            pygame.draw.rect(window, red_on, northwest_vertical)
            pygame.draw.rect(window, red_on, southeast_vertical)
            pygame.draw.rect(window, red_on, northeast_vertical)

            pygame.draw.rect(window, green_on, northeast_horizontal)
            pygame.draw.rect(window, green_on, northwest_horizontal)
            pygame.draw.rect(window, green_on, southwest_horizontal)
            pygame.draw.rect(window, green_on, southeast_horizontal)

            current = 11
            delay = go_time
        elif (current == 11): #East and West Yellow
            west_back_yellow.set_color(yellow_on)
            east_back_yellow.set_color(yellow_on)
            
            west_back_green.set_color(gray)
            east_back_green.set_color(gray)

            delay = yellow_time
            recorded_time =  pygame.time.get_ticks()
            end_time = recorded_time + delay
        
            while (recorded_time <= end_time):
                flash_red = not flash_red

                if flash_red:
                    pygame.draw.rect(window, red_on, northeast_horizontal)
                    pygame.draw.rect(window, red_on, northwest_horizontal)
                    pygame.draw.rect(window, red_on, southwest_horizontal)
                    pygame.draw.rect(window, red_on, southeast_horizontal)
                else:
                    pygame.draw.rect(window, black, northeast_horizontal)
                    pygame.draw.rect(window, black, northwest_horizontal)
                    pygame.draw.rect(window, black, southwest_horizontal)
                    pygame.draw.rect(window, black, southeast_horizontal)

                pygame.display.update()
                recorded_time =  pygame.time.get_ticks()
                pygame.time.wait(300)
                
            delay = 0
            current = 0
        else:
            current = 0
            delay = 300


        pygame.display.update()            #and show it all
        pygame.time.wait(delay)
        clock.tick(3)


run_intersection()
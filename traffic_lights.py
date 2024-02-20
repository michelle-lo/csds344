'''
Iterate through a traffic light cycle
'''


import sys, pygame
pygame.init()

size = width, height = 250, 250
speed = [2, 2]
black = 0, 0, 0
current = 0

TRAFFIC_SIZE = (20, 50)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

redLight = pygame.image.load("redLight.png").convert()
yellowLight = pygame.image.load("yellowLight.png").convert()
greenLight = pygame.image.load("greenLight.png").convert()

redLight = pygame.transform.scale(redLight, TRAFFIC_SIZE)
yellowLight = pygame.transform.scale(yellowLight, TRAFFIC_SIZE)
greenLight = pygame.transform.scale(greenLight, TRAFFIC_SIZE)

screen.blit(redLight, (115,100))        #draw the background
pygame.display.update()                #and show it all
while True:                   #animate 100 frames
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if (current == 0):
        screen.blit(greenLight, (115, 100))
        current = 1
        delay = 5000
    elif (current == 1):
        screen.blit(yellowLight, (115, 100))
        current = 2
        delay = 1000
    else:
        screen.blit(redLight, (115, 100))
        current = 0
        delay = 5000

    pygame.display.update()            #and show it all
    pygame.time.wait(delay)
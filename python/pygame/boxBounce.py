#!/usr/bin/python2

import pygame
import sys

# Pygame setup
pygame.init()

# Window size
size = width, height = 320, 240

# Animated box speed and direction
speed = [2, 2]

# Create window of specified size, and create an SDL display
screen = pygame.display.set_mode(size)

# Surface for bouncing box
s = pygame.Surface((100, 50))
s.fill((33,66,99)) # Fill blue
r = s.get_rect() # Get rect bounds

# Create clock
clock = pygame.time.Clock()

while 1:
        clock.tick(30) #limit framerate to 30 FPS
        for event in pygame.event.get(): # Event caught
                if event.type == pygame.QUIT: #if EXIT clicked
                        sys.exit() #close cleanly
        r=r.move(speed) #move the box by the "speed" coordinates
        #if we hit a  wall, change direction
        if r.left < 0 or r.right > width: speed[0] = -speed[0]
        if r.top < 0 or r.bottom > height: speed[1] = -speed[1]
        screen.fill((0,0,0)) #make redraw background black
        screen.blit(s,r) #render the surface into the rectangle
        pygame.display.flip() #update the screen

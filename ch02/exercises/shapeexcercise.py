#problems: "white" is not defined and "display" is not defined 
import pygame
import turtle
pygame.init()

screen = pygame.display.set_mode()
screen_size = screen.get_size()

while 1:
    pygame.event.get()
    dimensions = [screen_size[0] / 2, screen_size[1] / 2]
    screen.fill("white")
    pygame.time.wait(1000) #do I need wait function for this 
    pygame.draw.circle(screen,"blue", dimensions, 50)
    pygame.draw.circle(screen,"blue", [100,100], 75)
    pygame.draw.circle(screen,"blue", [150,150], 100)
    pygame.display.flip()
    pygame.time.wait(1000)
    break
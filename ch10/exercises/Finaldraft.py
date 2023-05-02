
import pygame 
import turtle
pygame.init
w = 10000
h = 1000
screen = pygame.display.set_mode((w,h))
screencords = pygame.display.get_window_size()
pygame.event.get() 
screen.fill("chartreuse4")
pygame.display.flip() 

class river:
    pygame.draw.rect(screen,"cadetblue2",(0,500,w,400))
    pygame.display.flip()
    pygame.time.wait(2000)

class frog:
    player = pygame.draw.circle()
    

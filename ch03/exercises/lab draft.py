import pygame 
import random 
import math

#Part A 
pygame.init
w = 600
h = 600
screen = pygame.display.set_mode((w,h))
screencords = pygame.display.get_window_size()
print(screencords[0])
print(screencords[1])
pygame.event.get() 
screen.fill("white")
pygame.display.flip() 
pygame.time.wait(250)
pygame.draw.circle(screen,"pink", [w / 2,h /2], h/2)
pygame.display.flip()
pygame.draw.line(screen,"black",(0, h /2),(w, h / 2))
pygame.draw.line(screen,"black",(w /2, 0),(w / 2, h))
pygame.display.flip() 
pygame.time.wait(1000)

#part B

for Z in range(10):
    x = random.randrange(0,w)
    y = random.randrange(0,h)
    distance_from_center = math.hypot(w/2- x, h/2 - y) #the distance formula
    is_in_circle = (distance_from_center <= h/2) #screen height
    if is_in_circle:
        pygame.draw.circle(screen,"black", (x,y), 5)
    else:
        pygame.draw.circle(screen,"red",(x,y), 5)
    pygame.display.flip()
pygame.time.wait(5000)


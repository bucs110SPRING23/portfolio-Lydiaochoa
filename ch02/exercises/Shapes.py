import pygame
pygame.init() 

screen = pygame.display.set_mode()
while 1: 
   pygame.event.get()
   screen.fill("green")
   pygame.display.flip()
   pygame.time.wait(1000)

   screen_size = screen.get_size()

   dimensions = [screen_size[0] / 2, screen_size[1] / 2, 250, 250]
   pygame.draw.rect(screen, "red", dimensions)

   # [x,y, width, height]
   dimensions = [300, 300, 250, 250]
   pygame.draw.rect(screen, "blue", dimensions)

   pygame.display.flip()
   pygame.time.wait(1000)
   break


#part B
#pygame.event.get?
pygame.init()
window = pygame.display.set_mode

color = ("blue")
pointslist = [] #can i just put points in like this 
num_sides = (int(input("enter number of sides:")))
side_length = (input("enter legnth of sides"))
xpos = 
ypos = 
for in (num_sides)
    angle= 360/number_of_sides
    radians = math.radians(angle * i)
    x =xpos + side_length * math.cos(radians)
    y = ypos + sde_length * math.sin(radians)
    break  
pygame.draw.polygon(pointslist,color)
color = ("blue")
pygame.display.flip 
pygame.time.wait(1000)
window.fill("white")
pygame.display.flip 
window.exitonclick
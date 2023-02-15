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

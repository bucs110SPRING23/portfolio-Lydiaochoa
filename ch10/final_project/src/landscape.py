import pygame
def land():
    pygame.init
    w = 10000
    h = 1000
    screen = pygame.display.set_mode((w,h))
    screencords = pygame.display.get_window_size()
    pygame.event.get() 
    screen.fill("chartreuse4")
    pygame.display.flip() 

    river_width = w
    river_height= (h / 5 ) * 2

    pygame.draw.rect(screen,"cadetblue2",(0,400,river_width,river_height))
    pygame.display.flip()
    pygame.draw.circle(screen,"chartreuse3",[300,600],60)
    pygame.draw.circle(screen,"chartreuse3",[500,500],60)
    pygame.draw.circle(screen,"chartreuse3",[800,600],60)
    pygame.draw.circle(screen,"chartreuse3",[1100,480],60)
    pygame.draw.circle(screen,"chartreuse3",[500,700],60)
    pygame.draw.circle(screen,"chartreuse3",[1100,700],60)
    pygame.display.flip()
    pygame.time.wait(2000)
land()

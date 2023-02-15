import pygame
pygame.init()

screen = pygame.display.set_mode()
window = screen
screen_size = screen.get_size()


dimensions = [screen_size[0] / 2, screen_size[1] / 2, 250, 250]
screen.fill(white)
pygame.time.wait(1000)
pygame.draw.circle(display,"blue", [200,150], 50)
screen.display.flip()
window.exitonclick()

import pygame 
pygame.init()
screen = pygame.display.set_mode()
#Part A
count = 0 
def threenp1(n):
    while n > 1.0:
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
    return None

while 1:
    count = count + 1
    print(count)
    break
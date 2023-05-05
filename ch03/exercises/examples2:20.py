##events 
# operating system handles events 
## your program to OS: ANything happening? 
# OS says --> event 
# type of event = operaration 
# connect actions to algorithms -->ex) if this happens, do ths (ex "if" statements)
#thngs
# - click
# - key presses

#Simon says
import pygame
import random
pygame.event.get() 
pygame.init()

screen = pygame.display.set_mode

colors = ["red", "green", "blue", "yellow"]
random.shuffle(colors)

for color in colors:
    screen.fill(color)
    pygame.display.flip()
    pygame.time.wait(1000)

screen.fill("black")
pygame.display.flip()
pygame.time.wait(1000)

#message = 
#    "Simon says:
###    UP RED DOWN CLUE LEFT GREEN RIGHT YELLOW 
response = input(message)

for event in pygame.event.get():
   if event.key == pygame.K_UP:
        screen.fill("red")
        user_sequence.append("red")
        elif event.key == pygame.K_DOWN
        screen.fill("blue")
        user_sequene.append("blue")
        elif event.key == pygame.K_LEFT
        screen.fill("green")
        user_sequence.append("green")
        elif event.key == pygame.K_RIGHT:
        screen.fill("yellow")
        user_sequence.append("yellow")
    


print("user sequence:",user_sequence)


import random
import pygame
import turtle
import math

#Part A
window = turtle.Screen()
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle1.speed(1)
turtle1.penup()
turtle2.speed(1)
turtle2.penup()
turtle1.shape("turtle")
turtle2.shape("turtle")
turtle1.color("blue")
turtle2.color("orange")

#race1
turtle1.goto(-100,20)
turtle2.goto(-100,-20)
turtle1.forward(random.randrange(1,101))
turtle2.forward(random.randrange(1,101))
turtle1.goto(-100,20) #is there a way i can make them return to a position without repeating 
turtle2.goto(-100,-20)

#race2
for r in range(0,10):
    turtle1.forward(random.randrange(1,11)) 
    turtle2.forward(random.randrange(1,11))
turtle1.goto(-100,20)
turtle2.goto(-100,-20)
window.exitonclick()

#part B
pygame.init()
pygame.event.get
screen= pygame.display.set_mode()

screen.fill("white")
pygame.display.flip() 
pygame.time.wait(1000)



Shapelist = [3,4,6,20,100,360]
side_length = (50)
xpos = 250
ypos = 250

for num_sides in Shapelist:
    points = []
    for i in range(num_sides):
        angle= 360/num_sides
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians) 
        points.append([x,y]) 
    pygame.draw.polygon(screen,"blue",points)
    pygame.display.flip() 
    pygame.time.wait(2000)

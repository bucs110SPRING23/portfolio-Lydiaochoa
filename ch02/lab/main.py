import random
import pygame
import turtle
import math

#Part A
window = turtle.Screen()
turtle1 = turtle.Turtle
turtle2 = turtle.Turtle
turtle1.shape("turtle")
turtle2.shape("turtle")
turtle1.color("blue")
turtle2.color("orange")

#race1
turtle1.goto(-100,20)
turtle2.goto(-100,-20)
turtle1.forward(random.randomrandrange(1,101))
turtle2.forward(random.randomrandrange(1,101))
turtle1.goto(-100,20) #is there a way i can make them return to a position without repeating 
turtle2.goto(-100,20)

#race2
for r in (0,10):
    random.randrange(1,11)
    turtle1.goto(-100,20)
    turtle2.goto(-100,-20)
    turtle1.forward(randomrandrange) #can i use period for this
    turtle2.forward(randomrandrange)
    turtle1.position(-100,20)
    turtle2.position(-100,20)
    break
window.exitonclick()


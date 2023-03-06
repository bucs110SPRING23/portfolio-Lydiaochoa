import random
import turtle 

window = turtle.Screen()
turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("pink")
turtle1.speed(0)

coin = random.randint(0,1)
distance = 10 
angle = 90 
is_in_screen() == True 
colors = ["red", "green", "yellow", "blue"]

while is_in_screen():
    coin = random.randint(0,1)
    if coin ==1: 
    turtle1.left(angle)
    turtle1.forward(distance)
    else: coin == 0:
        turtle1.right(angle)
    turtle1.forward(distance)

    turtleX = turtle1.xcor()
    turtleY = turtle1.ycorr()
    x_range = window.window_width() / 2 
    y_range = window.window_height() / 2 

    if abs(turtleX) . x_range or abs(turtleY) > y_range: 
        is_in_screen = False

window.exitonclick()




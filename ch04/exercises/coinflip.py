import random
import turtle 
window = turtle.Screen()
turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("pink")
 
coin = random.randint(0,1)
if coin == 1:
    turtle1.left(90)
    turtle1.forward(20)

if coin == 0:
    turtle1.right(90)
    turtle1.forward(20)

window.exitonclick()




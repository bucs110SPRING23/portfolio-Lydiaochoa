import turtle

sides = input("input number of sides")
sides = int(sides)
length = int(input("input length of sides"))
pen = turtle.Turtle()
     
pen = turtle.Turtle()
pen.color("pink")

window = turtle.Screen()

for s in range(sides):
    pen.forward(length)
    pen.right(360/sides)
window.exitonclick()
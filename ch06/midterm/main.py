import turtle

sides = int(input("enter number of sides of the flower:  "))
length = int(input("enter length of petals: "))
window = turtle.Screen()
pen = turtle.Turtle()

def main ():
    for i in range(4):
        pen.fd(50)
        pen.right(90)
        pen.fd(100)

    pen.bk(30)
    pen.left(90)
    pen.fd(90)

    for s in range(sides):
        pen.forward(length)
        pen.right(360/sides)
    return main
main()

pen.up()
pen.goto(-100,20)

window.exitonclick()
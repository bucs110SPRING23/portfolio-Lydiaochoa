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
main()


# def flower():
#     for i in range(4):
#         franklin.fd(50)
#         franklin.right(90)
#         franklin.fd(100)

#     franklin.bk(30)
#     franklin.left(90)
#     franklin.fd(90)

#     for s in range(sides):
#         franklin.forward(length)
#         franklin.right(360/sides)
#     return flower
# flower()

pen.up()
pen.goto(-100,20)

window.exitonclick()

# window = turtle.Screen()
# def shapeusingfuncionandt(): 
#     sides = input("input number of sides")
#     sides = int(sides)
#     length = (input("input length of sides"))
#     length = int(length)
#     pen = turtle.Turtle()
#     pen.color("pink")
#     for s in range(sides):
#         pen.forward(length)
#         pen.right(360/sides)

# window.exitonclick()

# def rectangle(): 
#     dimensions = int(input("enter the size of your house"))
#     return dimensions

# def main():
# dimensions: int(input("Input house size: "))


# pygame.init()
# pygame.event.get()
# screen = pygame.display.set_mode()
# screen.fill("White")
# pygame.display.flip()
# pygame.time.wait(200)
# pygame.draw.rect(screen,"blue",[500, 500, 400,400])
# pygame.display.flip()
# pygame.time.wait(5000)
# pygame.draw.polygon(screen,"green", [400,400])
# pygame.display.flip()
# pygame.time.wait(5000)


# def boat():
#     screen.fill("green")
#     pygame.display.flip()
#     pygame.time.wait(5000)


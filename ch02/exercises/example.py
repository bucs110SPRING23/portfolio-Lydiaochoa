import turtle
pen = turtle.Turtle()
pen2 = turtle.Turtle()
pen.shape("turtle")
pen2.shape("turtle")
pen2.color("purple")
pen.color("orange")
pen.speed(1)
pen2.speed(0)
window = turtle.Screen()
# variable = module.function()
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen2.forward(100)
pen2.left(90)
pen2.forward (100)
pen2.left(90)
pen2.forward(100)

window.exitonclick()


#window must always be last turtle command 
#part B
pygame.init()
window = pygame.display.set_mode
color = ("blue")
pointslist = [] #can i just put points in like this 
num_sides = (int(input("enter number of sides:")))
side_length = (input("enter legnth of sides"))
xpos = 
ypos = 
for in s (number_of_sides)
    angle= 360/number_of_sides
    radians = math.radians(angle * i)
    x =xpos + side_length * math.cos(radians)
    y = ypos + sde_length * math.sin(radians)
    break  
pygame.draw.polygon(pointslist,color)
color = ("blue")
pygame.display.flip 
pygame.time.wait(1000)
window.fill("white")
pygame.display.flip 
window.exitonclick
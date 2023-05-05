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


# class notes 3/6 

#def defines a fucntion
# funtcitons are always defined in  global scope 
#scope- where the data/ algorithm is accessible 
# vending machine 
# black boxing --> writing code that determines something, and then doesnt matter anymore/ we dont care how it works 
print("Welcome to the vending machine")
code = input("please enter a code: ")
money = input("give me money: ")

def my_vending_machine():
    if code == "A": 
        if money >= 1:
            print("you got a coke")
    elif code == "B":
        if money >= 1.5:
            print("you got a water")
        else: 
            print("you need more money")
    elif code == "c":
        if money >=2:
            print("you got a juice")
    else:
        print("invalid code")

def find_max(x, y, z): #def can acces varibles in a global scope: basically, def can provide a fucntion, but unless we run the code or input something, it doesnt get use 
   #print("please enter 3 numbers: ")
    #a = int(input(" : "))
    #b = int(input(" : "))
    #c = int(input(" : "))
    max = a 
    if y > max:
        max = y 
    if z > max:
        max = z
print(max)

for _ in range(3):
    print("please enter 3 numbers: ")
    a = int(input(" : "))
    b = int(input(" : "))
    c = int(input(" : "))
    find_max(a, b)
# not passing A,b , and c, ut their values as python has assigned them to x y z 
#collision: 2 variables of the same name 
# cant have variables of the same name in the same scope 
def foo(var): #var in fucntion scope assures that 2 different var are not the same--> using the same name as a global variable is called shadowing 
    var+= 1
    print(var)

var = 5 
foo(var)
print(var)

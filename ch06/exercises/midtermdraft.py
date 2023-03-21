import turtle
window = turtle.Screen()
franklin = turtle.Turtle()

def main():
    for i in range(4):
        franklin.fd(50)
        franklin.right(90)
        franklin.fd(100)

    for z in range(2):
        franklin.fd(85)
        franklin.right(90)
        franklin.fd(40)
        franklin.fd(1)
    return main
main()

franklin.up()
franklin.goto(-100,20)

# # def main (x,y):
#     sides = int(input("enter number of sides: "))
#     length = int(input("enter length: "))
#     result = multiply(x,y)
#     window = turtle.Screen()
#     franklin = turtle.Turtle()
#     for i in range(result):
#         franklin.forward(y)
#         franklin.right(360/x)
#     main(x,y)


# # def multiply(sides,length): 
#     x = sides * 3
#     y = length * 10 
#     return x,y


#  def multiply(x,y):
#     accumulator = 0
#     for _ in range(y):
#         accumulator = accumulator + x
#     return accumulator

# def exponent (x, y):
#     accumulator = 1 # accumulator staring pattern depends on your algorithm 
#     for _ in range(y):
#         accumulator = accumulator * x
#     return accumulator

# def sqaure (x):
#     return multiply (x,2) # could also be return multiple(x,x)

# def main(): 
#     x = int(input("enter a number:  "))
#     y = int(input("enter another number: "))
#     result = multiply (x, y)
#     print(result)
#     result = exponent (x,y)
#     print(result)
#     result = sqaure(x)
#     print(result)


# main()

# # def petal(sides,length):
# #     for i in range(sides):
# #         franklin.forward(length)
# #         franklin.right(360/sides)
# # petal(sides, length)

window.exitonclick()
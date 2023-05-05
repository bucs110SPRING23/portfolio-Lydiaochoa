def foo(): 
    x = 5 
    return tuple(range(6,61)) #return can only return one thing, but with a tuple, you can retuen multiple things in a list--> it is technically one thing. if we tried to use a list python would convertt hat to a tuple  

y = foo()
print(y, type(y))

def powerof(x=0,p= 0)
    power = p 
    y = x ** power
    return y

power = 2 
result = powerof(5,3)
print(result)

def foo():
    x = 5 
    print("1", x * x )

def foo2():
    x = 5
    return x * x

import random 
print("2", foo( abs( random.randint(1,100))))
print

#caseconventions 
#pdf, .py

#1000 line program 
#name collisions 
#global variables never leabe memeory while the program is running 
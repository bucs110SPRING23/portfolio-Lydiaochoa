
# Substitutions review 
# object oriented programming 
# classes 

# subs.py
import json 

def main(): 
    text = open('news.txt','r').read() #dont have to worry about closing because we are just reading the file 
    sub_fptr = open('substitutions.json', 'r')
    subs = json.load(sub_fptr)
    print(subs,type(subs))

    for k,v in subs.items(): 
    text = text.replace(k,v)
    fptr = open("betternews.txt", 'w')
    fptr.write(text)
    fptr.close()


main() 


#advanced programming just manages complexity 
# unix - basic operating system- about 10,000 SLOC

# complex objects
# - primitives: int, str,float,lists,dict,tuple
# turtle: x(int)y, heading, co,or(color), pensize(int), shape(str)
#  we want to bundle data and functions together 
    # state: the current value of the data in the object 
    # behavior: the functions that operate on the data in the object 

# point: object should be doing one thing 
# state; X,Y COLOR
# Behavior: change_color, move 
#classes == types 

# print(type(t)) complex 
# print(type(1)) primitive

# class are blueprint for objecs
# functions are store algorithms 
# class as a stored sata type--> ususally in global scope 
# classes are NOT exectuable code 
# dont put exectuable code in global scope, definititons are fine 

# point class 
# - instance: an object created from a specific classs 
# t = turtle.Turtle() #t is an instance of turtle 
# instance variable: an internal variable that is part of an instance 
# t,x,t.pos #x and pos are instance variables 
# interface: the miethods and variables of an object 

# ex) t.forward #forward () part of the intercaed of turtle 



# point: make it a class ourselves--> classes just allow us to name different types for ourselves 
class Point: 
    # classes always start with a capital leter 
    # usually, classes go in their own file 
    # 1 class per file 
    #dunders = double underscores on both sides of the name 

    def _init_(self): #self is the instance being created 
        self.xx = 0 #dot iperrator accessees instance variables of object. Adding self._ ties the scope of var to the object scope
        self.y = 0 
        self.color = ""

import point
p1= point.Point()#p1 is an instanceof point, Point is  a class 
p1.x = 10

p2 = point.Point()
p2.x = 5

# state of p1(x=10, y = 0, color='')
# state of p2(x = 5,y=0, color'')


#t = turtl.Turtle()
#w = turtle.Screen()

#3/27

# blueprint for an object: 
# def graph_point():
# class == type
# class are named with Titlecase

class Colorpoint:
    "docstring for point"
    def _init_(self): 
        self.xcoor =0 
        self.ycoor = 0 
        self.color = "red"

import point
import turtle 
import sub.module #folderr is sub, file is called module 

#from sub import module 

#snake case: snake_case, underscored for all spaces, all lowercase
#camelcase: camelCase, capital for space, starts lowercase lowercase 
# turtlecase: TitleCase, capital for spaces, starts capital
p1= point.Point() 
print(p1.xcoor, p1.ycoor,p2.color,type(p2))
p2= point.Point()
print(p2.xcoor,p2.ycoor,p2.color,type(p2))

#functions are called methods hren theyre in a classs
# in this case, the function  is a blueprint for how to create an object within this class

self.xcoor = abs(x)
self.ycoor = abs(y) 
self.on = True 
self.rect = pygame.Ract(abs(x), abs(y), 5,5)
self.color = color

def random_color(self)
    colors= []
    self.color = random.choice(colors)




#in another file: 
import random
p1 = point.Point() 
p2 = point.Point(3,4, "yellow")

p1.xcoor = 10 
print(p1.xcorr, p1.ycoor,p1.color type(p1), id(p1))
print(p2.xcoor,p2.ycoor,p2.color type(p2)id(p2))

points = []
for p in range(10) 
x = random.rantint(0,250)
y = random.randint(0,250)
points.append(point.Point(x,y))

t = turtle.Turtle()
for p in points 
p.random_color
t.color(p.color)
t.goto(p.xcoor,p.ycoor)

turtle.Screen().exitonclick()

class stars 
pygame.
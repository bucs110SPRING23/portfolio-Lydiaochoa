
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

#bool - boolian value 
# true/ false 
# caps are important 
# True is as much a value as 1 or "hello"
print(type(True))
print(bool(1), bool(-1), bool("hello"))

print(bool(0), bool(""), bool([]))

#boolean expressions: math expression that ends in either true or false 
x = 5 
y = 10 
print(x==y) #this is how you test for equality. = is assignment and == is boolean equality test
print(x > y)
print(x < y)
print(x >= y) # is more than or equal to 
print(x <= y) # less than or equal to 
print(x != y) #not equal
# and, or , not - semantic operators 
# and: and == true, when x and y are both true --> must have two trues 
print(True and True) #true 
print(True and False) # will give false 

#or- at least one true
print(True or True)#true 
print(True or False)#True 
print(False or True)#True 
print(False and False)#False 

#Not - negation 
print(not True) #false 
print('apple' == 'apple')
print('apple' < 'Apple pie')

#is - operator to check if a statement is true 
#ex)
print(1 is 1)

mynums= [1,2,3,4,5,6,7]
print(1 in mynums)
print(10 in mynums)
print(1 is 5//5) #remember you have to do a double // bc it is a float 

a = int(input("num:"))
if a > 10
    print("x is greater than 10")
elif a > 5
else: 
    print("x is less than or equal to 5")


#elif: always goes between the if and else. this is optional, you can have as many as you want.
# is<boolean condition> is required to do something 
# else is optional too 

# what is the difference between elif and else
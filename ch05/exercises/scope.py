def multiply(x,y):
    accumulator = 0
    for _ in range(y):
        accumulator = accumulator + x
    return accumulator

def exponent (x, y):
    accumulator = 1 # accumulator staring pattern depends on your algorithm 
    for _ in range(y):
        accumulator = accumulator * x
    return accumulator

def sqaure (x):
    return multiply (x,2) # could also be return multiple(x,x)

def main(): 
    x = int(input("enter a number:  "))
    y = int(input("enter another number: "))
    result = multiply (x, y)
    print(result)
    result = exponent (x,y)
    print(result)
    result = sqaure(x)
    print(result)


main()
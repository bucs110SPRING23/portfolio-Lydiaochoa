import random 
number = random.randrange(1,1000)

x = int(input("guess the number"))
while number in range(1,1000):
    if x > number:
            print("Too low")
            x = int(input("guess the number"))
    elif x < number:
            print("Too high")
            x = int(input("guess the number"))
    elif x == number:
            print("correct!")
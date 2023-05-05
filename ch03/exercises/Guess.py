import random 
number = random.randrange(1,11)

x = int(input("guess the number"))


for i in range(3):
    if x != number:
        if x > number:
            print("Too low")
            x = int(input("guess the number"))
        elif x < number:
            print("Too high")
            x = int(input("guess the number"))
        elif x == number:
            print("correct!")
           


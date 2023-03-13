# loop through range of values suppplied by the user 
# is value os divisible by 3, print fizz, 
# if the value is divisible by 5, print buzzif the value is divisible by 3 and 5, print fizzbuzz

num = int(input("enter an upper limit"))
for i in range(num +1): # includes upper limit
    print("number: ", i)
    if i % 5 ==0 and i % 3 ==0: 
        print("fizzbuzz")

    #if not i % 3:
    elif i % 3 ==0:
        print("buzz")
    elif i % 5 ==0:
        print("fizz")

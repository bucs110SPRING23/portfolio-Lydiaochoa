#NUMBER ADDING
print("enter numbers to sum ['q' to quit]")

sum = 0 
while sum != 'q':
    value= input("number: ")
    if value.isdigit():
        value = int(value)r
        sum += value #sum = sum + value 
    elif value == 'q':
        print("your total is:", sum)
        sum = value
        break 

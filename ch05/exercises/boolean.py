def percentage_to_letter(percent= 99): # we can use "pass" as a placeholder 
    """ 
    this a function that returns a letter based on a percentage
    args: percent(int)
    return:letter (str)
    """
    letter = "A"
    if 80 < percent < 90:
        letter = "B"
    elif 70 < percent < 80:
        letter = "C"
    elif 60 < percent < 70:
        letter = "D"
    else:
        letter = "F"
    return letter 

def is_passing(letter): #remember this is a boolean function, is_* convention
    return letter.lower() in "abc" #you can tell the fucntion to return this without saying (return true or return false)

def main(): #driver code: top level algorithm. called main for historical reasons
    grades= [90,80,70,60,50]
    for grade in grades:
        letter = percentage_to_letter(90)
        if is_passing(letter):
            print("you passed!")
        else: 
            print("someone messed up your grades")

main()

print(percentage_to_letter.__doc__)

def remove_vowels(string):
    vowels = "aeiou"
    vowels += vowels.upper() #includes upper case
    result = "" #why did we do this? because strings are immutable. if you want the new string to be different(ie adding or subtracting vowels) you need to make a wholenew string 
    for ch in string:
        if ch not in vowels:
            result +=ch
    return result
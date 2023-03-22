import json 

def main(): 
    text_fptr = open('news.txt','r').read() #dont have to worry about closing because we are just reading the file 
    sub_fptr = open('substitutions.json', 'r')
    subs = json.load(sub_fptr)

    print(subs,type(subs))


main() 
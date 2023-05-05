def main(): 
    file_pointer = open("assets/ideas.txt", "r") # r puts it in read mode. W writes to a file and A appends to a file 
    ideas = file_pointer.read()
    print(ideas)

    #you can also do file_pointer.readlines which will read out every single line in a file 
    #open("ideas.txt") #file must be from same folder as main function? you can do "folder"/"filename"

    file_pointer = open("ideas.txt" "a") #file gets truncated
    idea = input("enter an idea: ")
    ideas = []
    ideas.append(idea)
    for i in ideas:
         file_pointer.write(i + "backslash n")

main()

#OS manages files: programs can't access files
#request the file from the OS: need the name, location of file, and how to use file 
# working with files is one-way

# JSON
# JSON is a string format, not a file format
# doesnt matter if it is .txt or .json
# works with almost any programming language

file_contents = open("assets/ideas.txt", "r").read()
print(file_contents)
data = json.loads(file_contents)

# no single quote stings in json--> json converts all ur data into the type 
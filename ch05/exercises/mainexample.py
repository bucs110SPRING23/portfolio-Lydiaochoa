def main(): 
    file_pointer = open("assets/ideas.txt", "r") # r puts it in read mode. W writes to a file and A appends to a file 
    ideas = file_pointer.read()
    print(ideas)

    #you can also do file_pointer.readlines which will read out every single line in a file 
    #open("ideas.txt") #file must be from same folder as main function? you can do "folder"/"filename"

    file_pointer = open("ideas.txt" "w") #file gets truncated
    idea = input("enter an idea: ")
    ideas = []
    ideas.append(idea)
    print (ideas)

main()

#OS manages files: programs can't access files
#request the file from the OS: need the name, location of file, and how to use file 
# working with files is one-way
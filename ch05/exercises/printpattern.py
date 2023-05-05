def starpyramid(rows): #rows = levels 
    for i in range(1, rows +1):
        print("*" * i )

def rstar_pyramid(rows):
    for i in range(rows, 0, -1):
        print("*" * i)

levels = int(input("enter desired pyramid height:  "))
starpyramid(levels)
rstar_pyramid(levels)

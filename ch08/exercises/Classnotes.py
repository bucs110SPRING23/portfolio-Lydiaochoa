# class data: instance variables 
import turtle

class Num: 
    def _init_(self,n) -> None:
        self.data = n #instance variables for Num type objects 
        self.x = 'string'
    
    def addone(self):
        self.data += 1

    def
class Foo: 
    def main() ->  None:
        mynum = Num(7)
        mynum2 = Num(9)
        mynum3 = {'data':7, 'x':'string'} #or print(mynum3['data']) 
        print(mynum.data)
        print(mynum2.data)
        print(mynum3['data'])
        print(mynum._dict_)
        mynum.addone() 
        print(mynum.data)
        mynum2.addone()
        print(mynum2.data)

        dictionary = {'x':1,'y':2 ,'z':3}
        foo = Foo(**dictionary)

        t = turtle.Turtle()
        t.forward(56)
        mylist = [] #list()
        mylist.append
        index = 0
        mylist.pop(index)
        # mylist.forward would not work because list is not the type of varibale that has defined a forward function 
    main()


    # ** indicate dictionary, kwargs is a convention 

    num = 5 
    print(f"the number is: {num}") 
    mynewnum = num(5)
    print(f"The number is: {mynewnum}")
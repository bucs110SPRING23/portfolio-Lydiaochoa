class rectangle:
    def __init__(self, x, y ,height, width):
        self.xcoor = abs(x) 
        self.ycoor = abs(y) 
        self.height = 50
        self.width = 50 
        return str(self.xcoor,self.ycoor,self.height, self.width)

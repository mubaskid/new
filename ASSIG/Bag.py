class Bag:
    def __init__(self, color, shape, size, space, type):
        self.color = color
        self.shape = shape
        self.size = size
        self.space = space
        self.type = type

    def __init__(self, color:str, shape:str, size:str, space:str, type:str):
        self.color = color
        self.shape = shape
        self.size = size
        self.space = space
        self.type = type

    def display(self):
        print(self.color, self.size, self.shape, self.type)
        

bag = Bag("Black", "Big", "Oval", "400width", "travelingbag")
bag.display()
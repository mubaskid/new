class House:
    def __init__(self, livingroom, bedroom, dinningroom, bathroom, kitchen, store, type):
        self.livingroom = livingroom
        self.bedroom = bedroom
        self.dinningroom = dinningroom
        self.bathroom = bathroom
        self.kitchen = kitchen
        self.store = store
        self.type = type

    def __init__(self, livingroom:str, bedroom:str, dinningroom:str, bathroom:str, kitchen:str, store:str, type:str):
        self.livingroom = livingroom
        self.bedroom = bedroom
        self.dinningroom = dinningroom
        self.bathroom =bathroom
        self.kitchen = kitchen
        self.store = store
        self.type = type

    def display(self):
        print(self.livingroom, self.bedroom, self.dinningroom, self.bathroom, self.kitchen,self.store, self.type)
home = House("Livingroom", "bedroom", "dinningroom", "bathroom", "kitchen", "foodstore", "duplex")
home.display()
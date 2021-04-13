class Phone:
    def __init__(self, color, brand, model, screen, charger, intrnalStorage, version):
        self.color = color
        self.brand = brand
        self.model = model
        self.screen = screen
        self.charger = charger
        self.internalStorage =  intrnalStorage
        self.version = version

    def __init__(self, color:str, brand:str, model:int, screen:str, charger:str, internalStorage:float, version:float):
        self.color = color
        self.brand = brand
        self.model = model
        self.screen = screen 
        self.charger = charger
        self.internalStorage = internalStorage
        self.version = version

    def display(self):
        print(self.color, self.brand, self.model, self.screen, self.charger, self.internalStorage, self.version)
device = Phone('red', "IphoneXR", 4815, "GorrillaScreen", "Icharger", 280.1, 9.1)
device.display()
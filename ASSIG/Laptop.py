class Lapptop:
    def __init__(self, size, type, brand, RAM, InternalStorage, keyboard, touchpad, switch):
        self.size = size
        self.type = type
        self.brand = brand
        self.RAM = RAM
        self.InternalStorage = InternalStorage
        self.keyboard = keyboard
        self.touchpad = touchpad
        self.switch = switch

    def __init__(self, size:str, type:str, brand:str, RAM:float, InternalStorage:float, keyboard:str, touchpad:str, switch:str):
        self.size = size
        self.type = type
        self.brand = brand
        self.RAM = RAM
        self.InternalStorage = InternalStorage
        self.keyboard = keyboard
        self.touchpad = touchpad
        self.switch = switch

    def dipslay(self):
        print(self.size, self.type, self.brand, self.RAM, self.InternalStorage, self.keyboard, self.touchpad, self.switch)

laptop = Lapptop("17inches", "touchscreen", "Hp", 4.2, 258, "wide", "Hptouchpad", "switch")
laptop.dipslay()
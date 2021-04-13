class Gun:
    def __init__(self, length, weight, height, bullet, fireRange, type, size):
        self.length = length
        self.weight = weight
        self.height = height
        self.bullet = bullet
        self.fireRange = fireRange
        self.type = type
        self.size = size

    def __init__(self, length:float, weight:float, height:float, bullet:str, fireRange:str, type:str, size:str):
        self.length = length
        self.weight = weight
        self.height = height
        self.bullet = bullet
        self.fireRange = fireRange
        self.type = type
        self.size = size

    def  display(self):
        print(self.length, self.weight, self.height, self.bullet, self.fireRange, self.type, self.size)
weapon = Gun(17.5, 65.0, 1.0, "batterybullet", "265m", "XR1919", "big")
weapon.display()
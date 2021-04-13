class Fan:
    def __init__(self, slow, medium, fast, speed, radius, color):
        self.slow = slow
        self.medium = medium
        self.fast = fast
        self.speed = speed
        self.radius = radius
        self.color = color

    def myFan(self, slow=1, medium=2, fast=3, speed=5, radius=160.0, color='white'):
        self.slow = 1
        self.medium = 2
        self.fast = 3
        self.speed = 5
        self.radius = 160.0
        self.color = 'white'

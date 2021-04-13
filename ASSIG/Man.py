class Man:
    def __init__(self, ear, mouth, leg, nose, eyes, teeth, hair, name):
        self.ear = ear
        self. mouth = mouth
        self.leg = leg
        self.nose = nose
        self.eyes = eyes
        self.teeth = teeth
        self.hair = hair
        self.name = name

    def __init__(self, ear:str, mouth:str, leg:str, nose:str, eyes:str, teeth:str, hair:str, name:str):
        self.ear = ear
        self.mouth = mouth
        self.leg = leg
        self.nose = nose
        self.eyes = eyes
        self.teeth = teeth
        self.hair = hair
        self.name = name

    def display(self):
        print(self.ear, self.mouth, self.leg, self.nose, self.eyes, self.teeth, self.hair, self.name)
human = Man("flapear", "smallmouth", "legs", "pointednose", "eyes", "teeth", "hair", "name")
human.display()
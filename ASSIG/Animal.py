class Animal:
    def __init__(self, ears, eyes, nose, head, teeth, legs, species, hands):
        self.ears = ears
        self.eyes = eyes
        self.nose = nose
        self.head = head
        self.teeth = teeth
        self.legs = legs
        self.species = species
        self.hands = hands

    def __init__(self, ears:str, eyes:str, nose:str, head:str, teeth:str, legs:str, species:str, hands:str):
        self.ears = ears
        self.eyes = eyes
        self.nose = nose
        self.head = head
        self.teeth = teeth
        self.legs = legs
        self.species = species
        self.hands = hands 

    def displayAnimal(self):
        print(self.ears, self.eyes, self.nose, self.head, self.teeth, self.legs, self.species, self.hands)
animal = Animal("ears", "eyes", "nose", "head", "cannine", "legs", "mammal", "hands")
animal.displayAnimal()
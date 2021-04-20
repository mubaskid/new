import math
class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def discriminant(self):
        return ((self.__b)**2) - (4 * self.__a * self.__c)

    def root1(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.__b + math.sqrt(self.discriminant())) / (2 * self.__a)
    def root2(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.__b - math.sqrt(self.discriminant())) / (2 * self.__a)

a = QuadraticEquation(8,-7,-5)
print (a.root1())
print (a.root2())
print (a.discriminant())

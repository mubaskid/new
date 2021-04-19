import math

class QuadraticEquation:

    a = print(int(input("Enter a number: ")))
    b = print(int(input("Enter a number: ")))
    c = print(int(input("Enter a number: ")))
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def Equation(self):
        return ((self.b)**2) - (4*self.a*self.c)
        

    def rootA(self):
        if self.Equation() < 0:
            return False
        else:
            return (-self.b + math.sqrt(self.Equation())) / (2 * self.a)

    def rootB(self):
        if self.Equation() > 0:
            return True
        else:
            return(-self.b - math.sqrt(self.Equation())) / (2 * self.a )

    def rootC(self):
        if self.Equation() >= 0:
            return ("Done")
        else:
            return (-self.b - math.sqrt(self.Equation())) / (2 * self.a )


quadratic_equation = QuadraticEquation()

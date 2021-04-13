import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def Equation(self):
        return ((self.b)**2) - (4*self.a*self.c)
        

    def root1(self):
        if self.Equation() < 0:
            return None
        else:
            return (-self.b + math.sqrt(self.Equation())) / (2 * self.a)

    
    def root2(self):
        if self.Equation() > 0:
            return True
        else:

            return(-self.b - math.sqrt(self.Equation())) / (2 * self.a ) 

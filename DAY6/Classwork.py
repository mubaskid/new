class Student:
    def __init__(self, name, Class, school, rollnumber):
        self.name = name
        self.Class = Class
        self.school = school
        self.rollnumber = rollnumber

    def Display(self, name, Class, school, rollnumber):
        self.name = name
        self.Class = Class
        self.school = school
        self.rollnumber = rollnumber

    def setAge(self,age):
        self.age = age

    def setMark(self, mark):
        self.mark = mark
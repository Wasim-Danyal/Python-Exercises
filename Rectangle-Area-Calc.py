import random

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width  = width

    def area(self):
        return self.length*self.width

NewRec = Rectangle(3, 6)
print(NewRec.area())

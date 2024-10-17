'''
4. Create a base class Polygon with an abstract method area(). Create child classes Triangle and Rectangle that implement the area() method.
'''
from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

tri = Triangle(5, 10)
rec = Rectangle(4, 7)

print(tri.area())
print(rec.area())

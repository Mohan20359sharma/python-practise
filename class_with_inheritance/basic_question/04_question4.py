'''
4. Create a parent class Shape with a method area(). Inherit it in a class Circle and override the method to calculate the area of a circle (πr²).
'''
import math

class Shape:
    def area(self):
        pass
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

circle = Circle(5)
print(circle.area())
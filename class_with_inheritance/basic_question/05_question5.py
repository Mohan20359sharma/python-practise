'''
5. Create a class Rectangle with attributes width and height. Write a method to calculate its area.
'''
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        return self.height * self.width

rect = Rectangle(4,5)
print(rect.area())
        
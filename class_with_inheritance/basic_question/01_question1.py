'''
1. Define a class Car with an attribute color. Then, create an object and print the color.
'''
class Car:
    def __init__(self, color):
        self.color = color
car1 = Car("Red")
print(car1.color)
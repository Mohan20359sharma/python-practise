'''
7. Create a parent class Vehicle with a method move(). Create a child class Bike and call the move() method from the child class.
'''
class Vehicle:
    def move(self):
        return "Vehical is moving"
class Bike(Vehicle):
    pass
bike = Bike()
print(bike.move())
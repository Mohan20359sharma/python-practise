'''
10. Create a class Animal with an attribute species. Create two child classes Dog and Cat, each with their own speak() method.
'''
class Animal:
    def __init__(self, species):
        self.species = species
    
class Cat(Animal):
    def speak(self):
        return "Meow"
    
class Dog(Animal):
    def speak(self):
        return "Bark"

dog = Dog("Canine")
cat = Cat("Feline")

print(dog.speak())
print(cat.speak())
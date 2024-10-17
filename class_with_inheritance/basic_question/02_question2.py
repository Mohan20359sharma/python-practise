'''
2. Create a class Animal with a method speak(). Inherit it in a class Dog and override the method to print "Bark".
'''
class Animal:
    def speak(self):
        return "Animal sound"
class Dog(Animal):
    def speak(self):
        return "Bow! Bow!"
dog = Dog()
print(Animal().speak())
print(dog.speak())

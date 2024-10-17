'''
3. Write a class Person with attributes name and age. Create two objects and print their details.
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Mohan", 19)
person2 = Person("Rajat", 21)

print(person1.name, person1.age)
print(person2.name, person2.age)
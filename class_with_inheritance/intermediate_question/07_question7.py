'''
7. Create a class Person with private attributes __name and __age. Write getter and setter methods to access and update these attributes.
'''

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def str_age(self, age):
        if age>0:
            self.__age = age

person = Person("Mohan", 19)
print(person.get_name())
# person(35)
print(person.get_age())
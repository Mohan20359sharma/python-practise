'''
2. Create a class Employee with attributes name, position, and salary. Write a method give_raise() that increases the salary by a percentage.
'''

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, percentage):
        self.salary += self.salary * (percentage / 100)
        return f"New salare after {percentage}% raise:{self.salary}"

emp = Employee("Mohan", "Manager", 60000)
print(emp.give_raise(10))
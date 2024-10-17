'''
9. Create a class Employee with attributes name and salary. Add a method to display the employee’s details.
'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"
emp = Employee("Mohan", 1200000)
print(emp.show_details())
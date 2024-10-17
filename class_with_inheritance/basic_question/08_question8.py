'''
8. Define a class Calculator with methods to add, subtract, multiply, and divide two numbers.
''' 
class Calculator:
    def add(self, a, b):
        return a+b
    
    def sub(self, a, b):
        return a-b
    
    def multiply(self, a, b):
        return a*b
    
    def divide(self, a, b):
        return a / b
calc = Calculator()
print(calc.add(3,4))
print(calc.sub(3,4))
print(calc.multiply(3,4))
print(calc.divide(3,4))
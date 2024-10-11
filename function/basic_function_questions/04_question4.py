'''
Exercise 4: Function to Calculate Factorial of a Number
Write a function that takes an integer as input and returns its factorial.
'''
def factorial(n):
    result = 1
    for i in range (1,n+1):
        result *=i
        return result
result = factorial(5)
print("factorial", result)

'''
Exercise 4: Function with Keyword Arguments
Write a function describe_person that takes a name and age, and prints a description. 
Ensure the function works with keyword arguments as well.
'''
def description_person(name, age):
    print(f"{name} is {age} year old")
description_person(name="Mohan", age="19")
'''
Exercise 3: Default Arguments in Functions
Create a function greet with a default argument for the greeting. 
If no greeting is passed, it should default to "Hello".
'''

def greet(name, greeting="Hello"):
    print(f"{greeting},{name}")

greet("Mohan")
greet("bob","Hi")

'''
Exercise 3: Function to Find the Maximum of Three Numbers
Write a function that takes three numbers and returns the maximum of the three.
'''
def find_max(a,b,c):
    return max(a,b,c)
result = find_max(25,22,13)
print("Maximam number is:", result)
'''
Exercise 2: Function with Return Value
Write a function add_numbers that takes two numbers as parameters and returns their sum.
'''
def add_numbers(a, b):
    return a+b
result = add_numbers(5,7)
print(result)

'''
Exercise 2: Function to Check if a Number is Even or Odd
Write a function that takes an integer as input and returns whether the number is even or odd.
'''
def check_even_odd(num):
    if (num%2 == 0):
        return "Even"
    else:
        return "odd"
    

num = int(input("Enter number to check Even or Odd: "))
print(check_even_odd(num))
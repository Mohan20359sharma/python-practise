'''
Exercise 6: Function to Check if a String is Palindrome
Write a function that checks if a given string is a palindrome (reads the same forward and backward).
'''
def palindrome(s):
    return s==s[::-1]
result = palindrome("racecar")
# s = input("Enter word")
# palindrome(s)
print("palindrome:", result)

'''
Exercise 6: Passing Functions as Arguments
Write a function apply_operation that takes another function as an argument and applies it to two numbers.
'''
def add_number(a, b):
    return a+b
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
print(add_number(a, b))

'''

'''
def add(a, b):
    return a + b

def apply_operation(func, x, y):
    return func(x, y)

result = apply_operation(add, 5, 3)
print(result)  # Output: 8

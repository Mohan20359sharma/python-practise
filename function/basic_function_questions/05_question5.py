'''
Exercise 5: Function to Reverse a String
Write a function that takes a string as input and returns the reversed string
'''
def reverse_string(s):
    return s[::-1]
result = reverse_string("hello")
print("reverse string", result)
'''
Exercise 5: Function that Returns Multiple Values
Create a function get_min_max that takes a list of numbers and returns both the minimum and maximum numbers.
'''
def get_min_max(numbers):
    return min(numbers), max(numbers)
min_val, max_val = get_min_max([6,7,2,3,4,5,12])
print(f"Min: {min_val}, Max: {max_val}")
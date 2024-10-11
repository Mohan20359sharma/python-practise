'''
Exercise 8: Function to Return the Square of a Number
Write a function that takes a number as input and returns the square of that number.
'''
def square_num(n):
    return n*n
result = square_num(12)
print("square number:", result)

'''
Exercise 8: Lambda Function
Write a lambda function that squares a number and use it with Python's built-in map function to square each number in a list.
'''
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

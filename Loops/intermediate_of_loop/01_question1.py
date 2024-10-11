'''
 Sum of Digits of a Number
Write a Python program that reads an integer from the user and finds the sum of its digits using a loop.
'''
def sum_of_digits(n):
    sum_digits = 0 
    while n > 0:
        digit = n % 10
        sum_digits += digit
        n = n // 10
    return sum_digits

n = int(input("Enter a number: "))
result = sum_of_digits(n)
print(f"sum of digit: {result}")


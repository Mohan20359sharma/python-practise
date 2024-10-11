'''
2. Prime Numbers within a Range
Write a Python program to print all prime numbers between two numbers (inclusive).
'''
def is_prime(num):
    if num<=1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
          return False
    return True
        
def print_prime_numbers(start, end):
    for num in range(start, end+1):
        if is_prime(num):
            print(num, end=" ")

start = int(input("Enter the  start of the range: "))
end = int(input("Enter the end of range: "))
print("Print numbers in the range:")
print_prime_numbers(start, end)
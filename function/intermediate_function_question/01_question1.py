'''
Problem: Factorial Trailing Zeros
Write a function trailing_zeros(n) that takes a positive integer n and 
returns the number of trailing zeros in the factorial of n.
'''
def tralling_zeros(n):
    if n == 0:
        return 1
    else:
        return n * tralling_zeros(n-1) 

n = int(input("Enter a number: "))
print(tralling_zeros(n))
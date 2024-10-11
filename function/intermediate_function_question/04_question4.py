'''
Fibonacci Sequence:
Write a function fibonacci(n) that returns the nth Fibonacci number using recursion or an iterative approach.
'''
def fibonacci(n):
    if n==0:
        return 0 
    elif n == 1:
        return 1 

    a,b = 0,1
    for _ in range(2,n+1):
        a,b = b, a+b
    return b

print(fibonacci(7))

'''

'''
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
print(fibonacci(7))  # Output: 13
print(fibonacci(10))  # Output: 55

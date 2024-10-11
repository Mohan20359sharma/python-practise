'''
Sum of Divisors:
Write a function sum_of_divisors(n) that takes an integer n and returns the sum of all divisors of n.
'''
def sum_of_divisors(n):
    total = 0
    for i in range(1,n+1):
        if n % i == 0:
            total += i
    return total
     

n = int(input("Enter a number: "))
print(sum_of_divisors(n))
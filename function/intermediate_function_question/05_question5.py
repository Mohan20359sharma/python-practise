'''
 Prime Number Check:
Write a function is_prime(n) that checks if a given integer n is a prime number.
'''
def is_prime(n):
    if n <= 1:  # Prime numbers are greater than 1
        return False
    for i in range(2, int(n**0.5) + 1):  # Check divisors up to the square root of n
        if n % i == 0:
            return False
    return True

# Example usage:
print(is_prime(29))  # Output: True
print(is_prime(15))  # Output: False
print(is_prime(2))   # Output: True
print(is_prime(1))   # Output: False

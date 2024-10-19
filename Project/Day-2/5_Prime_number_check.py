def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)  + 1):
        if n % i == 0:
            return False
        return True

num = int(input('Enter a number: '))        
if prime_number(num):
    print(f'{num} is prime.')
else:
    print(f'{num} is not prime number.')

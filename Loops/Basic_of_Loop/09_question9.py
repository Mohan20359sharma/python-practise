# Solution
n = int(input("Enter how many Fibonacci numbers to generate: "))
a, b = 0, 1
if n == 1:
    print(a)
else:
    print(a, b, end=" ")
    for _ in range(n - 2):
        next_number = a + b
        print(next_number, end=" ")
        a, b = b, next_number


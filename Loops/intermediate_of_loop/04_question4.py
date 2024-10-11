'''
 '''
n = int(input("Enter a number: "))
result = 1
for i in range(1, n+1):
    result *= i
print(f"Factorial of {n} is: {result}")

#  in function foramate 

'''
def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num
n = int(input("Enter a number: "))
print(f"factorial of {n} is: {factorial(n)}")
'''
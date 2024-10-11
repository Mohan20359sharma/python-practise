'''
Exercise 7: Function to Find the Length of a List
Write a function that takes a list as input and returns the number of elements in the list.
'''
def list_length(s):
    return len(s)
result = list_length([1, 2, 3, 4, 5])
print(result)

'''
Exercise 7: Recursive Function
Write a recursive function factorial that computes the factorial of a number.
'''
def factorial(n):
    if n == 0 :
        return 1
    else:
        return n*factorial(n-1)
n = int(input("Enter a number: "))
print(factorial(n))
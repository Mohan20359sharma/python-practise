def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b != 0:
        return a/b
    else:
        print("b is zero.")
a = int(input("Enter a number."))
b = int(input("Enter a number."))
add = add(a, b)
substract = substract(a,b)
multiply = multiply(a,b)
divide = divide(a,b)
print(f"Sum of {a} + {b} is", add)
print(f"Sum of {a} - {b} is", substract)
print(f"Sum of {a} * {b} is", multiply)
print(f"divide of {a} / {b} is", divide)
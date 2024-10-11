num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter a operator (+, -, *, /):")

if operator == '+':
    print(f"result: {num1 + num2}")
elif operator == '-':
    print(f"result: {num1 - num2}")
elif operator == '*':
    print(f"result: {num1 * num2}")
elif operator == '/':
    if num2 != 0:
        print(f"result: {num1 / num2}")
    else:
        print("Cannot divided by zero.")
else:
    print("Invalid operator")
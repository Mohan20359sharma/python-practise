# make calculator
num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
operator = input("Enter operator (+,-,*,/)")
if operator == '+':
    print(f"result {num1 + num2}")
elif operator == '-':
    print(f"result {num1 - num2}")
elif operator == '*':
    print(f'result {num1 * num2}')
elif operator == '/':
    if num2 != 0:
        print(f'result {num1 / num2}')
    else:
        print('Zero not divided')
else:
    print('Invalid ')
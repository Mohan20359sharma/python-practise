'''
Addition, Substraction, Multiplication, Divide, Square root, Exponation, Modulus
'''
import math

def calculator():
    print('Select operation.')
    print('1. Addition')
    print('2. Substraction')
    print('3. multiply')
    print('4. Divide')
    print('5. Square Root')
    print('6. Exponation(x^y)')
    print('7. Module')

    choice = int(input('Enter choice(1/2/3/4/5/6/7):'))

    if choice == 5:
        num = float(input('Enter a number: '))
        print(f'The square of {num} is {math.sqrt(num)}')
    else:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))
    
        if choice == 1:
            print(f'{num1} + {num2} is: {num1 + num2}')

        elif choice == 2:
            print(f'{num1} - {num2} is: {num1 -num2}')

        elif choice == 3:
            print(f'{num1} X {num2} is: {num1 * num2}')

        elif choice == 4:
            if num2 != 0:
                print(f'{num1} / {num2} is: {num1 / num2}')
            else:
                print('Second Input is Zero.')

        elif choice == 6:
            print(f'{num1} ^ {num2} is: {num1 ** num2}')

        elif choice == 7:
            print(f'{num1} % {num2} is: {num1 % num2}')



calculator()
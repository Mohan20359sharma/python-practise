def calculator_bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Enter your Weight: "))
height = float(input("Enter your height: "))
bmi = calculator_bmi(weight,height)

print(f'Your BMI is {bmi:.2f}')
if bmi < 18.5:
    print('You are underweight.')
elif bmi < 24.9:
    print('You have normal weight.')
else:
    print('You are overweight. ')
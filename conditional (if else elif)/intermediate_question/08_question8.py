height = float(input("Enter your height in meter:"))
weight = float(input("enter your weight in kg: "))
bmi = weight / (height ** 2)

print(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("Category: UnderWeight")
elif 18.5 <= bmi < 24.9:
    print("Category: NormalWeight")
elif 25 <= bmi <29.9:
    print("Category: OverWeight")
else:
    print("Category: Obesity")

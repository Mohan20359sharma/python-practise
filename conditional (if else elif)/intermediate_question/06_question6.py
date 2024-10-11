# valid traingle
num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
num3 = int(input("Enter a number"))
if (num1+num2>num3) and (num1+num3>num2) and (num2+num3>num1):
    print("this triangle is valid.")
else:
    print("This trangle is not valid.")
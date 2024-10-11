n = int(input("Enter a number: "))

if n >= 16:
    print("You are eligible for drive")
    exit
if n >= 18:
    print("You are eligible for vote")
else:
    print("You are not eligible for vote and drive.")
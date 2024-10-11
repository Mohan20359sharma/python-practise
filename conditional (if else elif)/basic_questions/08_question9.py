# tringle type check
side1 = float(input("Enter first side length: "))
side2 = float(input("Enter first side length: "))
side3 = float(input("Enter first side length: "))

if side1 == side2 == side3 :
    print("Equilateral Triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
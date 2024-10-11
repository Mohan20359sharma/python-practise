# Grade Cheaker
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

n = int(input("Score: "))
if n >= 90 and n < 100:
    print("Grade: A")
elif n >= 80 and n < 89:
    print("Garde: B")
elif n >= 70 and n < 79:
    print("Grade: C")
elif n >= 60 and n < 69:
    print("Grade: D")
else:
    print("Fail")
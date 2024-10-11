def gcd(a, b):
    while b:
        a,b =b, a%b
    return a

def lcm(a,b):
    return a*b  // gcd(a,b)

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(f"LCM of {a} and {b} is: {lcm(a, b)}")
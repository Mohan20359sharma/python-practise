n = int(input("Enter the number of terms"))
a,b = 0,1
count = 0
 
if n<= 0:
    print("Please enter a positive integer.")
elif n == 0:
    print("Fibbonacci sequence up to 1 terms.", a)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a, end=" ")
        a,b = b, a+b
        count += 1
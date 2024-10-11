n = input("Enter a string: ")
if n == n[::-1]:
    print(f"{n} is palindrome")
else:
    print(f"{n} is not palindrome")
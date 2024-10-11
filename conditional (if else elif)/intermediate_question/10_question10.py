number = list(map(int, input("Enter numbers seprated by spaces: ").split()))
even_numbers = [num for num in number if num % 2 == 0]
print("Even number:", even_numbers)
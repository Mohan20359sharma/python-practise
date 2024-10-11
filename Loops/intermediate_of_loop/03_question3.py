'''

'''
def is_armstrong(num):
    num_str = str(num)
    num_digit = len(num_str)
    sum_digit = sum([int(digit) ** num_digit for digit in num_str])
    return sum_digit == num

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an armstrong number: ")
else:
    print(f"{num} is not an armstrong number: ")
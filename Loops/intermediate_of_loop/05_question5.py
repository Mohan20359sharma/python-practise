'''
reverse number4
'''
def reverse_number(n):
    reverse_num = 0
    while n > 0:
       digit = n % 10
       reverse_num = reverse_num * 10 + digit
       n = n // 10
    return reverse_num
n = int(input("Enter a number: "))
print(f"Reverse number: {reverse_number(n)}")
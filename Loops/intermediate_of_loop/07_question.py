'''
'''
def number_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
n = int(input("Enter a number: "))
number_pattern(n)

''
''
n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()
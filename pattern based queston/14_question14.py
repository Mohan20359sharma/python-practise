'''
     1 
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
'''
def pascal_tringal(n):
    for i in range(n):
        print(" " * (n-i), end="")
        val = 1
        for j in range(i + 1):
            print(val, end=" ")
            val = val * (i - j) // (j + 1)
        print()
n = int(input("Enter a number of rows:"))
pascal_tringal(n)
'''
    *
   * *
  *   *
 *     *
*********
'''
n = int(input("Enter a nmber of rows:"))
for i in range(1, n+1):
    if i == n:
        print("*" * (2 * n -1))
    else:
        print(" " * (n-i) + "*" + " " * (2*i-3)+("*" if i !=1 else ""))
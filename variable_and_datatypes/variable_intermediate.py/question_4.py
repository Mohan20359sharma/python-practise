'''
Given two sets, A and B, write a Python program to:
Find the union of A and B.
Find the intersection of A and B.
Find the difference between A and B.

# Your code here

# Expected output:
# Union: {1, 2, 3, 4, 5, 6, 7, 8}
# Intersection: {4, 5}
# Difference (A - B): {1, 2, 3}

'''
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union
print("Union :", A|B)

# Intersection
print("Intrsection :", A&B)

# Diffrence
print("Difference :", A - B)
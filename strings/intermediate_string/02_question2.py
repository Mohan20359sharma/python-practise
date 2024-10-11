'''
Exercise 2: Check if Two Strings are Anagrams
Write a Python program to check if two strings are anagrams. 
Two strings are anagrams if they contain the same characters, but the order may differ.
'''
def check(s1,s2):
    return sorted(s1) == sorted(s2)
s1="manhaa"
s2="mahana"
print(check(s1,s2))
'''
Exercise 5: Check if String is Palindrome
Write a Python program to check if a given string is a palindrome 
(a word, phrase, or sequence that reads the same backward as forward).
'''
string = input("enter a string:")

is_palindrome = string == string[::-1]

print(f"Is the string'{string}' a palindrone:", is_palindrome)
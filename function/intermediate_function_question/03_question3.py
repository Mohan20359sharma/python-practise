'''
Is Palindrome:
Write a function is_palindrome(s) that checks if a given string s is a palindrome. 
The function should ignore spaces, punctuation, and case.
'''
import string

def is_palindrome(s):
    # Remove spaces, punctuation, and convert to lowercase
    cleaned_s = ''.join(char.lower() for char  in s if char.isalnum())
    return cleaned_s==cleaned_s[::-1]
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("Hello"))
print(is_palindrome("jahaJ"))
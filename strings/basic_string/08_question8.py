'''
Exercise 8: Find a Substring
Write a Python program that checks if a specific substring exists in a given string
'''
string = "Tomorrow i watches a movie Stree 2. this is very amazing"
sub_string = input("Enter a SubString to find: ")
if sub_string in string:
    print(f"The Substring '{sub_string}' exist in the string")
else:
    print(f"The substring '{sub_string}' Not exist in the string")
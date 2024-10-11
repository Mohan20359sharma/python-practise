'''
Exercise 1: Count Vowels and Consonants
Write a Python program to count the number of vowels and consonants in a given string. 
Ignore any non-alphabet characters.
'''
def count_vowels_consonants(string):
    vowels="aeiouAEIOU"
    vowels_count = 0
    consonants_count = 0
    for char in string:
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
    return vowels_count, consonants_count

string = "Mohan Sharma"
vowels, consonants = count_vowels_consonants(string)
print(f"vowels:{vowels}, consonents:{consonants}")
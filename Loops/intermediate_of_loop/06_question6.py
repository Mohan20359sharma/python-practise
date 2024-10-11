'''
Count Vowels and Consonants
Write a Python program to count the number of vowels and consonants in a given string using a loop.
'''
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    count_vowels = 0
    count_consonents = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                count_vowels += 1
            else:
                count_consonents += 1
    return count_vowels, count_consonents
s = input("Enter a string: ")
vowels, consonents = count_vowels_consonants(s)
print(f"Vowels: {vowels}, Consonents: {consonents}")
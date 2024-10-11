'''
Exercise 3: Find the Longest Word in a Sentence
Write a Python program to find the longest word in a sentence.
'''

def longest_word(string):
    words = string.split()
    return max(words,key=len)
string = "Pythom is a poweerful programming langauge"
print(longest_word(string))
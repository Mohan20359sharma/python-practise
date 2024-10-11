# Exercise 4: Count Occurrences of a Character
# Write a Python program that takes a string and a character as input and counts 
# how many times the character appears in the string.
x = "Mohan is a good boy and he lost his skill of learning and he practise of learnig"
count = 0
for i in x:
    if i=='e':
        count=count+1
print("count of o in x", str(count))

# this is new input
# Input: "banana" and 'a'
# Output: 3

string = input("Enter a string: ")
char = input("Enter a character to count: ")

count = string.count(char)
print(f"The character '{char}' appears {count} times.")

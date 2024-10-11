from collections import defaultdict
word = "Hello"
letter_count = defaultdict(int)
for letter in word:
    letter_count[letter] += 1
print(letter_count) 
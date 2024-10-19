def palindrome(word):
    return word == word[::-1]
word = input("Enter a string: ").lower()
if palindrome(word):
    print(f'{word} is palindrome')
else:
    print(f'{word} is not a palindrome')

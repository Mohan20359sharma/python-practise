'''
Exercise 9: Function to Count the Number of Vowels in a String
Write a function that takes a string as input and returns the number of vowels in the string.
'''
def check_vowels_consonent(n):
    vowels = "aeiouAEIOU"
    count = 0
    for char in n:
        if char in vowels:
            count +=1
            
    return count
result = check_vowels_consonent("hello")
print("Vowels is:", result)

'''
Exercise 9: Function with Variable-Length Arguments (*args)
Create a function sum_all that takes any number of arguments and returns their sum
'''
def sum_all(*args):
    return sum(args)
print(sum_all(1,2,3,4))

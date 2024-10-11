'''
Exercise 4: Remove Duplicates from a String
Write a Python program to remove duplicate characters from a string while maintaining the original order.
'''
def duplicate_word(string):
    result = []
    for char in string:
        if char  not in result:
            result.append(char)
    return ''.join(result)

string="programming" 
print("string without duplicates:", duplicate_word(string))

'''
Exercise 10: Function to Convert Celsius to Fahrenheit
Write a function that converts temperature from Celsius to Fahrenheit. Use the formula:
F= (5/9) X C+32
'''
def temp_converture(celsius):
    return (9/5)*celsius+32

celsius = int(input("Enter a number:"))
# result  = temp_converture(25)
# print(result)
print(temp_converture(celsius))

'''
Exercise 10: Function with Keyword Variable-Length Arguments (**kwargs)
Write a function print_info that accepts any number of keyword arguments and prints them.
'''
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print_info(name="Mohan", age=19, city="Agra")
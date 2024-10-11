'''
You have a list of numbers. Use a list comprehension to create a new list containing only the even numbers from the original list and multiply them by 2.
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list=[num * 2 for num in numbers if num % 2 == 0]
print(new_list)
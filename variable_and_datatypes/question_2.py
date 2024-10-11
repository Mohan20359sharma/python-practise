'''
Convert age (which is an integer) to a float.
Convert height (which is a float) to an integer.
Convert is_student (which is a boolean) to a string.
'''
age = 25
height = 5.9
is_student = True

age_float = float(age)
height_int = int(height)
student_str = str(is_student)

print(age_float , type(age_float))
print(height_int, type(height_int))
print(student_str, type(student_str))
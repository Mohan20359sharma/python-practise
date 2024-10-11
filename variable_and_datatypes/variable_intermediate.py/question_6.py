'''
Unpack a tuple of three elements (representing a student's name, age, and grade) into separate variables.
Pass a tuple as an argument to a function that prints each element separately.
'''
student_info=("Mohan Sharma", 19, "A")
name,age,grade=student_info
print(f"Name : {name}, Age : {age},Grade : {grade}")
def print_student_info(name,age,grade):
    print(f"Name : {name}, Age : {age}, Grade : {grade}")
print_student_info(*student_info)
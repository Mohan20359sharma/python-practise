'''
Create a nested dictionary where each key is a student’s name and the value is another dictionary containing that student’s age and grades.
Write a Python program to:
Print each student’s name, age, and grade.
Calculate the average grade for all students.
'''
students = {
    "Mohan": {"age":19, "grade":[80,75,70]},
    "Than": {"age":22,"grade":[60,65,70]},
    "Anish": {"age":22, "grade":[70,60,65]}
}
for student, info in students.items():
    print(f"Name:{student}, Age:{info['age']}, Grade:{info['grade']}")


total_grade = sum(sum(info["grade"]) for info in students.values())
num_grade = sum(len(info["grade"]) for info in students.values())
average_grade = total_grade/num_grade
print("Average grade for all students:", average_grade)
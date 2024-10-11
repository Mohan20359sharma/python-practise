'''
Create a dictionary with five key-value pairs representing student names and their corresponding grades.
Add a new student and their grade to the dictionary.
Update the grade of one of the existing students.
Write a function to calculate the average grade of all students
'''

students = {
    "Mohan Sharma": 95,
    "Than Singh": 75,
    "Anish": 80,
    "Vikas Saini":75
}
# Add Student
students["Anubhav"] = 95
# existing
students["Vikas Saini"] = 80

# Calculate all grade
def aveage_grade(students):
    return sum(students.values())/len(students)
print("students:",students)
print("Average grade:", aveage_grade(students))
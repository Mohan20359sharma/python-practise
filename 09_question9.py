'''
9. Create a class Course with attributes course_name and students. Write methods to enroll students, drop students, and display the list of students.
'''

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []
 
    def enroll_student(self, student):
        self.students.append(student)
        return f"{student} enrolled in {self.course_name}"
    
    def drop_student(self, student):
        if student in self.students:
            self.students.remove(student)
            return f"{student} dropped from {self.course_name}"
        return f"{student} not found in {self.course_name}"
    
    def display_student(self):
        return f"Student in {self.course_name}: {', '.join(self.students)}" if self.students else "No students enrolled"

course = Course("Python Programming")
print(course.enroll_student("Mohan"))
print(course.enroll_student("Anubhav"))
print(course.display_student())
print(course.drop_student("Anubhav"))
print
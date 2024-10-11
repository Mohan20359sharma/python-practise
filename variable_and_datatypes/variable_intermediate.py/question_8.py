students = (("Mohan",80), ("Anish",75), ("Than",75))
# sort by grade
sorted_students = sorted(students, key=lambda x:x[1],reverse=True)
print(sorted_students)


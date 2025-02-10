students = (("Zakaria", 20, "A"), ("Saiful", 22, "C"), ("Imtiaz", 21, "B"))
sorted_students = tuple(sorted(students, key=lambda x: x[2]))
print(sorted_students)
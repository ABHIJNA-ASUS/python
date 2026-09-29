# main.py

import student

print("--- Student Information Report ---")
print("Name:", student.name)
print("Register Number:", student.register_number)
print("Course:", student.course)

print("\n--- Marks Obtained ---")

for subject, score in student.marks.items():
    print(f"{subject}: {score}/100")
    
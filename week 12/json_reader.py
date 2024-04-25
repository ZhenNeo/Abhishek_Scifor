import json

with open('Scifor/data.json', 'r') as file:
    data = json.load(file)

students = data['students']
print("list of students")

for student in students:
    print(student)

sorted_students = sorted(students, key=lambda x: x['age'])
print("\nStudents sorted by age: ")

for student in sorted_students:
    print(student)

young_students = filter(lambda x: x['age'] < 25, students)
print("\nStudents under the age of 25: ")

for student in young_students:
    print(student)

student_names = map(lambda x: x['name'], students)
for name in student_names:
    print(name)
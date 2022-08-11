import random

student_count = 10
course_count = 9
journal = []

for i in range(student_count):
    grades = []
    for j in range(course_count):
        grade = random.randint(2, 5)
        grades.append(grade)
    journal.append(grades)

print(journal)

avg_grades = []
for i in range(student_count):
    grades = journal[i]
    summa = 0
    for j in range(course_count):
        summa = summa + grades[j]

    avg_grade = summa / course_count
    avg_grades.append(round(avg_grade))

print(avg_grades)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n * n for n in numbers]

# print(squared_numbers)

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names}
# print(students_scores)

passed_students = {
    name: score for (name, score) in students_scores.items() if int(score) >= 60
}
# print(passed_students)

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for index, row in student_data_frame.iterrows():
    print(row.student)

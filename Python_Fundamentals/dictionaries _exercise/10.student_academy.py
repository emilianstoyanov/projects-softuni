n = int(input())
students_with_grades_dict = {}

for _ in range(n):
    (student, grade) = (input(), float(input()))   # получаваме студент и оценка
    if student not in students_with_grades_dict:   # ако нямаме студента, добавяме празен списък и добавяме оценката
        students_with_grades_dict[student] = []  # ако нямаме този студент, добавяме го
    students_with_grades_dict[student].append(grade)  # {'John': [5.5]}

students_with_average_grades_dict = \
    dict((key, sum(value) / len(value)) for (key, value) in students_with_grades_dict.items())
        # взимеме средната оценка

students_with_average_grades_filtred_dict = \
    dict((key, value) for (key, value) in students_with_average_grades_dict.items() if value >= 4.5)
        # филтрираме средната оценка да е по-голяма или равна от 4.50

for (key, value) in sorted(students_with_average_grades_filtred_dict.items(), key=lambda x: x[1], reverse=True):
    print(f"{key} -> {value:.2f}") # сортираме вече филтрираното dict и вече взетата му среда оценка
n = int(input())
students_with_grades_dict = {}

for _ in range(n):
    (student, grade) = (input(), float(input()))  
    if student not in students_with_grades_dict:  
        students_with_grades_dict[student] = []  
    students_with_grades_dict[student].append(grade)  

students_with_average_grades_dict = \
    dict((key, sum(value) / len(value)) for (key, value) in students_with_grades_dict.items())
     
students_with_average_grades_filtred_dict = \
    dict((key, value) for (key, value) in students_with_average_grades_dict.items() if value >= 4.5)
       

for (key, value) in sorted(students_with_average_grades_filtred_dict.items(), key=lambda x: x[1], reverse=True):
    print(f"{key} -> {value:.2f}") 

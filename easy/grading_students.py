# https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true

import random

# 0 <= grade <= 100
# grade < 40 is failing

# grade + 2 > next multiple of 5, round up to the multiple
# if grade < 38, grade isn't rounded up

def grading_students(grades):
    new_grades = []
    
    for grade in grades:
        if grade > 37:
            if grade % 10 > 7:
                grade = ((grade // 10) + 1) * 10
        
        new_grades.append(grade)
    
    return new_grades


nb_grades = 10
grades = [random.randint(0, 100) for _ in range(nb_grades)]
print(grades)
print(grading_students(grades))
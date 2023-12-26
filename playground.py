student_grades = {}

math_grades = student_grades.get('Alice', {})
math_grades['math'] = 90

student_grades['Alice'] = student_grades.get('Alice', {})

math_grades_2 = student_grades['Alice']
math_grades_2['math'] = 90



import math

salary = float(input())
average_grade = float(input())
min_salary = float(input())

social_scholarship = 0
grade_scholarship = 0

if salary < min_salary and average_grade > 4.50:
    social_scholarship = min_salary * 0.35

if average_grade >= 5.50:
    grade_scholarship = average_grade * 25

if social_scholarship == 0 and grade_scholarship == 0:
    print(f'You cannot get a scholarship!')
elif grade_scholarship != 0 and grade_scholarship >= social_scholarship:
    print(f'You get a scholarship for excellent results {math.floor(grade_scholarship)} BGN')
elif social_scholarship != 0 and social_scholarship > grade_scholarship:
    print(f'You get a Social scholarship {math.floor(social_scholarship)} BGN')

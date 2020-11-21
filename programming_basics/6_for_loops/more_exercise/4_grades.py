students_count = int(input())

total_grade = 0

fail = 0
under_four = 0
under_five = 0
top_grade = 0

for grade in range(students_count):
    student_grade = float(input())
    total_grade += student_grade

    if student_grade < 3:
        fail += 1
    elif student_grade < 4:
        under_four += 1
    elif student_grade < 5:
        under_five += 1
    else:
        top_grade += 1

average_grade = total_grade / students_count
percentage_fail = fail / students_count * 100
percentage_under_four = under_four / students_count * 100
percentage_under_five = under_five / students_count * 100
percentage_top_grades = top_grade / students_count * 100

print(f'Top students: {percentage_top_grades:.2f}%')
print(f'Between 4.00 and 4.99: {percentage_under_five:.2f}%')
print(f'Between 3.00 and 3.99: {percentage_under_four:.2f}%')
print(f'Fail: {percentage_fail:.2f}%')
print(f'Average: {average_grade:.2f}')

name = input()

counter = 1
total_grade = 0
bad_grades = 0

while counter <= 12:
    grade = float(input())
    if grade >= 4:
        counter += 1
        total_grade += grade
    else:
        bad_grades += 1
        if bad_grades == 2:
            print(f'{name} has been excluded at {counter} grade')
            break

average_grade = total_grade / 12
if not bad_grades == 2:
    print(f'{name} graduated. Average grade: {average_grade:.2f}')

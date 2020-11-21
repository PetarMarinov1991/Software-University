name = input()

counter = 1
total_grade = 0

while counter <= 12:
    grade = float(input())
    if grade >= 4:
        total_grade += grade
        counter += 1

average_grade = total_grade / 12
print(f'{name} graduated. Average grade: {average_grade:.2f}')

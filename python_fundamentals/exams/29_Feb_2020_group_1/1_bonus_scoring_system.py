students_count = int(input())
lectures = int(input())
bonus = int(input())

max_bonus = 0
max_attendances = 0

for _ in range(students_count):
    student_attendances = int(input())
    if student_attendances > max_attendances:
        max_attendances = student_attendances
    current_bonus = student_attendances / lectures * (5 + bonus)
    if current_bonus > max_bonus:
        max_bonus = current_bonus

print(f'Max Bonus: {round(max_bonus)}.')
print(f'The student has attended {max_attendances} lectures.')

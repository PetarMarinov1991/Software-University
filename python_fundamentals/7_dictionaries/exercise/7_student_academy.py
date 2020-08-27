students = dict()

for _ in range(0, int(input()) * 2, 2):
    student = input()
    grade = float(input())

    if student not in students:
        students.update({student: [grade]})
    else:
        students[student] += [grade]

filtered_students = dict()

for student, grade in students.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        filtered_students.update({student: average_grade})

filtered_students = {k: v for k, v in sorted(filtered_students.items(), key=lambda x: -x[1])}

print('\n'.join([f'{student} -> {grade:.2f}' for student, grade in filtered_students.items()]))

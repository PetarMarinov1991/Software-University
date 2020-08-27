grades = dict()

for _ in range(int(input())):
    line = input().split()
    student, grade = line[0], float(line[1])
    if student not in grades:
        grades[student] = []
    grades[student].append(grade)

for student, grades in grades.items():
    avg_grade = f'{sum(grades) / len(grades):.2f}'
    formatted = " ".join([f'{grade:.2f}' for grade in grades])
    print(f'{student} -> {formatted} (avg: {avg_grade})')

courses = dict()

while True:
    line = input().split(' : ')

    if line[0] == 'end':
        break

    course_name, student = line

    if course_name not in courses:
        courses.update({course_name: [1, student]})
    else:
        courses[course_name] += [student]
        courses[course_name][0] += 1

courses = {k: v for k, v in sorted(courses.items(), key=lambda x: -x[1][0])}

for course in courses:
    print(f'{course}: {courses[course][0]}')
    for student in sorted(courses[course][1:]):
        print(f'-- {student}')

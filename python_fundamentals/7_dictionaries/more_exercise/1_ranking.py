def sort_dict(my_dict):
    my_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda x: -x[1])}
    return my_dict


participants = dict()
passwords = dict()
scores = dict()

while True:
    first_line = input()

    if first_line == 'end of contests':
        break

    first_line = first_line.split(':')
    contest, password = first_line

    if contest not in passwords:
        passwords.update({contest: password})

while True:
    second_line = input()

    if second_line == 'end of submissions':
        break

    second_line = second_line.split('=>')
    contest, password, student, points = second_line

    if contest in passwords and password == passwords[contest]:
        if student not in participants:
            participants.update({student: {contest: int(points)}})
            scores.update({student: int(points)})
        elif student in participants and participants[student].__contains__(contest):
            if participants[student][contest] < int(points):
                participants[student][contest] = int(points)
                scores[student] += int(points)
        else:
            participants[student].update({contest: int(points)})
            scores[student] += int(points)

scores = sort_dict(scores)
for student, score in scores.items():
    print(f'Best candidate is {student} with total {score} points.')
    break

print('Ranking:')
for student, contests in sorted(participants.items()):
    contests = sort_dict(contests)
    print(student)
    for contest, points in contests.items():
        print(f'#  {contest} -> {points}')

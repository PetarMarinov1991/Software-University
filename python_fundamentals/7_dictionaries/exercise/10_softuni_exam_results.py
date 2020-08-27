def sort_dict(my_dict):
    my_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda x: (-x[1], x[0]))}
    return my_dict


participants = dict()
submissions = dict()

while True:
    line = input()

    if line == 'exam finished':
        break

    line = line.split('-')

    if len(line) == 3:
        student, language, points = line
        if student not in participants or int(points) > participants[student]:
            participants[student] = int(points)
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1
    else:
        student = line[0]
        if student in participants:
            del participants[student]

participants = sort_dict(participants)
submissions = sort_dict(submissions)

print('Results:')
print('\n'.join([f'{student} | {points}' for student, points in participants.items()]))
print('Submissions:')
print('\n'.join([f'{language} - {submit}' for language, submit in submissions.items()]))

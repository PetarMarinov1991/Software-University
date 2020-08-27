def sort_dict(my_dict):
    my_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda x: (-x[1], x[0]))}
    return my_dict


courses = dict()
standings = dict()

while True:
    line = input().split(' -> ')

    if line[0] == 'no more time':
        break

    username, course, score = line[0], line[1], int(line[2])

    if course not in courses:
        courses.update({course: {username: score}})
    elif username not in courses[course]:
        courses[course].update({username: score})
    elif courses[course][username] < score:
        courses[course][username] = score

for course, participants in courses.items():
    participants = sort_dict(participants)
    print(f'{course}: {len(participants)} participants')
    number = 1
    for participant, score in participants.items():
        print(f'{number}. {participant} <::> {score}')
        number += 1
        if participant not in standings:
            standings.update({participant: score})
        else:
            standings[participant] += score

print('Individual standings:')
standings = sort_dict(standings)
number = 1
for username, score in standings.items():
    print(f'{number}. {username} -> {score}')
    number += 1

users = dict()

limit = int(input())

while True:
    line = input().split('=')
    command = line[0]

    if command == 'Statistics':
        break

    if command == 'Add':
        name, sent, received = line[1], int(line[2]), int(line[3])
        if name not in users:
            users[name] = [0, 0]
        users[name][0] += sent
        users[name][1] += received
    elif command == 'Message':
        sender, receiver = line[1], line[2]
        if sender in users and receiver in users:
            users[sender][0] += 1
            users[receiver][1] += 1
            if sum(users[sender]) == limit:
                print(f'{sender} reached the capacity!')
                del users[sender]
            if sum(users[receiver]) == limit:
                print(f'{receiver} reached the capacity!')
                del users[receiver]
    elif command == 'Empty':
        name = line[1]
        if name == 'All':
            users.clear()
        elif name in users:
            del users[name]

print(f'Users count: {len(users)}')
users = {k: v for k, v in sorted(users.items(), key=lambda x: (-x[1][1], x[0]))}
for user, mails in users.items():
    print(f'{user} - {sum(mails)}')

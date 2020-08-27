users = dict()

while True:
    line = input().split('->')
    command = line[0]

    if command == 'Statistics':
        break

    username = line[1]
    if command == 'Add':
        if username not in users:
            users.update({username: []})
        else:
            print(f'{username} is already registered')
    elif command == 'Send':
        email = line[2]
        users[username].append(email)
    elif command == 'Delete':
        if username in users:
            del users[username]
        else:
            print(f'{username} not found!')

users = {k: v for k, v in sorted(users.items(), key=lambda x: (-len(x[1]), x[0]))}

print(f'Users count: {len(users.keys())}')
for user, emails in users.items():
    print(user)
    for mail in emails:
        print(f'- {mail}')

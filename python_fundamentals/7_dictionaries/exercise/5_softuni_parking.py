registrations = dict()

for _ in range(int(input())):
    line = input().split()
    command = line[0]
    user = line[1]

    if command == 'register':
        number = line[2]
        if user not in registrations:
            registrations.update({user: number})
            print(f'{user} registered {number} successfully')
        else:
            print(f'ERROR: already registered with plate number {registrations[user]}')
    elif command == 'unregister':
        if user in registrations:
            del registrations[user]
            print(f'{user} unregistered successfully')
        else:
            print(f'ERROR: user {user} not found')

print('\n'.join([f'{user} => {number}' for user, number in registrations.items()]))

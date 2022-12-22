train = [0] * int(input())

command = input()

while command != 'End':
    args = command.split()
    command = args[0]

    if command == 'add':
        people = int(args[1])
        train[-1] += people
    elif command == 'insert':
        idx, people = int(args[1]), int(args[2])
        train[idx] += people
    elif command == 'leave':
        idx, people = int(args[1]), int(args[2])
        train[idx] -= people

    command = input()

print(train)

gifts = input().split()

command = input()

while command != 'No Money':
    args = command.split()
    command, gift = args[0], args[1]

    if command == 'OutOfStock':
        for i in range(len(gifts)):
            gifts[i] = None if gifts[i] == gift else gifts[i]
    elif command == 'Required':
        index = int(args[2])
        if index in range(len(gifts) - 1):
            gifts[index] = gift
    elif command == 'JustInCase':
        gifts[-1] = gift

    command = input()

print(' '.join([x for x in gifts if x]))

gifts = input().split()

while True:
    line = input()

    if line == 'No Money':
        break

    line = line.split()
    command, gift = line[0], line[1]

    if command == 'OutOfStock':
        if gift in gifts:
            idx = gifts.index(gift)
            for idx, item in enumerate(gifts):
                if item == gift:
                    gifts[idx] = 'None'
    elif command == 'Required':
        idx = int(line[2])
        if 0 <= idx < len(gifts):
            gifts[idx] = gift
    elif command == 'JustInCase':
        gifts[-1] = gift

print(' '.join([gift for gift in gifts if gift is not 'None']))

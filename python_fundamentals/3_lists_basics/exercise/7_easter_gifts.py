gifts = input().split()

command = input()

while command != 'No Money':
    arg = command.split()

    if arg[0] == 'OutOfStock':
        gift = arg[1]
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = 'None'
    elif arg[0] == 'Required':
        idx = int(arg[2])
        if 0 <= idx < len(gifts):
            gifts[idx] = arg[1]
    elif arg[0] == 'JustInCase':
        gifts[-1] = arg[1]

    command = input()

result = []

for gift in gifts:
    if gift is not 'None':
        result.append(gift)

print(' '.join(result))

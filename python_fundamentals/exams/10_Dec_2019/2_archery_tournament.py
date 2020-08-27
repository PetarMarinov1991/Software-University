targets = list(map(int, input().split('|')))

collected_points = 0

while True:
    line = input().split('@')
    command = line[0]

    if command == 'Game over':
        break

    if command == 'Reverse':
        targets = targets[::-1]

    elif command == 'Shoot Left':
        idx_start, idx_len = int(line[1]), int(line[2])
        if not idx_start >= len(targets):
            target = idx_len % len(targets) + 1
            targets[target] -= 5
            if targets[target] < 0:
                targets[target] = 0
            collected_points += 5
    elif command == 'Shoot Right':
        idx_start, idx_len = int(line[1]), int(line[2])
        if not idx_start >= len(targets):
            targets = targets[::-1]
            target = idx_len % len(targets)
            targets[target] -= 5
            if targets[target] < 0:
                targets[target] = 0
            collected_points += 5
            targets = targets[::-1]

print(' - '.join([str(target) for target in targets]))
print(f'Iskren finished the archery tournament with {collected_points} points!')

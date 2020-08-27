targets = list(map(int, input().split()))

while True:
    command = input()

    if command == 'End':
        break

    idx = int(command)

    if 0 <= idx < len(targets):
        for i, target in enumerate(targets):
            if target > targets[idx] and target != -1:
                targets[i] -= targets[idx]
            elif target <= targets[idx] and target != -1 and i != idx:
                targets[i] += targets[idx]
        targets[idx] = -1

print(f'Shot targets: {targets.count(-1)} -> {" ".join([str(target) for target in targets])}')

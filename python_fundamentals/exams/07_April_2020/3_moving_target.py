def valid_index(my_list):
    if 0 <= idx < len(my_list) and my_list[idx] > 0:
        return my_list[idx]


def valid_index_range(my_list):
    valid = True
    for i in range(idx - value, idx):
        if i < 0 or i > len(my_list):
            valid = False
    for i in range(idx, idx + value + 1):
        if i < 0 or i > len(my_list):
            valid = False
    return valid


targets = list(map(int, input().split()))

while True:
    args = input().split()
    command = args[0]

    if command == 'End':
        break

    idx, value = int(args[1]), int(args[2])

    if command == 'Shoot':
        if valid_index(targets):
            targets[idx] -= value
            if targets[idx] <= 0:
                targets.remove(targets[idx])
    elif command == 'Add':
        if valid_index(targets):
            targets.insert(idx, value)
        else:
            print('Invalid placement!')
    elif command == 'Strike':
        if valid_index_range(targets):
            for _ in range(idx - value, idx + value + 1):
                targets.remove(targets[idx - 1])
        else:
            print('Strike missed!')

print('|'.join([str(target) for target in targets]))

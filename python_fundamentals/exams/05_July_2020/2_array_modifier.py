ints = [int(x) for x in input().split()]

while True:
    line = input().split()
    command = line[0]

    if command == 'end':
        break

    if command == 'decrease':
        ints = [x - 1 for x in ints]
        continue

    idx_1, idx_2 = int(line[1]), int(line[2])
    if command == 'swap':
        ints[idx_1], ints[idx_2] = ints[idx_2], ints[idx_1]
    elif command == 'multiply':
        ints[idx_1] *= ints[idx_2]

print(', '.join([str(num) for num in ints]))

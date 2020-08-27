def valid_idx(index, my_list):
    if 0 <= index < len(my_list):
        return True


weapon = input().split('|')

while True:
    line = input().split()
    command = line[0]

    if command == 'Done':
        break

    if command == 'Move':
        direction, idx = line[1], int(line[2])
        if valid_idx(idx, weapon):
            idx_to_insert = 0
            if direction == 'Left':
                idx_to_insert = idx - 1
            elif direction == 'Right':
                idx_to_insert = idx + 1

            if valid_idx(idx_to_insert, weapon):
                weapon.insert(idx_to_insert, weapon.pop(idx))

    elif command == 'Check':
        even_or_odd = line[1]
        if even_or_odd == 'Even':
            print(' '.join(weapon[::2]))
        elif even_or_odd == 'Odd':
            print(' '.join(weapon[1::2]))

weapon_name = ''.join(weapon)
print(f'You crafted {weapon_name}!')

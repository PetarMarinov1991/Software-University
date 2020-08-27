def valid_idx(my_list):
    if 0 <= idx <= len(my_list):
        return True
    else:
        print('Index out of range')


def valid_name(name, my_list):
    if name in my_list:
        return True


tanks = input().split(', ')

for _ in range(int(input())):
    line = input().split(', ')
    command = line[0]
    tank_name = line[1]

    if command == 'Add':
        if valid_name(tank_name, tanks):
            print('Tank is already bought')
        else:
            tanks.append(tank_name)
            print('Tank successfully bought')
    elif command == 'Remove':
        if valid_name(tank_name, tanks):
            tanks.remove(tank_name)
            print('Tank successfully sold')
        else:
            print('Tank not found')
    elif command == 'Remove At':
        idx = int(line[1])
        if valid_idx(tanks):
            tanks.remove(tanks[idx])
            print('Tank successfully sold')
    elif command == 'Insert':
        idx, tank_name = int(line[1]), line[2]
        if valid_idx(tanks):
            if not valid_name(tank_name, tanks):
                tanks.insert(idx, tank_name)
                print('Tank successfully bought')
            else:
                print('Tank is already bought')

print(', '.join([tank for tank in tanks]))

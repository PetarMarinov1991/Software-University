def valid_idx(index, my_list):
    return index in range(len(my_list))


frogs = input().split()

while True:
    line = input().split()
    command = line[0]

    if command == 'Print':
        order = line[1]
        if order == 'Normal':
            print(f'Frogs: {" ".join(frogs)}')
            break
        elif order == 'Reversed':
            print(f'Frogs: {" ".join(frogs[::-1])}')
            break

    if command == 'Join':
        name = line[1]
        frogs.append(name)
    elif command == 'Jump':
        name, idx = line[1], int(line[2])
        if valid_idx(idx, frogs):
            frogs.insert(idx, name)
    elif command == 'Dive':
        idx = int(line[1])
        if valid_idx(idx, frogs):
            frogs.remove(frogs[idx])
    elif command == 'First' or command == 'Last':
        count = int(line[1])
        if count >= len(frogs):
            print(' '.join(frogs))
        else:
            if command == 'Last':
                print(' '.join(frogs[-count:]))
            else:
                print(' '.join(frogs[:count]))

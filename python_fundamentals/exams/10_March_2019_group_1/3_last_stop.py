def exist(value, my_list):
    if value in my_list:
        return True


paintings = list(map(int, input().split()))

while True:
    line = input().split()
    command = line[0]

    if command == 'END':
        break

    if command == 'Change':
        num, change_num = int(line[1]), int(line[2])
        if exist(num, paintings):
            idx = paintings.index(num)
            paintings[idx] = change_num
    elif command == 'Hide':
        num = int(line[1])
        if exist(num, paintings):
            paintings.remove(num)
    elif command == 'Switch':
        num, num_2 = int(line[1]), int(line[2])
        if exist(num, paintings) and exist(num_2, paintings):
            idx, idx_2 = paintings.index(num), paintings.index(num_2)
            paintings[idx], paintings[idx_2] = paintings[idx_2], paintings[idx]
    elif command == 'Insert':
        idx, num = int(line[1]), int(line[2])
        if 0 < idx <= len(paintings):
            paintings.insert(idx + 1, num)
    elif command == 'Reverse':
        paintings = paintings[::-1]

print(f'{" ".join([str(num) for num in paintings])}')

def valid_idx(index, my_list):
    if 0 <= index < len(my_list):
        return True


tasks = list(map(int, input().split()))

while True:
    line = input().split()
    command = line[0]

    if command == 'End':
        break

    if command in ['Complete', 'Change', 'Drop']:
        idx = int(line[1])
        if valid_idx(idx, tasks):
            if command == 'Complete':
                tasks[idx] = 0
            elif command == 'Change':
                time = int(line[2])
                tasks[idx] = time
            elif command == 'Drop':
                tasks[idx] = -1

    elif command == 'Count':
        second_command = line[1]
        if second_command == 'Completed':
            print(tasks.count(0))
        elif second_command == 'Incomplete':
            print(len(tasks) - tasks.count(-1) - tasks.count(0))
        elif second_command == 'Dropped':
            print(tasks.count(-1))

filtered_tasks = [task for task in tasks if task > 0]
print(' '.join([str(task) for task in filtered_tasks]))

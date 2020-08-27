def valid_idx(i, my_string):
    return i in range(len(my_string))


stops = input()

while True:
    line = input().split(':')
    command = line[0]

    if command == 'Travel':
        break

    if command == 'Add Stop':
        idx, stop = int(line[1]), line[2]
        if valid_idx(idx, stops):
            stops = stops[:idx] + stop + stops[idx:]
        print(stops)
    elif command == 'Remove Stop':
        start_idx, end_idx = int(line[1]), int(line[2])
        if valid_idx(start_idx, stops) and valid_idx(end_idx, stops):
            stops = stops[:start_idx] + stops[end_idx + 1:]
        print(stops)
    elif command == 'Switch':
        old_string, new_string = line[1], line[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)

print(f'Ready for world tour! Planned stops: {stops}')

def valid_idx(idx, my_string):
    if idx in range(len(my_string)):
        return True


input_string = input()
new_string = ''

while True:
    line = input().split()
    command = line[0]

    if command == 'Finish':
        break

    if command == 'Replace':
        old_char, new_char = line[1], line[2]
        for char in input_string:
            if char == old_char:
                new_string += new_char
            else:
                new_string += char
        input_string = new_string
        new_string = ''
        print(input_string)
    elif command == 'Cut':
        start_idx, end_idx = int(line[1]), int(line[2])
        if valid_idx(start_idx, input_string) and valid_idx(end_idx, input_string):
            input_string = input_string[:start_idx] + input_string[end_idx + 1:]
            print(input_string)
        else:
            print('Invalid indexes!')
    elif command == 'Make':
        upper_or_lower = line[1]
        if upper_or_lower == 'Upper':
            input_string = input_string.upper()
        elif upper_or_lower == 'Lower':
            input_string = input_string.lower()
        print(input_string)
    elif command == 'Check':
        substring = line[1]
        if substring in input_string:
            print(f'Message contains {substring}')
        else:
            print(f'Message doesn\'t contain {substring}')
    elif command == 'Sum':
        start_idx, end_idx = int(line[1]), int(line[2])
        if valid_idx(start_idx, input_string) and valid_idx(end_idx, input_string):
            substring = input_string[start_idx:end_idx + 1]
            ascii_sum = sum([ord(char) for char in substring])
            print(ascii_sum)
        else:
            print('Invalid indexes!')

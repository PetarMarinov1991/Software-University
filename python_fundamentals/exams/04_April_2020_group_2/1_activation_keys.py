raw_activation_key = input()
activation_key = raw_activation_key

while True:
    line = input().split('>>>')
    command = line[0]

    if command == 'Generate':
        break

    if command == 'Contains':
        substring = line[1]
        if substring in activation_key:
            print(f'{activation_key} contains {substring}')
        else:
            print('Substring not found!')

    elif command == 'Flip':
        letter_case, start_idx, end_idx = line[1].lower(), int(line[2]), int(line[3])
        part = activation_key[start_idx:end_idx]
        if letter_case == 'Upper':
            activation_key = activation_key.replace(part, part.upper())
        elif letter_case == 'Lower':
            activation_key = activation_key.replace(part, part.lower())
        print(activation_key)

    elif command == 'Slice':
        start_idx, end_idx = int(line[1]), int(line[2])
        activation_key = activation_key[:start_idx] + activation_key[end_idx:]
        print(activation_key)

print(f'Your activation key is: {activation_key}')

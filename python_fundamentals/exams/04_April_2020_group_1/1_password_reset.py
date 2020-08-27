old_password = input()
password = old_password

while True:
    line = input().split()
    command = line[0]

    if command == 'Done':
        break

    if command == 'TakeOdd':
        new_password = ''
        for idx, letter in enumerate(password):
            if idx % 2 != 0:
                new_password += letter
        password = new_password
        print(password)

    elif command == 'Cut':
        idx, length = int(line[1]), int(line[2])
        password = password[:idx] + password[idx + length:]
        print(password)

    elif command == 'Substitute':
        substring, substitute = line[1], line[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print('Nothing to replace!')

print(f'Your password is: {password}')

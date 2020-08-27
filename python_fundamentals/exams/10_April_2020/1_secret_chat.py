text = input()
result = text

while True:
    line = input().split(':|:')
    command = line[0]

    if command == 'Reveal':
        break

    if command == 'InsertSpace':
        idx = int(line[1])
        result = result[:idx] + ' ' + result[idx:]

    elif command == 'Reverse':
        substring = line[1]
        if substring in result:
            result = result.replace(substring, '', 1)
            result += substring[::-1]
        else:
            print('error')
            continue

    elif command == 'ChangeAll':
        substring, replacement = line[1], line[2]
        result = result.replace(substring, replacement)

    print(result)

print(f'You have a new text message: {result}')

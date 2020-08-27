for _ in range(int(input())):
    name = ''
    age = ''
    text = input()
    for i in range(len(text)):
        if text[i] == '@':
            while not text[i + 1] == '|':
                name += text[i + 1]
                i += 1
        if text[i] == '#':
            while not text[i + 1] == '*':
                age += text[i + 1]
                i += 1
    print(f'{name} is {age} years old.')

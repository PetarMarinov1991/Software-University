def letter_case(lower_or_upper, text):
    if lower_or_upper == 'lower':
        text = text.lower()
    elif lower_or_upper == 'upper':
        text = text.upper()
    return text


def reverse_substring(start, end, text):
    if start in range(len(text)) and end in range(len(text)):
        return text[start:end + 1][::-1]


def cut_substring(sub_str, text):
    if sub_str in text:
        text = text.replace(sub_str, '')
    return text


def replace_with_star(replace, text):
    new_text = ''
    for ch in text:
        if ch == replace:
            new_text += '*'
        else:
            new_text += ch
    text = new_text
    return text


username = input()

while True:
    line = input()

    if line == 'Sign up':
        break

    line = line.split()
    command = line[0]

    if command == 'Case':
        case = line[1]
        username = letter_case(case, username)
        print(username)
    elif command == 'Reverse':
        start_idx, end_idx = int(line[1]), int(line[2])
        if reverse_substring(start_idx, end_idx, username):
            print(reverse_substring(start_idx, end_idx, username))
    elif command == 'Cut':
        substring = line[1]
        if substring in username:
            print(cut_substring(substring, username))
        else:
            print(f'The word {username} doesn\'t contain {substring}.')
    elif command == 'Replace':
        char = line[1]
        username = replace_with_star(char, username)
        print(username)
    elif command == 'Check':
        char = line[1]
        if char in username:
            print('Valid')
        else:
            print(f'Your username must contain {char}.')

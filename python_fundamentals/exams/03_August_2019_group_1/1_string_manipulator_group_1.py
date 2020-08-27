def translate(char, replacement, my_string):
    return my_string.replace(char, replacement)


def includes(sub_string, my_string):
    return sub_string in my_string


def start_with(sub_string, my_string):
    return my_string.startswith(sub_string)


def find_last_idx(char, my_string):
    return my_string.rfind(char)


def remove_substring(start_idx, count, my_string):
    my_string = my_string[:start_idx] + my_string[count:]
    return my_string


string = input()

while True:
    line = input().split()
    command = line[0]

    if command == 'End':
        break

    if command == 'Translate':
        string = translate(line[1], line[2], string)
        print(string)
    elif command == 'Includes':
        print(includes(line[1], string))
    elif command == 'Start':
        print(start_with(line[1], string))
    elif command == 'Lowercase':
        string = string.lower()
        print(string)
    elif command == 'FindIndex':
        print(find_last_idx(line[1], string))
    elif command == 'Remove':
        print(remove_substring(int(line[1]), int(line[2]), string))

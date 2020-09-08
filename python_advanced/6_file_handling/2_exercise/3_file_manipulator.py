import os


def create_file(name):
    with open(name, 'w') as file:
        file.write('')


def add_content(name, content):
    with open(name, 'a') as file:
        file.write(content + '\n')


def replace_substring(name, old_string, new_string):
    with open(name, 'r') as file:
        text = file.read()
    text = text.replace(old_string, new_string)
    with open(file_name, 'w') as file:
        file.write(text)


while True:
    line = input().split('-')
    command = line[0]

    if command == 'End':
        break

    file_name = line[1]
    if command == 'Create':
        create_file(file_name)
    elif command == 'Add':
        add_content(file_name, line[2])
    elif command in ['Replace', 'Delete']:
        if not os.path.exists(file_name):
            print('An error occurred')
        else:
            if command == 'Replace':
                replace_substring(file_name, line[2], line[3])
            else:
                os.remove(file_name)

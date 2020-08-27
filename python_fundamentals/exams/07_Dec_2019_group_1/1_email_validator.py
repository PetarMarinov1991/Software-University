def upper_or_lower(make, my_string):
    if make == 'Upper':
        my_string = my_string.upper()
    elif make == 'Lower':
        my_string = my_string.lower()
    return my_string


def get_domain(count, my_string):
    return my_string[len(my_string) - count:]


def get_username(my_string):
    username = ''
    if '@' not in my_string:
        username = f'The email {my_string} doesn\'t contain the @ symbol.'
    else:
        for i in range(len(my_string)):
            if my_string[i] == '@':
                break
            else:
                username += my_string[i]
    return username


def replace(char, my_string):
    new_string = ''
    for ch in my_string:
        if ch == char:
            new_string += '-'
        else:
            new_string += ch
    return new_string


def encrypt(my_string):
    ascii_codes = [ord(ch) for ch in my_string]
    return ' '.join([str(code) for code in ascii_codes])


email = input()

while True:
    line = input().split()
    command = line[0]

    if command == 'Complete':
        break

    if command == 'Make':
        email = upper_or_lower(line[1], email)
        print(email)
    elif command == 'GetDomain':
        print(get_domain(int(line[1]), email))
    elif command == 'GetUsername':
        print(get_username(email))
    elif command == 'Replace':
        print(replace(line[1], email))
    elif command == 'Encrypt':
        print(encrypt(email))

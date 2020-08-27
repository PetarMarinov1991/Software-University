import re
regex = r"([#, $, %, *, &])([A-z]{1,})\1=(\d{1,})!!(.{1,})"


def encrypt_message(my_key, my_string):
    encrypted = ''
    for ch in my_string:
        encrypted += chr(ord(ch) + my_key)
    return encrypted


while True:
    data = re.findall(regex, input())

    if data:
        for match in data:
            name, valid_length, message = match[1], int(match[2]), match[3]
            if len(message) == valid_length:
                print(f'Coordinates found! {name} -> {encrypt_message(valid_length, message)}')
                exit(0)
            else:
                print('Nothing found!')
    else:
        print('Nothing found!')

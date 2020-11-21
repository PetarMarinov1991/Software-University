command = input()

message = ''
secret_message = ''
c_count = 0
o_count = 0
n_count = 0

while command != 'End':
    letter = command

    if ord(letter) in range(65, 91) or ord(letter) in range(97, 123):
        if letter == 'c':
            c_count += 1
            if c_count > 1:
                message += letter
        elif letter == 'o':
            o_count += 1
            if o_count > 1:
                message += letter
        elif letter == 'n':
            n_count += 1
            if n_count > 1:
                message += letter
        else:
            message += letter

    if c_count >= 1 and o_count >= 1 and n_count >= 1:
        secret_message += message
        message = ' '
        c_count = 0
        o_count = 0
        n_count = 0

    command = input()

print(secret_message)

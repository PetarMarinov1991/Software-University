def valid_string(string):
    valid = True
    for i in range(len(string)):
        char = ord(string[i])
        if char not in range(100, 126) and char is not 35:
            valid = False
            break
    return valid


def decrypt(string):
    decrypted_book = ''
    for i in range(len(string)):
        decrypted_book += chr(ord(string[i]) - 3)
    return decrypted_book


def replace_substring(sub_1, sub_2, string):
    string = string.replace(sub_1, sub_2)
    return string


encrypted_book = input()
change_from, change_to = input().split()

if valid_string(encrypted_book):
    print(replace_substring(change_from, change_to, decrypt(encrypted_book)))
else:
    print('This is not the book you are looking for.')

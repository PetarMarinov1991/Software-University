def length_check(password):
    if not len(password) in range(6, 11):
        return f'Password must be between 6 and 10 characters'


def isalnum_check(password):
    if not password.isalnum():
        return f'Password must consist only of letters and digits'


def isdigit_check(password):
    digits = [char for char in password if char.isdigit()]
    if not len(digits) >= 2:
        return f'Password must have at least 2 digits'


def valid_password(password):
    if not length_check(password) and not isalnum_check(password) and not isdigit_check(password):
        return f'Password is valid'


def result_output(password):
    if valid_password(password) is not None:
        return valid_password(password)

    result = [length_check(password), isalnum_check(password), isdigit_check(password)]
    output = [value for value in result if value is not None]
    return '\n'.join(output)


password_input = input()

print(result_output(password_input))

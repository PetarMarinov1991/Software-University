def password_validator(password):
    condition_1 = len(password) in range(6, 11)
    condition_2 = password.isalnum()
    condition_3 = len([x for x in password if x.isdigit()]) >= 2

    is_valid = True if condition_1 and condition_2 and condition_3 else False

    if is_valid:
        print('Password is valid')
    else:
        if not condition_1:
            print('Password must be between 6 and 10 characters')
        if not condition_2:
            print('Password must consist only of letters and digits')
        if not condition_3:
            print('Password must have at least 2 digits')


password_validator(input())

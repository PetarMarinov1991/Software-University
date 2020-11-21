def password_finder(magic_number):
    counter = 0
    password = ''
    is_found = False

    for first_digit in range(1, 10):
        for second_digit in range(1, 10):
            for third_digit in range(1, 10):
                for fourth_digit in range(1, 10):

                    condition_1 = first_digit * second_digit + third_digit * fourth_digit == control_number
                    condition_2 = first_digit < second_digit and third_digit > fourth_digit
                    combination = f'{first_digit}{second_digit}{third_digit}{fourth_digit}'

                    if condition_1 and condition_2:
                        print(f'{combination}', end=' ')
                        counter += 1
                        if counter == 4:
                            password = f'Password: {combination}'
                            is_found = True

    if is_found:
        return f'\n{password}'
    else:
        return '\nNo!'


control_number = int(input())

print(password_finder(control_number))

def find_magic_number(num_1, num_2, magic_num):
    combination = 0

    for first_number in range(a, b + 1):
        for second_number in range(a, b + 1):

            combination += 1

            current_number = first_number + second_number

            if current_number == magic_number:
                return f'Combination N:{combination} ({first_number} + {second_number} = {magic_number})'

    return f'{combination} combinations - neither equals {magic_number}'


a = int(input())
b = int(input())
magic_number = int(input())

print(find_magic_number(a, b, magic_number))

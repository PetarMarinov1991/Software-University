number = int(input())
num_str = str(number)

for first_digit in range(1, int(num_str[2]) + 1):
    for second_digit in range(1, int(num_str[1]) + 1):
        for third_digit in range(1, int(num_str[0]) + 1):
            result = first_digit * second_digit * third_digit
            print(f'{first_digit} * {second_digit} * {third_digit} = {result};')

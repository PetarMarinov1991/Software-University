def sum_of_digits(n):
    return sum([int(x) for x in str(n)])


def check_if_number_is_special(n):
    special_numbers = [5, 7, 11]
    numbers = []

    for num in range(1, n + 1):
        is_special = True if sum_of_digits(num) in special_numbers else False
        numbers.append(f'{num} -> {is_special}')
    return '\n'.join(numbers)


n = int(input())
print(check_if_number_is_special(n))

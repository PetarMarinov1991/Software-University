def sum_even_digits(digit):
    even_sum = sum([int(digit) for digit in str(digit) if int(digit) % 2 == 0])
    return even_sum


def sum_odd_digits(digit):
    odd_sum = sum([int(digit) for digit in str(digit) if int(digit) % 2 == 1])
    return odd_sum


num = int(input())

print(f'Odd sum = {sum_odd_digits(num)},', end=' ')
print(f'Even sum = {sum_even_digits(num)}')

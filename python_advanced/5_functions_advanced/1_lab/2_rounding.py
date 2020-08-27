def round_numbers(numbers):
    return [round(float(x)) for x in numbers.split()]


print(round_numbers(input()))

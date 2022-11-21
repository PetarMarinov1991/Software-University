number = input()


def largest_possible_number(n):
    digits = [int(d) for d in n]

    return ''.join(str(d) for d in sorted(digits)[::-1])


print(largest_possible_number(number))

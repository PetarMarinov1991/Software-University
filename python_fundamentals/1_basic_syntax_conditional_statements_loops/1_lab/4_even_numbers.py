num = int(input())


def number_definer(n):
    for _ in range(n):
        i = int(input())

        if i % 2 != 0:
            return f'{i} is odd!'

    return 'All numbers are even.'


print(number_definer(num))

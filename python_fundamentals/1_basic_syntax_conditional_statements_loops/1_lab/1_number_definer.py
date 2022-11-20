num = float(input())


def number_definer(n):
    if n == 0:
        return 'zero'

    n_range = 'small ' if abs(n) <= 1 else 'large ' if abs(n) >= 1_000_000 else ''
    n_type = 'negative' if n < 0 else 'positive'
    return n_range + n_type


print(number_definer(num))

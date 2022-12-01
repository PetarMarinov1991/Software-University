from itertools import product
from string import ascii_lowercase


def three_letters_combination(n):
    letters_combinations = [''.join(x) for x in product([ascii_lowercase[i] for i in range(n)], repeat=3)]
    return '\n'.join(letters_combinations)


n = int(input())

print(three_letters_combination(n))

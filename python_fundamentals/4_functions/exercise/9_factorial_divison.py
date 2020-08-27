import math


def factorial_division(a, b):
    return f'{math.factorial(a) / math.factorial(b):.2f}'


print(factorial_division(a=int(input()), b=int(input())))

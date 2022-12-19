def subtract(a, b):
    return a - b


def add(a, b):
    return a + b


def divide(a, b):
    return int(a / b)


def multiply(a, b):
    return a * b


def solve(operator, a, b):
    calculations = {
        'subtract': subtract(a, b),
        'add': add(a, b),
        'divide': divide(a, b),
        'multiply': multiply(a, b)
    }
    return calculations[operator]


operator = input()
a = int(input())
b = int(input())

print(solve(operator, a, b))

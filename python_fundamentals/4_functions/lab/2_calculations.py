def solve(a, b, operator):
    result = {
        'multiply': a * b,
        'divide': a // b,
        'add': a + b,
        'subtract': a - b
    }
    return result.__getitem__(operator)


print(solve(operator=input(), a=int(input()), b=int(input())))

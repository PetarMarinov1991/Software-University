def solve(type_of_input, x):
    if type_of_input == 'int':
        return int(x) * 2
    if type_of_input == 'real':
        return f'{float(x) * 1.5:.2f}'
    if type_of_input == 'string':
        return f'${x}$'


type_of_input = input()
x = input()

print(solve(type_of_input, x))

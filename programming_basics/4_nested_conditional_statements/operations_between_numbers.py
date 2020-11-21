n1 = int(input())
n2 = int(input())
operation = input()

operations = {
    '+': n1 + n2,
    '-': n1 - n2,
    '*': n1 * n2,
    '/': f'{n1 / n2:.2f}' if n2 != 0 else 0,
    '%': n1 % n2 if n2 != 0 else 0
}
result = operations[operation]

if operation in ['/', '%']:
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
        exit(0)
    else:
        print(f'{n1} {operation} {n2} = {result}')
        exit(0)

if result % 2 == 0:
    even_or_odd = 'even'
else:
    even_or_odd = 'odd'

print(f'{n1} {operation} {n2} = {result} - {even_or_odd}')

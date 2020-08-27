import re

demons = dict()

delimiters = []
for i in range(20):
    delimiters.append(',' + ' ' * i)
regex = '|'.join(map(re.escape, delimiters))

text = re.split(regex, input())

for demon in text:
    regex = r"[+-]*\d+\.?\d+|\d+"
    matches = re.findall(regex, demon)
    number = sum([float(match) for match in matches])

    health = 0
    damage = 0
    operators = []

    for char in demon:
        if char.isalpha():
            health += ord(char)
        elif char in ['*', '/']:
            operators.append(char)

    for operator in operators:
        if operator == '*':
            damage += number * 2
        else:
            damage += number / 2

    demons.update({demon.strip(): [health, damage]})

demons = {k: v for k, v in sorted(demons.items(), key=lambda x: x[0])}

for demon, value in demons.items():
    print(f'{demon} - {value[0]} health, {value[1]:.2f} damage')

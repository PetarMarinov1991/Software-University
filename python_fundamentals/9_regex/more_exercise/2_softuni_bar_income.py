import re
regex = r"%([A-Z]{1}[a-z]+)%<(\w+)>(\w+)*\|(\d+)\|([a-z0-9\.]+)\$"

total_income = 0

while True:
    line = input()

    if line == 'end of shift':
        break

    data = re.search(regex, line)
    if data:
        name, product = data.group(1), data.group(2)
        price = ''
        for char in data.group(5):
            if char.isdigit() or char == '.':
                price += char
        income = int(data.group(4)) * float(price)

        print(f'{name}: {product} - {income:.2f}')
        total_income += income

print(f'Total income: {total_income:.2f}')

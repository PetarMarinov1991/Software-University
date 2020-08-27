import re
regex = r">>([a-zA-Z]+)<<(\d+\.?\d+)!(\d+)"

furniture = []
spend = 0

while True:
    text = input()

    if text == 'Purchase':
        break

    data = re.search(regex, text)
    if data:
        furniture.append(data.group(1))
        spend += float(data.group(2)) * float(data.group(3))

print('Bought furniture:')
for item in furniture:
    print(item)
print(f'Total money spend: {spend:.2f}')

elements = set()

for _ in range(int(input())):
    current_elements = [x for x in input().split()]
    for element in current_elements:
        elements.add(element)

print('\n'.join([element for element in elements]))

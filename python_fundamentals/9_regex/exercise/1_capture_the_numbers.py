import re

regex = r"\d+"
output = []

while True:
    text = input()

    if not text:
        break

    numbers = re.findall(regex, text)
    output += [number for number in numbers if number]

print(' '.join(output))

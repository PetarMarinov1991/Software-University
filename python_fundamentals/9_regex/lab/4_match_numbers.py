import re

regex = r"(^|(?<=\s))-?\d+(.\d+)?($|(?=\s))"
numbers = re.finditer(regex, input())

for number in numbers:
    print(number.group(0), end=' ')

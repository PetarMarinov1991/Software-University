import re
from functools import reduce

text = input()

regex = r"([:|*]{2})([A-Z][a-z]{2,})(\1)"
data = re.findall(regex, text)
matches = [''.join(match) for match in data]
numbers = [int(char) for char in text if char.isdigit()]
result = reduce((lambda x, y: x * y), numbers)

print(f'Cool threshold: {result}')
print(f'{len(matches)} emojis found in the text. The cool ones are:')
print('\n'.join([match for match in matches if sum(map(ord, match[2:-2])) >= result]))

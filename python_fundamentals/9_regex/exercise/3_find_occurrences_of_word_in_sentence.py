import re

text = input()
search = input()

regex = rf'\b{search}\b'

print(len(re.findall(regex, text, re.IGNORECASE)))

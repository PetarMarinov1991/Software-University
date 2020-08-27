import re

regex = r"(\+359([-| ])2\2\d{3}\2\d{4}\b)"
phones = re.findall(regex, input())

print(', '.join([phone for phone, sep in phones]))

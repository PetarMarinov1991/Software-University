import re

regex = r"\b[A-Z][a-z]+\s\b[A-Z][a-z]+\b"
matches = re.findall(regex, input())

print(' '.join(matches))

import re

regex = r"( |^)[0-9a-z]+([\.\-_][0-9a-z]+)*@[a-z]+(-[a-z]+)*(\.[a-z]+(-[a-z]+)*)+"
emails = re.finditer(regex, input())

for email in emails:
    print(email[0].strip())

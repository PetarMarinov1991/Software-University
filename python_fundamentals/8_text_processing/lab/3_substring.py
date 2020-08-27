banned = input()
text = input()

while banned in text:
    text = text.replace(banned, '')

print(text)

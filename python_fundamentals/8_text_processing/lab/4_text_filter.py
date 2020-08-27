banned = input().split(', ')
text = input()

for ban in banned:
    while ban in text:
        text = text.replace(ban, len(ban) * '*')

print(text)

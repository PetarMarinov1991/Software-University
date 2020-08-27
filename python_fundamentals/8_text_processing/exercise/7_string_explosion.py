text = input()
result = ''

i = 0
explosions = 0

while i < len(text):
    if not text[i] == '>':
        result += text[i]
        i += 1
    else:
        result += text[i]
        i += 1
        explosions += int(text[i])
        while explosions > 0 and not text[i] == '>':
            i += 1
            explosions -= 1
            if i == len(text):
                break

print(result)

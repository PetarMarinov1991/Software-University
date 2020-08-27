text = input()
result = ''

for idx, char in enumerate(text):
    if idx == len(text) - 1:
        result += char
        break
    if text[idx] == text[idx + 1]:
        continue
    result += char

print(result)

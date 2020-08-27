text = input().split()
result = ''

for word in text:
    multiply = len(word)
    result += word * multiply

print(result)

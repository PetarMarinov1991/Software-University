text = input().upper()

result = ''
final_result = ''

for i in range(len(text)):
    if text[i].isdigit():
        num = text[i]
        counter = i + 1
        while counter < len(text) and text[counter].isdigit():
            num += text[counter]
            counter += 1
        final_result += result * int(num)
        result = ''
    else:
        result += text[i]

print(f'Unique symbols used: {len(set(final_result))}')
print(final_result)

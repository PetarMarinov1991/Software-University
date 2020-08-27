numbers = input().split()
text = input()

characters = [char for char in text]

indices = []
for number in numbers:
    ord_value = 0
    for digit in number:
        ord_value += int(digit)
    if ord_value > len(text):
        indices.append(ord_value - len(text))
    else:
        indices.append(ord_value)

message = []
while indices:
    message.append(characters.pop(indices[0]))
    indices.remove(indices[0])

print(''.join(message))

key = int(input())
lines = int(input())

message = []

for char in range(lines):
    letter = input()
    ascii_value = (ord(letter) + key)
    message.append(chr(ascii_value))

print(''.join(message))

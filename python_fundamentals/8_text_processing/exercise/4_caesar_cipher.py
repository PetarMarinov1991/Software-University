text = input()
ciphered = ''

for char in text:
    ciphered += chr(ord(char) + 3)

print(ciphered)

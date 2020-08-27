line = input().split()
line = ''.join(line)

characters = dict()

for char in line:
    if char not in characters:
        characters.update({char: 1})
    else:
        characters[char] += 1

for char, value in characters.items():
    print(f'{char} -> {value}')

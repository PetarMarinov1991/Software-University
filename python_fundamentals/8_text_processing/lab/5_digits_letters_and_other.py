text = input()

print(''.join([char for char in text if char.isdigit()]))
print(''.join([char for char in text if char.isalpha()]))
print(''.join([char for char in text if not char.isdigit() and not char.isalpha()]))

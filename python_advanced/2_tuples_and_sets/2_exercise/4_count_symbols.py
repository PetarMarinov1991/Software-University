string = input()

unique_symbols = set()
for ch in string:
    unique_symbols.add(ch)

for ch in sorted(unique_symbols):
    print(f'{ch}: {string.count(ch)} time/s')

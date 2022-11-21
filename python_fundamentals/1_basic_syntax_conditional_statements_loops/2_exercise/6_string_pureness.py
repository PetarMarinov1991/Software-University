n = int(input())
forbidden_chars = set('.,_')
pure = True

for _ in range(n):
    text = input()

    if any((c in forbidden_chars) for c in text):
        pure = False

    if pure:
        print(f'{text} is pure.')
    else:
        print(f'{text} is not pure!')

def between_characters(a, b):
    if ord(a) > ord(b):
        a, b = b, a
    for char in range(ord(a) + 1, ord(b)):
        print(f'{chr(char)}', end=' ')


between_characters(a=input(), b=input())

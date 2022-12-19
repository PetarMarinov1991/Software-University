def chars_in_range(start, end):
    chars = [chr(x) for x in range(ord(start)+1, ord(end))]
    return ' '.join(chars)


start = input()
end = input()

print(chars_in_range(start, end))

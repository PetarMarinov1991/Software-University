def print_ascii_chars(start, end):
    chars = [chr(x) for x in range(start, end + 1)]
    return ' '.join(chars)


start = int(input())
end = int(input())

print(print_ascii_chars(start, end))

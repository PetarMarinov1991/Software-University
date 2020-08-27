start = input()
end = input()
text = input()

ascii_sum = 0

for char in text:
    if ord(char) in range(ord(start), ord(end)):
        if not ord(char) == ord(start) and not ord(char) == ord(end):
            ascii_sum += ord(char)

print(ascii_sum)

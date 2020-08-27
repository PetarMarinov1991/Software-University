word = input()

idx_word = []
idx_capitals = []

for char in word:
    idx_char = word.index(char)
    idx_word.append(idx_char)

    if 65 <= ord(char) <= 90:
        if idx_char in idx_capitals:
            idx_capitals.append(len(idx_word) - 1)
        else:
            idx_capitals.append(idx_char)

print(idx_capitals)

indices = [int(x) for x in input().split()]
text = [ch for ch in input()]

idx_codes = list(map(lambda e: sum(int(s) for s in str(e)), indices))
valid_indices = [i if i < len(text) else i - len(text) for i in idx_codes]

message = ''

for i in valid_indices:
    message += text[i]
    del text[i]

print(message)

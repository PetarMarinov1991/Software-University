strings = input().split()
strings.sort(key=lambda x: -len(x))
strings_len = len(strings[0]), len(strings[1])

result = 0

for i in range(min(strings_len)):
    result += ord(strings[0][i]) * ord(strings[1][i])

if max(strings_len) != min(strings_len):
    for j in range(min(strings_len), max(strings_len)):
        result += ord(strings[0][j])

print(result)

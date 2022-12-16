numbers = [x for x in input().split()]
indexes = [sum([int(x) for x in num]) for num in numbers]
chars = list(input())

message = ''

for i in indexes:
    if i > len(chars) - 1:
        i -= len(chars)
    message += chars[i]
    chars.remove(chars[i])

print(message)

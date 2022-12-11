numbers = [int(x) for x in input().split(', ')]
beggars = int(input())

result = [0] * beggars

for i in range(len(numbers)):
    idx = i % beggars
    result[idx] += numbers[i]

print(result)

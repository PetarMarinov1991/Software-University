numbers = input().split(', ')
beggars = int(input())

numbers_list = [int(num) for num in numbers]

result = [0] * beggars

for i in range(len(numbers_list)):
    idx = i % beggars
    result[idx] += numbers_list[i]

print(result)

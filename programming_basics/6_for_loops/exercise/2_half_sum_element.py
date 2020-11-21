n = int(input())

numbers = []
numbers_without_max = []

for _ in range(n):
    num = int(input())
    numbers.append(num)
    numbers_without_max.append(num)

max_num = max(numbers)
numbers_without_max.remove(max(numbers))

if sum(numbers_without_max) == max_num:
    print(f'Yes\nSum = {max_num}')
else:
    print(f'No\nDiff = {abs(max_num - sum(numbers_without_max))}')

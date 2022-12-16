from itertools import count

numbers = [int(num) for num in input().split(', ')]
result = [num for num in numbers if num != 0] + [0] * numbers.count(0)

print(result)

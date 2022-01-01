numbers = [int(x) for x in input().split(', ')]
zeros = numbers.count(0)

numbers = [n for n in numbers if n != 0] + [0] * zeros
print(numbers)

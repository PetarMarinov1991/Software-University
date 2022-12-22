numbers = [int(x) for x in input().split(', ')]

even_indexes = [i for i, n in enumerate(numbers) if n % 2 == 0]
print(even_indexes)

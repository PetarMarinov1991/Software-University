factor = int(input())
list_length = int(input())

print([num for num in range(factor, list_length * factor + 1, factor)])

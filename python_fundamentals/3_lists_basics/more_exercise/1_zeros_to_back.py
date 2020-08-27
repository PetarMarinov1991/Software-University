string = input().split(', ')

numbers = [int(num) for num in string if int(num) != 0]
zeros = [int(num) for num in string if int(num) == 0]

print(numbers + zeros)

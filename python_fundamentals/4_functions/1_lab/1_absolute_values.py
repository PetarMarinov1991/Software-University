def absolute_values(arr):
    return [abs(x) for x in arr]


numbers = [float(x) for x in input().split()]
print(absolute_values(numbers))

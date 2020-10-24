numbers = [int(x) for x in input().split(', ')]
index_needed = int(input())

print(sum([x for x in numbers if x <= numbers[index_needed]]))

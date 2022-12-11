n = int(input())
numbers = [int(input()) for _ in range(n)]

positives = [x for x in numbers if x >= 0]
negatives = [x for x in numbers if x not in positives]

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}')
print(f'Sum of negatives: {sum(negatives)}')

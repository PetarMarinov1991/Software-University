lines = int(input())

positives = []
negatives = []

for i in range(lines):
    num = int(input())
    if num < 0:
        negatives.append(num)
    else:
        positives.append(num)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}")

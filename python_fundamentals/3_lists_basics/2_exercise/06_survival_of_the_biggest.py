numbers = [int(x) for x in input().split()]
n = int(input())

for _ in range(n):
    numbers.remove(min(numbers))

print(', '.join([str(x) for x in numbers]))

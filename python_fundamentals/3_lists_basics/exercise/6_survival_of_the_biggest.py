numbers = list(map(int, input().split()))
remove = [numbers.remove(min(numbers)) for _ in range(int(input()))]

print(numbers)

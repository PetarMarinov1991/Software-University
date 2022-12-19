def is_even(x): return x % 2 == 0


numbers = [int(x) for x in input().split()]
print(list(filter(is_even, numbers)))

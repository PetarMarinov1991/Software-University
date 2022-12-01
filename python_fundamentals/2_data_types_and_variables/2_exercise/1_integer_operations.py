def int_operations(n):
    return int((n[0] + n[1]) // n[2] * n[3])


numbers = [int(input()) for _ in range(4)]

print(int_operations(numbers))

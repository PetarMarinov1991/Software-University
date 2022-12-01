def calculate_ascii_sum(n):
    ascii_sum = sum([ord(input()) for _ in range(n)])
    return f'The sum equals: {ascii_sum}'


n = int(input())

print(calculate_ascii_sum(n))

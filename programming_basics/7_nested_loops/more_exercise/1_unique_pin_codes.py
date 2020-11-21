n = int(input())
m = int(input())
k = int(input())

primes = [2, 3, 5, 7]

for first_digit in range(2, n + 1, 2):
    for second_digit in range(2, m + 1):
        if second_digit not in primes:
            continue
        for third_digit in range(2, k + 1, 2):
            print(f'{first_digit} {second_digit} {third_digit}')

first_pair_start = int(input())
second_pair_start = int(input())
first_pair_end = int(input()) + first_pair_start
second_pair_end = int(input()) + second_pair_start


def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


for first_num in range(first_pair_start, first_pair_end + 1):
    for second_num in range(second_pair_start, second_pair_end + 1):
        if is_prime(first_num) and is_prime(second_num):
            print(f'{first_num}{second_num}')

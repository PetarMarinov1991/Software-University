n = int(input())
n_doubled = n * 2

for i in range(n_doubled):
    if i <= n_doubled / 2:
        print('*' * i)
    else:
        print('*' * abs(i - n_doubled))

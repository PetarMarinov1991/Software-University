num = int(input())

for i in range(num):
    for j in range(i):
        print('*', end='')
    print('')

for k in range(num, 0, -1):
    for p in range(k):
        print('*', end='')
    print('')
